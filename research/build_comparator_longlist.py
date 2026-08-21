#!/usr/bin/env python3
"""Build the external Dutch WO-bachelor comparator longlist.

This is an experimental research utility for UCR Pathways.  It deliberately
builds the Dutch programme universe before any UCR-course feasibility filter.

Sources
-------
1. Studiekeuze123 WO-bachelor category pages: public discovery universe.
2. DUO RIO HO Opleidingsoverzicht CSV: official programme/status metadata.

Outputs are written under research/comparator_longlist/.
"""

from __future__ import annotations

import csv
import datetime as dt
import html
import io
import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

TODAY = dt.date.today()
OUT = Path("research/comparator_longlist")
OUT.mkdir(parents=True, exist_ok=True)

SK123_BASE = "https://www.studiekeuze123.nl"
SK123_CATEGORY = f"{SK123_BASE}/opleidingen/categorie/wo-bachelor-opleidingen"
DUO_CSV = (
    "https://onderwijsdata.duo.nl/dataset/"
    "7c0686f4-b5c2-418e-8e44-7be0057d8084/resource/"
    "ffffa7ad-e6a2-4ba7-9fc2-a09df4128555/download/ho_opleidingsoverzicht.csv"
)

UA = "Mozilla/5.0 (compatible; UCR-Pathways-research/1.0; +https://github.com/solmyr1980/ucr-pathways)"

PILOT_SEEDS = [
    ("Psychobiologie", "Universiteit van Amsterdam"),
    ("Environmental Sciences", "Wageningen University & Research"),
    ("Informatica", "Universiteit Utrecht"),
    ("Health Sciences", "Maastricht University"),
    ("Kunstgeschiedenis", "Universiteit Utrecht"),
    ("Rechtsgeleerdheid", "Universiteit Utrecht"),
    ("Biologie", "Universiteit Utrecht"),
    ("Business Administration", "Universiteit van Amsterdam"),
    ("Psychology", "Tilburg University"),
    ("Communicatiewetenschap", "Universiteit van Amsterdam"),
]

INSTITUTION_ALIASES = {
    "wageningen university & research": ["wageningen university", "wageningen university & research"],
    "universiteit utrecht": ["universiteit utrecht", "utrecht university"],
    "universiteit van amsterdam": ["universiteit van amsterdam", "university of amsterdam"],
    "maastricht university": ["maastricht university", "universiteit maastricht"],
    "tilburg university": ["tilburg university", "universiteit van tilburg"],
}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.lower().replace("&", " en ")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def get_text(url: str, timeout: int = 60, retries: int = 3) -> str:
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read()
                enc = r.headers.get_content_charset() or "utf-8"
                return raw.decode(enc, errors="replace")
        except Exception as e:
            last = e
            time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"Failed to fetch {url}: {last}")


def get_bytes(url: str, timeout: int = 120, retries: int = 3) -> bytes:
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:
            last = e
            time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"Failed to fetch {url}: {last}")


def strip_tags(s: str) -> str:
    s = re.sub(r"<script\b.*?</script>", " ", s, flags=re.I | re.S)
    s = re.sub(r"<style\b.*?</style>", " ", s, flags=re.I | re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def sk123_institutions(first_html: str) -> List[str]:
    # The filter section contains institution labels and counts. Extracting from
    # the HTML text is intentionally conservative; a fixed fallback covers the
    # standard WO providers if markup changes.
    text = strip_tags(first_html)
    known = [
        "Universiteit van Amsterdam", "Universiteit Leiden", "Rijksuniversiteit Groningen",
        "Vrije Universiteit Amsterdam", "Universiteit Utrecht", "Radboud Universiteit",
        "Maastricht University", "Tilburg University", "Erasmus Universiteit Rotterdam",
        "Universiteit Twente", "Wageningen University & Research", "Technische Universiteit Delft",
        "Technische Universiteit Eindhoven", "Open Universiteit", "Faculteit Militaire Wetenschappen",
        "Nyenrode Business Universiteit", "Breda University of Applied Sciences",
        "Protestantse Theologische Universiteit", "SOMT", "Theologische Universiteit Apeldoorn",
        "Theologische Universiteit Utrecht", "Universiteit voor Humanistiek",
    ]
    return [x for x in known if x in text] or known


def parse_sk123_cards(page_html: str, institutions: List[str]) -> List[dict]:
    # Programme URLs have a stable numeric-id + slug shape. We take the first
    # matching anchor's text as card text; duplicate links to the same page are
    # collapsed later.
    pat = re.compile(
        r'<a[^>]+href=["\'](?P<href>/opleidingen/\d+-[^"\']+)["\'][^>]*>(?P<body>.*?)</a>',
        re.I | re.S,
    )
    by_url = {}
    for m in pat.finditer(page_html):
        href = html.unescape(m.group("href"))
        body = strip_tags(m.group("body"))
        if not body or "wo bachelor" not in norm(body):
            continue
        url = urllib.parse.urljoin(SK123_BASE, href)
        if url in by_url:
            continue
        inst = next((i for i in sorted(institutions, key=len, reverse=True) if i in body), "")
        if not inst:
            continue
        before = body.split(inst, 1)[0].strip()
        programme = re.sub(r"^Bekijk opleiding\s+", "", before, flags=re.I).strip()
        # Remove accidental card/action prefix if markup includes it.
        programme = re.sub(r"^(Bewaar|Vergelijk)\s+", "", programme, flags=re.I).strip()
        if not programme:
            continue
        body_n = norm(body)
        full_time = "voltijd" in body_n
        part_time = "deeltijd" in body_n
        city = ""
        # City is typically directly after study form; keep a human-readable
        # card text too, so no information is lost if parsing is imperfect.
        mcity = re.search(r"Wo bachelor\s+(?:Voltijd\s+)?(?:Deeltijd\s+)?([A-ZÀ-ÖØ-Ý][A-Za-zÀ-ÿ .'-]+?)(?:\s+(?:Open dag|Informatie|Meeloop|Proefstuderen|Varianten:|$))", body)
        if mcity:
            city = mcity.group(1).strip()
        by_url[url] = {
            "sk123_programme": programme,
            "sk123_institution": inst,
            "sk123_city": city,
            "sk123_full_time": full_time,
            "sk123_part_time": part_time,
            "sk123_url": url,
            "sk123_card_text": body,
        }
    return list(by_url.values())


def collect_sk123() -> Tuple[List[dict], dict]:
    first = get_text(SK123_CATEGORY)
    institutions = sk123_institutions(first)
    all_rows = {}
    page = 1
    stale_pages = 0
    while page <= 40:
        url = SK123_CATEGORY if page == 1 else f"{SK123_CATEGORY}?pageNumber={page}"
        text = first if page == 1 else get_text(url)
        rows = parse_sk123_cards(text, institutions)
        before = len(all_rows)
        for r in rows:
            all_rows[r["sk123_url"]] = r
        added = len(all_rows) - before
        print(f"Studiekeuze123 page {page}: parsed {len(rows)}, new {added}, total {len(all_rows)}")
        if page > 1 and added == 0:
            stale_pages += 1
        else:
            stale_pages = 0
        if stale_pages >= 2:
            break
        # Current page size is about 20; 447 total implies ~23 pages.
        if len(all_rows) >= 447:
            break
        page += 1
        time.sleep(0.15)

    # Extract headline counts from visible text for reproducibility.
    text = strip_tags(first)
    def grab(pattern, default=None):
        m = re.search(pattern, text, re.I)
        return int(m.group(1)) if m else default
    meta = {
        "source": SK123_CATEGORY,
        "retrieved": TODAY.isoformat(),
        "reported_wo_bachelor_total": grab(r"Wo bachelor\s+(\d+)"),
        "reported_full_time": grab(r"Voltijd\s+(\d+)"),
        "reported_part_time": grab(r"Deeltijd\s+(\d+)"),
        "parsed_unique_programme_pages": len(all_rows),
    }
    return list(all_rows.values()), meta


def decode_csv(raw: bytes) -> Tuple[List[dict], str, List[str]]:
    text = raw.decode("utf-8-sig", errors="replace")
    sample = text[:10000]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=";,\t|")
        delim = dialect.delimiter
    except Exception:
        delim = ";"
    reader = csv.DictReader(io.StringIO(text), delimiter=delim)
    rows = list(reader)
    return rows, delim, reader.fieldnames or []


def parse_date(s: str):
    s = (s or "").strip()
    if not s:
        return None
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%Y%m%d"):
        try:
            return dt.datetime.strptime(s[:10], fmt).date()
        except Exception:
            pass
    return None


def active_rio(row: dict) -> bool:
    start = parse_date(row.get("AANGEBODEN_OPLEIDING_BEGINDATUM", ""))
    end = parse_date(row.get("AANGEBODEN_OPLEIDING_EINDDATUM", ""))
    if start and start > TODAY:
        # Future offerings are still useful to prospective students if intake
        # opens imminently; keep them if the first intake is not in the past.
        first = parse_date(row.get("EERSTE_INSTROOMDATUM", ""))
        if not first or first > TODAY + dt.timedelta(days=550):
            return False
    if end and end < TODAY:
        return False
    last = parse_date(row.get("LAATSTE_INSTROOMDATUM", ""))
    if last and last < TODAY:
        return False
    return True


def collect_rio() -> Tuple[List[dict], dict]:
    raw = get_bytes(DUO_CSV)
    rows, delim, fields = decode_csv(raw)
    def val(r, key):
        return (r.get(key) or "").strip()
    selected = []
    for r in rows:
        if val(r, "NIVEAU").upper() != "WO-BA":
            continue
        if "VOLTIJD" not in val(r, "VORM").upper():
            continue
        if not active_rio(r):
            continue
        selected.append(r)
    meta = {
        "source": DUO_CSV,
        "retrieved": TODAY.isoformat(),
        "delimiter": delim,
        "all_rio_rows": len(rows),
        "current_full_time_wo_bachelor_rows": len(selected),
        "columns": fields,
    }
    return selected, meta


def rio_key(r: dict) -> Tuple[str, str]:
    provider = (r.get("ONDERWIJSAANBIEDERID") or r.get("ONDERWIJSBESTUURID") or r.get("ONDERWIJSAANBIEDER_NAAM") or "").strip()
    code = (r.get("ERKENDEOPLEIDINGSCODE") or r.get("OPLEIDINGSEENHEIDCODE") or r.get("AANGEBODEN_OPLEIDINGCODE") or "").strip()
    return provider, code


def rio_programme(r: dict) -> str:
    for k in ("EIGENNAAM", "EIGENNAAM_LANG", "NAAM_LANG", "INTERNATIONALE_NAAM"):
        if (r.get(k) or "").strip():
            return (r.get(k) or "").strip()
    return ""


def rio_institution(r: dict) -> str:
    return (r.get("ONDERWIJSAANBIEDER_NAAM") or r.get("ONDERWIJSBESTUUR_NAAM") or "").strip()


def mark_pilot(programme: str, institution: str) -> str:
    p, i = norm(programme), norm(institution)
    for idx, (sp, si) in enumerate(PILOT_SEEDS, 1):
        spn = norm(sp)
        aliases = [norm(si)] + [norm(x) for x in INSTITUTION_ALIASES.get(si.lower(), [])]
        # Allow exact programme match or English/Dutch names containing one another.
        programme_match = p == spn or (len(spn) >= 8 and (spn in p or p in spn))
        institution_match = any(a == i or (len(a) >= 8 and (a in i or i in a)) for a in aliases)
        if programme_match and institution_match:
            return f"pilot-{idx:02d}"
    return ""


def token_similarity(a: str, b: str) -> float:
    aa, bb = set(norm(a).split()), set(norm(b).split())
    if not aa or not bb:
        return 0.0
    return len(aa & bb) / len(aa | bb)


def best_sk_match(programme: str, institution: str, sk_rows: List[dict]) -> Tuple[dict | None, float]:
    ni = norm(institution)
    best, bestscore = None, 0.0
    for s in sk_rows:
        si = norm(s["sk123_institution"])
        # Institution must be plausible before comparing programme names.
        inst_score = token_similarity(ni, si)
        if inst_score < 0.34 and ni not in si and si not in ni:
            continue
        ps = token_similarity(programme, s["sk123_programme"])
        score = 0.75 * ps + 0.25 * inst_score
        if score > bestscore:
            best, bestscore = s, score
    return best, bestscore


def write_csv(path: Path, rows: List[dict], fields: List[str] | None = None):
    if fields is None:
        fields = []
        seen = set()
        for r in rows:
            for k in r.keys():
                if k not in seen:
                    seen.add(k); fields.append(k)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def main():
    sk_rows, sk_meta = collect_sk123()
    sk_full = [r for r in sk_rows if r["sk123_full_time"]]
    print(f"Studiekeuze123 full-time parsed rows: {len(sk_full)}")

    rio_rows, rio_meta = collect_rio()
    print(f"RIO current full-time WO-BA rows: {len(rio_rows)}")

    # Preserve the official row-level extract first.
    raw_fields = list(rio_rows[0].keys()) if rio_rows else []
    write_csv(OUT / "rio_wo_bachelor_fulltime_offerings.csv", rio_rows, raw_fields)
    write_csv(OUT / "studiekeuze123_wo_bachelor_pages.csv", sk_rows)

    # Deduplicate official data at programme + provider level, preserving all
    # locations/languages/forms visible in underlying offering rows.
    groups = defaultdict(list)
    for r in rio_rows:
        groups[rio_key(r)].append(r)

    dedup = []
    for (provider_id, code), rs in groups.items():
        first = rs[0]
        programme = rio_programme(first)
        institution = rio_institution(first)
        locations = sorted({(x.get("ONDERWIJSLOCATIEPLAATS") or "").strip() for x in rs if (x.get("ONDERWIJSLOCATIEPLAATS") or "").strip()})
        languages = sorted({(x.get("VOERTAAL") or "").strip() for x in rs if (x.get("VOERTAAL") or "").strip()})
        forms = sorted({(x.get("VORM") or "").strip() for x in rs if (x.get("VORM") or "").strip()})
        websites = sorted({(x.get("WEBSITE") or "").strip() for x in rs if (x.get("WEBSITE") or "").strip()})
        sk, score = best_sk_match(programme, institution, sk_full)
        dedup.append({
            "programme": programme,
            "institution": institution,
            "official_programme_code": code,
            "provider_id": provider_id,
            "degree": (first.get("GRAAD") or "").strip(),
            "study_load": (first.get("STUDIELAST") or "").strip(),
            "locations": " | ".join(locations),
            "languages": " | ".join(languages),
            "forms": " | ".join(forms),
            "official_websites": " | ".join(websites),
            "rio_row_count": len(rs),
            "pilot_seed": mark_pilot(programme, institution),
            "sk123_match_score": f"{score:.3f}" if sk else "",
            "sk123_programme": sk["sk123_programme"] if sk else "",
            "sk123_institution": sk["sk123_institution"] if sk else "",
            "sk123_city": sk["sk123_city"] if sk else "",
            "sk123_url": sk["sk123_url"] if sk else "",
            # Subject-area enrichment is deliberately left to Step 3 unless it
            # can be obtained reliably from the public listing itself.
            "sk123_subject_area": "",
            "status_checked": TODAY.isoformat(),
            "status_source": "DUO RIO HO Opleidingsoverzicht",
        })

    dedup.sort(key=lambda r: (norm(r["institution"]), norm(r["programme"])))
    write_csv(OUT / "dutch_wo_bachelor_fulltime_longlist.csv", dedup)

    strong_matches = sum(1 for r in dedup if r["sk123_match_score"] and float(r["sk123_match_score"]) >= 0.72)
    pilot_hits = [r for r in dedup if r["pilot_seed"]]
    summary = {
        "generated": TODAY.isoformat(),
        "scope": "Current Dutch WO bachelor programmes with a full-time route; no UCR feasibility filter applied.",
        "studiekeuze123": sk_meta,
        "duo_rio": rio_meta,
        "deduplicated_programme_institution_candidates": len(dedup),
        "strong_sk123_matches": strong_matches,
        "pilot_seeds_found": len(pilot_hits),
        "pilot_seed_matches": [
            {"pilot_seed": r["pilot_seed"], "programme": r["programme"], "institution": r["institution"], "code": r["official_programme_code"]}
            for r in pilot_hits
        ],
        "notes": [
            "No UCR course evidence was used in Step 1.",
            "The RIO extract is the official status/code basis; Studiekeuze123 is the public discovery/count benchmark.",
            "Studiekeuze123 subject-area enrichment is not guessed when it cannot be reliably captured from the listing; it can be added in the later comparator-source/interest-language step.",
        ],
    }
    (OUT / "step1_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [
        "# Step 1 — Dutch WO bachelor longlist\n",
        f"Generated: {TODAY.isoformat()}\n",
        "## Scope\n",
        "Current Dutch WO bachelor programmes with a full-time route. This is an external candidate universe: **no UCR feasibility filtering has been applied**.\n",
        "## Counts\n",
        f"- Studiekeuze123 reports {sk_meta.get('reported_wo_bachelor_total')} WO bachelor offerings, including {sk_meta.get('reported_full_time')} with a full-time route.",
        f"- The scraper captured {sk_meta.get('parsed_unique_programme_pages')} unique Studiekeuze123 programme pages ({len(sk_full)} marked full-time).",
        f"- DUO RIO yielded {rio_meta.get('current_full_time_wo_bachelor_rows')} current full-time WO-BA offering/location rows.",
        f"- Deduplication at official programme + institution/provider level yielded **{len(dedup)} candidates**.",
        f"- Strong automatic links back to Studiekeuze123: {strong_matches}.",
        f"- Existing pilot seeds found automatically in the official longlist: {len(pilot_hits)}/10.\n",
        "## Files\n",
        "- `rio_wo_bachelor_fulltime_offerings.csv` — preserved official row-level extract.",
        "- `studiekeuze123_wo_bachelor_pages.csv` — public discovery pages captured from the WO-bachelor listing.",
        "- `dutch_wo_bachelor_fulltime_longlist.csv` — deduplicated programme + institution candidate view for Step 2.",
        "- `step1_summary.json` — machine-readable provenance and counts.\n",
        "## Methodological boundary\n",
        "No programme has been excluded because it looks difficult for UCR. UCR feasibility belongs to Step 2. Subject-area and student-interest-language enrichment is also deferred rather than guessed where the public listing does not expose it reliably.\n",
    ]
    (OUT / "README.md").write_text("\n".join(md), encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
