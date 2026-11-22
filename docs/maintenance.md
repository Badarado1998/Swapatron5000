# Maintenance schedule (proposal)

> **Nothing here is decided.** This is a draft for comment. The schedule starts when the box opens, proposed for Saturday, April 24, 2027.

A swap box only works if someone looks after it. This page is the plan for that, and the place to sign up.

## The recurring schedule

| How often | When | Time needed | People |
|---|---|---|---|
| Weekly check | Any day, Saturday to Monday | 10 minutes | 1 |
| Monthly service | First Saturday of each month | 30 minutes | 1 or 2 |
| Seasonal service | First Saturday of May and of October | 1 to 2 hours | 2 or 3 |
| Yearly review | Around the opening anniversary | A meeting | Everyone |

## Weekly check (10 minutes)

- [ ] Remove anything on the "not welcome" list, especially batteries
- [ ] Remove wet, broken, or unlabeled junk
- [ ] Check the sealed bin lid is closed and the gasket is seated
- [ ] Look at the desiccant indicator color
- [ ] Restock anti-static bags, zip bags, and labels
- [ ] Wipe the door and check the sign is readable
- [ ] Log the check (see below)

## Monthly service (first Saturday)

- [ ] Everything in the weekly check
- [ ] Replace or recharge the desiccant
- [ ] Check hinges, latch, vents, and roof for leaks or damage
- [ ] Check power, lighting, and sensors, once installed
- [ ] Update the wishlist for used-up supplies

## Seasonal service (May and October)

- [ ] Everything in the monthly service
- [ ] Inspect sealant, paint, and gaskets. Reseal if needed
- [ ] Check the mount for movement or rot
- [ ] Empty the box fully, clean it, and sort the stock
- [ ] October only: prepare for winter. Check the roof and door seal before the first freeze
- [ ] May only: check for winter damage

## Yearly review

What worked, what broke, what was taken, what was left. Decide what to change, and write it in [DECISIONS.md](../DECISIONS.md).

## The rota

Each line is one week. Stewards take turns.

| Week starting | Steward (GitHub username) | Done? |
|---|---|---|
| Sat Apr 24, 2027 | Open | |
| Sat May 1, 2027 (monthly and seasonal) | Open | |
| Sat May 8, 2027 | Open | |
| Sat May 15, 2027 | Open | |
| Sat May 22, 2027 | Open | |
| Sat May 29, 2027 | Open | |

### How to take a week

**Easy way:** open an [idea](../../../issues/new?template=idea.yml) with the title "Rota: I'll take the week of [date]". A maintainer adds you.

**Do it yourself:**

1. Tap the pencil icon at the top right of this page.
2. Replace "Open" with your GitHub username on the week you want.
3. Tap **Commit changes**, then **Propose changes**, then **Create pull request**.

### How to log a check

After your check, open the standing "Box check log" issue and leave a comment: the date, what you found, and anything that needs fixing. A photo helps. Each logged check earns a spot on the [Contributors Wall](../CONTRIBUTORS.md).

## If something is wrong

Anyone can report a problem. Scan the QR code on the box, or open a [help issue](../../../issues/new?template=help.yml).

## If nobody takes a week

Two missed weeks in a row is a warning sign. The maintainers will ask for volunteers. If the rota can not be filled for a month, the box should be emptied and closed until it can.

## Alerts (planned)

Once a sensor node is built, it should open an issue when humidity in the sealed bin stays high, when the battery is low, or when no check has been logged in 10 days.
