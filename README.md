<div align="center">

# 🧭 NavigatorsLab (`@Kayforkind`)

**Software that runs in your browser tab or on your local machine — never on our servers.**  
*Zero uploads · Zero accounts · Zero runtime telemetry · MIT open source*

[![Live Hub](https://img.shields.io/badge/Live_Hub-navigatorslab.com-2dd4bf?style=for-the-badge)](https://navigatorslab.com)
[![24 Browser Tools](https://img.shields.io/badge/24_Tools-navigatorslab.com%2Ftools-38bdf8?style=for-the-badge)](https://navigatorslab.com/tools/)
[![PDF Studio](https://img.shields.io/badge/PDF_Studio-213★_Flagship-818cf8?style=for-the-badge)](https://navigatorslab.com/pdf-studio/)
[![Reimagine](https://img.shields.io/badge/Reimagine-17_Directions-f472b6?style=for-the-badge)](https://navigatorslab.com/reimagine/)

<a href="https://navigatorslab.com/tools/videos/notebooklm-overview.mp4">
  <img src="https://navigatorslab.com/tools/shots/notebooklm-overview.jpg" alt="Watch the NotebookLM Video Deep Dive on NavigatorsLab" width="820" />
</a>
<br>
<b>🎙️ <a href="https://navigatorslab.com/tools/videos/notebooklm-overview.mp4">Watch the NotebookLM Audio/Video Deep Dive</a></b> ·
<b>🎬 <a href="https://navigatorslab.com/tools/#library">Explore 24 Interactive Tool Videos & Output Examples</a></b>

</div>

---

## 🚀 Flagship Applications & Developer Platforms

| Product | What It Does | Concrete Input → Output Example | Live / Repo |
|---|---|---|---|
| 📜 **[PDF Studio](https://github.com/Kayforkind/NavigatorsLab-PDF-Studio)** *(213★)* | Full in-browser PDF editor: edit existing PDF text in place, fill forms, OCR scans, sign, vector-redact, organize pages, diff revisions, and ask on-device AI. | **IN:** Scanned 12-page contract with SSNs<br>**OUT:** In-place edited, vector-redacted, searchable signed PDF | [Live App](https://navigatorslab.com/pdf-studio/) · [▶ Video](https://navigatorslab.com/tools/videos/pdfstudio.mp4) |
| 🎨 **[reimagine-it](https://github.com/Kayforkind/reimagine-it)** *(92★ · OpenSSF 7.7)* | Content-derived HTML redesign engine & CLI. Rebuilds any HTML page into **17 design directions** from the nouns, dates, numbers, and colors already in your markup. | **IN:** Raw, unstyled HTML report or gov page<br>**OUT:** 17 redesigned HTML pages (Infographic, 3D, Editorial...) | [Playground](https://navigatorslab.com/reimagine/) · [▶ Video](https://navigatorslab.com/tools/videos/reimagine.mp4) |
| 🧭 **[NavigatorsLab Tools](https://github.com/Kayforkind/NavigatorsLab-Tools)** | **24 local-first browser utilities & projects** under `CSP: default-src 'none'`, plus a stateless MCP server (`POST /tools/mcp`). | **IN:** Vacation photos, 16 MB scans, receipts, NDAs<br>**OUT:** Stripped JPEGs, ≤300 KB images, `expenses.csv`, signed PDFs | [Launch Hub](https://navigatorslab.com/tools/) · [▶ Video](https://navigatorslab.com/tools/videos/notebooklm-overview.mp4) |
| 🩺 **[Design Health Action](https://github.com/Kayforkind/design-health-action)** | **18 deterministic HTML/CSS design-quality checks** for GitHub Actions across typography, palette, motion, content, structure, and performance. | **IN:** `dist/**/*.html` in Pull Request<br>**OUT:** 18/18 deterministic Pass/Fail CI verdict in <2s | [GitHub Action](https://github.com/Kayforkind/design-health-action) · [▶ Video](https://navigatorslab.com/tools/videos/designhealth.mp4) |
| 🕵️ **[liecatchers](https://github.com/Kayforkind/liecatchers)** | Post-run verification CLI for coding agents. **10 workspace sensors** audit declared commands, git diffs, lockfiles, and handoffs. | **IN:** Agent claims *"All done & tested!"*<br>**OUT:** Cryptographically signed `RECEIPT.json` proof | [GitHub Repo](https://github.com/Kayforkind/liecatchers) · [▶ Video](https://navigatorslab.com/tools/videos/liecatchers.mp4) |
| 🔪 **[Skill Slice](https://github.com/Kayforkind/skill-slice)** | Copy **one Read-verified skill folder** at a time (`npx skills add ... --skill <name>`) for Cursor, Claude, and `agentskills.io` hosts. | **IN:** Need one verified debugging/testing skill<br>**OUT:** Single verified `SKILL.md` slice installed | [Explorer](https://kayforkind.github.io/skill-slice/) · [▶ Video](https://navigatorslab.com/tools/videos/skillslice.mp4) |
| 📚 **[Book Guide MCP](https://github.com/Kayforkind/book-guide-mcp)** | Local-first Python MCP server over `stdio` turning your personal book library into agent-callable citations, playbooks, and Socratic tutors. | **IN:** Local EPUB/PDF/MD technical library<br>**OUT:** Chapter/page locators + executable playbooks | [Docs & Site](https://kayforkind.github.io/book-guide-mcp/) · [▶ Video](https://navigatorslab.com/tools/videos/bookguide.mp4) |
| 📡 **[Data Insights](https://github.com/Kayforkind/data-insights)** | Founder intelligence platform synthesizing public tech, security, and research signals into daily **5W1H** briefs and weekly reports. | **IN:** Public RSS/API feeds across tech & security<br>**OUT:** Daily 5W1H brief, weekly PDF & agent JSON API | [Docs & Site](https://kayforkind.github.io/data-insights/) · [▶ Video](https://navigatorslab.com/tools/videos/datainsights.mp4) |
| 🪓 **[Iron Axe: Legacy](https://github.com/Kayforkind/iron-axe-legacy)** | Original side-scrolling arcade beat 'em up built in **Godot 4** with combos, throws, elevation lanes, and team magic. | **IN:** Gamepad/keyboard combat input in Godot 4.3+<br>**OUT:** 60 FPS arcade action with 100% original art | [Project Page](https://kayforkind.github.io/iron-axe-legacy/) · [▶ Video](https://navigatorslab.com/tools/videos/ironaxe.mp4) |

---

## 🛠️ The 16 In-Browser Daily Utilities (`CSP: default-src 'none'`)

Every utility runs 100% inside your browser tab, works offline as an installable PWA, and is verified on every commit by 39 automated Playwright E2E checks:

| Tool | Concrete Input → Output Example | Sample Proof | Links |
|---|---|---|---|
| 🛡️ **Photo Privacy Kit** | `vacation-photo.jpg` (GPS 41.0°N, 28.9°E) → `clean.jpg` (0 EXIF bytes) | `Pixels SHA-256: IDENTICAL` | [Open](https://navigatorslab.com/tools/exif.html) · [▶ Video](https://navigatorslab.com/tools/videos/exif.mp4) · [Repo](https://github.com/Kayforkind/NavigatorsLab-Photo-Privacy-Kit) |
| 🔐 **Password Breach Checker** | Password typed locally → 5-char SHA-1 prefix (`5BAA6`) queried against HIBP | `800M+ corpus · 0 full hashes sent` | [Open](https://navigatorslab.com/tools/breachcheck.html) · [▶ Video](https://navigatorslab.com/tools/videos/breachcheck.mp4) |
| 🔍 **Metadata Checker** | `Proposal.docx` / `Model.pdf` → Author, Company & editing time stripped | `OOXML + PDF Info + XMP cleaned` | [Open](https://navigatorslab.com/tools/metadata.html) · [▶ Video](https://navigatorslab.com/tools/videos/metadata.mp4) · [Repo](https://github.com/Kayforkind/NavigatorsLab-Metadata-Checker) |
| 🗜️ **Image Shrinker** | `16.0 MB scan.png` + `"under 300 KB"` cap → `294 KB JPG` in 8 binary-search steps | `16 MB → 294 KB (≤300 KB)` | [Open](https://navigatorslab.com/tools/shrink.html) · [▶ Video](https://navigatorslab.com/tools/videos/shrink.mp4) · [Repo](https://github.com/Kayforkind/NavigatorsLab-Image-Shrinker) |
| 📄 **Scan & Screenshot Cleaner** | Skewed, shadowed phone photos of a lease → Straight, 300-DPI B&W PDF | `±4° deskew + auto-levels` | [Open](https://navigatorslab.com/tools/scan.html) · [▶ Video](https://navigatorslab.com/tools/videos/scan.mp4) · [Repo](https://github.com/Kayforkind/NavigatorsLab-Scan-Cleaner) |
| ✍️ **Local E-Sign Pad** | Unsigned `NDA.pdf` + drawn/typed signature → Flattened signed PDF | `0 editable form fields left` | [Open](https://navigatorslab.com/tools/sign.html) · [▶ Video](https://navigatorslab.com/tools/videos/sign.mp4) · [Repo](https://github.com/Kayforkind/NavigatorsLab-E-Sign-Pad) |
| 🧾 **Receipts → One PDF** | 18 unsorted receipt photos → 1 chronologically ordered, date-stamped PDF | `Sorted by EXIF DateTimeOriginal` | [Open](https://navigatorslab.com/tools/receipts.html) · [▶ Video](https://navigatorslab.com/tools/videos/receipts.mp4) · [Repo](https://github.com/Kayforkind/NavigatorsLab-Receipts-to-PDF) |
| 🔢 **Receipt OCR → CSV** | Receipt photos (`GREEN GROCER $23.98`) → `expenses.csv` via Tesseract WASM | `100% same-origin WASM OCR` | [Open](https://navigatorslab.com/tools/ocr.html) · [▶ Video](https://navigatorslab.com/tools/videos/ocr.mp4) · [Repo](https://github.com/Kayforkind/NavigatorsLab-Receipt-OCR) |
| 🔳 **QR Studio** | Wi-Fi / vCard / URL → Crisp vector SVG & PNG (plus local `jsQR` decoder) | `Encode → Decode round-trip exact` | [Open](https://navigatorslab.com/tools/qr.html) · [▶ Video](https://navigatorslab.com/tools/videos/qr.mp4) · [Repo](https://github.com/Kayforkind/NavigatorsLab-QR-Studio) |
| 🎧 **Audio Trimmer** | 40-min voice memo → Sample-accurate slice with fades & normalized MP3/WAV | `Web Audio + self-hosted LAME` | [Open](https://navigatorslab.com/tools/audio.html) · [▶ Video](https://navigatorslab.com/tools/videos/audio.mp4) · [Repo](https://github.com/Kayforkind/NavigatorsLab-Audio-Trimmer) |
| 🧮 **Invoice Generator** | Line items + discount + tax → Vector PDF invoice (`$408.00` total) | `Preview IS the PDF renderer` | [Open](https://navigatorslab.com/tools/invoice.html) · [▶ Video](https://navigatorslab.com/tools/videos/invoice.mp4) · [Repo](https://github.com/Kayforkind/NavigatorsLab-Invoice-Generator) |
| 🗂️ **Batch Rename & Sort** | `IMG_5847.jpg` → `2026-09-05-receipt-001.jpg` packed in one ZIP | `EXIF date + JSZip in-tab` | [Open](https://navigatorslab.com/tools/rename.html) · [▶ Video](https://navigatorslab.com/tools/videos/rename.mp4) · [Repo](https://github.com/Kayforkind/NavigatorsLab-Batch-Rename) |
| 🖨️ **Print-Shop Prep** | Camera photo + `4×6 in` size → DPI verdict + `306×450 pt` PDF with bleed | `True 300 DPI MediaBox` | [Open](https://navigatorslab.com/tools/printprep.html) · [▶ Video](https://navigatorslab.com/tools/videos/printprep.mp4) · [Repo](https://github.com/Kayforkind/NavigatorsLab-Print-Shop-Prep) |
| 📑 **PDF Pages** | 40-page packet → Drag to reorder, rotate, delete, insert blank, or merge | `pdf.js + pdf-lib local rebuild` | [Open](https://navigatorslab.com/tools/pdfpages.html) · [▶ Video](https://navigatorslab.com/tools/videos/pdfpages.mp4) · [Repo](https://github.com/Kayforkind/NavigatorsLab-PDF-Pages) |
| 🔬 **Text Diff** | Contract v1 vs Counterparty v2 → Line & word-level LCS diff + `.diff` export | `Word-level redline spans` | [Open](https://navigatorslab.com/tools/textdiff.html) · [▶ Video](https://navigatorslab.com/tools/videos/textdiff.mp4) · [Repo](https://github.com/Kayforkind/NavigatorsLab-Text-Diff) |
| 📊 **Text Stats** | Essay draft → Words, Flesch grade, keyword density & sentence rhythm chart | `One-click Markdown table copy` | [Open](https://navigatorslab.com/tools/textstats.html) · [▶ Video](https://navigatorslab.com/tools/videos/textstats.mp4) · [Repo](https://github.com/Kayforkind/NavigatorsLab-Text-Stats) |
