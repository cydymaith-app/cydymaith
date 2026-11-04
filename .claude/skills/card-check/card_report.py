"""Print each card (a section of a page) as a reader meets it, top first, and flag what the top promises that the rows do not keep.

A card's top is its title, its stated order (`order`), its intro and its box. The rows are the concepts under it.
The script prints the top, then every row (Welsh / English, with any note and "also heard" forms), then findings
it can see mechanically. The rest is judgement: see SKILL.md, Step 2.

Usage: python .claude/skills/card-check/card_report.py [content/<project>] [--page SLUG ...] [--quiet] [--held]
Run it from the repository root. Exit status is 1 when there are problems (notes do not count).
"""

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

MARK = re.compile(r"\{\{([^}]+)\}\}")
SMALL, LARGE = 3, 10


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def norm(text):
    text = unicodedata.normalize("NFKD", text.casefold())
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9']+", " ", text.replace("’", "'")).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project", nargs="?")
    ap.add_argument("--page", action="append", default=[], help="only this page (repeatable)")
    ap.add_argument("--quiet", action="store_true", help="print only the findings")
    ap.add_argument("--held", action="store_true", help="also check held-back cards (status: development)")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    root = Path(args.project) if args.project else next(p for p in sorted(Path("content").iterdir()) if p.is_dir())
    edition = load(next((root / "editions").glob("*.json")))
    heard = (edition.get("default_pair") or ["cy", "en"])[0]
    other = (edition.get("default_pair") or ["cy", "en"])[1]
    problems, notes = [], []

    for page_file in sorted((root / "pages").glob("*.json")):
        slug = page_file.stem
        if args.page and slug not in args.page:
            continue
        page = load(page_file)
        if page.get("status") == "development" and not args.held:
            continue
        packs = {}
        for code in (heard, other):
            f = root / "packs" / code / "pages" / f"{slug}.json"
            packs[code] = load(f) if f.exists() else {"sections": {}}
        if not args.quiet:
            print(f"\n=== {slug}")
        for section in page["sections"]:
            if section.get("status") == "development" and not args.held:
                continue
            sid = section["id"]
            where = f"{slug}/{sid}"
            h = packs[heard]["sections"].get(sid, {})
            o = packs[other]["sections"].get(sid, {})
            rows = [c for c in section.get("concepts", [])]
            if section.get("figure") and not rows:
                continue
            if not args.quiet:
                print(f"\n--- {where}: {h.get('title', '?')} / {o.get('title', '?')}")
                for label, pack in ((heard, h), (other, o)):
                    print(f"  [{label}] order: {pack.get('order', '(none)')}")
                    if pack.get("intro"):
                        print(f"  [{label}] intro: {pack['intro']}")
                    if pack.get("box"):
                        print(f"  [{label}] box: {pack['box'].get('title', '')}: {pack['box'].get('body', '')}")
                for n, cid in enumerate(rows, 1):
                    a = h.get("concepts", {}).get(cid, {})
                    b = o.get("concepts", {}).get(cid, {})
                    extra = ""
                    if a.get("note"):
                        extra += f"  note: {a['note']}"
                    if a.get("also"):
                        extra += f"  also: {', '.join(a['also'])}"
                    print(f"  {n:>2}. {a.get('text', '?')}  /  {b.get('text', '?')}{extra}")

            # Findings the script can see.
            if not h.get("order"):
                problems.append(f"{where}: the card states no order (`order` in the {heard} pack).")
            if not h.get("title") or not o.get("title"):
                problems.append(f"{where}: a title is missing in one language.")
            for cid in rows:
                for label, pack in ((heard, h), (other, o)):
                    if not pack.get("concepts", {}).get(cid, {}).get("text"):
                        problems.append(f"{where}: row {cid} has no text in {label}.")
            texts = [norm(h.get("concepts", {}).get(cid, {}).get("text", "")) for cid in rows]
            texts += [norm(x) for cid in rows for x in h.get("concepts", {}).get(cid, {}).get("also", [])]
            # An example in the intro or box (marked {{…}} and ending in an ellipsis, or any whole row) should be something the rows show.
            for label, pack in ((heard, h), (other, o)):
                prose = " ".join(filter(None, [pack.get("intro", ""), (pack.get("box") or {}).get("body", "")]))
                for m in MARK.findall(prose):
                    if "…" not in m and "..." not in m:
                        continue
                    stem = norm(m.replace("…", "").replace("...", ""))
                    if stem and not any(stem in t for t in texts):
                        problems.append(f"{where}: the {label} intro shows “{m}” but no row begins or contains it.")
            if len(rows) < SMALL:
                notes.append(f"{where}: only {len(rows)} rows; a card this small may belong with another.")
            if len(rows) > LARGE:
                notes.append(f"{where}: {len(rows)} rows; split it, or say the order so it can be scanned.")
            order = h.get("order", "")
            steps = [s for s in re.split(r",\s*(?:then\s+)?|\s+then\s+", order) if s.strip()]
            if len(steps) > 1 and len(steps) > len(rows):
                notes.append(f"{where}: the order names {len(steps)} steps but there are {len(rows)} rows.")

    print("\nPROBLEMS" if problems else "\nPROBLEMS: none")
    for p in problems:
        print("  - " + p)
    print("NOTES" if notes else "NOTES: none")
    for n in notes:
        print("  - " + n)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
