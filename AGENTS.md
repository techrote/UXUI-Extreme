# AGENTS.md — UXUI-Extreme

Rules for any agent working on this suite. They apply to this repo and to the module forks it coordinates. They do not apply to any other techrote project.

## Read first

1. [RAG.md](RAG.md) — facts, constraints and decisions.
2. [docs/PROGRAMME.md](docs/PROGRAMME.md) — order of work.
3. The owning issue in the repository being changed, including all comments and linked dependencies. Module issues normally live in the module; cross-module work lives here.
4. The module's own upstream conventions (its README/CONTRIBUTING) for code style.
5. Live state: default branches, open PRs and CI runs of the module you will change.

## Who the owner is

The owner directs, judges and tests; they do not write or debug code. Therefore:

- Explain choices as short options with pros/cons, in plain language.
- Never hand them a raw stack trace or build log as their task. Translate failures into what went wrong and what happens next.
- A human test request must be one short card: what to download (exact link), what to try, what "good" looks like, what to reply.
- Windows-first. Supply the owner with a verified CI artifact, never "build it yourself". RetroBar tests use portable zips with their runtime prerequisites stated. Open-Shell has no qualified portable package: its installer needs the fork-build and snapshot-VM gates in [docs/BUILD-AND-TEST.md](docs/BUILD-AND-TEST.md) before any owner test.
- Give direct links (artifact downloads, pages, settings) instead of click-path directions wherever a link exists. Post the build link on the issue as soon as CI finishes.
- If the owner must run commands: one copy-paste code block with everything bundled, and every prerequisite, warning and caveat written **before** the block. They paste and press Enter before reading what follows.
- Minimise human steps. If an agent can do it, the agent does it.

## Work rules

- **One issue, one branch, one PR for new work.** Task IDs are `UX-###`; check all coordinated repositories before allocating the next ID. Branch names: `ux-###-short-name`. Preserve historical grouped work such as RetroBar PR #24 and identify every linked work item; do not reopen or split completed history to fit this rule.
- **Overview here, detail in the module.** This repo holds the plan ([docs/PROGRAMME.md](docs/PROGRAMME.md)) and checklist. Each work item's full agent instructions, technical notes and progress live in an issue in the module repo it changes; PRs close it with `Closes #N`. Use this repo's issues only for work spanning several modules.
- **Keep the overview current.** When a module issue is created, finished or re-scoped, update its row in PROGRAMME.md (and PARITY.md if a feature's status changed).
- **PRs target the fork, never upstream.** Forks default PRs to the parent repo. Always pass the fork explicitly (for example `gh pr create --repo techrote/RetroBar-Extreme --base master`).
- **Stay mergeable with upstream.** Prefer new files and small, clearly marked hooks into existing code. Do not reformat or reorganise upstream files. Mark fork-only source hooks with a `UXUI-Extreme:` comment using the language's comment syntax (`//` in C#/C++, `<!-- -->` in XAML/XML). Ordinary documentation edits do not need code-comment markers.
- **Merge when ready.** Squash-merge after the module's own CI is green on the final head and the issue's acceptance criteria are met. Visual/behaviour issues also need the owner's PASS on a CI build, recorded on the issue.
- **Verify the end state.** Confirm the merge landed and default-branch CI is green; don't assume.
- **Umbrella changes.** Run `python3 tools/check_docs.py` and `python3 -m unittest discover -s tests -v`; require the umbrella documentation workflow on the final PR head and merged main. A documentation-only change does not create a new Windows visual-test requirement or establish module acceptance.
- **Inspect workflow side effects before dispatch.** The inherited Open-Shell manual-master path signs and publishes; do not dispatch it unchanged as a build-only check. [UX-020](https://github.com/techrote/Open-Shell-Menu-Extreme/issues/1) owns its replacement.

## Evidence

Keep these separate and say which you have:

- **compiled** — CI built it;
- **reviewed** — code reasoning only;
- **automated-check passed** — name the contract/test, OS, command and exact source; this is neither a visual test nor proof that every behavior works;
- **owner-tested** — the owner ran the exact CI build and reported the result.

A green build proves it compiles, not that it looks or behaves right. Rendering, fonts and colour work are perceptual: the owner's eyes on a real screen are the acceptance test. Never claim owner-tested without their reply.

Link the issue/PR, tested SHA, workflow and artifact when available. Preserve an older owner report as historical evidence for that build; do not transfer it to a newer head. If an older record names only a PR or short SHA, say so. Avoid the ambiguous label "agent-tested"; state what was actually run. Each cross-module status refresh needs a checked date and exact module heads, as in [the audit record](docs/audits/2026-11-04-quality-audit.md).

## Safety

- Nothing in this suite may stop Windows from booting, logging in or restoring its own taskbar and Start menu. Quitting or uninstalling a module must return the stock behaviour.
- Explorer-injecting work (Open-Shell, skinning) is tested in a VM with snapshots before the owner's daily machine.
- Personal use only: no code signing, telemetry, updaters calling home, or store packaging.

These are acceptance requirements. Inherited module code is not automatically compliant: [UX-019](https://github.com/techrote/RetroBar-Extreme/issues/34) and [UX-020](https://github.com/techrote/Open-Shell-Menu-Extreme/issues/1) track updater/build-policy gaps identified in the audit. Preserve upstream licenses, font licenses and attribution in source and test packages.
