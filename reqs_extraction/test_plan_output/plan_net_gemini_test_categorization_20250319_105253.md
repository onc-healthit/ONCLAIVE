# Test Categorization for Plan Net

## Generated on: 2025-03-19 10:55:18

## FHIR Implementation Guide Requirements Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-NOT-01 | Hybrid | Moderate | - Test client capable of making authenticated and unauthenticated requests. - Network monitoring tools to inspect traffic for identifying information. |  While testing for the absence of authentication is straightforward, verifying that no identifying information is logged requires a combination of network analysis and server-side log inspection. |
| REQ-SERVER-SHALL-NOT-02 | Hybrid | Moderate | - Test client capable of simulating a directory app with configurable identifying information. - Network monitoring tools to inspect traffic for identifying information. | Similar to REQ-SERVER-SHALL-NOT-01, testing requires verifying both the server's lack of requirement for identifying information and the absence of such information in the actual requests. |
| REQ-CLIENT-SHALL-NOT-01 | Automatic | Simple | - Test client capable of simulating a directory app with configurable identifying information. | This requirement can be tested automatically by configuring the test client to send and not send identifying information and verifying the request payload. |
| REQ-SERVER-SHALL-01 | Automatic | Moderate | - Test client capable of querying for resources and validating the presence and completeness of Must Support data elements. - Definition of all Must Support data elements within the scope of the Implementation Guide. | This requirement can be tested automatically by validating the presence of all required data elements in the returned resources. The complexity arises from the need to define and maintain the list of Must Support elements. |
| REQ-SERVER-SHALL-NOT-03 | Automatic | Moderate | - Test client capable of querying for resources and validating the absence of specific data elements. - Definition of all data elements with minimum cardinality 0 within the scope of the Implementation Guide. - Ability to configure test data to trigger scenarios where these elements would be absent. | This requirement can be tested automatically by configuring specific scenarios where data elements with minimum cardinality 0 should be absent and verifying their exclusion from the returned resources. | 


## Analysis of FHIR Implementation Guide Requirements

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-04 | Hybrid | Moderate | - FHIR server implementing the IG<br>- Test cases with missing Must Support data elements | Automatically testable by sending requests with missing data and verifying the presence of nullFlavors or dataAbsentReason extension. Manual inspection might be needed to confirm the appropriateness of the chosen reason. |
| REQ-CLIENT-SHALL-02 | Automatic | Simple | - FHIR client implementing the IG<br>- Test cases with resource instances containing Must Support data elements | Can be automatically tested by sending various valid resource instances with Must Support data to the client and verifying no errors occur. |
| REQ-CLIENT-SHOULD-01 | Manual | Complex | - FHIR client implementing the IG<br>- Access to client's user interface or data storage | Requires manual inspection of the client's user interface or data storage to confirm if Must Support data is displayed/stored appropriately. Subjective assessment of "human use" is involved. |
| REQ-CLIENT-SHALL-03 | Hybrid | Moderate | - FHIR client implementing the IG<br>- Mock FHIR server with controllable responses | Requires a combination of automated testing (verifying client behavior when receiving resources with missing data) and manual inspection/analysis of client logic to confirm the interpretation of missing data. |
| REQ-CLIENT-SHALL-04 | Automatic | Simple | - FHIR client (Consumer App) implementing the IG<br>- Test cases with resource instances containing Must Support data elements asserting missing information (e.g., using nullFlavors) | Similar to REQ-CLIENT-SHALL-02, this can be automatically tested by sending resource instances with assertions of missing information and verifying the client processes them without errors. | 


## FHIR Implementation Guide Requirements Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-CLIENT-SHOULD-02 | Hybrid | Moderate | - Test client capable of caching query results. - Server supporting _lastUpdated search parameter. |  - **Automatic:** Can automatically send queries with _lastUpdated filter and verify results. - **Manual:** Requires inspection to confirm client caching mechanism is utilizing the timestamp appropriately. |
| REQ-CLIENT-SHOULD-03 | Hybrid | Moderate | - Test client capable of caching query results. - Server supporting _id queries. | - **Automatic:** Can automatically send periodic _id queries for cached data and verify responses. - **Manual:** Requires inspection to confirm client behavior upon receiving "not found" responses (e.g., data refresh). |
| REQ-SERVER-SHALL-01 | Automatic | Simple | - Test client capable of querying HealthcareService resources. | Straightforward verification by querying for HealthcareService resources and confirming their existence. |
| REQ-SERVER-SHOULD-01 | Manual | Simple | - Access to HealthcareService resources. - Understanding of expected Organization association logic. | Requires inspecting HealthcareService resources to verify the presence and correctness of Organization references, considering the "solo practitioner" exception. |
| REQ-SERVER-SHOULD-02 | Manual | Moderate | - Access to PractitionerRole and OrganizationAffiliation resources. - Understanding of Network linking logic. |  Requires inspecting PractitionerRole and OrganizationAffiliation resources to confirm the presence and correctness of Network references, ensuring alignment with the described logic. | 


## FHIR Implementation Guide Requirement Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHOULD-03 | Hybrid | Moderate | Access to PractitionerRole, OrganizationAffiliation, HealthcareServices, Organization, Network, and Location resources. |  Automatic verification of resource presence and linkage is possible. However, manual inspection might be needed to confirm the semantic correctness of the associations. |
| REQ-SERVER-MAY-01 | Automatic | Simple |  N/A | This requirement can be tested automatically by checking if Location resources can have a valid GeoJSON object associated with them. |
| REQ-SERVER-SHALL-01 | Manual | Complex |  Complete list of defined profiles in the Implementation Guide. |  This requires manual verification by comparing the supported profiles against the defined profiles in the IG. |
| REQ-SERVER-SHALL-02 | Hybrid | Complex |  Access to FHIR specification and understanding of RESTful behavior. |  Automated tests can cover standard RESTful operations. However, manual review and specific test cases might be needed for edge cases and complex interactions. |
| REQ-SERVER-SHALL-03 | Automatic | Moderate |  Ability to trigger different request scenarios. |  This can be tested automatically by sending requests that should trigger each specific response class and verifying the returned status code. | 


## Analysis of FHIR Implementation Guide Requirements

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-04 | Automatic | Simple | - Test client capable of sending JSON requests  - Access to Plan-Net Server endpoint |  Verifying JSON support can be automated by sending a JSON request and checking for a successful response code (e.g., 200 OK). |
| REQ-SERVER-SHALL-05 | Automatic | Simple | - Test client capable of retrieving FHIR resources - Access to Plan-Net Server endpoint |  Automated tests can retrieve resources and assert the presence and correctness of the `meta.profile` attribute. |
| REQ-SERVER-SHALL-06 | Hybrid | Complex | - Test client capable of constructing complex search queries - Comprehensive list of supported search parameters and their combinations - Access to Plan-Net Server endpoint with populated data |  Testing individual search parameters can be automated. However, testing all combinations might be impractical. A hybrid approach using automated tests for common combinations and manual spot-checks for edge cases is recommended. |
| REQ-SERVER-SHALL-07 | Hybrid | Moderate | - Test client capable of constructing chained search queries - List of search parameters with the 'chain' property - Access to Plan-Net Server endpoint with data supporting chained relationships |  Automated tests can verify forward and reverse chaining for each specified parameter. Manual review might be needed to confirm the correctness of chained results in specific scenarios. |
| REQ-SERVER-SHOULD-01 | Automatic | Simple | - Test client capable of sending XML requests - Access to Plan-Net Server endpoint |  Similar to JSON support, XML support can be tested by sending an XML request and verifying the response code. As it's a SHOULD requirement, failure shouldn't be a blocking issue. | 


## FHIR Implementation Guide Requirement Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-08 | Automatic | Simple | - Test client capable of sending unauthorized requests  - Server running with authentication enabled |  Verifying HTTP response codes can be automated. Authentication setup is a common prerequisite. |
| REQ-SERVER-SHALL-01 | Automatic | Moderate | - Test client capable of sending search-type and read requests | Requires testing multiple interaction types, increasing complexity slightly. |
| REQ-SERVER-SHOULD-01 | Automatic | Simple | - Test client capable of sending vread requests |  Similar to read interaction testing, but with a specific version request. |
| REQ-SERVER-SHALL-02 | Automatic | Simple | - Test client capable of sending GET requests with specific IDs |  Straightforward resource retrieval by ID. |
| REQ-SERVER-SHOULD-02 | Automatic | Moderate | - Test client capable of sending GET requests with specific IDs and versions |  Similar to retrieving by ID, but includes version parameter, adding complexity. | 


## FHIR Implementation Guide Requirement Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-03 | Automatic | Simple | - FHIR Server running  - Test client capable of making GET requests with _include parameters | This requirement involves a specific GET request with a defined parameter. Automated tests can easily construct and execute this request, then validate the response structure. |
| REQ-SERVER-SHALL-04 | Automatic | Moderate | - FHIR Server running  - Test client capable of making GET requests with search parameters  - Pre-existing Organization resource | This requirement involves searching with a specific search parameter. Automated tests can create an Organization resource, use its ID in the search request, and validate the response. |
| REQ-SERVER-SHALL-05 | Automatic | Simple | - FHIR Server running  - Test client capable of making GET requests with search parameters  - Pre-existing Endpoint resource | This requirement involves searching by _id, which is straightforward to test automatically. Tests can create an Endpoint resource, use its ID in the search request, and validate the response. |
| REQ-SERVER-SHALL-06 | Automatic | Simple | - FHIR Server running  - Test client capable of making GET requests with search parameters | This requirement involves searching by _lastUpdated. Automated tests can easily construct a GET request with a valid date/time value for this parameter and validate the response. |
| REQ-SERVER-SHALL-07 | Hybrid | Moderate | - FHIR Server running  - Test client capable of making GET and SEARCH requests  - Understanding of FHIR search-type interaction | This requirement involves verifying support for both 'search-type' and 'read' interactions. While 'read' can be tested automatically, 'search-type' might require manual inspection of CapabilityStatement or conformance documentation alongside automated 'SEARCH' requests. | 


## FHIR Implementation Guide Requirement Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHOULD-03 | Hybrid | Simple | FHIR Server supporting vread | While the request can be automated, verifying the content requires manual inspection against the specification. |
| REQ-SERVER-SHALL-08 | Automatic | Simple | FHIR Server with HealthcareService resources | This involves a simple GET request and response code validation (200). |
| REQ-SERVER-SHOULD-04 | Automatic | Moderate | FHIR Server with versioned HealthcareService resources | Requires constructing a specific URL with ID and version, but the validation is automated. |
| REQ-SERVER-SHALL-09 | Automatic | Moderate | FHIR Server with HealthcareService resources and linked resources | Involves multiple GET requests with _includes, but response validation is automated. |
| REQ-SERVER-SHALL-10 | Automatic | Moderate | FHIR Server with HealthcareService resources and reverse-linked resources | Similar to REQ-SERVER-SHALL-09, but with _revincludes, requiring specific data setup. | 


## Analysis of FHIR Implementation Guide Requirements

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-11 | Automatic | Simple | - FHIR Server running<br>- Test HealthcareService resources with location data | This requirement focuses on a single search parameter and a simple GET request, making it suitable for automated testing. |
| REQ-SERVER-SHALL-12 | Automatic | Simple | - FHIR Server running<br>- Test HealthcareService resources with coverage-area data | Similar to REQ-SERVER-SHALL-11, this requirement can be automatically tested with a specific GET request and pre-populated data. |
| REQ-SERVER-SHALL-13 | Automatic | Simple | - FHIR Server running<br>- Test HealthcareService resources with organization data | This requirement follows the same pattern as the previous two, allowing for straightforward automated testing. |
| REQ-SERVER-SHALL-14 | Automatic | Simple | - FHIR Server running<br>- Test HealthcareService resources with endpoint data | This requirement can be automatically tested by sending a GET request with the specified search parameter and verifying the response. |
| REQ-SERVER-SHALL-15 | Automatic | Simple | - FHIR Server running<br>- Test HealthcareService resources with name data | This requirement can be automatically tested using a GET request with the 'name' search parameter and pre-populated data. | 

**General Notes:**

* All requirements are categorized as "Automatic" because they involve testing specific API endpoints and responses, which can be automated using testing frameworks.
* The complexity is "Simple" for all requirements because they involve single search parameters and basic GET requests.
* Prerequisites for all tests include a running FHIR server and pre-populated test data containing the relevant information (location, coverage-area, organization, endpoint, name) for HealthcareService resources. 


## FHIR Implementation Guide Requirements Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-16 | Automatic | Simple | - FHIR Server running<br>- Test HealthcareService resources with different service-category values | The requirement clearly defines the search parameter and expected behavior. Automated tests can send requests with different `service-category` values and verify the response. |
| REQ-SERVER-SHALL-17 | Automatic | Simple | - FHIR Server running<br>- Test HealthcareService resources with different service-type values | Similar to REQ-SERVER-SHALL-16, this requirement is specific and can be tested automatically by sending requests with various `service-type` values. |
| REQ-SERVER-SHALL-18 | Automatic | Simple | - FHIR Server running<br>- Test HealthcareService resources with different specialty values |  This requirement follows the same pattern as the previous two and can be tested automatically using different `specialty` values in the requests. |
| REQ-SERVER-SHALL-19 | Automatic | Simple | - FHIR Server running<br>- Test HealthcareService resources with known IDs | This requirement can be tested automatically by querying for resources with known IDs and verifying the response. |
| REQ-SERVER-SHALL-20 | Automatic | Moderate | - FHIR Server running<br>- Test HealthcareService resources with different lastUpdated timestamps<br>- Ability to manipulate resource timestamps for testing | This requirement can be tested automatically, but requires the ability to control and manipulate the `_lastUpdated` timestamp of test resources to ensure accurate verification. | 


## FHIR Implementation Guide Requirement Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-21 | Automatic | Simple | - FHIR Server running  - Test client capable of sending search-type and read requests | This requirement focuses on standard FHIR interactions (search-type, read) which can be tested automatically. |
| REQ-SERVER-SHOULD-05 | Automatic | Simple | - FHIR Server running  - Test client capable of sending vread requests | Similar to the previous requirement, this one focuses on a standard FHIR interaction (vread) and can be tested automatically. |
| REQ-SERVER-SHALL-22 | Automatic | Simple | - FHIR Server running  - Test client capable of sending GET requests  - Pre-existing InsurancePlan resource with known ID | This requirement specifies a concrete GET request format for retrieving a resource by ID, making it suitable for automated testing. |
| REQ-SERVER-SHOULD-06 | Automatic | Moderate | - FHIR Server running  - Test client capable of sending GET requests  - Pre-existing InsurancePlan resource with known ID and version | Similar to the previous requirement, but includes version in the request, slightly increasing complexity. |
| REQ-SERVER-SHALL-23 | Automatic | Complex | - FHIR Server running  - Test client capable of sending GET requests with _includes  - Pre-existing InsurancePlan resources with related resources (administered-by, owned-by, coverage-area) | This requirement involves testing _includes functionality, which requires setting up relationships between resources, making it more complex. | 


## Analysis of FHIR Implementation Guide Requirements

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-24 | Automatic | Simple | - FHIR Server running<br>- Test data with InsurancePlan resources and varying `administered-by` values | This requirement involves a simple GET request with a search parameter. Automated tests can easily construct the request and verify the response. |
| REQ-SERVER-SHALL-25 | Automatic | Simple | - FHIR Server running<br>- Test data with InsurancePlan resources and varying `owned-by` values | Similar to REQ-SERVER-SHALL-24, this involves a straightforward GET request with a different search parameter. |
| REQ-SERVER-SHALL-26 | Automatic | Moderate | - FHIR Server running<br>- Test data with InsurancePlan resources and varying `coverage-area` values<br>- Understanding of FHIR Location resources and their representation in search parameters | This involves a GET request with a reference parameter. The complexity arises from ensuring the test data includes valid FHIR Location resources and correctly uses their references in the search parameter. |
| REQ-SERVER-SHALL-27 | Automatic | Simple | - FHIR Server running<br>- Test data with InsurancePlan resources and varying `name` values | This involves a simple GET request with a string-based search parameter. Automated tests can easily handle this. |
| REQ-SERVER-SHALL-28 | Automatic | Moderate | - FHIR Server running<br>- Test data with InsurancePlan resources and varying `plan-type` values<br>- Understanding of FHIR CodeableConcept and its representation in search parameters | This involves a GET request with a token-based search parameter. The complexity arises from constructing the search parameter correctly using the `system` and `code` components of the CodeableConcept. | 

**Note:** 

* This analysis assumes the existence of suitable testing frameworks and tools for FHIR.
* The "Complexity" assessment is relative and might vary depending on the specific testing tools and infrastructure used.
* While these requirements are categorized as "Automatic," manual review of test results and edge case handling might still be necessary. 


## Analysis of FHIR Implementation Guide Requirements

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-29 | Automatic | Simple | - Test FHIR server endpoint<br>- Valid InsurancePlan resource with identifier | This requirement focuses on a simple GET request with an identifier parameter. Automated tests can easily construct the request and verify the response. |
| REQ-SERVER-SHALL-30 | Automatic | Simple | - Test FHIR server endpoint<br>- Valid InsurancePlan resource with _id | Similar to REQ-SERVER-SHALL-29, this involves a simple GET request with an _id parameter, making it suitable for automated testing. |
| REQ-SERVER-SHALL-31 | Automatic | Simple | - Test FHIR server endpoint<br>- Valid InsurancePlan resource with _lastUpdated | This requirement can be tested automatically by constructing a GET request with a valid _lastUpdated parameter and verifying the response. |
| REQ-SERVER-SHALL-32 | Automatic | Simple | - Test FHIR server endpoint<br>- Valid InsurancePlan resource with type | Similar to previous requirements, this involves a simple GET request with a type parameter, making it suitable for automated testing. |
| REQ-SERVER-SHALL-01 | Hybrid | Moderate | - Test FHIR server endpoint<br>- Access to server's CapabilityStatement | This requirement involves verifying the presence of a specific profile in the server's CapabilityStatement. While the presence can be checked automatically, confirming adherence to the profile might require manual inspection or more complex automated validation against the profile definition. | 


## FHIR Implementation Guide Requirement Analysis: Location Resource

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-02 | Automatic | Simple | FHIR Server running, Test client capable of sending search-type and read requests | This requirement focuses on standard FHIR interactions and can be tested by sending specific requests and verifying the response codes. |
| REQ-SERVER-SHOULD-01 | Automatic | Simple | FHIR Server running, Test client capable of sending vread requests | Similar to REQ-SERVER-SHALL-02, this focuses on a standard FHIR interaction (vread) and can be tested automatically. |
| REQ-SERVER-SHALL-03 | Automatic | Simple | FHIR Server running, Test client capable of sending GET requests, Existing Location resource with known ID | This requirement can be tested by sending a GET request to the specified endpoint with a known Location ID and verifying the response code and content. |
| REQ-SERVER-SHOULD-02 | Automatic | Moderate | FHIR Server running, Test client capable of sending GET requests, Existing Location resource with known ID and version ID | Similar to REQ-SERVER-SHALL-03, but requires knowledge of a specific version ID for the Location resource. |
| REQ-SERVER-SHALL-04 | Automatic | Moderate | FHIR Server running, Test client capable of sending GET requests with _includes parameter | This requirement can be tested by sending GET requests with the specified _includes parameters and verifying the response code and the presence of the included resources. | 


## FHIR Implementation Guide Requirement Analysis

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-05 | Automatic | Moderate | - FHIR Server running<br>- Test data with Locations and related resources | This requirement specifies concrete API calls with _revincludes, allowing for automated testing of response structure and content. |
| REQ-SERVER-SHALL-06 | Automatic | Complex | - FHIR Server running<br>- Test data with Locations and diverse search parameters | This requirement lists specific search parameters and their expected behavior, enabling automated tests for each parameter with various valid and invalid inputs. |
| REQ-SERVER-SHALL-07 | Manual | Simple | - FHIR Server CapabilityStatement | This requirement mandates support for specific profiles, requiring manual inspection of the CapabilityStatement to verify the presence of declared profiles. |
| REQ-SERVER-SHALL-08 | Automatic | Simple | - FHIR Server running | This requirement specifies support for standard interactions (search-type, read) on the Organization resource, which can be tested automatically by attempting the operations. |
| REQ-SERVER-SHOULD-03 | Automatic | Simple | - FHIR Server running | Similar to REQ-SERVER-SHALL-08, this requirement focuses on the "vread" interaction and can be tested automatically by attempting the operation. Note: "SHOULD" implies flexibility in implementation, so test failure might not be a strict violation. | 


## FHIR Implementation Guide Requirement Analysis: Organization Resource

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
|---|---|---|---|---|
| REQ-SERVER-SHALL-09 | Automatic | Simple | - FHIR Server running  - Valid Organization resource ID | This requirement involves a simple GET request with a known resource ID. Automated tests can easily execute the request and verify the response status code (200) and resource type. |
| REQ-SERVER-SHOULD-04 | Automatic | Moderate | - FHIR Server running - Valid Organization resource ID - Existing Organization resource with version history | This requirement involves a GET request with a specific version ID. Automated tests can retrieve a resource, capture its version ID, and then attempt to retrieve that specific version. Verification includes checking the response status code (200) and the returned resource's metadata. |
| REQ-SERVER-SHALL-10 | Automatic | Moderate | - FHIR Server running - Valid Organization resource with populated references for each _include | This requirement involves multiple GET requests with different _include parameters. Automated tests can execute each request and verify the response status code (200) and the presence of included resources in the response bundle. |
| REQ-SERVER-SHALL-11 | Automatic | Complex | - FHIR Server running - Valid Organization resource with corresponding resources for each _revinclude | This requirement involves multiple GET requests with different _revinclude parameters. Automated tests can execute each request and verify the response status code (200) and the presence of reversely included resources in the response bundle. The complexity arises from ensuring the existence and proper linking of resources for each _revinclude. | 
