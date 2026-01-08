<old_ig_narrative>
{OLD_IG_NARRATIVE}
</old_ig_narrative>

<new_ig_narrative>
{NEW_IG_NARRATIVE}
</new_ig_narrative>

<differences>
{DIFFERENCES}
</differences>

<formatting_example>
1. Removal of Must Support Elements

**Old version**: "Each Condition Must Support: 1. a clinical status of the condition (e.g., active or resolved) 2. a verification status 3. an encounter 4. a date of diagnosis* 5. abatement date (in other words, date of resolution or remission) 6. a date when recorded*"

**New version**: "Each Condition Must Support: 1. an encounter 2. date record was first recorded**

**Summary**: The new version removes clinical status, verification status, date of diagnosis, and abatement date as Must Support elements.
</formatting_example>

You are tasked with verifying differences which have been found between two versions of a FHIR implementation guide narrative.

<instructions>
Follow these steps to extract the requirements:

1. Analyze the differences found in the <differences> tag above.
2. Remove any differences which are not substantive and are unlikely to impact conformance testing. The original narrative is provided in the <old_ig_narrative> and <new_ig_narrative> tags. Examples of possible nonsubstantive differences which should be removed are:
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
3. If no substantive differences are found, output "No substantive differences found" with no additional introductory or explanatory text.
4. If substantive differences are found, output them in the format shown in the <formatting_example> tag above.
</instructions>
