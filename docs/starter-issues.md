# Starter issues

Maintainers: you do not need to create these by hand. Open the **Actions** tab, choose **Set up labels and issues**, and press **Run workflow**. Leave "dry run" ticked the first time to preview the list, then run it again with the box unticked. It is safe to run twice, because existing issues are skipped. The script is `scripts/bootstrap.py`, and it reads the tables below and in `DECISIONS.md`, `CHALLENGES.md`, and `BOUNTIES.md`.

Events are not created automatically. Create each one after the lab confirms the date.

Once the issues exist, you can delete this file.

| Title | Labels |
|---|---|
| Confirm site approval with the lab and the property owner | `needs owner` |
| Choose the standard gasketed bin (this sets the module size) | `hardware`, `rfc` |
| Design the weather shell around the standard bin | `hardware`, `needs owner` |
| Design the sign and QR code | `docs`, `good first issue` |
| Review the share-alike licenses in `LICENSE.md` before January 31, 2027 | `decision` |
| Add a code of conduct | `docs`, `good first issue` |
| Wishlist: anti-static bags, zip bags, desiccant, labels (standing issue) | `supplies` |
| Power budget for solar, battery, and LED lighting | `electronics`, `needs owner` |
| Pick a battery chemistry and enclosure for outdoor temperatures | `electronics`, `rfc` |
| Sensor node: temperature, humidity, door switch | `electronics`, `needs owner` |
| Choose the radio link: lab Wi-Fi or LoRa | `electronics`, `rfc` |
| Alerts: open an issue when humidity is high or a check is missed | `software`, `needs owner` |
| Simple inventory v1: QR code to a "took / left" form | `software`, `good first issue` |
| AI inventory with an interior camera (privacy review required) | `software`, `rfc` |
| Should any part of the box unlock through GitHub? | `rfc` |
| Set up the weekly check rota | `needs owner` |
| Plan the first build day | `needs owner` |
| Fix anything confusing in the GitHub tutorial | `docs`, `good first issue` |
| Share a design sketch for the box (one issue per sketch is fine) | `hardware`, `good first issue` |
| Suggest a gasketed bin for the standard module, with a store link | `hardware`, `good first issue` |
| Draw a logo a kid would want as a sticker | `docs`, `good first issue` |
| Test the QR code page on your phone and report what is confusing | `docs`, `good first issue` |
| Write the cut list once a shell design is picked (lumber sizes and lengths) | `hardware`, `needs owner` |
| Propose an architecture for the box management software | `software`, `rfc` |
| Design the took and left form | `software`, `good first issue` |

## Decision issues

Create one issue for each open question in `DECISIONS.md`, with the `decision` label, so people have a place to comment. Then replace "Issues tab" in that table with a link to each issue. The two longest ones, the GitHub unlock and battery sharing, have full drafts in [issue-drafts.md](issue-drafts.md).

Also create:

| Title | Labels |
|---|---|
| Box check log (standing issue for weekly check reports) | `needs owner` |
| Build day sign-up (open in February 2027) | `needs owner` |
| One issue per bounty in `BOUNTIES.md`, titled "Bounty (points): job" | `bounty` |
| Confirm with the lab whether parcels can be received, then remove the notice in `ASKS.md` | `needs owner` |

Also create the `ask`, `bounty`, `decision`, `challenge`, and `event` labels. The "Ask for a part" and "This won't work because" forms need their labels to exist.

Create one `challenge` issue for each row in the table in `CHALLENGES.md`, so people can pile on.

## Events

Confirm each date in `docs/events.md` with the lab. For each confirmed event, create an issue with the `event` label so people can give it a thumbs up to say they are coming.

## How to write an easy win

A good easy win is specific enough that someone can do it without asking a question. Say exactly what, how many, and where it goes.

- Vague: "Need wood"
- Clear: "Need two cedar 4x4 posts, 8 feet long, dropped at the lab front desk"

Lumber and hardware easy wins come from the cut list, so they open up as soon as a shell design is picked.
