## Test Generation Pipeline

The layout for Onclaive artifacts is as follows:

```
├── ig
│   ├── cleaned_markdown
│   ├── converted_markdown
│   └── site
├── prompts
│   ├── reqs_extraction.md
│   ├── reqs_grouping.md
│   ├── reqs_refinement.md
│   ├── test_gen.md
│   └── test_plan.md
├── requirements
│   ├── final
│   ├── initial_extraction
│   └── revised
├── test_plan
└── tests
```

In order of the pipeline processing, these are the contents of the directories:

- `ig` - the original and processed Implementation Guide
  - `site` - the original HTML files for the IG. These are the only files
    needed to run the pipeline.
  - `converted_markdown` - markdown files converted directly from the IG
    HTML
  - `cleaned_markdown` - cleaned markdown files which will be used for
    requirements extraction
- `prompts` - prompts to provided to the LLM for the LLM-based steps of the
  pipeline. If no prompts are provided, default prompts will be used.
  - `reqs_extraction.md` - prompt for extracting requirements from the IG
    markdown
  - `reqs_refinement.md` - prompt for revising the requirements
  - `reqs_grouping.md` - prompt for grouping requirements in the test plan
  - `test_plan.md` - prompt for creating the test plan
  - `test_gen.md` - prompt for creating the tests
- `requirements` - the requirements extracted from the IG
  - `initial_extraction` - requirements from the first pass extraction from the
    IG markdown files
  - `revised` - requirements after filtering out duplicates and untestable
    requirements, formatted in a consistent manner
  - `final` - deduplicated requirements which are used to generate the test plan
- `test_plan` - test plan generated based on the final requirements
- `tests` - tests generated based on the test plan


## IG Version Differences

The artifacts used to find differences in narrative requirements between IG
versions are as follows:

```
├── ig
│   ├── checked_differences.md
│   ├── cleaned_markdown
│   ├── converted_markdown
│   ├── differences.md
│   └── site
├── prompts
│   ├── reqs_check.md
│   └── reqs_difference.md
```

- `ig` - the original and processed Implementation Guide
  - `site` - the original HTML files for the IG. These are the only files
    needed to run the pipeline.
  - `converted_markdown` - markdown files converted directly from the IG
    HTML
  - `cleaned_markdown` - cleaned markdown files which will be used for
    requirements extraction
  - `differences.md` - the initial differences found between versions
  - `checked_differences.md` - the final differences found after a round of
    checking
- `prompts`
  - `reqs_check.md` - prompt for checking the differences found from the
    `reqs_difference.md` prompt
  - `reqs_difference.md` - prompt for finding the differences in requirements
    between IG versions

