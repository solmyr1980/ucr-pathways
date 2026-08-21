#!/usr/bin/env python3
"""Build Step 1: external Dutch full-time WO-bachelor candidate universe.

No UCR course evidence is consulted here.
Discovery/count benchmark: Studiekeuze123.
Official identity/status/code source: DUO RIO HO Opleidingsoverzicht.
"""
from __future__ import annotations

import csv, datetime as dt, difflib, html, io, json, re, time, unicodedata, urllib.request
from collections import defaultdict
from pathlib import Path

TODAY = dt.date.today()
OUT = Path("research/comparator_longlist")
OUT.mkdir(parents=True, exist_ok=True)
SK123 = "https://www.studiekeuze123.nl/opleidingen/categorie/wo-bachelor-opleidingen"
DUO = "https://onderwijsdata.duo.nl/dataset/7c0686f4-b5c2-418e-8e44-7be0057d8084/resource/ffffa7ad-e6a2-4ba7-9fc2-a09df4128555/download/ho_opleidingsoverzicht.csv"
UA = "Mozilla/5.0 (compatible; UCR-Pathways-research/1.0; +https://github.com/solmyr1980/ucr-pathways)"

PILOTS = [
    ("Psychobiologie", ["Universiteit van Amsterdam"]),
    ("Environmental Sciences", ["Wageningen University", "Wageningen University & Research"]),
    ("Informatica", ["Universiteit Utrecht", "Utrecht University"]),
    ("Health Sciences", ["Universiteit Maastricht", "Maastricht University"]),
    ("Kunstgeschiedenis", ["Universiteit Utrecht", "Utrecht University"]),
    ("Rechtsgeleerdheid", ["Universiteit Utrecht", "Utrecht University"]),
    ("Biologie", ["Universiteit Utrecht", "Utrecht University"]),
    ("Business Administration", ["Universiteit van Amsterdam"]),
    ("Psychology", ["Tilburg University"]),
    ("Communicatiewetenschap", ["Universiteit van Amsterdam"]),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c)).lower().replace("&", " en ")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", s)).strip()


def sim(a, b):
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


def fetch(url, binary=False):
    err = None
    for i in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"})
            with urllib.request.urlopen(req, timeout=120) as r:
                raw = r.read()
                return raw if binary else raw.decode(r.headers.get_content_charset() or "utf-8", errors="replace")
        except Exception as e:
            err = e; time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"Could not fetch {url}: {err}")


def visible_text(x):
    x = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", x, flags=re.I | re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x))).strip()


def sk_counts():
    t = visible_text(fetch(SK123))
    def n(p):
        m = re.search(p, t, re.I); return int(m.group(1)) if m else None
    return {
        "source": SK123,
        "retrieved": TODAY.isoformat(),
        "reported_wo_bachelor_offerings": n(r"Wo bachelor\s+(\d+)"),
        "reported_full_time_offerings": n(r"Voltijd\s+(\d+)"),
        "reported_part_time_offerings": n(r"Deeltijd\s+(\d+)"),
    }


def date(s):
    s = (s or "").strip()
    if not s: return None
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%Y%m%d"):
        try: return dt.datetime.strptime(s[:10], fmt).date()
        except ValueError: pass
    return None


def current(r):
    # The DUO dataset already describes current/future offerings. Exclude only
    # records whose recognised programme or offered programme explicitly ended.
    for k in ("EINDDATUM", "AANGEBODEN_OPLEIDING_EINDDATUM"):
        d = date(r.get(k, ""))
        if d and d < TODAY: return False
    return True


def load_rio():
    text = fetch(DUO, binary=True).decode("utf-8-sig", errors="replace")
    try: delim = csv.Sniffer().sniff(text[:12000], delimiters=";,\t|").delimiter
    except csv.Error: delim = ";"
    rdr = csv.DictReader(io.StringIO(text), delimiter=delim)
    all_rows = list(rdr); fields = rdr.fieldnames or []
    rows = []
    for r in all_rows:
        # RIO's documented SOORT values are OPLEIDING and VARIANT. Both can be
        # real public bachelor choices. Requiring an ERKENDEOPLEIDINGSCODE drops
        # unrecognised internal components such as premasters/minors.
        if (r.get("SOORT") or "").strip().upper() not in {"OPLEIDING", "VARIANT"}: continue
        if (r.get("NIVEAU") or "").strip().upper() != "WO-BA": continue
        if "VOLTIJD" not in (r.get("VORM") or "").upper(): continue
        if not (r.get("ERKENDEOPLEIDINGSCODE") or "").strip(): continue
        if not current(r): continue
        rows.append(r)
    return all_rows, rows, fields, delim


def write_csv(path, rows, fields=None):
    if fields is None:
        fields=[]; seen=set()
        for r in rows:
            for k in r:
                if k not in seen: seen.add(k); fields.append(k)
    with Path(path).open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=fields, extrasaction="ignore"); w.writeheader(); w.writerows(rows)


def key(r):
    # Variant identity lives in OPLEIDINGSEENHEIDCODE; recognised programme code
    # alone would incorrectly collapse e.g. distinct public programme variants.
    return (
        (r.get("ONDERWIJSAANBIEDERID") or r.get("ONDERWIJSBESTUURID") or "").strip(),
        (r.get("OPLEIDINGSEENHEIDCODE") or r.get("ERKENDEOPLEIDINGSCODE") or "").strip(),
    )


def inst(r):
    return (r.get("ONDERWIJSAANBIEDER_NAAM") or r.get("ONDERWIJSBESTUUR_NAAM") or "").strip()


def group_names(rs):
    vals=set()
    for r in rs:
        for k in ("NAAM_LANG", "INTERNATIONALE_NAAM", "EIGENNAAM", "EIGENNAAM_ENGELS"):
            v=(r.get(k) or "").strip()
            if v: vals.add(v)
    return sorted(vals)


def mark_pilots(cands):
    # Institution matching is exact after normalization; programme matching may
    # bridge Dutch/English names. Exactly one best candidate is marked per seed.
    for idx, (pname, institutions) in enumerate(PILOTS, 1):
        allowed={norm(x) for x in institutions}
        best=None; score=-1
        for c in cands:
            if norm(c["institution"]) not in allowed: continue
            s=max(sim(pname, x) for x in c["all_registered_names"].split(" | "))
            if s>score: best,score=c,s
        if best and score>=0.58:
            best["pilot_seed"]=f"pilot-{idx:02d}"; best["pilot_match_score"]=f"{score:.3f}"


def main():
    sk=sk_counts(); all_rio,rio,fields,delim=load_rio()
    write_csv(OUT/"rio_wo_bachelor_fulltime_offerings.csv", rio, fields)

    groups=defaultdict(list)
    for r in rio: groups[key(r)].append(r)
    cands=[]
    for (provider, unitcode),rs in groups.items():
        f=rs[0]; names=group_names(rs)
        programme=(f.get("EIGENNAAM") or f.get("NAAM_LANG") or "").strip()
        cands.append({
            "programme": programme,
            "registered_name": (f.get("NAAM_LANG") or "").strip(),
            "international_name": (f.get("INTERNATIONALE_NAAM") or "").strip(),
            "institution": inst(f),
            "kind": (f.get("SOORT") or "").strip(),
            "official_programme_code": (f.get("ERKENDEOPLEIDINGSCODE") or "").strip(),
            "rio_programme_unit_code": unitcode,
            "provider_id": provider,
            "degree": (f.get("GRAAD") or "").strip(),
            "study_load": (f.get("STUDIELAST") or "").strip(),
            "locations": " | ".join(sorted({(r.get("ONDERWIJSLOCATIEPLAATS") or "").strip() for r in rs if (r.get("ONDERWIJSLOCATIEPLAATS") or "").strip()})),
            "languages": " | ".join(sorted({(r.get("VOERTAAL") or "").strip() for r in rs if (r.get("VOERTAAL") or "").strip()})),
            "official_websites": " | ".join(sorted({(r.get("WEBSITE") or "").strip() for r in rs if (r.get("WEBSITE") or "").strip()})),
            "rio_rows": len(rs),
            "all_registered_names": " | ".join(names),
            "pilot_seed": "", "pilot_match_score": "",
            "status_checked": TODAY.isoformat(), "status_source": "DUO RIO HO Opleidingsoverzicht",
        })
    mark_pilots(cands)
    cands.sort(key=lambda x:(norm(x["institution"]),norm(x["programme"]),norm(x["kind"])))
    write_csv(OUT/"dutch_wo_bachelor_fulltime_longlist.csv", cands)

    pilots=sorted([c for c in cands if c["pilot_seed"]], key=lambda x:x["pilot_seed"])
    kinds={k:sum(1 for c in cands if c["kind"].upper()==k) for k in ("OPLEIDING","VARIANT")}
    summary={
        "generated":TODAY.isoformat(),
        "scope":"Current recognised Dutch WO bachelor offerings with a full-time route; no UCR feasibility filter applied.",
        "studiekeuze123":sk,
        "duo_rio":{"source":DUO,"retrieved":TODAY.isoformat(),"delimiter":delim,"all_rows":len(all_rio),"retained_full_time_wo_bachelor_rows":len(rio)},
        "deduplicated_public_candidates":len(cands),
        "candidate_kinds":kinds,
        "pilot_seeds_found":len(pilots),
        "pilot_seed_matches":[{"seed":c["pilot_seed"],"programme":c["programme"],"institution":c["institution"],"kind":c["kind"],"code":c["official_programme_code"],"score":c["pilot_match_score"]} for c in pilots],
        "method_notes":[
            "No UCR course evidence was used.",
            "Both recognised HO programmes and recognised HO programme variants are retained because variants can be separate public study choices.",
            "Rows without an ERKENDEOPLEIDINGSCODE are excluded; this prevents internal components such as premasters/minors from entering the bachelor universe.",
            "Rows are deduplicated by provider plus RIO programme-unit code, preserving distinct variants while collapsing duplicate language/location records.",
            "Studiekeuze123 supplies the public benchmark count; DUO RIO supplies official identity, status and codes."
        ]}
    (OUT/"step1_summary.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")

    lines=["# Step 1 — Dutch WO bachelor longlist","",f"Generated: {TODAY.isoformat()}","",
      "## Scope","","Current recognised Dutch WO bachelor offerings with a full-time route. This is an external candidate universe: **no UCR feasibility filtering has been applied**.","",
      "## Counts","",
      f"- Studiekeuze123 reports **{sk['reported_wo_bachelor_offerings']}** WO bachelor offerings, including **{sk['reported_full_time_offerings']}** with a full-time route.",
      f"- DUO RIO contributes {len(rio)} current full-time WO-bachelor rows after retaining recognised `OPLEIDING` and `VARIANT` records.",
      f"- Deduplication by provider + RIO programme-unit code yields **{len(cands)} public programme/variant candidates** ({kinds['OPLEIDING']} programmes; {kinds['VARIANT']} variants).",
      f"- Existing pilot seeds identified: **{len(pilots)}/10**.","",
      "## Saved files","","- `rio_wo_bachelor_fulltime_offerings.csv` — official retained RIO rows.","- `dutch_wo_bachelor_fulltime_longlist.csv` — deduplicated candidate universe for Step 2.","- `step1_summary.json` — provenance, counts and pilot matches.","",
      "## Boundary","","No candidate has been removed because it looks difficult for UCR. UCR feasibility belongs to Step 2. Any remaining difference from the Studiekeuze123 count is retained transparently for reconciliation rather than resolved by subjective selection.",""]
    (OUT/"README.md").write_text("\n".join(lines),encoding="utf-8")
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=="__main__": main()
