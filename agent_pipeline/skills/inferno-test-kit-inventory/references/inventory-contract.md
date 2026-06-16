# Inferno Inventory Contract

Use this contract for the directory produced by `pipeline/inferno_inventory.py`.

## Files

- `repos.jsonl`: one record describing the source test-kit repository.
- `runnables.jsonl`: suites, groups, and tests with IDs, titles, source files, requirement IDs, resources, profiles, search parameters, and line numbers.
- `requirements.jsonl`: known requirement records extracted from test-kit requirement sources.
- `coverage.jsonl`: requirement coverage rows and not-tested explanations.
- `summary.json`: counts and generation metadata.

## Important Runnable Fields

- `id`
- `title`
- `runnable_type`
- `suite_hint`
- `source_file`
- `line`
- `requirement_ids`
- `resource_types`
- `profile_urls`
- `search_parameters`
- `must_support_elements`

## Reuse Rules

Reuse an existing inventory only when all are true:

- Same test-kit repository or commit
- Same baseline suite ID
- Same baseline IG version intent
- Same inventory script behavior

If any of those are uncertain, rebuild the inventory.
