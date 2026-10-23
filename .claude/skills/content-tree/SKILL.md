---
name: content-tree
description: Critique and reorganise the knowledge tree of a phrasebook project: groups (trunk branches), pages (tiles), sections (twiglets) and concepts (leaves). Use when asked to review how a group's content is organised, where a word or topic belongs, whether pages or sections should be split, merged, moved or renamed, or how a new group (news, sport, geography) should be shaped. Also use it to grade tiles and sections from beginner to advanced, check the grades (`python build.py --grades`), or decide whether a level should be set by hand.
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

## Grading: beginner to advanced

Every group, page and section has a level from 1 (beginner) to 3 (advanced), so tiles and sections can be ordered simple first or advanced first. The level is **worked out from the content, not decided by feel**; the rule is `framework/phrasebook/grading.py` and the reference is *Grading* in `framework/docs/FRAMEWORK.md`. Use it when new content is added, when content is moved between sections or pages, and when asked to grade or review the grades.

**What the rule does.** The level follows the median number of words per entry in the language being heard (Welsh here). Under 1.5 words is level 1 (words: *gogledd*, north), under 2.5 is level 2 (short phrases: *Yng Nghymru*, in Wales), and more is level 3 (*Yn y gogledd*, in the north; sentences such as *Bydd hi'n heulog yfory*). A group is graded from every entry on the pages it lists, a page from every entry on it, a section from its own, so a page's level is not the average of its sections.

**How to grade the current content.**

1. Run `python build.py --grades` from the repository root. It prints every group, page and section with its level, median and entry count, builds nothing, and covers what the release publishes (add `--channel development` for held-back sections).
2. Read it as a learner would: single words should come before the phrases built on them, and sentence patterns last. The user's own example: *north = gogledd* is simple; *from the north-east* is more complex and follows for a beginner.
3. Only where the rule is **plainly wrong** set `"level": 1`, `2` or `3` on that group (`structure.json`), page or section (`pages/<slug>.json`). The usual cause is a closed set of beginner vocabulary written as several words, such as the days (*Dydd Llun* is one item to learn, set to 1 in `pages/when.json`). A long single word, a colloquial form or a note about mutation is not by itself a reason to override. If many sections need correcting, the bounds are wrong: change `grading.bounds` in the edition instead.
4. Say why in `tests/test_project.py` (`GradingTests`), which also keeps the number of hand-set levels small (five at most) and checks the user's examples: points below directions and landscape, sentence patterns level 3, single-word pages level 1.
5. The grades are a judgement about difficulty: add a line to `docs/REVIEW.md` so a fluent speaker reviews them with the Welsh.

**What the grades do in the app.** Every tile and topic section carries its level (`data-level`), and **Settings** offers *Default* (as written: the listen-first order, and what everyone gets until they choose), *Simplest first* and *Most advanced first*; `assets/order.js` puts tiles, sections and the "On this page" list in order before the page is painted, and in the copy of a page that slides in. A person's own arranged tile order wins over the setting, the same level keeps the written order, and *Most advanced first* is the levels reversed (phrases before words, which is what the user asked for: more advanced users may want the other way round). So **do not reorder `structure.json` or the pages to show a grade**: the written order is the listen-first order and the default. A section with no level (a figure) stays where it is.

**Keep the framework neutral.** No Welsh, and no language names, in `framework/`; the counting is by white space, which does not suit a language written without spaces (set `grading.bounds` or levels by hand there).

## Rules when the plan is approved

- New or changed Welsh (titles included) is a draft: add a line to `docs/REVIEW.md`.
- Keep every leaf. A reorganisation moves, merges or splits; it never silently drops a word. Count leaves before and after.
- Check the build: `python build.py dist`, then `python -m unittest discover -s tests -v`, then rerun `tree_report.py` and confirm the warnings it raised are gone.
- If content moved or was added, run `python build.py --grades` and check the levels of what changed (see *Grading*).
- Tick `docs/TODO.md` in the commit that completes an item.
- British spelling.
