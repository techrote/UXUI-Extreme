# Programme

Order of work across the suite. Module issues contain implementation instructions and progress; this page is the overview. **Reconciled 4 November 2026** against the module heads in the [audit record](audits/2026-11-04-quality-audit.md). Historical owner reports apply to their tested builds, not automatically to current `master`.

## Phase 0 — Workshop and qualification

| Work | Status and next step |
|---|---|
| Umbrella rules, plan and evidence | [UX-018](https://github.com/techrote/UXUI-Extreme/issues/5): [PR #7](https://github.com/techrote/UXUI-Extreme/pull/7) delivered initial reconciliation; [PR #8](https://github.com/techrote/UXUI-Extreme/pull/8) extends build/evidence corrections and consolidates the checks. The concurrent [issue #6](https://github.com/techrote/UXUI-Extreme/issues/6) is retained as closed history. |
| RetroBar build route | Portable artifacts and installer CI passed at `65b36c0`; [exact downloads and runtime prerequisites](BUILD-AND-TEST.md). |
| RetroBar upstream updater | [UX-019](https://github.com/techrote/RetroBar-Extreme/issues/34), [draft PR #35](https://github.com/techrote/RetroBar-Extreme/pull/35): application and installer probes repaired at `497379a`; [all four Windows workflows passed](https://github.com/techrote/RetroBar-Extreme/issues/34#issuecomment-6620164980). Owner acceptance and module merge remain pending. |
| Open-Shell fork build and offline policy | [UX-020](https://github.com/techrote/Open-Shell-Menu-Extreme/issues/1): unsigned, non-publishing CI; reconcile inherited updater; produce a qualified installer. No fork CI evidence was available at inspection. |
| Windows VM with snapshots | Still required before Open-Shell/other Explorer-injecting tests. Record install, login, exit, uninstall and stock-shell recovery on the exact Windows build before any daily-machine test. |

The Open-Shell inherited manual workflow includes signing and release publication; it must not be dispatched unchanged to satisfy the build requirement. See [BUILD-AND-TEST](BUILD-AND-TEST.md).

## Phase 1 — RetroBar implementation and acceptance

The newest observed personal prerelease is [v1.23.43-extreme-delta.1](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.43-extreme-delta.1), whose tag resolves to inspected `master` `65b36c0`. Earlier alpha releases are historical, not the current task list. This is a prerelease label, not a declaration of production readiness.

Historical release sequence: [alpha 1](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.31-extreme-alpha.1) → [alpha 2](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.32-extreme-alpha.2) → [alpha 3](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.34-extreme-alpha.3) → [alpha 4](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.35-extreme-alpha.4) → [beta 1](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.38-extreme-beta.1) → [beta 2](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.39-extreme-beta.2) → [delta 1](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.43-extreme-delta.1).

The first-impression work was developed in the following order. **Merged** means the change is in the inspected source. **Recorded owner report** links the historical issue record; exactness varies and is detailed in the audit.

| ID / owning issue | Work | Implementation | Historical owner evidence / remaining work |
|---|---|---|---|
| [UX-001 / #2](https://github.com/techrote/RetroBar-Extreme/issues/2) | Tray inversion set/clear and live refresh | [PR #1](https://github.com/techrote/RetroBar-Extreme/pull/1) merged | [PASS report](https://github.com/techrote/RetroBar-Extreme/issues/2#issuecomment-6124231926); default matching and brightness-based policy were deferred. |
| [UX-002 / #3](https://github.com/techrote/RetroBar-Extreme/issues/3) | Sharp text in stretch mode | [PR #6](https://github.com/techrote/RetroBar-Extreme/pull/6) merged; **issue still open** | Default/cleanup follow-up remains; assess against native sizing and bundled fonts before deciding more work. |
| [UX-005 / #7](https://github.com/techrote/RetroBar-Extreme/issues/7) | Font settings and row growth | [PR #8](https://github.com/techrote/RetroBar-Extreme/pull/8) merged | [Report at `1ae8938`](https://github.com/techrote/RetroBar-Extreme/issues/7#issuecomment-6126564765). |
| [UX-006 / #9](https://github.com/techrote/RetroBar-Extreme/issues/9) | Native sizing | [PR #10](https://github.com/techrote/RetroBar-Extreme/pull/10) merged | [Report at `40455bf`](https://github.com/techrote/RetroBar-Extreme/issues/9#issuecomment-6127224058); native is the default. |
| [UX-007 / #11](https://github.com/techrote/RetroBar-Extreme/issues/11) | Menus, symbol fonts and row height | [PR #12](https://github.com/techrote/RetroBar-Extreme/pull/12) merged | [PASS at `9e7ff3e`](https://github.com/techrote/RetroBar-Extreme/issues/11#issuecomment-6128686146). |
| [UX-008 / #13](https://github.com/techrote/RetroBar-Extreme/issues/13) | Line spacing, clock fit and width | [PR #14](https://github.com/techrote/RetroBar-Extreme/pull/14) merged | [PASS at `6af9fd1`](https://github.com/techrote/RetroBar-Extreme/issues/13#issuecomment-6130777321). |
| [UX-003 / #4](https://github.com/techrote/RetroBar-Extreme/issues/4) | Colour/gradient layer over themes | [PR #15](https://github.com/techrote/RetroBar-Extreme/pull/15) merged | [Owner report](https://github.com/techrote/RetroBar-Extreme/issues/4#issuecomment-6215917137); fonts remain separate settings. |
| [UX-004 / #5](https://github.com/techrote/RetroBar-Extreme/issues/5) | Colours editor and named styles | [PR #16](https://github.com/techrote/RetroBar-Extreme/pull/16) merged | [Owner report](https://github.com/techrote/RetroBar-Extreme/issues/5#issuecomment-6218017594); a named style is not a full settings backup. |
| [UX-009 / #17](https://github.com/techrote/RetroBar-Extreme/issues/17) | Colourways, palette and copy/paste | [PR #20](https://github.com/techrote/RetroBar-Extreme/pull/20) merged | [Owner report](https://github.com/techrote/RetroBar-Extreme/issues/17#issuecomment-6219971124); applying writes the active style, named copies are optional. |
| [UX-010 / #18](https://github.com/techrote/RetroBar-Extreme/issues/18) | Start image colour extraction/recolouring | [PR #21](https://github.com/techrote/RetroBar-Extreme/pull/21) merged | [Exact-head PASS at `273f12a`](https://github.com/techrote/RetroBar-Extreme/issues/18#issuecomment-6222247337). |
| [UX-011 / #19](https://github.com/techrote/RetroBar-Extreme/issues/19) | LUT-coloured textures | [PR #23](https://github.com/techrote/RetroBar-Extreme/pull/23) merged | [Exact-head PASS at `51c5695`](https://github.com/techrote/RetroBar-Extreme/issues/19#issuecomment-6223445529). |
| [UX-012 / #22](https://github.com/techrote/RetroBar-Extreme/issues/22) | Start/Show desktop/clock layout | [PR #24](https://github.com/techrote/RetroBar-Extreme/pull/24) merged; issue closed | Source/automated records exist; no separate exact-head owner PASS recovered in this audit. |
| [UX-013 / #25](https://github.com/techrote/RetroBar-Extreme/issues/25) | Texture angle/patterns and borders | [PR #24](https://github.com/techrote/RetroBar-Extreme/pull/24) merged; issue closed | Same qualification boundary as UX-012. Later delta changes also affect these controls. |
| [UX-014 / #26](https://github.com/techrote/RetroBar-Extreme/issues/26) | Global/per-app task-button controls | [PR #24](https://github.com/techrote/RetroBar-Extreme/pull/24) merged; issue closed | Same qualification boundary as UX-012. |
| [UX-015 / #27](https://github.com/techrote/RetroBar-Extreme/issues/27) | Custom Start/quick-launch PNG icons and size sets | [PR #24](https://github.com/techrote/RetroBar-Extreme/pull/24) merged; issue closed | Previously missing from this overview; source support does not certify every DPI/image. |
| [UX-016 / #28](https://github.com/techrote/RetroBar-Extreme/issues/28) | Tray-toggle image, mirroring and margins | [PR #24](https://github.com/techrote/RetroBar-Extreme/pull/24) merged; issue closed | Previously missing from this overview; owner qualification remains separately recorded. |
| [UX-017 / #29](https://github.com/techrote/RetroBar-Extreme/issues/29) | 24 built-in font families, example styles and Extras packaging | [PR #30](https://github.com/techrote/RetroBar-Extreme/pull/30) merged; issue closed | Contract/build evidence exists; no separate exact-head owner PASS recovered. |

PR #24 historically grouped UX-012–016. Its merge `dba7b477622ebc54f47c3149a7292ed6d3f42051` supersedes the old “in PR / awaiting merge” rows. PR #30 merged as `c51ee1c97f1976cd315f7df1588d7d7911462f93`. Later [PR #31](https://github.com/techrote/RetroBar-Extreme/pull/31) and [PR #33](https://github.com/techrote/RetroBar-Extreme/pull/33) add Start/Quick and Icons controls, per-row app layout/alignment/height, extended texture/style controls and stability fixes in the current delta source. Release narratives report daily use; they do not substitute for an exact-build owner acceptance record for every change.

Remaining styling choices are in [STYLE-ENGINE](STYLE-ENGINE.md): native scaling is resolved, bundled fonts already exist, while arbitrary private-font loading, automatic tray brightness policy and full configuration export remain proposals. Do not restart merged slices from the old design order.

## Phase 2 — Qualify taskbar parity

Use [PARITY](PARITY.md) to select a bounded task. Priorities remain the owner's labelled, never-combined, compact taskbar; qualify exact layouts, fonts, multi-monitor/DPI, drag/drop and flyouts as needed. Distinguish missing implementation from present-but-unqualified behavior.

RetroBar already recognizes Open-Shell windows and has a menu invocation/placement path. End-to-end pairing still needs the exact two builds, settings and Windows version recorded, after UX-020's VM/build prerequisites. Jump-list quality, covered-window auto-hide, optional grouping and other unverified items must be investigated before promising implementation.

## Phase 3 — Start menu and Explorer gaps

Start with [UX-020](https://github.com/techrote/Open-Shell-Menu-Extreme/issues/1). Its admission gate is an unsigned, non-publishing fork build, updater-policy reconciliation, a usable installer and snapshot-VM recovery results. Only then qualify the menu/search/Explorer features and the RetroBar pair. A cleanup function in source is not a passed uninstall or login test.

## Phase 4 — Extreme extras

Ratrod skin pack, whole-window skinning and further owner-selected additions. No window-skinning module has been chosen. Existing RetroBar textures, example styles and embedded fonts are implemented groundwork, not evidence of a whole-window skinning engine.

## Updating this programme

1. Read the module default branch, issues, PRs, checks and releases; record the checked date and exact SHA.
2. Distinguish merged source, green CI, release-noted daily use and an exact-build owner PASS.
3. Update this programme, [PARITY](PARITY.md), [RAG](../RAG.md) and linked evidence together.
4. Run the [repository checks](../README.md#repository-checks). They validate local navigation, not live module status or Windows outcomes.
