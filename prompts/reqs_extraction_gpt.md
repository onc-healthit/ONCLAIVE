You are tasked with analyzing segments of text from a FHIR Implementation Guide to extract specific, testable requirements. Your objective is to format these requirements according to the INCOSE Systems Engineering standards so they can be directly included in an INCOSE-style Software Requirements Specification.

**Instructions:**
1. Thoroughly review the text provided within the <fhir_text> tag.
2. Identify specific, testable requirements describing explicit behavior or capabilities.
3. Ensure each requirement is complete, atomic, and objectively verifiable, meeting the <guidelines> criteria below.
4. Extract each requirement using the exact quote as much as possible, preserving necessary context.
5. Format each requirement using the structure and style shown in <formatting_example>.
6. Group multiple small requirements about the same topic into a single requirement as appropriate (for example, several search parameters for the same resource type).
7. List the extracted requirements in the order they appear in the source text.
8. Use 'Unspecified' for any missing information (such as Context, Conditional, etc.).
9. Set 'Source' to 'Unspecified' if the section is ambiguous or not explicitly referenced.

After preparing the list of requirements, review your output to verify that each extracted requirement is testable, complete, formatted according to the template, and preserves conformance language and actor assignments. Revise as needed before submitting the final output.

**Guidelines for requirement selection and formatting:**
- Only include requirements that define specific, testable, and objectively verifiable behaviors or capabilities.
- Requirements must be clearly testable via software testing or attestation.
- Use explicit conformance language (SHALL, SHOULD, MAY, MUST, REQUIRED, etc.) where possible.
- Separate individual requirements and identify the responsible actor for each ('Server' or 'Client').
- Preserve the original conformance strength.
- Mark requirements as conditional if they are dependent on optional features.
- Use exact quotes with preserved context as much as possible.

**Output Format:**
Present all extracted requirements as a markdown list using this template:

```
## REQ-[ID]

**Summary**: <Summary>
**Text**: "<Exact quote, with necessary [clarifications] and [additions] for completeness>"
**Context**: <Context or 'Unspecified'>
**Verification**: <Verification method or 'Unspecified'>
**Actor**: <'Server' or 'Client'>
**Conformance**: <Conformance level>
**Conditional**: <True/False or 'Unspecified'>
**Source**: <Section reference or 'Unspecified'>
```

- Requirements should be presented in the order they appear in the source text.
- Use 'Unspecified' for any field with missing information.
- For ambiguous or uncited sources, use 'Unspecified' for Source.

If the <fhir_text> contains no requirements, output nothing (no comments or responses).

Here is the chunk of FHIR Implementation Guide text to analyze:

<fhir_text>
{FHIR_TEXT}
</fhir_text>