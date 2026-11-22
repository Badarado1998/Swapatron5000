# Live Bill of Materials

[BOM.csv](BOM.csv) is the single list of everything the box needs. GitHub shows it as a table you can search.

## Columns

| Column | Meaning |
|---|---|
| `item` | What is needed |
| `category` | shell, storage, supplies, signage, power, lighting, sensing |
| `qty_needed` | How many the build needs |
| `qty_pledged` | How many people have promised so far |
| `status` | `needed`, `partly pledged`, `pledged`, or `received` |
| `pledged_by` | GitHub usernames of donors |
| `notes` | Specs, open questions, links to issues |

## Two ways to pledge

**Easy:** open a "Pledge a part" issue. A maintainer updates the table for you.

**Do it yourself:** edit `BOM.csv` in your browser and open a pull request. See [Learn GitHub](../docs/learn-github.md), Step 3.

## Rules for the table

- One item per row. Do not delete rows. Mark them `received` instead.
- A maintainer changes `status` to `received` only when the part is physically at the lab.
- To add something the list is missing, add a new row and explain why in your pull request.
- No prices or personal contact details in this file.

## Dropping off pledged parts

Drop-off details will be posted here once the site is approved.
