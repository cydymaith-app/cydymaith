---
name: listening-layout
description: Critique and restructure a phrasebook topic (weather, news, sport) for a viewer following a Welsh broadcast who pauses and rewinds to look up what they just heard. Use when asked to review the layout, ordering or findability of a section's words and phrases, or to reshape a section "for listening" or "for watching along".
---

# Listening layout

## The reader

A learner watching a broadcast in Welsh, such as the TV weather forecast. They:

- hear a word or phrase, pause, and perhaps rewind;
- know roughly how it sounded, not how it is spelt, and rarely its dictionary form;
- hold a phone in one hand and scan;
- want the meaning in seconds, then resume.

Every judgement in this skill is one question: **can this person get from the sound they heard to its meaning in a few seconds?**

Welsh specifics (mutation decoder, sentence frames, candidate gaps) are in [welsh-listening.md](welsh-listening.md). Read it when the pack is `cy`.

## Step 1: Gather

For the group or page under review, read:

1. `content/<project>/structure.json`: page order within the group.
2. `content/<project>/pages/<slug>.json`: sections, concept ids, any `figure`.
3. `content/<project>/packs/<code>/pages/<slug>.json` for **both** languages: `text`, `forms`, `note`, section `intro` and `box`.
4. `dist/<slug>.html` if built: what the reader actually sees (column order, which text is small print).
5. `framework/phrasebook/dictionary.py`: what search indexes. Today it indexes `text` and `forms` only, **not** notes, intros or boxes.
6. `docs/REVIEW.md`, `docs/TODO.md`, `framework/docs/TODO.md`: known gaps and planned features (for example the language-pair control).

## Step 2: Critique against the checklist

Rate each item **ok / weak / broken**, with file and line evidence.

1. **Direction.** Is the heard language the first, bold, scanning column? A listener scans the language they heard, not the one they know.
2. **Heard forms findable.** Are mutated, plural, contracted and colloquial forms present as `text` or `forms` so search and the eye can find them? Or only in notes and intros, which search ignores?
3. **One decoder, not copies.** Is a grammar explanation written once and linked, or pasted onto several pages? Do its examples match the page it sits on?
4. **Order principle.** Sections follow the broadcast's running order. Within a section there is one visible principle: an intensity scale, a time sequence, compass order, or alphabetical order in the heard language. Arbitrary order is **broken**.
5. **Section size.** About 8 to 10 rows at most. Longer lists are split or alphabetised.
6. **Word families together.** Noun, plural, adjective and verb of one root are adjacent, or in one row.
7. **Sentences decomposable.** Sentences are taught as frames with slots that point to the vocabulary, glossed literally enough to segment the heard language. Whole fixed sentences that will never be heard verbatim are low value.
8. **Coverage of what is actually said.** Connectives, verbs of change, time and place prepositions, the presenter's opening and closing, common colloquial forms. Listening content is kept apart from speaking content (asking questions, small talk).
9. **Gloss accuracy and uniqueness.** Each gloss matches its own entry. No two different entries share one gloss. Concept ids match their glosses.
10. **Legibility.** Anything needed to match a sound is in normal-sized text, not a small note.

## Step 3: Propose the listen-first format

Recommend this target, adapted to the section:

**Accepted reference:** `docs/mockups/listening-rain.html` and `docs/mockups/listening-football.html`. Match them.

1. **Heard language first, on one line.** Welsh bold on the left, English on the right of the same row, so a row costs one line of height. "Also heard" chips sit under the row, full width. Interim, content-only: none. Proper fix: the language-pair control in `framework/docs/TODO.md`, or `default_pair` in the edition (a site-wide decision for the user).
2. **One row per word family**, with an "also heard as" line holding mutated, plural and colloquial forms, each searchable.
3. **Sections in running order**, each with a stated order: scale, time, compass, or alphabetical.
4. **A frames page** replacing per-page "in a sentence" lists: each frame (`Bydd hi'n ___`) with a literal gloss, two or three real examples, and links to the pages that fill the slot.
5. **One mutation decoder**, linked from every page: "heard a word you cannot find? Change the first letter like this."
6. **Listening and speaking separated**: conversational pages are labelled or moved out of the broadcast group.
7. **Glosses with a literal line** for sentences: natural English, then word-by-word.

Map every proposal to the data model and say which side it falls on:

| Kind | Where | Example |
|---|---|---|
| Content only | `pages/`, `packs/`, `structure.json` | reorder concepts, split a section, add frames page, add concepts, fix glosses, move an `intro` to one page |
| Content using an existing feature | `forms`, `box`, `figure`, `status: development` | a form without `varieties` for a common alternative; hold a new page back while drafting |
| Framework change | `framework/` submodule, own repository | an indexed "also heard as" field; search over notes; heard-language-first layout; collation |

Framework proposals must stay language-neutral: no Welsh and no language names in `framework/`.

## Step 4: Output

Deliver, in this order:

1. **Checklist table**: item, rating, evidence (file links with line numbers).
2. **Defects**: concrete bugs (duplicate glosses, copied intros, mismatched ids), each with a file link.
3. **Proposed format**: one real section from the group redrawn in the new format as a markdown table, with its order principle named.
4. **Change plan**, split into content changes (this repository) and framework changes (submodule, separate commit and pull request).

Stop there. Do not edit content until the user approves the plan.

## Rules when the plan is approved

- **New or changed Welsh is a draft.** Mark its source `draft`, add a line to `docs/REVIEW.md`, and say plainly which items are uncertain. Never present new Welsh as reviewed.
- **Keep packs in step.** Every concept id in `pages/*.json` has an entry in both `en` and `cy` packs.
- **Keep the framework neutral.** Mutation tables, frames and examples live in content, never in `framework/`.
- **Check the build:** `python build.py dist`, then `python -m unittest discover -s tests -v`.
- **Tick `docs/TODO.md`** in the commit that completes an item.
- British spelling.
