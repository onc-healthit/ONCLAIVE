You are tasked with analyzing chunks of text from a FHIR Implementation Guide to extract specific, testable requirements and format them according to INCOSE Systems Engineering standards. Your goal is to create requirements that can be directly inserted into an INCOSE-style Software Requirements Specification.

<instructions>
Follow these steps to extract and format the requirements:

1. Carefully read through the provided text in the <fhir_text> tag below.
2. Identify specific, testable requirements that describe behavior or capability.
3. Ensure each requirement is complete, atomic, and objectively verifiable, and meets the guidelines in the <guidelines> tag below.
4. Extract the exact quote for each requirement, preserving necessary context.
5. Format each requirement according to the INCOSE standard exemplified in the <formatting_example> tag below.
6. If a section has multiple small requirements relating to the same topic, group those together as one (e.g., requirements for multiple search paramters for the same resource type)
7. Identify most appropriate group for each requirement (based on list provided below)
</instructions>

Format each extracted requirement as shown in the <formatting_example> tag below:
<formatting_example>
```
## REQ-[ID]

**URL**: URL of the page that the requirement content is taken from. If available, look for the IG package name, any complete URLs in the file (in links, copyright, or metadata), extract the base path from them, and reconstruct the full URL of the page if possible. If unavailable, leave blank.
**Summary**: Summary description of the requirement
**Requirement**: "[exact quote with necessary [clarifications] and [additions] to make it a full phrase or sentence]"
**Context**: Overview of context within which requirement is set to provide background needed to understand requirement for later test planning activities. This can include any clarifications or interpretations.
**Conformance**: Conformance level, one of "[SHALL/SHOULD/MAY/SHOULD NOT/SHALL NOT]"
**Actor**: The actor, or actors, that the requirement constrains
**Sub-Requirement(s)**: The requirement set id and requirement id(s) of external requirements that are referenced by this requirement. This column will only be used when this requirements document points to requirements from a different requirement set. If not applicable, enter "NA"
**Conditionality**: Either "[True/False]" depending on whether or not the requirement is conditional on a prerequisite clause. An example of a conditional requirement is, "If the value is X, then the server SHALL do Y." Note: A blank value carries no information and does not indicate if Conditionality is true or false.
**Conditionality Details**: If the requirement is conditional, detail on when it is in force.
**Verifiable**: either "[Yes/No]" - A determination as to whether this requirement can be verified:: 'No' - the requirement cannot be verified, e.g., because it is not specific enough; 'Yes' - the requirement can be verified using mechanical means or an attestation
**Verifiability Details**: Recommended verification method; one of "[Attestation/Automation/Out of Scope]"
**Section**: Section reference from the Implementation Guide
**Grouping**: Most appropriate group that the requirement falls under, from the list of potential options below
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

For each extracted requirement, identify the most appropriate category or group it belongs to. Group the requirements by the resource profiles that make up the implementation guide from which these requirements were extracted, which are listed below:
AllergyIntolerance
CarePlan
CareTeam
Condition
Coverage
Device
DiagnosticReport
DocumentReference
Encounter
Goal
Immunization
Location
Medication
MedicationDispense
MedicationRequest
Observation
Organization
Patient
Practitioner
PractitionerRole
Procedure
Provenance
QuestionnaireResponse
RelatedPerson
ServiceRequest
Specimen

If the requirement does not belong to any of the specific resource profiles listed, use one of the following categories instead:
- Capability Statement
- General/Cross-Resource
- Security
- Privacy

Do not choose another category and only provide the group name, do not include any other descriptive text.
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
{FHIR_TEXT}
</fhir_text>

If no requirements are found in the provided text in the <fhir_text> tag, do not add any text or commentary. Simply provide no output.

Your final output should consist only of the extracted requirements formatted according to the INCOSE standard, presented as a list. Do not include any introductory or concluding comments.