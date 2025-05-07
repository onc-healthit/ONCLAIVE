Your task is to review this list of FHIR Implementation Guide requirements and create a refined, concise list of only the testable requirements. Follow these guidelines carefully:

1. Produce a list of (maximum 50) clear, testable requirements that a conformance testing tool could verify.

2. Include ONLY requirements that:
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

4. For each requirement, include:
   - A clear, concise statement of what MUST, SHOULD, MAY, SHALL, etc. be implemented
   - The actor responsible (Server, Client, Application, etc.)
   - The conformance level (SHALL, SHOULD, MAY, MUST, REQUIRED, etc.)

5. Format each requirement consistently:
   - Use active voice
   - Begin with the actor (e.g., "Server SHALL...")
   - Make each requirement atomic and independently testable
   - Ensure requirements are implementation-neutral

After filtering, verify that each requirement in your final list represents a discrete, testable capability or constraint that would be appropriate for conformance testing.

Keep the formatting of each requirement as follows- renumber requirement IDs as you keep requirements in a list, starting with 01:
    
    ---
    # REQ-XX
    **Summary**: [summary text]
    **Description**: "[description text]"
    **Verification**: [method]
    **Actor**: [actor]
    **Conformance**: [SHALL/SHOULD/MAY/etc.]
    **Conditional**: [True/False]
    **Source**: [reference]
    ---

Do not include any other text in the response output, besides the requirements list. 

Here is the list of requirements to refine:

{requirements_list}