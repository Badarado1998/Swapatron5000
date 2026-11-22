# Contributing

Everyone is welcome, including people who have never used GitHub. If that is you, read [Learn GitHub in 15 minutes](docs/learn-github.md) first.

## Ways to contribute

- **Share a design sketch.** A photo of a pencil drawing is welcome. See [hardware/README.md](hardware/README.md).
- **Join a team.** Box design, electronics, box management software, or UI and UX. See the table in the [README](README.md).
- **Pledge parts or supplies.** See [bom/README.md](bom/README.md).
- **Take a task.** Comment "I'll take this" on an issue. A maintainer will assign it to you.
- **Propose an idea.** Open an "Idea" issue before doing a lot of work, so others can weigh in.
- **Improve the docs.** If something confused you, fixing it is a great first pull request.
- **Help on site.** Build days and the weekly check rota are listed in [docs/maintenance.md](docs/maintenance.md).

## The Contributors Wall

Every contribution earns a line in `contributions.csv`, which builds the [Contributors Wall](CONTRIBUTORS.md) and its leaderboard automatically. One contribution is one point, whatever its size or cost.

Maintainers add the line when a part is received, a pull request is merged, or a box check is done:

```
date,username,type,description
2026-12-01,your-username,part,Anti-static bags
```

Types: `part`, `build`, `code`, `docs`, `upkeep`, `idea`. If you would rather not be listed, say so and you will be left off.

## Labels

| Label | Meaning |
|---|---|
| `good first issue` | Small, well described, good for newcomers and kids |
| `hardware` | Shell, modules, mounting |
| `electronics` | Power, lighting, sensors |
| `software` | Inventory, alerts, dashboard |
| `supplies` | Things the box uses up |
| `docs` | Guides, rules, signs |
| `needs owner` | Nobody is working on this yet |
| `rfc` | A bigger decision that needs discussion first |

## Pull requests

- Keep each pull request to one change.
- Say what you changed and why in plain words.
- Changes to the physical box at the first site need a maintainer's approval and the host's approval. See [GOVERNANCE.md](GOVERNANCE.md).

## Safety

- No designs that use mains voltage.
- Battery designs must name the chemistry, the temperature rating, and the enclosure.
- Anything with a camera or microphone must go through an `rfc` issue first.

## Be kind

Many contributors here are learning. Explain, do not scold. A code of conduct will be added before launch.
