"""Command-line entry points.

    python -m pec.cli samples ./sample_docs      create the fictional sample corpus
    python -m pec.cli analyze ./folder --name "Full Name" [--engine rules]
    python -m pec.cli dossier out.docx [--supported] [--gaps] [--sources] [--appendix]
    python -m pec.cli report report.docx         full evidence report (audit trail)
"""

from __future__ import annotations

import argparse

from . import queries
from .db import Store
from .pipeline import analyze, ingest_folder


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(prog="pec")
    sub = parser.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("samples")
    s.add_argument("folder")
    a = sub.add_parser("analyze")
    a.add_argument("folder")
    a.add_argument("--name", default="")
    a.add_argument("--engine", default="rules")
    d = sub.add_parser("dossier")
    d.add_argument("output")
    d.add_argument("--supported", action="store_true", help="include supported evidence")
    d.add_argument("--gaps", action="store_true", help="include Evidence Still to Locate")
    d.add_argument("--sources", action="store_true", help="include the full source list")
    d.add_argument("--appendix", action="store_true", help="include an appendix of additional evidence")
    r = sub.add_parser("report")
    r.add_argument("output")
    args = parser.parse_args(argv)

    if args.cmd == "samples":
        from .samples import build

        print(f"Sample documents written to {build(args.folder)}")
        return

    store = Store()
    if args.cmd == "analyze":
        if args.name:
            store.set_setting("candidate_name", args.name)
        outcomes = ingest_folder(store, args.folder)
        print(f"Files: {dict(outcomes)}")
        stats = analyze(store, args.engine, lambda i, n, f: print(f"[{i}/{n}] {f}"))
        c = queries.counts(store)
        print(f"Documents analyzed: {c['documents']}. Evidence items: {c['evidence']}. Items needing review: {c['review']}.")
        for err in stats["errors"]:
            print("Error:", err)
    elif args.cmd == "dossier":
        from .dossier import DossierOptions, dossier_docx, generate

        options = DossierOptions(include_supported=args.supported, include_gaps=args.gaps,
                                 include_source_list=args.sources, include_appendix=args.appendix)
        with open(args.output, "wb") as fh:
            fh.write(dossier_docx(generate(store, options)))
        print(f"Dossier written to {args.output}")
    elif args.cmd == "report":
        from .dossier import full_report_docx

        with open(args.output, "wb") as fh:
            fh.write(full_report_docx(store))
        print(f"Full evidence report written to {args.output}")


if __name__ == "__main__":
    main()
