# Test Categorization for Plan Net

## Generated on: 2025-03-19 10:32:56

## FHIR Implementation Guide Requirements Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-NOT-01 | Hybrid | Moderate | - Test client capable of making authenticated and unauthenticated requests<br>- Access to server logs |  While testing unauthenticated access is straightforward, verifying the absence of user association in logs requires manual inspection. |
| REQ-SERVER-SHALL-NOT-02 | Hybrid | Moderate | - Test client simulating a directory app<br>- Ability to inspect server-side requests |  Requires simulating a specific client type and verifying the absence of identifying information in requests received by the server. |
| REQ-CLIENT-SHALL-NOT-01 | Automatic | Simple | - Test client simulating a directory app |  Can be automatically verified by inspecting the client-generated requests before sending. |
| REQ-SERVER-SHALL-01 | Automatic | Moderate | - Test client capable of parsing FHIR resources<br>- Defined list of Must Support data elements |  Testable by automatically querying the server and verifying the presence of all required data elements in the returned FHIR resource. |
| REQ-SERVER-SHALL-NOT-03 | Automatic | Moderate | - Test client capable of parsing FHIR resources<br>- Defined list of Must Support data elements with minimum cardinality 0<br>- Test data setup with missing information for specific elements |  Testable by automatically querying for resources with known missing data and verifying the absence of corresponding elements in the returned FHIR resource. | 


## Analysis of FHIR Implementation Guide Requirements

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-04 | Hybrid | Moderate | - Test data with missing Must Support elements. - Value set definitions for dataAbsentReason extension. | Requires automated tests to trigger specific data scenarios and manual verification to confirm the correct reason code or extension is used. |
| REQ-CLIENT-SHALL-02 | Automatic | Simple | - Test data with populated Must Support elements. | Can be tested automatically by sending valid resources with Must Support data and verifying no errors are thrown. |
| REQ-CLIENT-SHOULD-01 | Manual | Complex | - Access to the client application UI or data storage. - Defined acceptance criteria for "displaying for human use" or "storing for other purposes". | Requires manual inspection of the application's UI or data storage to confirm the requirement is met. Subjective criteria necessitate clear acceptance criteria. |
| REQ-CLIENT-SHALL-03 | Hybrid | Moderate | - Test data with missing Must Support elements. - Mechanism to verify the client's interpretation of missing data (e.g., logs, specific UI element). | Requires automated tests to trigger scenarios with missing data and manual verification to confirm the client's interpretation aligns with the requirement. |
| REQ-CLIENT-SHALL-04 | Automatic | Simple | - Test data with Must Support elements asserting missing information (e.g., using nullFlavors or dataAbsentReason). | Can be tested automatically by sending resources containing assertions of missing information and verifying the client processes them without errors. | 


## Analysis of FHIR Implementation Guide Requirements

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-CLIENT-SHOULD-02 | Hybrid | Moderate | - Test client capable of caching query results. - Server supporting _lastUpdated search parameter. |  **Automatic:** Can automatically send queries with _lastUpdated and verify results. **Manual:** Requires inspection to confirm client caching logic. |
| REQ-CLIENT-SHOULD-03 | Hybrid | Moderate | - Test client capable of caching query results. - Server supporting _id queries. | **Automatic:** Can automate _id queries for cached data. **Manual:** Requires inspection to confirm client's periodic verification logic. |
| REQ-SERVER-SHALL-01 | Automatic | Simple | - Test client capable of querying HealthcareService resources. | Straightforward verification by querying for HealthcareService resources and confirming existence. |
| REQ-SERVER-SHOULD-01 | Manual | Simple | - Access to HealthcareService resources. - Knowledge of expected Organization association. | Requires human inspection of HealthcareService resources to verify the presence and correctness of Organization association. |
| REQ-SERVER-SHOULD-02 | Manual | Moderate | - Access to PractitionerRole and OrganizationAffiliation resources. - Knowledge of expected Network linking. | Requires human inspection of PractitionerRole and OrganizationAffiliation resources to confirm the presence and accuracy of Network linking. | 


## FHIR Implementation Guide Requirement Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHOULD-03 | Hybrid | Moderate |  - Valid PractitionerRole and OrganizationAffiliation resources  - HealthcareService, Organization, Network, and Location resources with expected associations |  - Automated checks can verify the presence and structure of resources and references.  - Manual inspection might be needed to confirm the semantic correctness of associations. |
| REQ-SERVER-MAY-01 | Automatic | Simple | - Location resource with GeoJSON data | - Automated tests can easily verify the presence and validity of GeoJSON data within Location resources. |
| REQ-SERVER-SHALL-01 | Manual | Complex | - Complete list of defined profiles in the Implementation Guide | - Requires manual inspection of server capabilities and comparison against the defined profiles. - Complexity arises from the potential number of profiles and the need for in-depth knowledge of each. |
| REQ-SERVER-SHALL-02 | Hybrid | Complex | - FHIR specification  - Test cases covering various RESTful interactions | - Automated tests can validate conformance to a subset of RESTful behaviors. - Manual review and specialized testing tools might be needed for comprehensive coverage of the FHIR RESTful specification. |
| REQ-SERVER-SHALL-03 | Automatic | Moderate | - Test cases triggering specific error conditions | - Automated tests can simulate requests leading to the defined error responses and verify the returned status codes. | 


## Analysis of FHIR Implementation Guide Requirements

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-04 | Automatic | Simple | - Test client capable of sending JSON requests<br>- Access to Plan-Net Server endpoint | This requirement can be tested by sending a valid JSON request to the server and verifying the response code (2xx). |
| REQ-SERVER-SHALL-05 | Automatic | Simple | - Test client capable of retrieving resource metadata<br>- Access to Plan-Net Server endpoint | This requirement can be tested by retrieving a resource from the server and verifying the presence and correctness of the `meta.profile` attribute. |
| REQ-SERVER-SHALL-06 | Hybrid | Complex | - Test client capable of constructing complex search queries<br>- Access to Plan-Net Server endpoint<br>- Knowledge of all supported search parameters and their combinations | This requirement requires both automated tests for individual parameters and manual review/testing for complex combinations to ensure comprehensive coverage. |
| REQ-SERVER-SHALL-07 | Hybrid | Moderate | - Test client capable of constructing chained search queries<br>- Access to Plan-Net Server endpoint<br>- Knowledge of search parameters supporting chaining | This requirement can be partially automated by testing individual chained queries. However, manual review might be needed for complex chaining scenarios. |
| REQ-SERVER-SHOULD-01 | Automatic | Simple | - Test client capable of sending XML requests<br>- Access to Plan-Net Server endpoint | Similar to REQ-SERVER-SHALL-04, this can be tested by sending a valid XML request and verifying the response code. Note that this is a SHOULD requirement, meaning it's not mandatory but recommended. | 


## FHIR Implementation Guide Requirements Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-08 | Automatic | Simple | - Test client capable of sending unauthorized requests  - Server running with authentication enabled | Straightforward to test by sending an unauthorized request and verifying the response code. |
| REQ-SERVER-SHALL-01 | Automatic | Moderate | - Test client capable of sending search-type and read requests | Requires testing multiple interaction types, increasing complexity slightly. |
| REQ-SERVER-SHOULD-01 | Automatic | Simple | - Test client capable of sending vread requests | Similar to read interaction testing, but with a different interaction type. |
| REQ-SERVER-SHALL-02 | Automatic | Simple | - Test client capable of sending GET requests - Existing Endpoint resource with known ID | Simple retrieval of a resource by ID. |
| REQ-SERVER-SHOULD-02 | Automatic | Moderate | - Test client capable of sending GET requests - Existing Endpoint resource with known ID and version | Similar to retrieving by ID, but requires managing resource versions. | 


## FHIR Implementation Guide Requirement Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-03 | Automatic | Simple | - FHIR Server running  - Test Endpoint resource with associated Organization | This requirement involves a standard _include operation with a specific parameter. Automated tests can easily construct the request and verify the response includes the organization data. |
| REQ-SERVER-SHALL-04 | Automatic | Simple | - FHIR Server running - Test Endpoint resource with associated Organization | This requirement involves a standard search operation with a specific search parameter. Automated tests can easily construct the request with a known organization ID and verify the response. |
| REQ-SERVER-SHALL-05 | Automatic | Simple | - FHIR Server running - Test Endpoint resource with a known ID | This requirement involves a standard search operation using the _id parameter. Automated tests can easily construct the request with a known Endpoint ID and verify the response. |
| REQ-SERVER-SHALL-06 | Automatic | Simple | - FHIR Server running - Test Endpoint resource with a known lastUpdated timestamp | This requirement involves a standard search operation using the _lastUpdated parameter. Automated tests can easily construct the request with a known timestamp and verify the response. |
| REQ-SERVER-SHALL-07 | Hybrid | Moderate | - FHIR Server running - Test HealthcareService resource | This requirement involves verifying support for both search-type and read interactions. While automated tests can check the server's capability statement for these interactions, manual verification might be needed to confirm actual functionality (e.g., attempting a search and read operation). | 


## FHIR Implementation Guide Requirement Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHOULD-03 | Automatic | Simple | - FHIR Server running  - Test client capable of sending vread requests | The requirement specifies a standard FHIR interaction (vread) which can be tested by sending a request and verifying the response code. |
| REQ-SERVER-SHALL-08 | Automatic | Simple | - FHIR Server running  - Test client capable of sending GET requests | The requirement specifies a specific GET request format and expected response. This can be tested automatically. |
| REQ-SERVER-SHOULD-04 | Automatic | Moderate | - FHIR Server running  - Test client capable of sending GET requests  - Pre-existing HealthcareService resource with a known ID and version | Similar to REQ-SERVER-SHALL-08, but requires a specific resource state (versioned resource) to be present. |
| REQ-SERVER-SHALL-09 | Automatic | Moderate | - FHIR Server running  - Test client capable of sending GET requests with _include parameters  - Pre-existing HealthcareService resources with linked resources (location, coverage-area, organization, endpoint) | The requirement involves testing _include functionality, requiring linked resources to be present and the server correctly returning them. |
| REQ-SERVER-SHALL-10 | Automatic | Complex | - FHIR Server running  - Test client capable of sending GET requests with _revinclude parameters  - Pre-existing HealthcareService resources with reverse links from PractitionerRole and OrganizationAffiliation resources | Similar to REQ-SERVER-SHALL-09, but involves _revinclude, which requires specific reverse links to be set up in the data. | 


## FHIR Implementation Guide Requirement Analysis: HealthcareService Search Parameters

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-11 | Automatic | Simple | - FHIR Server running - Test HealthcareService resources with location data | This requirement focuses on a single search parameter (location) with a straightforward reference search. Automated tests can easily construct the search URL and validate the response. |
| REQ-SERVER-SHALL-12 | Automatic | Simple | - FHIR Server running - Test HealthcareService resources with coverage-area data | Similar to REQ-SERVER-SHALL-11, this requirement involves a single search parameter (coverage-area) and a reference search, making it suitable for automated testing. |
| REQ-SERVER-SHALL-13 | Automatic | Simple | - FHIR Server running - Test HealthcareService resources with organization data | This requirement follows the same pattern as the previous two, focusing on a single search parameter (organization) and a reference search, making it easily testable through automation. |
| REQ-SERVER-SHALL-14 | Automatic | Simple | - FHIR Server running - Test HealthcareService resources with endpoint data | This requirement, like the previous ones, involves a single search parameter (endpoint) and a reference search, allowing for straightforward automated testing. |
| REQ-SERVER-SHALL-15 | Automatic | Simple | - FHIR Server running - Test HealthcareService resources with name data | This requirement, while using a string search instead of a reference search, remains simple to test automatically. The test can easily construct the search URL with different name values and validate the server's response. | 


## FHIR Implementation Guide Requirements Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-16 | Automatic | Simple | - FHIR Server running  - Test HealthcareService resources with different service-category codes | The requirement clearly defines the search parameter and expected behavior. Automated tests can send requests with various codes and verify the response. |
| REQ-SERVER-SHALL-17 | Automatic | Simple | - FHIR Server running  - Test HealthcareService resources with different service-type codes | Similar to REQ-SERVER-SHALL-16, this requirement is testable by sending requests with different service-type codes and verifying the response. |
| REQ-SERVER-SHALL-18 | Automatic | Simple | - FHIR Server running  - Test HealthcareService resources with different specialty codes |  Similar to previous requirements, automated tests can verify this functionality by sending requests with different specialty codes. |
| REQ-SERVER-SHALL-19 | Automatic | Simple | - FHIR Server running  - Test HealthcareService resources with known IDs | This requirement can be tested automatically by querying the server with known HealthcareService IDs and verifying the response. |
| REQ-SERVER-SHALL-20 | Automatic | Moderate | - FHIR Server running  - Test HealthcareService resources with different lastUpdated timestamps  - Understanding of FHIR date/time formats | This requirement involves date/time comparisons, requiring more complex test logic. Automated tests can create resources with specific timestamps and verify the server's response to _lastUpdated queries. | 


## FHIR Implementation Guide Requirement Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-21 | Automatic | Simple | - FHIR Server running  - Test client capable of sending search-type and read requests for InsurancePlan resources | This requirement can be tested by sending standard FHIR requests and verifying the response codes (200 for success). |
| REQ-SERVER-SHOULD-05 | Automatic | Simple | - FHIR Server running  - Test client capable of sending vread requests for InsurancePlan resources | Similar to REQ-SERVER-SHALL-21, this can be tested by sending a vread request and verifying the response code. |
| REQ-SERVER-SHALL-22 | Automatic | Simple | - FHIR Server running  - Test client capable of sending GET requests for InsurancePlan resources by ID | This can be tested by sending a GET request with a known InsurancePlan ID and verifying the response code and content. |
| REQ-SERVER-SHOULD-06 | Automatic | Moderate | - FHIR Server running  - Test client capable of sending GET requests for InsurancePlan resources by ID and version  - Pre-existing InsurancePlan resource with a history of versions | This requires retrieving a specific version of a resource, necessitating a pre-existing resource with version history. |
| REQ-SERVER-SHALL-23 | Automatic | Complex | - FHIR Server running  - Test client capable of sending GET requests with _includes parameters  - Pre-existing InsurancePlan resources with linked administered-by, owned-by, and coverage-area resources | This involves testing the server's ability to handle _includes, requiring pre-existing linked resources and verifying the response includes the requested data. | 


## Analysis of FHIR Implementation Guide Requirements

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-24 | Automatic | Simple | - FHIR Server running<br>- Test InsurancePlan resources with 'administered-by' populated | This requirement focuses on a simple GET request with a search parameter. Automated tests can easily construct the request and verify the response. |
| REQ-SERVER-SHALL-25 | Automatic | Simple | - FHIR Server running<br>- Test InsurancePlan resources with 'owned-by' populated | Similar to REQ-SERVER-SHALL-24, this requirement can be automatically tested by constructing a GET request with the specified search parameter. |
| REQ-SERVER-SHALL-26 | Automatic | Moderate | - FHIR Server running<br>- Test InsurancePlan resources with 'coverage-area' populated<br>- Understanding of FHIR Location resources and their representation in search parameters | This requirement involves a reference to a FHIR Location resource, requiring the test to potentially create and reference a valid Location resource. |
| REQ-SERVER-SHALL-27 | Automatic | Simple | - FHIR Server running<br>- Test InsurancePlan resources with 'name' populated | This requirement involves a simple string search parameter, making it easily testable with automated requests. |
| REQ-SERVER-SHALL-28 | Automatic | Moderate | - FHIR Server running<br>- Test InsurancePlan resources with 'plan-type' populated<br>- Understanding of FHIR Coding system and code representation in search parameters | This requirement involves a token search parameter, requiring the test to correctly format the system and code values in the request. | 


## FHIR Implementation Guide Requirement Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-29 | Automatic | Simple | - Test FHIR server endpoint  - Valid InsurancePlan resource with identifier | This requirement focuses on a simple GET request with an identifier parameter. Automated tests can easily construct the request and verify the response. |
| REQ-SERVER-SHALL-30 | Automatic | Simple | - Test FHIR server endpoint  - Valid InsurancePlan resource with _id | Similar to REQ-SERVER-SHALL-29, this involves a simple GET request with an _id parameter, easily testable automatically. |
| REQ-SERVER-SHALL-31 | Automatic | Simple | - Test FHIR server endpoint  - Valid InsurancePlan resource with _lastUpdated | This requirement can be tested automatically by constructing a GET request with a valid _lastUpdated parameter and verifying the response. |
| REQ-SERVER-SHALL-32 | Automatic | Simple | - Test FHIR server endpoint  - Valid InsurancePlan resource with type | Similar to previous requirements, this involves a simple GET request with a type parameter, easily automated. |
| REQ-SERVER-SHALL-01 | Hybrid | Moderate | - Test FHIR server endpoint  - Access to server's CapabilityStatement | This requirement involves checking the server's CapabilityStatement for the supported profile. While the retrieval and parsing of the CapabilityStatement can be automated, verifying the presence of the specific profile might require manual inspection or more complex logic within the automated test. | 


## Analysis of FHIR Implementation Guide Requirements

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-02 | Automatic | Simple | FHIR server running, Test client capable of sending search-type and read requests | This requirement specifies standard FHIR interactions (search-type, read) which can be tested automatically by sending requests and verifying responses. |
| REQ-SERVER-SHOULD-01 | Automatic | Simple | FHIR server running, Test client capable of sending vread requests | Similar to the previous requirement, this involves testing a standard FHIR interaction (vread) and can be automated. |
| REQ-SERVER-SHALL-03 | Automatic | Simple | FHIR server running, Test client capable of sending GET requests, Existing Location resource with known ID | This requirement involves a simple GET request with a known resource ID, making it straightforward to automate. |
| REQ-SERVER-SHOULD-02 | Automatic | Moderate | FHIR server running, Test client capable of sending GET requests, Existing Location resource with known ID and version ID | This test requires retrieving a specific version of a resource, adding a layer of complexity to the test setup. |
| REQ-SERVER-SHALL-04 | Automatic | Moderate | FHIR server running, Test client capable of sending GET requests with _includes parameter, Existing Location resources with related endpoint, organization, and partof resources | This requirement involves testing the _includes parameter with different resource types, requiring more complex test setup and data preparation. | 


## FHIR Implementation Guide Requirement Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-05 | Automatic | Moderate | - FHIR Server running<br>- Test data with Locations and related resources | This requirement specifies concrete API calls with _revincludes. Automated tests can be written to execute these calls and validate the response structure and content. |
| REQ-SERVER-SHALL-06 | Automatic | Complex | - FHIR Server running<br>- Test data with Locations and diverse search parameters | This requirement lists various search parameters for the Location resource. Automated tests can be designed to cover different combinations of search parameters and validate the results. The complexity arises from the need to generate diverse test data and cover various search scenarios. |
| REQ-SERVER-SHALL-07 | Manual | Simple | - FHIR Server CapabilityStatement | This requirement mandates the support of specific Organization resource profiles. Verification involves inspecting the server's CapabilityStatement to confirm the presence of these profiles. |
| REQ-SERVER-SHALL-08 | Automatic | Simple | - FHIR Server running | This requirement specifies support for specific interactions (search-type, read) on the Organization resource. Automated tests can be implemented to perform these interactions and validate the server's response. |
| REQ-SERVER-SHOULD-03 | Automatic | Simple | - FHIR Server running | Similar to REQ-SERVER-SHALL-08, this requirement focuses on the 'vread' interaction. Automated tests can be used to verify its support, but the 'SHOULD' conformance implies that failing this test might not be a critical failure. | 


## Analysis of FHIR Implementation Guide Requirements

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-09 | Automatic | Simple | - FHIR Server running<br>- Valid Organization resource ID | This requirement involves a simple GET request with a known resource ID. Automated tests can easily verify the response status code (200) and content type (application/fhir+json). |
| REQ-SERVER-SHOULD-04 | Automatic | Moderate | - FHIR Server running<br>- Valid Organization resource ID<br>- Existing resource history (previous version) | This requirement involves retrieving a specific version of a resource. Automated tests can verify the response, but require managing resource versions and obtaining valid version IDs. |
| REQ-SERVER-SHALL-10 | Automatic | Moderate | - FHIR Server running<br>- Valid Organization resource with related resources (partof, endpoint, coverage-area) | This requirement involves testing _include functionality. Automated tests can verify the response includes the specified related resources, but require setting up resources with the correct relationships. |
| REQ-SERVER-SHALL-11 | Automatic | Complex | - FHIR Server running<br>- Valid Organization resource with reverse relationships (Endpoint, HealthcareService, InsurancePlan, OrganizationAffiliation) | This requirement involves testing _revinclude functionality, which is more complex than _include. Automated tests can verify the response includes the resources referencing the target Organization, but require setting up various resources with correct reverse relationships. | 

**Note:** The last requirement (REQ-SERVER-SHALL-11) seems incomplete in the provided information. 

This analysis provides a starting point for your testing strategy. You might need to adjust the complexity and prerequisites based on your specific implementation and testing environment. 
