# ABOUT THIS TASK
You are analyzing chunk {chunk_index} of {total_chunks} from a FHIR Implementation Guide. Your task is to:
1. Extract specific, testable requirements
2. Format them according to INCOSE Systems Engineering standards
3. Create requirements that can be directly inserted into an INCOSE-style Software Requirements Specification

# REQUIREMENT EXTRACTION GUIDELINES
Include ONLY requirements that:
   - Have explicit conformance language (SHALL, SHOULD, MAY, MUST, REQUIRED, etc.)
   - Describe specific, verifiable behavior or capability
   - Could be objectively tested through software testing or attestation
- Each requirement must be complete, atomic, and testable
- Separate individual requirements
- Identify the actor responsible for implementing each requirement
- Preserve the original conformance level (SHALL, SHOULD, MAY, MUST, REQUIRED, etc.)
- Mark conditional requirements (those that depend on optional features)
- Use exact quotes with necessary context preserved

# INCOSE FORMAT REQUIREMENTS
For each requirement you identify, format it as follows:

```
## REQ-[ID]

**Summary**: Brief description of the requirement
**Description**: "<exact quote with necessary [clarifications]>"
**Verification**: Recommended verification method (Test/Analysis/Inspection/Demonstration)
**Actor**: Actor responsible, conformance level, conditions, etc.
**Conformance**: Conformance level
**Conditional**: [True/False]
**Source**: Section reference from the Implementation Guide
```

Where [ID] starts at 1 and follows in sequential order.

# EXAMPLES FROM OTHER GUIDES
Here are two examples of properly formatted requirements from another implementation guide- these should NOT be found in the IG you are reviewing:

```
## REQ-01

**Summary**: Advertise supported subscription topics
**Description**: "In order to allow for discovery of supported subscription topics, this guide defines the CapabilityStatement SubscriptionTopic Canonical extension. The extension allows server implementers to advertise the canonical URLs of topics available to clients."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Subscription Discovery Section
```

```
## REQ-02

**Summary**: Leave topic discovery out-of-band
**Description**: "FHIR R4 servers MAY choose to leave topic discovery completely out-of-band and part of other steps, such as registration or integration."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: MAY, Conditional: False
**Source**: Subscription Configuration Section
```

Content to analyze:
{content}

Generate your INCOSE-style requirements extraction now. For each chunk, list each requirement using the format specified above. If you find no requirements in this chunk, do not add any text and move to the next chunk. Do not include any introductory or conclusion/summary comments in your response. Only include the requirements as a list.