# IG Version Differences

Utilities for comparing requirements-relevant narrative between versions of the
US Core HL7 FHIR Implementation Guide (IG). The workflows prepare IG package
zips or requirements spreadsheets, convert the relevant content to cleaned
Markdown, and use an LLM to summarize substantive requirement differences.

## Extractor Support Scope

The base `ig_narrative_extractor.py` has only been used and tested with US Core,
specifically for comparing US Core versions 7, 8, and 9. Other IGs may have
different package layouts, navigation markup, or file naming conventions and
should be validated before relying on this extractor.

CARIN for Blue Button comparisons are supported through the separate
`carin_bb_ig_narrative_extractor.py` path by passing `--c4bb-ig` to the
preparation scripts.

## Directory Contents

- `process_igs.py`: prepares an old and new IG package zip for an
  IG narrative-to-narrative comparison.
- `compare_igs.py`: compares cleaned old/new narrative Markdown files, writes
  `ig/differences.md`, and removes no-difference sections from the final report.
- `process_ig_and_reqs.py`: prepares an old requirements spreadsheet and a new
  IG package zip for a requirements-to-narrative comparison.
- `compare_reqs_to_ig.py`: compares old requirements Markdown against new IG
  narrative Markdown, writes `ig/reqs_difference_output.md`, and removes
  no-difference sections from the final report.
- `ig_narrative_extractor.py`: extracts selected HTML files from US Core IG
  packages and converts them to Markdown.
- `carin_bb_ig_narrative_extractor.py`: extracts selected HTML files from CARIN
  for Blue Button packages, including CARIN layout differences across versions.
- `ig_requirements_extractor.py`: converts rows from a requirements Excel
  spreadsheet into per-page Markdown files using the `URL*` column.
- `markdown_cleaner.py`: removes navigation, footer, generated tables, and other
  non-requirements content from converted Markdown.
- `difference_finder.py`: builds comparison prompts and sends requests through
  the shared LLM client.
- `difference_output_cleaner.py`: removes generated report sections that say no
  substantive differences were found.

## Prerequisites

Run commands from the repository root.

Install dependencies:

```sh
uv sync
```

Configure the LLM provider you plan to use in `.env`:

```sh
ANTHROPIC_API_KEY=your_anthropic_key_here
GEMINI_API_KEY=your_gemini_key_here
OPENAI_API_KEY=your_openai_key_here
```

The compare scripts support `-a claude`, `-a gemini`, and `-a gpt`. Claude is
the default.

## Artifact Layout

The preparation scripts create this working structure under the `artifacts_dir`
argument:

```text
<artifacts_dir>/
  ig/
    site/
      old/
      new/
    converted_markdown/
      old/
      new/
    cleaned_markdown/
      old/
      new/
    differences.md
    reqs_difference_output.md
```

`differences.md` is produced by `compare_igs.py`.
`reqs_difference_output.md` is produced by `compare_reqs_to_ig.py`.

## Compare Two IG Versions

Use this workflow when both the old and new inputs are IG package zips. Sources
can be remote URLs or local `.zip` paths.

```sh
uv run ig_version_differences/process_igs.py \
  -o https://hl7.org/fhir/us/core/STU7/full-ig.zip \
  -n https://hl7.org/fhir/us/core/STU8/full-ig.zip \
  demo-artifacts/us-core-7-to-8

uv run ig_version_differences/compare_igs.py \
  -a claude \
  demo-artifacts/us-core-7-to-8
```

The first command extracts, converts, and cleans IG narrative files. The second
command compares each new cleaned Markdown file with the matching old file. If a
matching old file is missing, the comparison treats the new file as an addition.

## Compare Old Requirements To A New IG

Use this workflow when the old input is an Excel requirements spreadsheet and
the new input is an IG package zip. This option was created in order to use an
Inferno requirements spreadsheet in the comparison, but these spreadsheets are not
always available.

The spreadsheet must include a `Requirements` sheet and a `URL*` column. Each
row is written to a Markdown file named after the HTML page in `URL*`.

```sh
uv run ig_version_differences/process_ig_and_reqs.py \
  -o path/to/old_requirements.xlsx \
  -n https://hl7.org/fhir/us/core/STU8/full-ig.zip \
  demo-artifacts/reqs-to-us-core-8

uv run ig_version_differences/compare_reqs_to_ig.py \
  -a claude \
  demo-artifacts/reqs-to-us-core-8
```

## CARIN For Blue Button

CARIN package structures differ across versions. Add `--c4bb-ig` when preparing
CARIN for Blue Button comparisons so the scripts use the CARIN-specific
extractor.

The CARIN extractor prefers HTML under `site/en/` or `en/`. If neither location
contains HTML files, it falls back to top-level `site/*.html` files. It also
normalizes numbered HTML filename prefixes before writing extracted files.

```sh
uv run ig_version_differences/process_igs.py \
  --c4bb-ig \
  -o path/to/old-carin-full-ig.zip \
  -n path/to/new-carin-full-ig.zip \
  demo-artifacts/carin-comparison
```

The requirements-to-narrative workflow also supports `--c4bb-ig`:

```sh
uv run ig_version_differences/process_ig_and_reqs.py \
  --c4bb-ig \
  -o path/to/old_requirements.xlsx \
  -n path/to/new-carin-full-ig.zip \
  demo-artifacts/carin-reqs-comparison
```

## Useful Options

- `-v`, `--verbose`: print extraction and conversion progress.
- `-e`, `--exclude-pattern`: add a regular expression for HTML files to skip.
  This option can be repeated.
- `-a`, `--api-type`: choose the LLM provider for comparison. Supported values
  are `claude`, `gemini`, and `gpt`.
- `--c4bb-ig`: use CARIN for Blue Button extraction rules.

## Prompt Customization

Comparison prompts are loaded from `<artifacts_dir>/prompts/` when present.
Otherwise, the scripts fall back to the repository-level `default_prompts/`
directory.

Relevant prompt files:

- `reqs_difference.md`: used by `compare_igs.py`
- `reqs_ig_content_difference.md`: used by `compare_reqs_to_ig.py`

## Notes

- LLM comparison runs once per new cleaned Markdown file, so large IGs can incur
  noticeable API cost and runtime.
- The scripts focus on substantive requirements differences and prompt the LLM
  to ignore formatting-only changes.
- Compare scripts remove sections where the LLM reports no substantive
  differences before writing the final report.
- Existing contents under the chosen `artifacts_dir` may be overwritten during
  extraction, conversion, and cleaning.
