Your task is to review this list of FHIR Implementation Guide requirements and create a refined, concise list of only the testable requirements. Follow these guidelines carefully:

1. Identify a final list of clear, testable requirements that a conformance testing tool could verify. Requirements should start with a header such as # REQ-XX and be followed by a list of characteristics. Ignore and move past text describing that a section does not contain a requirement- move to the next section to review for a requirement.

2. Include ONLY requirements that:
   - Are atomic
   - Have explicit conformance language (SHALL, SHOULD, MAY, MUST, REQUIRED, etc.)
   - Describe specific, verifiable behavior or capability
   - Could be objectively tested through software testing or attestation

3. EXCLUDE the following types of content:
   - General introductory or conclusive/summarization comments
   - Implementation guidance or explanatory text
   - Examples or sample queries
   - Duplicate requirements (consolidate similar requirements)
   - Information about resource relationships without conformance statements
   - General structural information about profiles or resources
   - Requirements fragments that should be part of a single testable requirement

4. For each requirement description, keep the original language as much as possible. Do not revise the language of the requirement description for requirements that you decide are appropriate to include in the final list.

After filtering, verify that each requirement in your final list represents a discrete, testable capability or constraint that would be appropriate for conformance testing.

Keep the formatting of each requirement as follows. Renumber requirement IDs as you keep requirements in a list, starting with 01:

    ---
    # REQ-XX
    **Summary**: [summary text, exactly as it was]
    **Description**: "[description text, exactly as it was]"
    **Verification**: [method]
    **Actor**: [actor]
    **Conformance**: [SHALL/SHOULD/MAY/etc.]
    **Conditional**: [True/False]
    **Source**: [reference]
    ---

Do not include any introductory or conclusion/summary comments in your response. Only include the requirements as a list.

Here is the list of requirements to refine:

{requirements_list}