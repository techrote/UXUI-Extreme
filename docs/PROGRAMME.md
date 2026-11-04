# Programme

Cross-module work map. **Reconciled 4 November 2026** against [RetroBar-Extreme `master` `65b36c0`](https://github.com/techrote/RetroBar-Extreme/commit/65b36c0fba6ef8d8e44294b3ea332b03e32f638c), [merged PR #24](https://github.com/techrote/RetroBar-Extreme/pull/24), [UX-017 PR #30](https://github.com/techrote/RetroBar-Extreme/pull/30), subsequent delta PRs and release metadata. All links and status claims are **point-in-time evidence**, not automatic live synchronization.

**Status terminology:** *merged* = code integrated into the module branch; *CI green* = a named check passed at a named SHA; *release-noted owner use* = release notes say owner-tested; *feature-specific owner PASS* = explicit visual acceptance for the exact build. Do not conflate these.

## Phase 0 — Workshop and recovery safeguards

- Umbrella repo, rules, checklist and module boundaries: established.
- RetroBar PR portable builds: established; latest verified default-branch [RetroBar workflow](https://github.com/techrote/RetroBar-Extreme/actions/runs/39116769177) **passed on `65b36c0` (18 October 2026)**, with concurrent Extras/colourway/texture contract workflows passing.
- A snapshotted Windows test VM for **Explorer-injecting** Open-Shell or future skinning changes remains a prerequisite; not confirmed complete.
- Umbrella documentation checks: introduced in [UX-018](https://github.com/techrote/UXUI-Extreme/issues/6). They do not build RetroBar or test Windows.

## Phase 1 — RetroBar look, layout and customisation (delivered baseline)

Release sequence: [alpha 1](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.31-extreme-alpha.1) → [alpha 2](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.32-extreme-alpha.2) → [alpha 3](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.34-extreme-alpha.3) → [alpha 4](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.35-extreme-alpha.4) → [beta 1](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.38-extreme-beta.1) → [beta 2](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.39-extreme-beta.2) → **[delta 1](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.43-extreme-delta.1)**, published **18 October 2026**, sourced from `65b36c0`. Delta release notes report daily owner use; they are not a per-feature Windows test report.

| ID | Implemented work | Module evidence | Qualification distinction |
|---|---|---|---|
| UX-001 | Tray icon effects clear and update on settings/theme changes | [Issue #2](https://github.com/techrote/RetroBar-Extreme/issues/2), [PR #1](https://github.com/techrote/RetroBar-Extreme/pull/1) merged | Earlier owner-tested per prior programme |
| UX-002 | Opt-in crisp scaled text, later superseded in normal use by native sizing | [Issue #3](https://github.com/techrote/RetroBar-Extreme/issues/3), [PR #6](https://github.com/techrote/RetroBar-Extreme/pull/6) merged | Not the default native-sizing path |
| UX-003 | Per-theme colour and gradient override layer | [Issue #4](https://github.com/techrote/RetroBar-Extreme/issues/4), [PR #15](https://github.com/techrote/RetroBar-Extreme/pull/15) merged | Earlier owner-tested; [map](STYLE-MAP.md) |
| UX-004 | Live Colours editor and named styles | [Issue #5](https://github.com/techrote/RetroBar-Extreme/issues/5), [PR #16](https://github.com/techrote/RetroBar-Extreme/pull/16) merged | Earlier owner-tested |
| UX-005 | Font family, size, weight and italic controls | [Issue #7](https://github.com/techrote/RetroBar-Extreme/issues/7), [PR #8](https://github.com/techrote/RetroBar-Extreme/pull/8) merged | Earlier owner-tested |
| UX-006 | Native sizing default; stretch fallback | [Issue #9](https://github.com/techrote/RetroBar-Extreme/issues/9), [PR #10](https://github.com/techrote/RetroBar-Extreme/pull/10) merged | Earlier owner-tested |
| UX-007 | Menu/symbol text, row-height fixes | [Issue #11](https://github.com/techrote/RetroBar-Extreme/issues/11), [PR #12](https://github.com/techrote/RetroBar-Extreme/pull/12) merged | Earlier owner-tested |
| UX-008 | Line spacing, clock lines and steady width | [Issue #13](https://github.com/techrote/RetroBar-Extreme/issues/13), [PR #14](https://github.com/techrote/RetroBar-Extreme/pull/14) merged | Earlier owner-tested |
| UX-009 | Colourways, palette, derived schemes and presets | [Issue #17](https://github.com/techrote/RetroBar-Extreme/issues/17), [PR #20](https://github.com/techrote/RetroBar-Extreme/pull/20) merged | Earlier owner-tested; UI evolved in delta |
| UX-010 | Start artwork palette extraction and recolouring | [Issue #18](https://github.com/techrote/RetroBar-Extreme/issues/18), [PR #21](https://github.com/techrote/RetroBar-Extreme/pull/21) merged | Earlier owner-tested |
| UX-011 | LUT-coloured procedural/PNG textures | [Issue #19](https://github.com/techrote/RetroBar-Extreme/issues/19), [PR #23](https://github.com/techrote/RetroBar-Extreme/pull/23) merged | Earlier owner-tested |
| UX-012 | Layout: vertical Start/clock and Show Desktop placement | [Issue #22](https://github.com/techrote/RetroBar-Extreme/issues/22), [PR #24](https://github.com/techrote/RetroBar-Extreme/pull/24) **merged 17 Oct** | Beta release-noted owner use; no independent PASS established here |
| UX-013 | Texture angles/noise patterns; per-part borders | [Issue #25](https://github.com/techrote/RetroBar-Extreme/issues/25), [PR #24](https://github.com/techrote/RetroBar-Extreme/pull/24) merged | Same combined-PR gate |
| UX-014 | Global and per-app task button width/icon/label controls | [Issue #26](https://github.com/techrote/RetroBar-Extreme/issues/26), [PR #24](https://github.com/techrote/RetroBar-Extreme/pull/24) merged | Same combined-PR gate |
| UX-015 | Start/Quick Launch custom PNGs and multi-size icon sets | [Issue #27](https://github.com/techrote/RetroBar-Extreme/issues/27), [PR #24](https://github.com/techrote/RetroBar-Extreme/pull/24) merged | Same combined-PR gate |
| UX-016 | Tray toggle PNG, mirroring and margins | [Issue #28](https://github.com/techrote/RetroBar-Extreme/issues/28), [PR #24](https://github.com/techrote/RetroBar-Extreme/pull/24) merged | Same combined-PR gate |
| UX-017 | 24 built-in fonts, 26 saved example styles, Extras included in builds | [Issue #29](https://github.com/techrote/RetroBar-Extreme/issues/29), [PR #30](https://github.com/techrote/RetroBar-Extreme/pull/30) merged | [Beta 2 notes](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.39-extreme-beta.2) report owner-tested daily use |

**Later delta polish (not a new UX-### ticket in this programme):** [PR #31](https://github.com/techrote/RetroBar-Extreme/pull/31) and [PR #33](https://github.com/techrote/RetroBar-Extreme/pull/33) add Start/Quick, per-row layouts, Icons, extended texture/style controls and stability fixes. See [delta 1 notes](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.43-extreme-delta.1) for scope. No RetroBar PR was open during the 4 November 2026 audit.

> **Process exception:** PR #24 consolidated UX-012–016 rather than following the normal one-issue/one-PR rule. Keep the history accurate; do not retroactively imply five independent merges.

## Phase 2 — Remaining StartAllBack taskbar parity (candidate work)

Use [PARITY.md](PARITY.md) as the checklist. Priorities require fresh module issues and physical Windows acceptance: RetroBar Start button integration with Open-Shell, jump-list behaviour, nuanced auto-hide, multi-monitor and DPI testing, and window preview/drag-and-drop parity. These are **not** claimed completed.

## Phase 3 — Start menu and Explorer gaps

[Open-Shell-Menu-Extreme](https://github.com/techrote/Open-Shell-Menu-Extreme) is the separate implementation fork. Do not conflate repository existence with validated integration on the owner's Windows build. Require VM snapshots before invasive Explorer experiments.

## Phase 4 — Extreme extras (future proposals)

Additional ratrod skin packs, whole-window skinning and other non-parity customisation. The shipped RetroBar texture/style extras do not imply that a whole-window skinning module exists.

## Updating this programme

1. Read the module's authoritative **default branch, issues, merged PRs, checks and release notes**; record exact source SHA/date and link.
2. Record *merged*, *CI green*, *release-noted owner use* and *specific physical PASS* separately.
3. Update this programme, [PARITY.md](PARITY.md) for changed capabilities, and [RAG.md](../RAG.md) for architectural facts; do not copy stale states from historical umbrella issues.
4. Run the [documentation checks](../README.md#repository-checks). They cover only local Markdown integrity, not live GitHub state or on-device outcomes.
