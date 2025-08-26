You are tasked with analyzing chunks of text from a FHIR Implementation Guide to extract specific, testable requirements and format them according to INCOSE Systems Engineering standards. Your goal is to create requirements that can be directly inserted into an INCOSE-style Software Requirements Specification.

<instructions>
Follow these steps to extract and format the requirements:

1. Carefully read through the provided text in the <fhir_text> tag below.
2. Identify specific, testable requirements that describe behavior or capability.
3. Ensure each requirement is complete, atomic, and objectively verifiable, and meets the guidelines in the <guidelines> tag below.
4. Extract the exact quote for each requirement, preserving necessary context.
5. Format each requirement according to the INCOSE standard exemplified in the <formatting_example> tag below.
6. If a section has multiple small requirements relating to the same topic, group those together as one (e.g., requirements for multiple search paramters for the same resource type)
</instructions>

Format each extracted requirement as shown in the <formatting_example> tag below:
<formatting_example>
```
## REQ-[ID]

**Summary**: Brief description of the requirement
**Description**: "[exact quote with necessary [clarifications]]"
**Verification**: Recommended verification method (Test/Analysis/Inspection/Demonstration)
**Actor**: Actor responsible, conformance level, conditions, etc.
**Conformance**: Conformance level
**Conditional**: [True/False]
**Source**: Section reference from the Implementation Guide
```
</formatting_example>

<guidelines>
Guidelines for requirement selection and formatting:
- Include ONLY requirements that describe specific, testable, automatically verifiable behavior or capability.
- Ensure requirements could be objectively tested through software testing or attestation.
- Most requirements should have explicit conformance language (SHALL, SHOULD, MAY, MUST, REQUIRED, etc.).
- Separate individual requirements.
- Identify the actor responsible for implementing each requirement.
- Preserve the original conformance level.
- Mark conditional requirements (those that depend on optional features).
- Use exact quotes with necessary context preserved, when possible.
</guidelines>

Here is an example: 
<examples>
<example>
<FHIR_TEXT>
FHIR RESTful Capabilities
The Plan-Net Server SHALL:
Support all profiles defined in this Implementation Guide.
Support the searchParameters on each profile individually and in combination.

Endpoint
Conformance Expectation: SHALL
Supported Profiles: Plan-Net Endpoint
Reference Policy: resolves

Profile Interaction Summary:
SHALL support search-type, read.
SHOULD support vread.

Fetch and Search Criteria:
A Server SHALL be capable of returning a Endpoint resource using:
GET [base]/Endpoint/[id]

A Server SHALL be capable of supporting the following _includes:
Endpoint:organization - GET [base]/Endpoint?[parameter=value]&_include=Endpoint:organization

Search Parameter Summary:
Conformance	Parameter	Type	Example
SHALL	_lastUpdated	date	GET [base]/Endpoint?_lastUpdated=[_lastUpdated]

Search Parameter Summary:
Conformance	Parameter	Type	Example
SHALL	organization	reference	GET [base]/Endpoint?organization=[organization]
SHALL	_id	token	GET [base]/Endpoint?_id=[id]
SHALL	_lastUpdated	date	GET [base]/Endpoint?_lastUpdated=[_lastUpdated]
</FHIR_TEXT>
<ideal_output>
<requirement_extraction>
Potential requirements:

- The Plan-Net server SHALL support all profiles defined in this Implementation Guide.
- The Plan-Net server SHALL support the searchParameters on each profile individually
- The Plan-Net server SHALL support the searchParameters on each profile...in combination.
- A Server SHALL be capable of returning a Endpoint resource using:
GET [base]/Endpoint/[id]
- A Server SHALL be capable of supporting the following _includes: Endpoint:organization - GET [base]/Endpoint?[parameter=value]&_include=Endpoint:organization
- A Server SHALL be capable of supporting the following search: GET [base]/Endpoint?_lastUpdated=[_lastUpdated]

Search Parameter Summary:
Conformance	Parameter	Type	Example
SHALL	_lastUpdated	date	GET [base]/Endpoint?_lastUpdated=[_lastUpdated]

</requirement_extraction>

REQ-XX
Summary: Plan-Net Server Profile Support
Description: "Plan-Net Server SHALL: Support all profiles defined in this Implementation Guide."
Verification: Test
Actor: Plan-Net Server
Conformance: SHALL
Conditional: False
Source: FHIR RESTful Capabilities Section

REQ-XX
Summary: Plan-Net Server searchParameter Support- Individual
Description: "Plan-Net Server SHALL: Support the searchParameters on each profile individually."
Verification: Test
Actor: Plan-Net Server
Conformance: SHALL
Conditional: False
Source: FHIR RESTful Capabilities Section

REQ-XX
Summary: Plan-Net Server searchParameter Support- Combination
Description: "Plan-Net Server SHALL: Support the searchParameters on each profile... in combination"
Verification: Test
Actor: Plan-Net Server
Conformance: SHALL
Conditional: False
Source: FHIR RESTful Capabilities Section

REQ-XX
Summary: A server SHALL support searching by _id on the Endpoint resource.
Description: "A Server SHOULD be capable of returning a Endpoint resource using:
GET [base]/Endpoint/[id]/_history/vid"
Verification: Test
Actor: Plan-Net Server
Conformance: SHALL
Conditional: False
Source: FHIR RESTful Capabilities Section

REQ-XX
Summary: A server SHALL support searching by _id on the Endpoint resource.
Description: "A Server SHOULD be capable of returning a Endpoint resource using:
GET [base]/Endpoint/[id]/_history/vid"
Verification: Test
Actor: Plan-Net Server
Conformance: SHALL
Conditional: False
Source: FHIR RESTful Capabilities Section- Endpoint

REQ-XX
Summary: A server SHALL support searching by organization on the Endpoint resource.
Description: "A Server SHALL be capable of supporting the following _includes: Endpoint:organization - GET [base]/Endpoint?[parameter=value]&_include=Endpoint:organization"
Verification: Test
Actor: Plan-Net Server
Conformance: SHALL
Conditional: False
Source: FHIR RESTful Capabilities Section- Endpoint

REQ-XX
Summary: A server SHALL support searching by _lastUpdated on the Endpoint resource.
Description: "A Server SHALL be capable of supporting the following search: GET [base]/Endpoint?_lastUpdated=[_lastUpdated]"
Verification: Test
Actor: Plan-Net Server
Conformance: SHALL
Conditional: False
Source: FHIR RESTful Capabilities Section- Endpoint
</ideal_output>
</example>
</examples>

Here is the chunk of FHIR Implementation Guide text to analyze:

<fhir_text>
{{FHIR_TEXT}}
</fhir_text>

If no requirements are found in the provided text in the <fhir_text> tag, do not add any text or commentary. Simply provide no output.

Your final output should consist only of the extracted requirements formatted according to the INCOSE standard, presented as a list. Do not include any introductory or concluding comments.