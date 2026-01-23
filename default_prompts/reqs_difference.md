<old_ig_narrative>
{OLD_IG_NARRATIVE}
</old_ig_narrative>

<new_ig_narrative>
{NEW_IG_NARRATIVE}
</new_ig_narrative>

You are tasked with analyzing chunks of text from a FHIR Implementation Guide to identify requirements which have changed between versions.

<formatting_example>
1. Removal of Must Support Elements

**Old version**: "Each Condition Must Support: 1. a clinical status of the condition (e.g., active or resolved) 2. a verification status 3. an encounter 4. a date of diagnosis* 5. abatement date (in other words, date of resolution or remission) 6. a date when recorded*"

**New version**: "Each Condition Must Support: 1. an encounter 2. date record was first recorded**

**Summary**: The new version removes clinical status, verification status, date of diagnosis, and abatement date as Must Support elements.
</formatting_example>

<instructions>
Follow these steps to extract the requirements:

1. Analyze the narrative from the old version of the IG in the <old_ig_narrative> tag above.
2. Analyze the narrative from the new version of the IG in the <new_ig_narrative> tag above.
3. Identify concrete changes in requirements which are likely to impact conformance testing from the old version to the new version.
4. If there are no substantive differences between the versions, only output "No substantive differences found" with no additional explanatory text.
5. If substantive differences are found, summarize the change, and extract the exact quote for the requirement change, preserving necessary context, as shown in the formatting_example tag above.
6. Only include concrete requirements changes. Do not include:
    - Version number changes
    - Standard status changes
    - Capitalization changes
    - Punctuation changes
    - Spacing changes
    - Formatting changes
    - Changes in links to other parts of the IG
    - Changes from ONC to ASTP
    - Changes in guidance which do not affect how data is exchanged
    - Changes in examples
</instructions>
