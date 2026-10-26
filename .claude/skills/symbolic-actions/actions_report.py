"""List the controls in a built site that carry visible words, so each can be judged: should it be a symbol?

Usage: python build.py <outdir> (from the repository root), then
       python .claude/skills/symbolic-actions/actions_report.py <outdir>

Looks at every <button>, and every <a> or <input> that acts as a button (role="button", type=button/submit), on every page.
A control counts as "words" when, after taking out its icon, it still shows letters. Words that are only for a screen
reader (class sr-only) are not visible words. Prints each distinct control once, with the pages it is on.
Exit status is 0: this is a prompt for judgement, not a pass/fail test.
"""

import re
import sys
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path

VOID = {"input", "br", "img", "meta", "link", "hr"}


class Controls(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.found = []  # (key, visible text, has icon)
        self.stack = []  # open controls: [tag, key, text parts, icon]
        self.hidden = 0  # depth inside sr-only or svg
        self.skip = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get("class") or "").split()
        if tag in VOID:
            if tag == "input" and a.get("type") in ("button", "submit", "reset") and a.get("value"):
                self.found.append((f"input[{a.get('type')}] {a.get('id') or ''}".strip(), a["value"], False))
            return
        if self.stack:
            if tag == "svg":
                self.stack[-1][3] = True
            if "sr-only" in cls or tag == "svg":
                self.skip.append(tag)
            elif self.skip:
                self.skip.append(tag)
        if tag == "button" or (tag == "a" and a.get("role") == "button"):
            key = tag + ("." + ".".join(cls) if cls else "") + "".join(f"[{k}]" for k in a if k.startswith("data-act") or k == "data-arrange-done" or k == "data-arrange-reset")
            self.stack.append([tag, key, [], False])

    def handle_endtag(self, tag):
        if self.skip and self.skip[-1] == tag:
            self.skip.pop()
        if self.stack and self.stack[-1][0] == tag and not self.skip:
            _, key, parts, icon = self.stack.pop()
            self.found.append((key, " ".join("".join(parts).split()), icon))

    def handle_data(self, data):
        if self.stack and not self.skip:
            self.stack[-1][2].append(data)


def main():
    if len(sys.argv) != 2 or not Path(sys.argv[1]).is_dir():
        sys.exit(__doc__)
    sys.stdout.reconfigure(encoding="utf-8")
    seen = defaultdict(set)
    for page in sorted(Path(sys.argv[1]).glob("*.html")):
        parser = Controls()
        parser.feed(page.read_text(encoding="utf-8"))
        for key, text, icon in parser.found:
            seen[(key, text, icon)].add(page.name)
    words = {k: v for k, v in seen.items() if re.search(r"[^\W\d_]", k[1])}
    symbols = {k: v for k, v in seen.items() if k not in words}
    print(f"CONTROLS WITH WORDS ({len(words)}): judge each; a symbol is better where one says it")
    for (key, text, icon), pages in sorted(words.items()):
        where = f"{len(pages)} pages" if len(pages) > 3 else ", ".join(sorted(pages))
        print(f"  {key}: '{text}'{' (with an icon)' if icon else ''}  [{where}]")
    print(f"CONTROLS WITH NO VISIBLE WORDS ({len(symbols)}): each needs aria-label and title")
    for (key, text, icon), pages in sorted(symbols.items()):
        print(f"  {key}{' (icon)' if icon else ''}")


if __name__ == "__main__":
    main()
