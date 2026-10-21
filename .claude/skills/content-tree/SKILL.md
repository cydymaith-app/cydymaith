---
name: content-tree
description: Critique and reorganise the knowledge tree of a phrasebook project: groups (trunk branches), pages (tiles), sections (twiglets) and concepts (leaves). Use when asked to review how a group's content is organised, where a word or topic belongs, whether pages or sections should be split, merged, moved or renamed, or how a new group (news, sport, geography) should be shaped.
---

# Content tree

## The tree

| Level | In the repository | On screen | Name used here |
|---|---|---|---|
| 1 | a group in `structure.json` | a tile on the home page | branch |
| 2 | a page, `pages/<slug>.json` | a tile inside the group | sub-branch |
| 3 | a section of a page | a heading and a card of rows | twiglet |
| 4 | a concept id in a section | one row | leaf |

The reader is the one in the `listening-layout` skill: a viewer who heard a word and must find it in a few taps. A good tree lets them **guess the right path before they open it**.

## Step 1: Gather

1. Run `python .claude/skills/content-tree/tree_report.py --group <id>` from the repository root. It prints every level with sizes and flags small and large twiglets, single-page groups, single-section pages, repeated section ids, concepts with several homes, and shared labels.
2. Read the `en` and `cy` pack pages for labels, intros and boxes.
3. Read `docs/TODO.md`, `docs/REVIEW.md` and `framework/docs/TODO.md` for planned groups (news, sport, geography) that will need the same leaves.
4. Know the data-model limits (Step 4).

## Step 2: Critique against the checklist

Rate each item **ok / weak / broken**, with file links.

1. **One axis per level.** Siblings are the same kind of thing. Phenomena (rain, wind), framing (when, where), genre (warnings) and mode (speaking) are different axes: mixing them at one level makes paths unguessable.
2. **Labels predict contents.** Each label names a category that covers everything under it, no more and no less. No list labels ("North, south, east and west"), no label narrower than its contents ("Today and tomorrow" holding "next week"), and the same grammatical shape across siblings (nouns, or questions, not both).
3. **Each leaf has one obvious home.** Ask: where would a listener look for this word first? Flag leaves split from their family (storm on one page, thunderstorm on another) and leaves under a misleading parent ("in places" under Landscape).
4. **Shared branches are shared.** Leaves that other groups will need (days, times, compass points, regions, numbers) live in one canonical place and are linked, not copied into each group.
5. **Content kinds kept apart.** Vocabulary, sentence patterns, grammar decoders and speaking phrases are different kinds. A section type repeated on many pages ("In a sentence") is a sign that a kind is scattered and wants its own branch.
6. **A home for the glue.** There is a branch for the words that hold a broadcast together: connectives, extent ("in places", "on the whole"), change verbs (clearing, spreading). Without a home, they never get added.
7. **Balance.** Twiglets of about 4 to 10 leaves. Pages of 2 to 4 twiglets. Fewer than 4 leaves: merge. More than 10: split, or order it so it can be scanned.
8. **Depth earns its taps.** A group with one page, or a page with one section, adds a layer that carries no choice: flatten it. **Exception: deliberate placeholders.** Held-back groups (`status: development`) and the Everyday > Food and drink page (one word, `milk`, kept to show where sections will go and to demonstrate the `llefrith`/`llaeth` regional split) are scaffolding. Mention them at most as "placeholder, not yet filled" and never propose flattening them.
9. **Sibling order.** Each level has one stated order: the running order of the broadcast, a scale, time or compass. The most-used and orienting branches come first.
10. **Ids are stable and honest.** Concept ids match their glosses. Section ids name the topic, not the content kind. Slugs match page titles closely enough to recognise.

## Step 3: Propose a revised tree

1. Draw the **current tree** and the **proposed tree** side by side as indented lists, with leaf counts at each twiglet.
2. For every moved, merged, split or renamed node, say why, citing the checklist item.
3. List the **leaves that move**, as `from page/section → to page/section`.
4. Name any **new branch** and the gap it fills; leave its leaves as candidates (Welsh unreviewed).
5. Show how the proposal fits the agreed listen-first page format (see `listening-layout`).

Stop there. Do not edit content until the user approves the plan.

## Step 4: Data-model limits

Check every proposal against these, and split the plan into content changes and framework changes.

- **A page may be listed in only one group** (`structure.json`; the build fails otherwise). A shared branch reached from several groups needs a framework change: a tile that links to a page in another group.
- **A concept id may appear on several pages**, and search merges them into one entry with links to each page. **But its text lives in each page's pack file**, so a second home duplicates the Welsh and can drift. Prefer one home plus a link, or a framework change for a shared store.
- **Moving a concept changes its address** (`slug.html#section.concept`). Renaming a page slug breaks bookmarks and the installed app's cache. Keep slugs and section ids unless the gain is clear, and say so when they change.
- **`"status": "development"`** holds a page or section back from the release. Use it for new branches while they are drafted.
- **Both packs move together.** Every concept id in `pages/` has an entry in `en` and `cy`, and every new title has both languages.
- **The framework stays language-neutral.** No Welsh and no language names in `framework/`.

## Rules when the plan is approved

- New or changed Welsh (titles included) is a draft: add a line to `docs/REVIEW.md`.
- Keep every leaf. A reorganisation moves, merges or splits; it never silently drops a word. Count leaves before and after.
- Check the build: `python build.py dist`, then `python -m unittest discover -s tests -v`, then rerun `tree_report.py` and confirm the warnings it raised are gone.
- Tick `docs/TODO.md` in the commit that completes an item.
- British spelling.
