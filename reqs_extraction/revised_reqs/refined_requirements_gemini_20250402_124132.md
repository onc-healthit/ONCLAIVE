It seems you are asking to extract testable requirements from a FHIR implementation guide, but the provided text chunks do not contain any explicit requirements statements. 

To effectively extract testable requirements, I need chunks of text that contain:

* **Explicit conformance verbs:** SHALL, SHOULD, MAY, MUST, etc.
* **Clear descriptions of expected behavior:** What the system or actor must, should, or may do. 
* **Testable conditions:**  Situations or triggers for the behavior.

**Example of a text chunk containing a testable requirement:**

"A Plan-Net Server SHALL return an HTTP 401 Unauthorized response code if the client request does not contain a valid authentication token."

**From this statement, we can extract the following requirement:**

---
# REQ-01
**Summary**: Server returns 401 Unauthorized for unauthenticated requests.
**Description**: "Upon receiving a client request without a valid authentication token, the Plan-Net server shall respond with an HTTP 401 Unauthorized status code."
**Verification**: Test - Send a request without a valid token and verify the response code.
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: True (when the request lacks a valid token)
**Source**: [Section reference in the Implementation Guide]
---

**Please provide text chunks that contain clear requirement statements for me to analyze and format.** 
