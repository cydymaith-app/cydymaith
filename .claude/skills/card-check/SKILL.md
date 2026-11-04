---
name: card-check
description: Check that a card (a section of a page) keeps the promises its top makes. Reads the title, the stated order, the intro and the box, then tests every row against them. Run it whenever a page or card is added or changed, and as part of any listening-layout review.
---

# Card check

## The question

A card's **top** is its title, its stated order (*Order: …*), its intro and its box. Each is a promise to the reader.

**Does every row keep the promises the top makes?**

Worked example, `patterns/place-first` (first titled *Putting the place first*, order *where, then when, then what was seen, then what is in charge*; since retitled *Putting the main thing first* and reordered):

| Row | Promise kept? |
|---|---|
| *Y gorllewin fydd yn gweld y gwaetha* | Where. Yes. |
| *Dros nos fydd yn gweld …* | **When**, not a place. The title says place. |
| *Y gogledd welodd orau'r heulwen* | Where again, **after** when. Order broken. |
| *Gwasgedd uchel sy'n dechrau rheoli* | A thing in charge, not a place. The title says place. |

Two failures: the order is not followed, and the title is narrower than the contents.
The fix is one of: reorder, retitle (*Putting the key word first*), or split the card.

## Step 1: Run the report

From the repository root:

```
python .claude/skills/card-check/card_report.py --page <slug>
```

- Prints each card's top, then each row (Welsh / English, note, "also heard" forms).
- `--quiet` prints the findings only. `--held` includes held-back cards. Omit `--page` to check every page.
- Exit status 1 means problems.
- **Problems the script finds:** no stated order, a missing title or row text, an intro example (`{{… …}}`) that no row shows.
- **Notes:** very small or large cards, an order with more steps than rows.

## Step 2: Judge, row by row

The script cannot read meaning. Do this by hand for every card added or changed.

1. **Title.** Does it cover every row, no more and no less? Is there a row it does not describe?
2. **Order.** Say the stated order aloud. Walk the rows. Does each row fall in a step, and are the steps in sequence?
   - A step with no rows is a promise broken, or an order that is too long.
   - A row that fits no step means the order or the card is wrong.
   - Alphabetical cards are checked by `OrderOfACardTests`. Do not re-check them.
3. **Intro.** Is each claim true of the rows? Is each example (`{{… …}}`) one of the rows, or a plain part of one? Does it name the right words (*fydd*, *sy'n*, *welodd*) and do the rows use them?
4. **Box.** Does it explain something in this card's rows, with examples from them?
5. **Rows against each other.** Same kind of thing, same shape. A row of another kind belongs elsewhere (see `content-tree`, item 5).
6. **Notes and "also" forms.** Each note is about its own row. Each "also heard" form belongs to that row.
7. **Glosses.** The English matches its own Welsh. The same words are not glossed twice (see `listening-layout`, item 9).
8. **Size.** About 4 to 10 rows.

Rate each card **ok / weak / broken**. A broken promise is **broken**.

## Step 3: Report

1. One line per card: `page/section`, rating, and which promise failed with the row.
2. Propose one fix: reorder, retitle, edit the intro, or split. Give the reason in a line.
3. If two fixes would give different cards, ask the developer (as in *Ordering a card*, `content-tree`).
4. Do not edit until approved, unless the user asked for the fix.

## After a change

1. Rerun the report: no problems.
2. A new or changed title, order or intro is Welsh-side commentary or English: both packs move together.
3. New or changed Welsh is a draft: add a line to `docs/REVIEW.md`.
4. `python build.py dist`, then `python -m unittest discover -s tests`.
5. British spelling.

## Do not flag

- The one-word Everyday > Food and drink card (placeholder).
- Held-back cards (`status: development`) until released.
- Typos or missing circumflexes in S4C subtitles: they are noise.
