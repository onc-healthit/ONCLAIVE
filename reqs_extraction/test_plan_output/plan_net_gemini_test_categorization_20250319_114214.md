# Test Categorization for Plan Net

## Generated on: 2025-03-19 11:43:17

## FHIR Implementation Guide Requirement Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-AUTH-01 | Hybrid | Moderate | - Test client capable of sending authenticated and unauthenticated requests <br> - Defined list of resources/endpoints to test against | Authentication mechanisms can be automatically tested, but verifying the absence of consumer association in server records likely requires manual inspection or logs analysis. |
| REQ-CLIENT-01 | Automatic | Simple | - Test client capable of sending various queries <br> - Definition of "consumer identifiable information" within the IG context | Client requests can be automatically inspected for specific data elements or patterns. |
| REQ-DATA-01 | Automatic | Moderate | - Test client capable of querying resources <br> - List of Must Support data elements for each resource being tested |  Response payloads can be automatically parsed and validated against the expected data elements. |
| REQ-DATA-02 | Automatic | Moderate | - Test client capable of querying resources <br> - List of Must Support data elements with minimum cardinality 0 for each resource being tested | Response payloads can be automatically parsed to check for the absence of specific data elements when no information is expected. | 


## FHIR Implementation Guide Requirement Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-DATA-03 | Automatic | Simple | - Access to server API<br>- Test data with missing Must Support elements | This requirement can be tested by sending requests for resources and verifying the response includes the appropriate nullFlavor or dataAbsentReason extension for missing Must Support data elements. |
| REQ-CLIENT-02 | Hybrid | Moderate | - Client application<br>- Test data with various Must Support element combinations |  This requires automated testing to ensure the client doesn't crash or error. However, manual inspection of logs or error handling mechanisms might be needed to confirm proper "processing" beyond basic functionality. |
| REQ-CLIENT-03 | Manual | Moderate | - Client application with user interface or accessible storage | This requirement involves subjective evaluation of "appropriate handling" for human use. It necessitates manual inspection of the client interface or data storage to assess clarity and usability of Must Support element presentation. |
| REQ-CLIENT-04 | Hybrid | Moderate | - Client application<br>- Test data with missing Must Support elements | Automated tests can trigger client logic based on missing data. However, verifying the "appropriate" interpretation of missing data might require manual inspection of client behavior or outputs. |
| REQ-CLIENT-05 | Automatic | Complex | - Client application<br>- Test data with Must Support elements asserting missing information | This requires constructing test data with specific assertions within Must Support elements and then verifying the client processes these assertions without errors or unexpected behavior. The complexity arises from the need to accurately represent various assertion scenarios. | 


## FHIR Implementation Guide Requirements Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-CACHE-01 | Hybrid | Moderate | - Test client capable of making FHIR search requests<br>- Access to server logs or client-side instrumentation | While automated tests can verify the use of _lastUpdated and _id parameters, determining "appropriate" cache management might require manual inspection of logs or client behavior. |
| REQ-RESOURCE-01 | Automatic | Moderate | - Test data conforming to Plan-Net profiles<br>- FHIR validation tooling | Automated tests can validate resource conformance to profiles and verify supported interactions using FHIR validation tools and test requests. |
| REQ-RESOURCE-02 | Automatic | Complex | - Test data covering all Plan-Net search parameters<br>- FHIR search operation testing framework | Automated tests can systematically verify each search parameter's functionality against defined Plan-Net profiles using a testing framework. |
| REQ-RESOURCE-03 | Automatic | Moderate | - Test data with linked resources for _includes and _revincludes<br>- FHIR resource retrieval testing framework | Automated tests can verify the correctness of returned related resources for each _include and _revinclude using a testing framework. |
| REQ-SERVER-01 | Automatic | Simple | - Ability to simulate various request scenarios (e.g., invalid parameters, unauthorized access)<br>- FHIR client for sending test requests | Automated tests can easily simulate different request scenarios and verify the server returns the expected HTTP status codes. | 


## Analysis of FHIR Implementation Guide Requirements

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-02 | Hybrid | Moderate | - Test FHIR client capable of interacting with the server  - A list of expected Plan-Net profiles supported by the server | JSON format support can be automatically tested. However, verifying the correct profile identification in the `meta.profile` attribute requires manual comparison against the expected list of profiles. |
| REQ-SERVER-03 | Automatic | Complex | - Test FHIR client capable of constructing complex search queries  - A set of test resources with known relationships and search parameter values |  Both combined search parameter functionality and chaining can be tested by constructing specific search queries and verifying the returned results against expected resources. |
| REQ-SERVER-04 | Automatic | Simple | - Test FHIR client capable of sending and receiving XML formatted requests and responses |  XML format support can be automatically tested by sending requests and verifying responses in XML format. | 
