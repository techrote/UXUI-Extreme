# AGENTS.md — UXUI-Extreme

Rules for any agent working on this suite. They apply to this repo and to the module forks it coordinates. They do not apply to any other techrote project.

## Read first

1. [RAG.md](RAG.md) — facts, constraints and decisions.
2. [docs/PROGRAMME.md](docs/PROGRAMME.md) — order of work.
3. The owning issue in this repo, including all comments.
4. The module's own upstream conventions (its README/CONTRIBUTING) for code style.
5. Live state: default branches, open PRs and CI runs of the module you will change.

## Who the owner is

The owner directs, judges and tests; they do not write or debug code. Therefore:

- Explain choices as short options with pros/cons, in plain language.
- Never hand them a raw stack trace or build log as their task. Translate failures into what went wrong and what happens next.
- A human test request must be one short card: what to download (exact link), what to try, what "good" looks like, what to reply.
- Windows-first. Builds the owner runs must be portable zips from CI, never "build it yourself".

## Work rules

- **One issue, one branch, one PR.** Task IDs are `UX-###`. Branch names: `ux-###-short-name`.
- **Overview here, detail in the module.** This repo holds the plan ([docs/PROGRAMME.md](docs/PROGRAMME.md)) and checklist. Each work item's full agent instructions, technical notes and progress live in an issue in the module repo it changes; PRs close it with `Closes #N`. Use this repo's issues only for work spanning several modules.
- **Keep the overview current.** When a module issue is created, finished or re-scoped, update its row in PROGRAMME.md (and PARITY.md if a feature's status changed).
- **PRs target the fork, never upstream.** Forks default PRs to the parent repo. Always pass the fork explicitly (for example `gh pr create --repo techrote/RetroBar-Extreme --base master`).
- **Stay mergeable with upstream.** Prefer new files and small, clearly marked hooks into existing code. Do not reformat or reorganise upstream files. Mark fork-only edits with a `// UXUI-Extreme:` comment.
- **Merge when ready.** Squash-merge after the module's own CI is green on the final head and the issue's acceptance criteria are met. Visual/behaviour issues also need the owner's PASS on a CI build, recorded on the issue.
- **Verify the end state.** Confirm the merge landed and default-branch CI is green; don't assume.

## Evidence

Keep these separate and say which you have:

- **compiled** — CI built it;
- **reviewed** — code reasoning only;
- **owner-tested** — the owner ran the exact CI build and reported the result.

A green build proves it compiles, not that it looks or behaves right. Rendering, fonts and colour work are perceptual: the owner's eyes on a real screen are the acceptance test. Never claim owner-tested without their reply.

## Safety

- Nothing in this suite may stop Windows from booting, logging in or restoring its own taskbar and Start menu. Quitting or uninstalling a module must return the stock behaviour.
- Explorer-injecting work (Open-Shell, skinning) is tested in a VM with snapshots before the owner's daily machine.
- Personal use only: no code signing, telemetry, updaters calling home, or store packaging.
