#!/usr/bin/env python3
"""Build and save Step 1: the external Dutch full-time WO-bachelor universe.

The longlist is built without consulting the UCR course database.

Discovery/count benchmark: Studiekeuze123 WO-bachelor overview.
Official programme/status/code source: DUO RIO HO Opleidingsoverzicht.
"""

from __future__ import annotations

import csv
import datetime as dt
import difflib
import html
import io
import json
import re
import time
import unicodedata
import urllib.request
from collections import defaultdict
from pathlib import Path

TODAY = dt.date.today()
OUT = Path("research/comparator_longlist")
OUT.mkdir(parents=True, exist_ok=True)

SK123 = "https://www.studiekeuze123.nl/opleidingen/categorie/wo-bachelor-opleidingen"
DUO = (
    "https://onderwijsdata.duo.nl/dataset/"
    "7c0686f4-b5c2-418e-8e44-7be0057d8084/resource/"
    "ffffa7ad-e6a2-4ba7-9fc2-a09df4128555/download/ho_opleidingsoverzicht.csv"
)
UA = "Mozilla/5.0 (compatible; UCR-Pathways-research/1.0; +https://github.com/solmyr1980/ucr-pathways)"

PILOTS = [
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

INST_ALIASES = {
    "Universiteit van Amsterdam": ["Universiteit van Amsterdam", "University of Amsterdam"],
    "Wageningen University & Research": ["Wageningen University", "Wageningen University & Research"],
    "Universiteit Utrecht": ["Universiteit Utrecht", "Utrecht University"],
    "Maastricht University": ["Maastricht University", "Universiteit Maastricht"],
    "Tilburg University": ["Tilburg University", "Universiteit van Tilburg"],
}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c)).lower().replace("&", " en ")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def fetch(url: str, binary: bool = False, tries: int = 3):
    err = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"})
            with urllib.request.urlopen(req, timeout=120) as r:
                raw = r.read()
                if binary:
                    return raw
                return raw.decode(r.headers.get_content_charset() or "utf-8", errors="replace")
        except Exception as e:
            err = e
            time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"Could not fetch {url}: {err}")


def visible_text(raw_html: str) -> str:
    x = re.sub(r"<script\b.*?</script>", " ", raw_html, flags=re.I | re.S)
    x = re.sub(r"<style\b.*?</style>", " ", x, flags=re.I | re.S)
    x = re.sub(r"<[^>]+>", " ", x)
    return re.sub(r"\s+", " ", html.unescape(x)).strip()


def sk123_counts() -> dict:
    text = visible_text(fetch(SK123))
    def n(pattern):
        m = re.search(pattern, text, re.I)
        return int(m.group(1)) if m else None
    return {
        "source": SK123,
        "retrieved": TODAY.isoformat(),
        "reported_wo_bachelor_offerings": n(r"Wo bachelor\s+(\d+)"),
        "reported_full_time_offerings": n(r"Voltijd\s+(\d+)"),
        "reported_part_time_offerings": n(r"Deeltijd\s+(\d+)"),
    }


def parse_date(s: str):
    s = (s or "").strip()
    if not s:
        return None
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%Y%m%d"):
        try:
            return dt.datetime.strptime(s[:10], fmt).date()
        except ValueError:
            pass
    return None


def still_current(r: dict) -> bool:
    # Both the recognised programme and the provider's offering must not have ended.
    for key in ("EINDDATUM", "AANGEBODEN_OPLEIDING_EINDDATUM"):
        d = parse_date(r.get(key, ""))
        if d and d < TODAY:
            return False
    # If RIO explicitly records that intake has ended, it is not a current
    # prospective-student offering even if administrative closure is later.
    last = parse_date(r.get("LAATSTE_INSTROOMDATUM", ""))
    if last and last < TODAY:
        return False
    return True


def load_rio():
    raw = fetch(DUO, binary=True)
    text = raw.decode("utf-8-sig", errors="replace")
    try:
        delimiter = csv.Sniffer().sniff(text[:12000], delimiters=";,\t|").delimiter
    except csv.Error:
        delimiter = ";"
    reader = csv.DictReader(io.StringIO(text), delimiter=delimiter)
    all_rows = list(reader)
    fields = reader.fieldnames or []

    selected = []
    for r in all_rows:
        # Critical distinction: RIO also stores programme components, premasters,
        # double-degree components, etc.  Step 1 wants recognised programmes only.
        if (r.get("SOORT") or "").strip().upper() != "OPLEIDING":
            continue
        if (r.get("NIVEAU") or "").strip().upper() != "WO-BA":
            continue
        if "VOLTIJD" not in (r.get("VORM") or "").upper():
            continue
        if not (r.get("ERKENDEOPLEIDINGSCODE") or "").strip():
            continue
        if not still_current(r):
            continue
        selected.append(r)

    return all_rows, selected, fields, delimiter


def write_csv(path: Path, rows: list[dict], fields: list[str] | None = None):
    if fields is None:
        fields, seen = [], set()
        for r in rows:
            for k in r:
                if k not in seen:
                    seen.add(k); fields.append(k)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)


def candidate_key(r: dict):
    return (
        (r.get("ONDERWIJSAANBIEDERID") or r.get("ONDERWIJSBESTUURID") or "").strip(),
        (r.get("ERKENDEOPLEIDINGSCODE") or "").strip(),
    )


def institution(r: dict) -> str:
    return (r.get("ONDERWIJSAANBIEDER_NAAM") or r.get("ONDERWIJSBESTUUR_NAAM") or "").strip()


def names_for_group(rs: list[dict]) -> list[str]:
    vals = set()
    for r in rs:
        for k in ("NAAM_LANG", "INTERNATIONALE_NAAM", "EIGENNAAM", "EIGENNAAM_ENGELS"):
            v = (r.get(k) or "").strip()
            if v:
                vals.add(v)
    return sorted(vals)


def similarity(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


def institution_matches(actual: str, expected: str) -> bool:
    na = norm(actual)
    return any(similarity(na, norm(x)) >= 0.72 for x in INST_ALIASES.get(expected, [expected]))


def choose_pilot_matches(candidates: list[dict]):
    # Mark exactly one best candidate per pilot seed. This is a convenience marker,
    # not a selection criterion for the longlist.
    for idx, (pname, pinst) in enumerate(PILOTS, 1):
        best = None
        best_score = 0.0
        for c in candidates:
            if not institution_matches(c["institution"], pinst):
                continue
            score = max(similarity(pname, n) for n in c["all_registered_names"].split(" | "))
            if score > best_score:
                best, best_score = c, score
        if best is not None and best_score >= 0.58:
            best["pilot_seed"] = f"pilot-{idx:02d}"
            best["pilot_match_score"] = f"{best_score:.3f}"


def main():
    sk = sk123_counts()
    all_rio, rio, fields, delimiter = load_rio()
    write_csv(OUT / "rio_wo_bachelor_fulltime_offerings.csv", rio, fields)

    groups = defaultdict(list)
    for r in rio:
        groups[candidate_key(r)].append(r)

    candidates = []
    for (provider_id, code), rs in groups.items():
        first = rs[0]
        names = names_for_group(rs)
        registered = (first.get("NAAM_LANG") or "").strip() or (first.get("EIGENNAAM") or "").strip()
        locations = sorted({(r.get("ONDERWIJSLOCATIEPLAATS") or "").strip() for r in rs if (r.get("ONDERWIJSLOCATIEPLAATS") or "").strip()})
        languages = sorted({(r.get("VOERTAAL") or "").strip() for r in rs if (r.get("VOERTAAL") or "").strip()})
        websites = sorted({(r.get("WEBSITE") or "").strip() for r in rs if (r.get("WEBSITE") or "").strip()})
        candidates.append({
            "programme": registered,
            "international_name": (first.get("INTERNATIONALE_NAAM") or "").strip(),
            "institution": institution(first),
            "official_programme_code": code,
            "provider_id": provider_id,
            "degree": (first.get("GRAAD") or "").strip(),
            "study_load": (first.get("STUDIELAST") or "").strip(),
            "locations": " | ".join(locations),
            "languages": " | ".join(languages),
            "official_websites": " | ".join(websites),
            "rio_rows": len(rs),
            "all_registered_names": " | ".join(names),
            "pilot_seed": "",
            "pilot_match_score": "",
            "status_checked": TODAY.isoformat(),
            "status_source": "DUO RIO HO Opleidingsoverzicht",
        })

    choose_pilot_matches(candidates)
    candidates.sort(key=lambda x: (norm(x["institution"]), norm(x["programme"])))
    write_csv(OUT / "dutch_wo_bachelor_fulltime_longlist.csv", candidates)

    pilots = [c for c in candidates if c["pilot_seed"]]
    summary = {
        "generated": TODAY.isoformat(),
        "scope": "Current recognised Dutch WO bachelor programmes with a full-time route; no UCR feasibility filter applied.",
        "studiekeuze123": sk,
        "duo_rio": {
            "source": DUO,
            "retrieved": TODAY.isoformat(),
            "delimiter": delimiter,
            "all_rows": len(all_rio),
            "recognised_current_full_time_wo_bachelor_rows": len(rio),
        },
        "deduplicated_programme_institution_candidates": len(candidates),
        "pilot_seeds_found": len(pilots),
        "pilot_seed_matches": [
            {"seed": c["pilot_seed"], "programme": c["programme"], "institution": c["institution"], "code": c["official_programme_code"], "score": c["pilot_match_score"]}
            for c in sorted(pilots, key=lambda x: x["pilot_seed"])
        ],
        "method_notes": [
            "No UCR course evidence was used.",
            "RIO rows with SOORT other than OPLEIDING were excluded so premasters, minors and internal programme components are not mistaken for bachelor programmes.",
            "The longlist is deduplicated by recognised programme code plus education provider; multiple languages/locations remain preserved as metadata.",
            "Studiekeuze123 is used as the public discovery/count benchmark; DUO RIO is used for official programme identity, code and current status.",
        ],
    }
    (OUT / "step1_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# Step 1 — Dutch WO bachelor longlist", "", f"Generated: {TODAY.isoformat()}", "",
        "## Scope", "",
        "Current recognised Dutch WO bachelor programmes with a full-time route. This is an external candidate universe: **no UCR feasibility filtering has been applied**.", "",
        "## Counts", "",
        f"- Studiekeuze123 reports {sk['reported_wo_bachelor_offerings']} WO bachelor offerings, including {sk['reported_full_time_offerings']} with a full-time route.",
        f"- DUO RIO contains {len(rio)} current full-time WO-bachelor offering/location rows after restricting to `SOORT = OPLEIDING`.",
        f"- Deduplication by recognised programme code + provider yields **{len(candidates)} programme/institution candidates**.",
        f"- Existing pilot seeds identified in the official longlist: **{len(pilots)}/10**.", "",
        "## Saved files", "",
        "- `rio_wo_bachelor_fulltime_offerings.csv` — official RIO rows retained for audit/reconstruction.",
        "- `dutch_wo_bachelor_fulltime_longlist.csv` — deduplicated candidate universe for Step 2.",
        "- `step1_summary.json` — source provenance, counts and pilot-seed matches.", "",
        "## Boundary", "",
        "No candidate has been removed because it looks difficult for UCR. UCR feasibility belongs to Step 2. The difference between Studiekeuze123's offering count and the RIO programme/provider count is retained transparently rather than forced away: the two sources use different units (public offerings versus recognised programme/provider records).", "",
    ]
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
