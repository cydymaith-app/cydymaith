---
name: tiles-check
description: Sanity check the lists of tiles a reader taps through: the home page's group tiles, each group's page tiles, each page's section list and each related row. Checks contents (missing, empty, orphaned, untitled), repeats (a title that repeats its parent, a sibling, or another list) and ordering (levels, icons). Use when asked to check, audit or tidy the tiles, titles or tile order, after adding or renaming a group, page, section or related link, or before a release.
---

# Tiles check

## What counts as a tile list

| List | Source | Shown as |
|---|---|---|
| `HOME` | groups in `structure.json` | the home page's tiles |
| `GROUP <id>` | the group's `pages`, then its `links` | the tiles inside a group |
| `SECTIONS of <slug>` | `sections` in `pages/<slug>.json` | a topic's sections and its "On this page" list |
| `RELATED of <slug>` | `related` in `pages/<slug>.json` | a topic's row of related tiles |

Titles come from the packs (`pack.json` for groups, `pages/<slug>.json` for pages and sections) in both languages of the edition's default pair. Levels come from `python build.py --grades`.

## Step 1: Run the report

From the repository root:

```
python .claude/skills/tiles-check/tiles_report.py
```

- It prints every list in the order written, each tile as `Welsh / English  L<level> <icon>`, then **PROBLEMS** and **NOTES**.
- `--page <slug>` (repeatable) and `--group <id>` (repeatable) limit the lists and findings to those pages or groups. A page also shows the group list its tile sits in, so its siblings can be compared.
- `--quiet` prints the findings only. `--no-levels` skips the grading. `--held` also checks held-back content (`status: development`), which is otherwise listed but left out of the findings.
- Exit status 1 means there are problems.

## Step 2: Read the findings

**Problems** (fix, or say why not):

- A tile with no title in a language.
- A tile whose title repeats the list it sits in (group `Geography` holding a page `Geography`; a page holding a section of the same name). This is the habit to watch for. It is acceptable only where the layer is deliberate, and then say so.
- A section title that is the page title with more added (page *Temperature*, section *Temperature and humidity*).
- Two siblings with the same title in one language (case, accents and punctuation ignored).
- The same group or page title in more than one list.
- A page in no group, in two groups, or in both `pages` and `links` of one group.
- A group with no pages, a page with no sections, a `related` entry that is missing, repeated or the page itself.

**Notes** (judge, then fix or leave):

- A section id equal to its page's slug (the address repeats; change the title, not the id).
- A section title that contains the page title but narrows it (*Wind strength* on *Wind*): often fine.
- An entry whose text is the page title or the section title (*Tymheredd* on *Tymheredd*). Often a real word to learn, so judge it.
- A section title that joins two things ("Hot and cold", "Temperature and humidity"): a list label, so check it predicts everything under it.
- The same section title on different pages.
- Siblings sharing an icon, or a tile with no icon.
- A title over 28 characters (it wraps on a phone), stray spacing or trailing punctuation.
- A title the same in both languages (an untranslated copy, or a shared word).
- A group with one page, or more than three related tiles.
- Levels that go up and down. The written order is the listen-first default, so this is only a prompt to check it is deliberate. Do not reorder to show a grade (see *Grading* in the `content-tree` skill).

## Step 3: Check by eye what the script cannot judge

The script looks at titles, ids, icons and levels. It does **not** read the words in each entry, so it will not find a section that mixes two ideas, a missing mutated form, an uncertain Welsh word or a gap in vocabulary. Those need the `content-tree` and `listening-layout` skills and a fluent speaker. Read the printed lists for the order:

1. **One order per list.** Running order of the broadcast, a scale, time or compass. Orienting and most-used tiles first.
2. **Siblings the same kind of thing**, in the same grammatical shape.
3. **Titles say what is inside**, and differ from the parent's title.
4. **The same tile in two places is on purpose.** A `links` tile (When, Where under Weather forecast) is a second route to one page, not a copy.
5. Whether **Welsh and English titles mean the same thing** (a fluent speaker's check, for `docs/REVIEW.md`).

## Step 4: Report

1. List each finding with the file to change (`structure.json`, `pages/<slug>.json`, `packs/<code>/pack.json`, `packs/<code>/pages/<slug>.json`).
2. Propose the fix. Do not edit titles or order until the user approves.
3. Renaming a page slug or section id changes addresses and breaks bookmarks and the cached app; change the title, not the id, unless the user asks.
4. Both packs move together: a new title needs both languages.

## Do not flag

- The one-word Everyday > Food and drink page (a placeholder for the `llefrith`/`llaeth` demo).
- Held-back groups, pages and sections, until they are released.

## After a change

1. Run the report again and confirm the findings are gone.
2. `python build.py dist`, then `python -m unittest discover -s tests`.
3. New or changed Welsh titles are drafts: add a line to `docs/REVIEW.md`.
4. British spelling.
