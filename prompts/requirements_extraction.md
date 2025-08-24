# ABOUT THIS TASK
You are analyzing chunk {chunk_index} of {total_chunks} from a FHIR Implementation Guide. Your task is to:
1. Extract specific, testable requirements
2. Format them according to INCOSE Systems Engineering standards
3. Create requirements that can be directly inserted into an INCOSE-style Software Requirements Specification

# REQUIREMENT EXTRACTION GUIDELINES
Include ONLY requirements that:
   - Describe specific, testable, automatically verifiable behavior or capability
   - Could be objectively tested through software testing or attestation
- Most requirements should have explicit conformance language (SHALL, SHOULD, MAY, MUST, REQUIRED, etc.)
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

Content to analyze:
{content}

Generate your INCOSE-style requirements extraction now. For each chunk, list each requirement using the format specified above. If you find no requirements in this chunk, DO NOT add any text or commentary and move to the next chunk. Do not include any introductory or conclusion/summary comments in your response. Only include the extracted requirements as a list.