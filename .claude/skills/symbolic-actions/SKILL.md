---
name: symbolic-actions
description: Keep form actions and card controls symbolic, not worded. The reader is scanning words to learn, so the only words on a screen should be the ones being learned. Use when adding or changing a button, a field, a card or a sheet; when asked to review controls, labels or icons; or to audit which controls still carry words.
---

# Symbolic actions

## The rule

**Actions on forms and cards are symbols, not words, wherever a symbol says it.** The reader is learning words from the screen. Every other word competes with the ones that matter, so use as few as possible.

- **Close** is the x (`close`). **Clear a field** is the delete symbol, a left-pointing key with an x (`backspace`). **Search**, **help**, **edit order** and **settings** are already icons in the rail.
- A symbol-only control still has a **name**: `aria-label` and `title`, both from a message, so a screen reader and a long press say what it does. The name is the only place the word lives.
- **Words stay** where a symbol is ambiguous or none exists (a destructive action such as resetting everything, a choice between options, a sentence that explains). Say why in the commit, do not drop the word silently.
- **One control, one symbol.** Hide the browser's own (the search field's native clear button) so there are not two.
- The icons are in `framework/phrasebook/ui-icons/`. A new one needs an entry in `framework/docs/ASSETS.md` (Carbon, or drawn for this site under MIT) and the list in `framework/tests/test_tree.py`.
- Touch size is at least 2.75rem square, as the other icon buttons.
- The rule is in *Conventions followed* in `framework/docs/FRAMEWORK.md` (Form actions).

## Step 1: Audit

1. `python build.py <outdir>` from the repository root.
2. `python .claude/skills/symbolic-actions/actions_report.py <outdir>`.
3. For each control **with words**, decide: symbol, or keep the word and say why.
4. For each control **without words**, check it has `aria-label` and `title` (the report lists them).

The audit of 2026-10-26 found these still worded (the search card's Close and clear are done):

| Control | Words | Likely symbol |
|---|---|---|
| Edit-order bar | Save order, Reset | a tick, and an undo arrow |
| Settings | Reset tile layouts | keep the words: it is a bulk reset |
| Help sheet | What's this?, Report a problem, Copy, Back | question mark, flag or envelope, copy, back arrow |
| About | Share | the share symbol |

## Step 2: Change one control at a time

1. Replace the text with the icon from `ui-icons/`; keep a visible focus ring and the hover state.
2. Add `aria-label` and `title` from the same message the button used to show.
3. Add a test that the control has an icon, a name and no words (see `test_the_search_card_actions_are_symbols_with_names_for_a_screen_reader`).
4. Update the help book text that names the control, and the keys and touch lines.
5. Run the framework tests, then `node --test tests/*.test.js`.
6. Look at it in a browser at phone width, in light and dark, and with forced colours.

## Welsh

- A name shown in both languages (the help sheet's x) needs a Welsh draft in `packs/cy/pack.json` `ui`, and a line in `docs/REVIEW.md`. The search card's names use the interface language, so they have none yet (see `framework/docs/app-help-todo.md`).
- Fewer worded buttons means fewer strings to translate and check. Prefer that over a shorter word.
- British spelling in names and docs.
