# Change Evidence Matcher Content Guide

This skill gathers and reconciles evidence. It does not decide whether to add, revise, relax, or remove tests.

## Matching Goal

For each IG change, answer:

- Which existing baseline test-kit files or runnables are plausibly relevant?
- Which candidates are false positives?
- What evidence supports or weakens each candidate?
- What evidence is missing?

The output should make the impact assessor faster and more accurate.

## Search Query Playbook

Search with multiple forms of the same concept:

- resource type, such as `Coverage` or `ExplanationOfBenefit`,
- profile ID and canonical URL,
- element path, slice name, and short element name,
- search parameter name and URL,
- include value, such as `ExplanationOfBenefit:payee`,
- code system, code, display, or binding name,
- requirement ID and full requirement ID,
- distinctive words from old and new text,
- local test IDs or generated file names suggested by inventory candidates.

Use `rg` for source search and preserve exact query text in evidence notes when useful.

## Relevance Strength

Rank candidates by specificity:

1. Exact requirement ID or `verifies_requirements` match.
2. Exact element path, search parameter, include value, or code system match.
3. Exact profile URL or profile ID match.
4. Exact resource group plus matching test type.
5. Shared helper that implements the changed behavior for many tests.
6. Broad resource or narrative match.

Only the first five usually justify `relevant`. Broad resource or narrative matches are usually `possibly_relevant` or
`not_relevant`.

## False Positive Patterns

Reject or downgrade candidates when:

- the file only names the same resource but not the changed element or behavior,
- a CapabilityStatement group is matched only because the artifact is a CapabilityStatement,
- a shared helper is matched but the changed behavior is not in that helper,
- a profile validation test is matched for a narrative/security requirement,
- a Patient or Organization match is only topical,
- a generated group file registers children but the relevant child test is absent,
- the candidate is from a future target implementation not explicitly provided as draft work.

## Evidence Reconciliation

Compare structured inventory with code search:

- If both point to the same file and exact behavior, mark high confidence.
- If inventory points to a profile/resource but code search cannot find the changed behavior, mark possible or add a gap.
- If code search finds a better file than inventory, include both and explain why the code-search target is stronger.
- If all candidates are broad, reject them and mark a gap.

## Target-Version Leakage

Baseline implementation files are valid evidence. Target-version implementation files are not valid evidence for pre-target
migration planning unless the user explicitly says they are draft implementation to assess.

Target IG artifacts are valid evidence. Target generated implementation files are different from target IG artifacts.

When a repository contains both baseline and target implementation folders, search only baseline paths and shared helpers that
are needed to understand baseline candidates. Do not search target paths just because they are present locally.

Use these labels consistently:

- `baseline_evidence`: existing baseline inventory, baseline files, baseline-derived source search, and shared helpers reached
  from baseline files.
- `target_ig_artifact`: target IG narrative, package content, structured requirements, CapabilityStatement, SearchParameter,
  StructureDefinition, terminology, or invariants.
- `target_implementation`: target test-kit source files, generated output, fixtures, specs, or requirement mappings.
- `evaluation_oracle`: target implementation files intentionally saved for after-the-fact comparison once the updater has
  produced a candidate.

During evidence matching, `target_implementation` and `evaluation_oracle` are forbidden unless the user explicitly changes the
task from pre-target planning to target-draft assessment.

## Output Quality

A good `relevance_assessment` includes:

- ranked relevant targets,
- possible targets when confidence is limited,
- rejected candidates with reasons,
- confidence and rationale,
- evidence sources,
- gaps.

Do not collapse uncertainty into a final implementation decision. That belongs to the impact assessor.
