<old_ig_narrative>
{OLD_IG_NARRATIVE}
</old_ig_narrative>

<new_ig_narrative>
{NEW_IG_NARRATIVE}
</new_ig_narrative>

{OLD_IG_REQUIREMENTS_BLOCK}

You are tasked with analyzing chunks of text from a FHIR Implementation Guide to identify requirements which have changed between versions.

<formatting_example>

## 1. Removal of Must Support Elements

**Old version**: [ID=none, Conformance=SHALL, Actor=Health Plan, Scope=unknown, Planning To Test=unknown]
"Each Condition Must Support: 1. a clinical status of the condition (e.g., active or resolved) 2. a verification status 3. an encounter 4. a date of diagnosis* 5. abatement date (in other words, date of resolution or remission) 6. a date when recorded*"

**New version**: "Each Condition Must Support: 1. an encounter 2. date record was first recorded**"

**Summary**: The new version removes clinical status, verification status, date of diagnosis, and abatement date as Must Support elements.

---

## 2. Weakening of careTeam.sequence conformance requirement

**Old version**: [ID=122, Conformance=SHOULD NOT, Actor=Consumer, Scope=AUTOMATION, Planning To Test=Yes]
"Client app implementations SHOULD NOT assign any significance to the sequence values."

**New version**: "Client app implementations should not assign any significance to the sequence values."

**Summary**: Formal SHOULD NOT downgraded to informal lowercase guidance with no conformance verb.

</formatting_example>

<instructions>
Follow these steps to extract the requirements:

1. Analyze the narrative from the old version of the IG in the <old_ig_narrative> tag above.
2. Analyze the narrative from the new version of the IG in the <new_ig_narrative> tag above.
3. If an <old_ig_requirements> block is present above, use it to look up the ID, Conformance, Actor,
   Scope, and Planning To Test values for any old requirement you identify. Match on URL or text similarity.
4. Identify concrete changes in requirements which are likely to impact conformance testing.
5. If there are no substantive differences between the versions, output only: "No substantive differences found"
6. If substantive differences are found, format each change as shown in the formatting_example above:
   - A numbered ## heading naming the change
   - **Old version**: A metadata tag line in square brackets, then the verbatim old requirement text.
     The tag line MUST always be present and MUST include:
       ID=<integer id from requirements table, or "none" if not found or no table provided>
       Conformance=<infer from the old narrative text: SHALL/SHOULD/MAY/SHOULD NOT/SHALL NOT/DEPRECATED/guidance_only>
       Actor=<infer from old narrative: Health Plan/Consumer/Server/Client/All/unknown>
       Scope=<from requirements table if available, otherwise "unknown">
       Planning To Test=<from requirements table if available, otherwise "unknown">
     If multiple old requirements map to this change, include one tag line per requirement, each on its own line.
   - **New version**: The verbatim quote from the new IG narrative
   - **Summary**: One sentence describing what changed and its likely impact on conformance testing
   - A horizontal rule (---) between changes
7. Only include concrete requirement changes. Do not include:
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