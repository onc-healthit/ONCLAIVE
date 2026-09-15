# ONCLAIVE Agent Evaluation Dashboard

A focused Streamlit dashboard for visualizing one Agent Usage Metrics report or comparing one Codex report with one Claude Code report. The interface uses a light, readable reporting-tool visual system and keeps all processing local to the current session.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Choose **Visualize a Report** or **Compare Reports** before uploading. Visualize mode accepts exactly one valid Codex or Claude Code report. Compare mode accepts exactly two valid reports and requires one Codex report plus one Claude Code report. Agent identity still comes from `run_metadata.agent`, so filenames and upload order do not affect validation. Example files are available in `sample_data/`.

## Supported report shape

The loader expects the revised `run_metadata` contract and exactly the eight main metrics listed below. Each metric is indexed by `name`; metric order is ignored. Missing values must remain present with `value: null` and `status: "missing"`.

Required metadata fields are `agent`, `session_files`, `conversation_name`, `workspace_name`, `scope_type`, `model`, and `generated_at`. The agent must be exactly `codex` or `claude_code`; `conversation_name`, `workspace_name`, and `model` may be `null` when unavailable.

- `wall_clock_time_seconds`
- `estimated_cost` with `unit: "USD"` when a value is available
- `human_prompts_required`
- `tool_calls`
- `file_edits`
- `input_tokens`
- `output_tokens`
- `total_tokens`

Missing, partial, and estimated statuses remain visible. A missing value displays as `N/A`, produces no delta, and never generates a guessed takeaway.

The dashboard reads `total_tokens` directly from the uploaded report and does not derive it from input/output tokens.

Core metrics use Plotly vertical bar charts. Every card has an independent scale, and exact values, status, and source are available on hover.

## Tests

```bash
python -m unittest discover -s tests -v
```
