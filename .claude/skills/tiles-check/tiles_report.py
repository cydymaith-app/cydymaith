"""Print every list of tiles a reader meets, in the order written, and flag repeats, odd contents and odd ordering.

The lists are: the home page (groups), each group (its pages, then the pages it links to), each page's sections and each
page's related row. Each tile is shown with its title in both languages of the edition's default pair, its icon and its level.
Beyond the lists themselves it flags a section that repeats its page (title, id or first word) and an entry that repeats its
page or section title.

Usage: python .claude/skills/tiles-check/tiles_report.py [content/<project>] [--page SLUG ...] [--group ID ...]
                                                         [--no-levels] [--quiet] [--held]
Run it from the repository root. Exit status is 1 when there are problems (notes do not count).
"""

import argparse
import json
import re
import subprocess
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

LONG = 28  # characters; a title longer than this wraps on a phone tile
GRADE_LINE = re.compile(r"^( *)(\S+)\s+level (\d)(\*?)\s")
LIST_LABEL = re.compile(r"(?:^|\s)(and|a|ac|&)(?:\s|$)", re.IGNORECASE)  # "Hot and cold", "Poeth ac oer"


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def norm(text):
    """Compare titles as a reader would: ignore case, accents, spacing and punctuation."""
    text = unicodedata.normalize("NFKD", text.casefold())
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def contains(long, short):
    """Whether the words of `short` open or sit inside `long`, as whole words (both already normalised)."""
    return bool(short) and f" {short} " in f" {long} "


def levels_from_build(root):
    """{(group,) | ("page", slug) | ("section", slug, id): (level, by_hand)} from `python build.py --grades`."""
    out = subprocess.run(
        [sys.executable, "build.py", "--grades", "--project", str(root)], capture_output=True, text=True, encoding="utf-8"
    )
    found, page = {}, None
    for line in out.stdout.splitlines():
        m = GRADE_LINE.match(line)
        if not m:
            continue
        indent, name, level, hand = len(m[1]), m[2], int(m[3]), bool(m[4])
        if indent == 0:
            page = None
            found[(name,)] = (level, hand)
        elif indent == 2:
            page = name
            found[("page", name)] = (level, hand)
        else:
            found[("section", page, name)] = (level, hand)
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project", nargs="?")
    ap.add_argument("--page", action="append", default=[], help="only this page (repeatable)")
    ap.add_argument("--group", action="append", default=[], help="only this group and its pages (repeatable)")
    ap.add_argument("--no-levels", action="store_true", help="do not run the grading")
    ap.add_argument("--quiet", action="store_true", help="print only the findings")
    ap.add_argument("--held", action="store_true", help="also check held-back content (status: development)")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")  # Welsh letters, on a console that is not UTF-8

    root = Path(args.project) if args.project else next(p for p in sorted(Path("content").iterdir()) if p.is_dir())
    structure = load(root / "structure.json")
    edition = load(next((root / "editions").glob("*.json")))
    langs = list(edition.get("default_pair") or [])
    langs += [p.name for p in sorted((root / "packs").iterdir()) if p.is_dir() and p.name not in langs]
    packs = {code: load(root / "packs" / code / "pack.json") for code in langs}
    levels = {} if args.no_levels else levels_from_build(root)

    skel = {p.stem: load(p) for p in sorted((root / "pages").glob("*.json"))}
    words = {
        (code, slug): load(root / "packs" / code / "pages" / f"{slug}.json")
        for code in langs
        for slug in skel
        if (root / "packs" / code / "pages" / f"{slug}.json").exists()
    }
    groups = structure["groups"]

    # -- scope: the names a finding or a list may be tied to
    scope = set(args.page) | set(args.group)
    for slug in args.page:
        if slug not in skel:
            sys.exit(f"no page '{slug}'")
    for gid in args.group:
        g = next((g for g in groups if g["id"] == gid), None)
        if g is None:
            sys.exit(f"no group '{gid}'")
        scope |= set(g.get("pages", []))

    def wanted(where):
        return not scope or bool(set(where) & scope)

    def page_title(code, slug):
        return words.get((code, slug), {}).get("title", "")

    def section_title(code, slug, sid):
        return words.get((code, slug), {}).get("sections", {}).get(sid, {}).get("title", "")

    def entry_texts(code, slug, sid):
        """{concept id: its text(s)} for a section in one language."""
        out = {}
        for cid, c in words.get((code, slug), {}).get("sections", {}).get(sid, {}).get("concepts", {}).items():
            out[cid] = [c["text"]] if c.get("text") else [f.get("text", "") for f in c.get("forms", [])]
        return out

    def page_held(slug):
        sections = skel[slug].get("sections", [])
        return bool(sections) and all(x.get("status") == "development" for x in sections)

    def group_held(g):
        return g.get("status") == "development" or (bool(g.get("pages")) and all(page_held(x) for x in g["pages"] if x in skel))

    problems, notes = [], []

    def flag(bucket, text, *where):
        bucket.append((text, set(where)))

    lists = []  # {"name", "kind", "parent": {code: title}, "tiles": [...], "held", "where"}

    def tile(ident, titles, icon, level, held=False, kind=""):
        return {"id": ident, "titles": titles, "icon": icon, "level": level, "held": held, "kind": kind}

    def lvl(key):
        return levels.get(key, (None, False))

    # -- home
    lists.append(
        {
            "name": "HOME",
            "kind": "group",
            "held": False,
            "where": set(),
            "parent": {},
            "tiles": [
                tile(g["id"], {c: packs[c].get("groups", {}).get(g["id"], "") for c in langs}, g.get("icon"), lvl((g["id"],))[0], group_held(g), "group")
                for g in groups
            ],
        }
    )

    # -- each group
    placed = defaultdict(list)
    for g in groups:
        gt = {c: packs[c].get("groups", {}).get(g["id"], "") for c in langs}
        tiles = []
        for kind, slugs in (("page", g.get("pages", [])), ("link", g.get("links", []))):
            for slug in slugs:
                if slug not in skel:
                    flag(problems, f"group {g['id']}: {kind} '{slug}' has no pages/{slug}.json", g["id"])
                    continue
                if kind == "page":
                    placed[slug].append(g["id"])
                tiles.append(
                    tile(slug, {c: page_title(c, slug) for c in langs}, skel[slug].get("icon"), lvl(("page", slug))[0], page_held(slug), kind)
                )
        lists.append(
            {
                "name": f"GROUP {g['id']}",
                "kind": "page",
                "parent": gt,
                "tiles": tiles,
                "held": group_held(g),
                "where": {g["id"], *g.get("pages", []), *g.get("links", [])},
            }
        )
        if not g.get("pages"):
            flag(problems, f"group {g['id']}: no pages, so its tile opens an empty list", g["id"])
        elif len(g["pages"]) == 1 and not group_held(g):
            flag(notes, f"group {g['id']}: one page, so its tile layer is an extra tap (fine for a deliberate placeholder)", g["id"])
        for slug in sorted(set(g.get("pages", [])) & set(g.get("links", []))):
            flag(problems, f"group {g['id']}: '{slug}' is in both 'pages' and 'links', so it has two tiles", g["id"], slug)

    for slug in skel:
        if not placed[slug]:
            flag(problems, f"page {slug}: in no group, so no tile leads to it", slug)
        if len(placed[slug]) > 1:
            flag(problems, f"page {slug}: listed in more than one group: {', '.join(placed[slug])}", slug)

    if list(packs[langs[0]].get("groups", {})) != [g["id"] for g in groups]:
        flag(notes, f"pack.json ({langs[0]}) lists the groups in a different order from structure.json; only structure.json decides")

    # -- each page: sections, then the related row
    for slug, page in skel.items():
        pt = {c: page_title(c, slug) for c in langs}
        near = {slug}
        sections = page.get("sections", [])
        held_page = page_held(slug)
        lists.append(
            {
                "name": f"SECTIONS of {slug}",
                "kind": "section",
                "held": held_page,
                "where": near,
                "parent": pt,
                "tiles": [
                    tile(s["id"], {c: section_title(c, slug, s["id"]) for c in langs}, None, lvl(("section", slug, s["id"]))[0], s.get("status") == "development", "section")
                    for s in sections
                ],
            }
        )
        if not sections:
            flag(problems, f"page {slug}: no sections", *near)

        # a section that repeats its page, and an entry that repeats its page or section
        if args.held or not held_page:
            for s in sections:
                sid = s["id"]
                if s.get("status") == "development" and not args.held:
                    continue
                if sid == slug:
                    flag(notes, f"page {slug}: its section id '{sid}' is the page's own name, so the address repeats (rename the title, not the id)", *near)
                # each finding is made once, if either language triggers it, and shows the titles in both
                both = lambda f: " / ".join(f(c) for c in langs[:2])  # noqa: E731
                stitles = {c: section_title(c, slug, sid) for c in langs}
                starts, inside, label = False, False, False
                for code in langs:
                    ptitle, stitle = norm(pt[code]), norm(stitles[code])
                    if not (ptitle and stitle) or ptitle == stitle:
                        continue
                    tokens, head = stitle.split(), ptitle.split()
                    if tokens[: len(head)] == head and len(tokens) > len(head) and tokens[len(head)] in ("and", "a", "ac", "with"):
                        starts = True  # "Temperature and humidity" on the page "Temperature"
                    elif contains(stitle, ptitle):
                        inside = True  # "Wind strength" on the page "Wind"
                    if LIST_LABEL.search(stitles[code]):
                        label = True
                shown = both(lambda c: f"'{stitles[c]}'")
                if starts:
                    flag(problems, f"page {slug}: section title {shown} is the page title with more added", *near)
                elif inside:
                    flag(notes, f"page {slug}: section title {shown} repeats the page title inside it (fine if it narrows the topic)", *near)
                if label:
                    flag(notes, f"page {slug}: section title {shown} joins two things; check it predicts everything under it", *near)
                reps = {"page": [], "section": []}
                texts_by = {c: entry_texts(c, slug, sid) for c in langs}
                for cid in texts_by[langs[0]]:
                    for code in langs:
                        for text in texts_by[code].get(cid, []):
                            if text and norm(text) == norm(pt[code]):
                                reps["page"].append(cid)
                            elif text and norm(text) == norm(stitles[code]):
                                reps["section"].append(cid)
                for kind, cids in reps.items():
                    for cid in dict.fromkeys(cids):
                        pair = both(lambda c: f"'{(texts_by[c].get(cid) or ['?'])[0]}'")
                        flag(notes, f"page {slug}/{sid}: entry {pair} repeats the {kind} title", *near)

        related = page.get("related", [])
        tiles, seen = [], set()
        for entry in related:
            target, _, sid = entry.partition("#")
            if target not in skel:
                flag(problems, f"page {slug}: related '{entry}' names a page that does not exist", *near)
                continue
            if target == slug:
                flag(problems, f"page {slug}: related '{entry}' is the page itself", *near)
            if target in seen:
                flag(problems, f"page {slug}: related names '{target}' more than once", *near)
            seen.add(target)
            if sid and sid not in {s["id"] for s in skel[target].get("sections", [])}:
                flag(problems, f"page {slug}: related '{entry}' names a section that page does not have", *near)
                sid = ""
            if sid:
                titles = {c: section_title(c, target, sid) for c in langs}
                level = lvl(("section", target, sid))[0]
            else:
                titles = {c: page_title(c, target) for c in langs}
                level = lvl(("page", target))[0]
            tiles.append(tile(entry, titles, skel[target].get("icon"), level, False, "related"))
        if tiles:
            lists.append({"name": f"RELATED of {slug}", "kind": "related", "parent": pt, "tiles": tiles, "held": held_page, "where": near})
            if len(tiles) > 3:
                flag(notes, f"page {slug}: {len(tiles)} related tiles; a row is meant to be one to three", *near)

    # -- print
    first, second = langs[0], langs[1] if len(langs) > 1 else langs[0]
    if not args.quiet:
        for lst in lists:
            if scope and not wanted(lst["where"]):
                continue
            print(f"{lst['name']} ({len(lst['tiles'])})")
            for i, t in enumerate(lst["tiles"], 1):
                held = " [held back]" if t["held"] else ""
                lv = f"L{t['level']}" if t["level"] else "L-"
                icon = f" {t['icon']}" if t["icon"] else ""
                print(f"  {i:>2}. {t['titles'][first] or '?'} / {t['titles'][second] or '?'}  {lv}{icon}{held}  <{t['kind']} {t['id']}>")

    # -- checks on each list
    for lst in lists:
        if (lst["held"] and not args.held) or (scope and not wanted(lst["where"])):
            continue
        name, parent, where = lst["name"], lst["parent"], lst["where"]
        tiles = [t for t in lst["tiles"] if args.held or not t["held"]]
        for code in langs:
            by_title = defaultdict(list)
            for t in tiles:
                title = t["titles"][code]
                if not title:
                    flag(problems, f"{name}: {t['kind']} '{t['id']}' has no title in {code}", *where)
                    continue
                by_title[norm(title)].append(t["id"])
                if title != title.strip() or title.rstrip().endswith((".", ":", ",")):
                    flag(notes, f"{name}: '{title}' ({code}) has stray spacing or ends in punctuation", *where)
                if len(title) > LONG and t["kind"] != "section":
                    flag(notes, f"{name}: '{title}' ({code}) is {len(title)} characters; it will wrap on a tile", *where)
                if parent.get(code) and norm(title) == norm(parent[code]):
                    flag(problems, f"{name}: '{title}' ({code}) repeats the title of the list it sits in", *where)
            for key, ids in by_title.items():
                if len(ids) > 1:
                    flag(problems, f"{name}: {len(ids)} tiles are titled alike in {code}: {', '.join(ids)}", *where)
        for t in tiles:
            if len(langs) > 1:
                a, b = t["titles"][first], t["titles"][second]
                if a and b and norm(a) == norm(b) and t["kind"] != "section":
                    flag(notes, f"{name}: '{a}' is the same in {first} and {second} (untranslated, or a shared word)", *where)
        icons = defaultdict(list)
        for t in tiles:
            if t["icon"]:
                icons[t["icon"]].append(t["id"])
            elif t["kind"] in ("group", "page", "link", "related"):
                flag(notes, f"{name}: tile '{t['id']}' has no icon", *where)
        for icon, ids in icons.items():
            if len(ids) > 1:
                flag(notes, f"{name}: icon '{icon}' is used by {', '.join(ids)}; they will look alike", *where)
        got = [t["level"] for t in tiles if t["level"]]
        steps = list(zip(got, got[1:]))
        if lst["kind"] in ("page", "section") and any(b > a for a, b in steps) and any(b < a for a, b in steps):
            flag(
                notes,
                f"{name}: levels run {','.join(str(x) for x in got)}, up and down; the written order is the listen-first default, so check it is deliberate",
                *where,
            )

    # -- a title used by different lists at the same level of the tree
    seen = defaultdict(list)
    for lst in lists:
        for t in lst["tiles"]:
            if t["kind"] in ("group", "page", "section") and (args.held or not (t["held"] or lst["held"])):
                seen[(t["kind"], norm(t["titles"][first]))].append((lst["name"], lst["where"], t))
    for (kind, title), uses in seen.items():
        places = {name for name, _, _ in uses}
        where = set().union(*(w for _, w, _ in uses))
        if title and len(places) > 1 and wanted(where):
            line = f"{kind} title '{uses[0][2]['titles'][first]}' ({first}) is used in more than one list: {', '.join(sorted(places))}"
            flag(problems if kind != "section" else notes, line, *where)

    def show(label, bucket):
        lines = list(dict.fromkeys(text for text, where in bucket if wanted(where) or not where and not scope))
        print(f"{label} ({len(lines)})" if lines else f"{label} (none)")
        for line in lines:
            print(" ", line)
        return lines

    print()
    bad = show("PROBLEMS", problems)
    show("NOTES", notes)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
