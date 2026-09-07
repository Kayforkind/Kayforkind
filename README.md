<p align="center">
  <img src="assets/header-dark.svg#gh-dark-mode-only" alt="Kazim Merchant — founder of NavigatorLabs, local-first agent tooling" width="100%">
  <img src="assets/header-light.svg#gh-light-mode-only" alt="Kazim Merchant — founder of NavigatorLabs, local-first agent tooling" width="100%">
</p>

I'm **Kazim Merchant** — founder of **[NavigatorLabs](https://navigatorslab.com)**, the lab where local-first, private-by-default software gets built, shipped, and documented. Find the lab at [navigators.com](https://navigators.com) too.

I build tools that coding agents can run on a machine you control, then I send the hard fixes back upstream. Python, TypeScript, MCP. Everything open source, everything building in public — and everything **audited**: SLSA provenance on releases, SHA-pinned CI, an OpenSSF Scorecard of **7.0**, and proof artifacts that regenerate **byte-identically** in CI rather than screenshots nobody can reproduce.

**The flagship — [reimagine-it](https://github.com/Kayforkind/reimagine-it):** Content-Derived Design. It reads an HTML page and redesigns it from its *own* nouns, dates, numbers, and colors — never invented — across **17 design directions** with **96.8% measured pairwise distinctness**. **88★**, **1,700+ npm downloads a week**, **23 releases** in under three months, and 23 merged PRs shipped through a protected `main` with 16+ required checks on every one.

<p align="center">
  <a href="https://github.com/Kayforkind/reimagine-it"><strong>/reimagine-it</strong></a>
  ·
  <a href="https://kayforkind.github.io/NavigatorsLab-PDF-Studio/"><strong>pdf-studio</strong></a>
  ·
  <a href="https://navigatorslab.com/tools/"><strong>tools</strong></a>
  ·
  <a href="https://github.com/Kayforkind/book-guide-mcp"><strong>book-guide-mcp</strong></a>
  ·
  <a href="https://github.com/Kayforkind/research"><strong>research</strong></a>
  ·
  <a href="https://github.com/sponsors/Kayforkind"><strong>sponsor</strong></a>
</p>

## What I build

| Project | What it is | Proof |
|---------|------------|-------|
| **[reimagine-it](https://github.com/Kayforkind/reimagine-it)** | **Content-Derived Design** CLI + Agent Skill (Claude Code, Cursor, Codex, Copilot, Gemini CLI). Paste HTML; get a standalone redesign whose palette, motif, and motion derive from the source's own facts — never invented. 17 directions, Auto direction-picking, a 19-rule deterministic audit, an MCP server, a Design Health GitHub Action, and a live playground. Not a mood board. | ⭐ 88 · v2.13.1 · [1.7k dl/week](https://www.npmjs.com/package/reimagine-it) · [live playground](https://kayforkind.github.io/reimagine-it/#playground) |
| **[NavigatorsLab PDF Studio](https://github.com/Kayforkind/NavigatorsLab-PDF-Studio)** | A genuinely free, private, full-featured PDF editor that runs 100% in your browser. Edits the text *already inside* the PDF (not just stamps on top), fills & flattens AcroForms, OCRs scans locally, signs, redacts, reorders/merges/splits, diffs two revisions, and answers questions via an on-device LLM. | [Try it live](https://kayforkind.github.io/NavigatorsLab-PDF-Studio/) — no uploads, no accounts, no watermarks · MIT |
| **[NavigatorsLab Tools](https://github.com/Kayforkind/NavigatorsLab-Tools)** | Fifteen free, open-source utilities that run 100% in your browser: strip photo GPS, shrink images to an exact size, clean phone-scanned documents, sign PDFs, reorganize/merge pages, OCR receipts to CSV, generate QR codes privately, diff contracts word-level, trim audio, generate invoices, batch-rename by EXIF, print prep. **Speaks agent too:** an MCP endpoint (`/tools/mcp`), deep-link parameters on every tool, and llms.txt machine-readable docs. | [Try them live](https://navigatorslab.com/tools/) — no uploads, nothing retained, ever · MIT |
| **[book-guide-mcp](https://github.com/Kayforkind/book-guide-mcp)** | Playbooks and tutors (Socratic, Avicenna) your agents run locally across Cursor, Claude, VS Code, and Zed. Citations from books you own. No API keys for the core loop. | v0.2.0 |
| **[study-guide](https://github.com/Kayforkind/study-guide)** | Exam-guides platform — certification prep with topic units and quizzes. | Live product |
| **[design-health-action](https://github.com/Kayforkind/design-health-action)** | The 18 deterministic design-quality checks from reimagine-it, standalone — drop it on any HTML repo as a CI gate. No LLM, no API key. | GitHub Action |

Also in the lab: **[skill-slice](https://github.com/Kayforkind/skill-slice)** (copy one Read-verified SKILL.md folder), **[liecatchers](https://github.com/Kayforkind/liecatchers)** (your agent said Done — ten sensors, one RECEIPT.json, prove it), **[agenthub](https://github.com/Kayforkind/agenthub)** (community Claude Code plugin marketplace), and **[research](https://github.com/Kayforkind/research)** (dated public notes on local-first agents, MCP, and the failure modes that show up when tools actually have to run).

<p align="center">
  <a href="https://kayforkind.github.io/reimagine-it/#results">
    <img alt="reimagine-it — fourteen real sources, no shared silhouette" src="https://raw.githubusercontent.com/Kayforkind/reimagine-it/main/docs/og.png" width="100%">
  </a>
  <br>
  <sub><em>/reimagine-it — fourteen real sources, no shared silhouette. Every tile is a real, committed <code>.html</code> artifact that regenerates byte-identically in CI.</em></sub>
</p>

## The numbers — all live, all checkable

<p align="center">
  <img src="assets/stats-dark.svg#gh-dark-mode-only" alt="Live shipping numbers: stars, merged PRs, commits, releases, downloads" width="100%">
  <img src="assets/stats-light.svg#gh-light-mode-only" alt="Live shipping numbers: stars, merged PRs, commits, releases, downloads" width="100%">
</p>

The tiles above are re-rendered every week from public GitHub and npm APIs by [`scripts/refresh-stats.py`](scripts/refresh-stats.py) — every tile links its source; no third-party counters. Static highlights, verified at v2.13.1:

- **88★** on reimagine-it · **1,732** npm downloads last week · **23 releases** · **23 merged PRs in reimagine-it** (59 across all repos)
- **OpenSSF Scorecard 7.0** — Token-Permissions 10, Security-Policy 10, SLSA provenance + cosign signatures on npm releases
- **96.8%** mean pairwise distinctness across all 136 design-direction pairs · benchmark **100/100 on all 17 tokens × 4 sources**
- **116 tests** (68 unit + 20 MCP + 28 e2e) over a **155-file parity corpus**; **17 committed artifacts** reproduce byte-identically in CI
- A proof lane of **six real public-domain government pages** — NPS Yellowstone, NASA Artemis II, NWS/NOAA hurricane outlook, US Census P60-282, Federal Register FOIA, Smithsonian Apollo 11 — each Auto-routed at 84–100% source fidelity

## Upstream

Hard, reviewable work — not drive-by typo farms.

| Repository | Change | Status |
|------------|--------|--------|
| [simonw/llm](https://github.com/simonw/llm) | Set `conversation_id` correctly in `llm logs --data-ids` | **Merged** — [#1613](https://github.com/simonw/llm/pull/1613) |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | reimagine-it added to the curated skill list (×2, incl. the update) | **Merged** — [#966](https://github.com/VoltAgent/awesome-agent-skills/pull/966), [#988](https://github.com/VoltAgent/awesome-agent-skills/pull/988) |
| [nullorder/agenthub](https://github.com/nullorder/agenthub) | reimagine-it plugin added | **Merged** — [#35](https://github.com/nullorder/agenthub/pull/35) |
| [simonw/llm](https://github.com/simonw/llm) | Accept JSON Schema type names in `schema_dsl` | Open — [#1612](https://github.com/simonw/llm/pull/1612) |
| [pypa/hatch](https://github.com/pypa/hatch) | Build a wheel from the sdist when both targets are requested | Open — [#2386](https://github.com/pypa/hatch/pull/2386) |

AI agents help me move faster. I own every upstream diff I open.

## Contact

The lab: [navigatorslab.com](https://navigatorslab.com) · GitHub is the right place: [@Kayforkind](https://github.com/Kayforkind)

