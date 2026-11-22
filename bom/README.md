# The wishlist (live Bill of Materials)

[BOM.csv](BOM.csv) is the one list of everything the box needs. GitHub shows it as a table you can search.

> **The list is a draft.** The design is not chosen yet, so shell materials and quantities will change. The final wishlist is due by Sunday, February 7, 2027, and the gathering phase runs to March 14. See the [timeline](../ROADMAP.md).
>
> **Safe to pledge now:** anything in the `supplies` category, such as anti-static bags, zip bags, desiccant, and labels. Every design needs those.

## How to give something

1. Find an item in [BOM.csv](BOM.csv) with status `needed` or `partly pledged`.
2. [Open a "Pledge a part" issue](../../../issues/new?template=pledge-a-part.yml) and say what you are giving and how many.
3. Get it to the lab. You can drop it off, or buy it from the store link in the table and ship it. Drop-off and shipping details will be posted here once the site is approved.
4. When the part arrives, a maintainer marks it `received`, closes your issue, and adds you to the [Contributors Wall](../CONTRIBUTORS.md).

Comfortable with GitHub? You can skip the form and edit `BOM.csv` yourself in a pull request. See [Learn GitHub](../docs/learn-github.md), Step 3.

## Why a form and not checkboxes?

On GitHub, only maintainers can tick a checkbox in someone else's list. The pledge form lets anyone with a free account claim an item.

## Columns

| Column | Meaning |
|---|---|
| `item` | What is needed |
| `category` | shell, storage, supplies, signage, power, lighting, sensing |
| `qty_needed` | How many the build needs |
| `qty_pledged` | How many people have promised so far |
| `status` | `needed`, `partly pledged`, `pledged`, or `received` |
| `pledged_by` | GitHub usernames of donors |
| `buy_link` | Optional link to a suitable product at any store |
| `notes` | Specs, open questions, links to issues |

## Rules for the table

- This table is the source of truth. Store wishlists are a convenience and must match it.
- One item per row. Do not delete rows. Mark them `received` instead.
- `received` means the part is physically at the lab.
- No prices and no personal contact details in this file.
