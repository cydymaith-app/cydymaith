"""Print the content tree of a project (group > page > section > concept) with sizes and warnings.

Usage: python .claude/skills/content-tree/tree_report.py [content/<project>] [--group ID] [--lang en]
"""

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

SMALL, LARGE = 4, 10


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project", nargs="?", default=None)
    ap.add_argument("--group")
    ap.add_argument("--lang", default="en")
    args = ap.parse_args()

    root = Path(args.project) if args.project else next(p for p in Path("content").iterdir() if p.is_dir())
    structure = load(root / "structure.json")
    pack = load(root / "packs" / args.lang / "pack.json")
    group_titles = pack.get("groups", {})

    homes = defaultdict(list)
    section_ids = Counter()
    labels = defaultdict(list)
    warnings = []

    for group in structure["groups"]:
        if args.group and group["id"] != args.group:
            continue
        status = f" [{group['status']}]" if group.get("status") else ""
        print(f"GROUP {group['id']} '{group_titles.get(group['id'], '?')}'{status} pages={len(group['pages'])}")
        if len(group["pages"]) == 1:
            warnings.append(f"group {group['id']}: one page, so its tile layer is an extra tap")
        for slug in group["pages"]:
            page = load(root / "pages" / f"{slug}.json")
            pack_file = root / "packs" / args.lang / "pages" / f"{slug}.json"
            words = load(pack_file) if pack_file.exists() else {"sections": {}}
            total = sum(len(s["concepts"]) for s in page["sections"])
            extra = "".join(f" {k}={page[k]}" for k in ("figure",) if k in page)
            print(f"  PAGE {slug} '{words.get('title', '?')}' sections={len(page['sections'])} concepts={total}{extra}")
            if len(page["sections"]) == 1:
                warnings.append(f"page {slug}: one section, so the section heading adds nothing")
            for section in page["sections"]:
                sid = section["id"]
                section_ids[sid] += 1
                sw = words["sections"].get(sid, {})
                n = len(section["concepts"])
                flag = " SMALL" if n < SMALL else " LARGE" if n > LARGE else ""
                held = f" [{section['status']}]" if section.get("status") else ""
                print(f"    {sid:<18} {n:>3}  '{sw.get('title', '?')}'{flag}{held}")
                for cid in section["concepts"]:
                    homes[cid].append(f"{slug}/{sid}")
                    text = sw.get("concepts", {}).get(cid, {}).get("text")
                    if text:
                        labels[text.casefold()].append(f"{slug}/{sid}/{cid}")

    print("\nWARNINGS")
    for w in warnings:
        print(" ", w)
    for sid, n in section_ids.items():
        if n > 1:
            print(f"  section id '{sid}' is used on {n} pages (a repeated twiglet type, not a topic)")
    for cid, where in homes.items():
        if len(where) > 1:
            print(f"  concept {cid} has {len(where)} homes: {', '.join(where)}")
    for text, where in labels.items():
        if len(where) > 1:
            print(f"  label '{text}' ({args.lang}) is shared by: {', '.join(where)}")


if __name__ == "__main__":
    main()
