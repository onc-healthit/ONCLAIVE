# Comprehensive Test Plan for Plan Net

## Generated on: 2025-03-19 11:02:50



## Test Plan for Server-SHALL NOT

## Test Plan: FHIR Implementation Guide Conformance

**Document Version:** 1.0
**Date:** 2023-10-27

## 1. Executive Summary

This document outlines the test plan for validating conformance to the FHIR Implementation Guide, specifically focusing on the Plan-Net service's privacy and security requirements. The primary objective is to ensure the service adheres to the specified requirements regarding authentication and data privacy.

**Scope:**

* This test plan covers the verification of requirements REQ-SERVER-SHALL-NOT-01 and REQ-SERVER-SHALL-NOT-02.
* It focuses on black-box testing of the Plan-Net service API.

**Key Testing Considerations:**

* **Privacy Focus:** The tests prioritize verifying the absence of authentication mechanisms and the prevention of consumer identification through queries.
* **Black-box Approach:** Tests will interact with the Plan-Net service API without knowledge of its internal implementation.
* **Automated Testing:** Where applicable, automated tests will be developed to ensure repeatability and efficiency.

## 2. Test Environment Requirements

**Infrastructure:**

* **FHIR Server:** A running instance of the Plan-Net service compliant with the FHIR specification.
* **Test Client:** A tool capable of sending HTTP requests to the FHIR server (e.g., Postman, REST Assured).
* **Network Connectivity:**  Uninterrupted network connectivity between the test client and the FHIR server.

**Tools:**

* **FHIR Validator:** A tool for validating FHIR resources against the base FHIR specification and any applicable profiles (e.g., FHIR Validator online).
* **Test Management Tool:** Optional tool for managing test cases, results, and reporting (e.g., TestRail, Zephyr).

**Test Data:**

* **Sample FHIR Resources:** Representative FHIR resources for testing various API endpoints.
* **Modified FHIR Resources:**  Resources modified to include potentially identifying information for negative testing scenarios.

**FHIR Server Configuration:**

* The FHIR server should be configured according to the implementation guide, with specific attention to any security and privacy settings.

## 3. Test Groupings

**Group 1: Authentication and Authorization**

* **Requirements:** REQ-SERVER-SHALL-NOT-01
* **Test Approach:** Attempt to access protected resources with and without authentication credentials. Verify that access is granted in both cases.
* **Key Considerations:**  Focus on testing various authentication mechanisms (e.g., Basic Auth, OAuth2) to ensure none are enforced.

**Group 2: Data Privacy**

* **Requirements:** REQ-SERVER-SHALL-NOT-02
* **Test Approach:** Send requests with and without potentially identifying information in headers, parameters, and resource bodies. Verify that responses are consistent and do not leak identifying information.
* **Key Considerations:**  Test a variety of API endpoints and resource types to ensure comprehensive coverage.

## 4. Individual Test Cases

**Test Case ID:** TC-REQ-SERVER-SHALL-NOT-01-01

* **Requirement:** REQ-SERVER-SHALL-NOT-01
* **Preconditions:** 
    * FHIR server is running and accessible.
    * Test client is configured with the FHIR server endpoint.
* **Test Steps:**
    1. Send a GET request to a protected resource endpoint without any authentication headers.
    2. Verify that the server responds with a 200 OK status code and the requested resource.
* **Expected Results:** The server should grant access to the protected resource without requiring authentication.
* **Validation Criteria:**
    * HTTP status code: 200 OK
    * Response body: Contains the requested resource data.

**Test Case ID:** TC-REQ-SERVER-SHALL-NOT-02-01

* **Requirement:** REQ-SERVER-SHALL-NOT-02
* **Preconditions:** 
    * FHIR server is running and accessible.
    * Test client is configured with the FHIR server endpoint.
* **Test Steps:**
    1. Send a GET request to a resource endpoint with potentially identifying information included in the request headers (e.g., custom header "X-Consumer-ID").
    2. Send another GET request to the same endpoint without the identifying header.
    3. Compare the responses received in steps 1 and 2.
* **Expected Results:** The server responses should be identical, regardless of the presence or absence of the identifying header.
* **Validation Criteria:**
    * Response bodies from both requests are identical.
    * No identifying information from the request header is present in the response body.

**Test Logic Outline (Pseudocode):**

```
function test_no_identifying_info_leakage(endpoint, resource_id):
  headers_with_id = {"X-Consumer-ID": "test-user-123"}
  response_with_id = send_request("GET", endpoint + "/" + resource_id, headers=headers_with_id)
  response_without_id = send_request("GET", endpoint + "/" + resource_id)
  assert response_with_id.body == response_without_id.body
  assert "test-user-123" not in response_with_id.body
```

## 5. Special Testing Considerations

**Edge Cases:**

* Test with various combinations of potentially identifying information in different parts of the request (headers, parameters, resource body).
* Test with malformed or unexpected data in the identifying fields to ensure the server handles these cases gracefully.

**Performance Considerations:**

* While not the primary focus, monitor response times for all test cases to identify potential performance bottlenecks.
* Consider conducting load testing to assess the service's performance under high traffic.

**Security Testing Aspects:**

* Conduct vulnerability scanning and penetration testing to identify and mitigate potential security risks.
* Review the server's logging mechanisms to ensure no sensitive information is being logged.

This test plan provides a comprehensive framework for validating the privacy and security requirements of the Plan-Net service. By executing these tests, stakeholders can gain confidence that the service adheres to the specified requirements and protects consumer data appropriately. 


## Test Plan for Server-SHALL

## Test Plan: Plan-Net FHIR Implementation Guide

**Version:** 1.0
**Date:** 2023-10-27

### 1. Executive Summary

This document outlines the test plan for validating conformance to the Plan-Net FHIR Implementation Guide. The purpose of this plan is to ensure that FHIR servers claiming conformance to the guide meet all specified requirements. 

**Scope:**

This test plan covers the following aspects of the Plan-Net FHIR Implementation Guide:

* Support for mandatory FHIR resources and profiles.
* Implementation of RESTful interactions as defined in the FHIR specification.
* Handling of specific HTTP response codes.
* Support for search parameters, including chaining and combinations.
* Security considerations related to unauthorized requests.

**Key Testing Considerations:**

* This test plan utilizes a combination of automated and manual testing approaches.
* Test data will be used to simulate real-world scenarios and edge cases.
* Performance and security testing will be conducted to assess the server's robustness.

### 2. Test Environment Requirements

**Infrastructure:**

* A FHIR server claiming conformance to the Plan-Net FHIR Implementation Guide.
* A testing client capable of sending FHIR requests and receiving responses (e.g., Postman, Insomnia).
* Optionally, a FHIR testing tool for automated test execution (e.g., Touchstone, Inferno).

**Tools:**

* FHIR validator for validating resource instances against Plan-Net profiles.
* Tool for generating synthetic FHIR data conforming to Plan-Net profiles.

**Test Data:**

* A set of synthetic FHIR resources conforming to the Plan-Net profiles, covering various scenarios.
* Test data should include valid and invalid instances to test validation rules.

**FHIR Server Configuration Requirements:**

* The FHIR server should be configured to expose the Plan-Net FHIR API endpoints.
* Authentication and authorization mechanisms should be enabled as per the guide's security requirements.

### 3. Test Groupings

The requirements are grouped into the following logical test categories:

**Group 1: General Server Conformance (REQ-SERVER-SHALL-01 to REQ-SERVER-SHALL-08)**

* **Test Approach:** This group focuses on verifying general server capabilities and adherence to the FHIR specification. Automated tests will be primarily used to validate RESTful behavior, response codes, and support for JSON format.
* **Key Considerations:**  Ensure the server correctly implements HTTP methods (GET, POST, PUT, DELETE), handles different resource versions, and returns accurate OperationOutcome resources for errors.

**Group 2: Resource Interactions and Search (REQ-SERVER-SHALL-09 to REQ-SERVER-SHALL-32)**

* **Test Approach:** This group validates the server's ability to handle resource-specific interactions like read, search-type, _include, and _revinclude. Automated and manual testing will be employed to verify the correct implementation of search parameters, including chaining and combinations.
* **Key Considerations:**  Pay close attention to the supported search parameters for each resource, their types, and modifiers. Test various combinations of search parameters to ensure accurate results filtering.

**Group 3: Profile Validation (REQ-SERVER-SHALL-01, REQ-SERVER-SHALL-07)**

* **Test Approach:** This group focuses on validating that the server correctly supports and identifies the Plan-Net profiles. Inspection of the CapabilityStatement and resource instances will be used to confirm profile conformance.
* **Key Considerations:**  Verify that the `meta.profile` element in resource instances accurately reflects the Plan-Net profile used.

**Group 4: Security (REQ-SERVER-SHALL-08)**

* **Test Approach:** This group focuses on verifying the server's security mechanisms. Manual and automated tests will be used to simulate unauthorized requests and validate the server's response.
* **Key Considerations:**  Test different authentication methods and authorization levels to ensure only authorized users can access protected resources.

### 4. Individual Test Cases

**Group 1: General Server Conformance**

| Test Case ID | Preconditions | Test Steps | Expected Results | Validation Criteria | Test Logic/Pseudocode |
|---|---|---|---|---|---|
| TC-SERVER-SHALL-01 | Server is running and accessible. | 1. Send a request to the server's base URL. | 2. Server returns a valid CapabilityStatement resource. | 1. HTTP status code 200 OK. 2. Returned resource conforms to the CapabilityStatement profile. | - |
| TC-SERVER-SHALL-02 | N/A | 1. Send various FHIR RESTful requests (create, read, update, delete, search) using JSON format. | 2. Server processes requests and returns appropriate responses according to the FHIR specification. | 1. HTTP status codes are returned as per the FHIR specification. 2. Returned resources are valid FHIR resources. | - |
| TC-SERVER-SHALL-03 | N/A | 1. Trigger scenarios that should result in specific HTTP response codes (400, 401/4xx, 403, 404, 410). | 2. Server returns the expected HTTP response codes with appropriate OperationOutcome resources. | 1. Correct HTTP status code is returned. 2. OperationOutcome resource contains relevant details about the error. | - |
| TC-SERVER-SHALL-04 | N/A | 1. Send FHIR requests using JSON format. | 2. Server successfully processes the requests. | 1. HTTP status code 200 OK or 201 Created for successful requests. | - |
| TC-SERVER-SHALL-05 | N/A | 1. Retrieve a resource instance from the server. | 2. The resource instance contains the `meta.profile` element with the correct Plan-Net profile URL. | 1. The `meta.profile` element is present. 2. The element contains the correct Plan-Net profile URL. | - |
| TC-SERVER-SHALL-06 | N/A | 1. Perform searches using individual search parameters. 2. Perform searches using combinations of search parameters. | 2. Server returns the correct filtered results based on the search criteria. | 1. Returned resources match the search criteria. 2. No unexpected errors occur when combining search parameters. | - |
| TC-SERVER-SHALL-07 | N/A | 1. Perform searches using search parameters that support chaining. | 2. Server correctly applies forward and reverse chaining logic to return the expected results. | 1. Returned resources reflect the chaining behavior defined for the search parameter. | - |
| TC-SERVER-SHALL-08 | N/A | 1. Send an unauthorized request to a protected resource. | 2. Server rejects the request with HTTP 401 Unauthorized. | 1. HTTP status code 401 Unauthorized is returned. | - |

**Group 2: Resource Interactions and Search**

This group will follow a similar structure to Group 1, with individual test cases for each requirement (REQ-SERVER-SHALL-09 to REQ-SERVER-SHALL-32). Each test case will focus on verifying the specific interaction or search parameter defined in the requirement.

**Group 3: Profile Validation**

| Test Case ID | Preconditions | Test Steps | Expected Results | Validation Criteria | Test Logic/Pseudocode |
|---|---|---|---|---|---|
| TC-SERVER-SHALL-01 | N/A | 1. Inspect the CapabilityStatement resource for supported profiles. | 2. The CapabilityStatement lists all mandatory Plan-Net profiles. | 1. All required Plan-Net profiles are present in the CapabilityStatement. | - |
| TC-SERVER-SHALL-07 | N/A | 1. Retrieve instances of resources that have specific Plan-Net profiles defined. | 2. The retrieved resource instances validate successfully against the corresponding Plan-Net profiles. | 1. No validation errors are reported for the resource instances. | - |

**Group 4: Security**

This group will have additional test cases based on the specific security mechanisms implemented by the server. These test cases should cover scenarios like:

* Accessing protected resources with invalid credentials.
* Attempting to perform unauthorized actions (e.g., a user without write permissions trying to update a resource).
* Testing for vulnerabilities like cross-site scripting (XSS) and SQL injection.

### 5. Special Testing Considerations

**Edge Cases:**

* Test the server's behavior with boundary values for search parameters (e.g., date ranges, numerical limits).
* Use special characters and non-Latin characters in resource data to test for encoding issues.
* Simulate scenarios with large datasets to assess the server's performance.

**Performance Considerations:**

* Measure the response time for various FHIR interactions, especially search operations.
* Conduct load testing to determine the server's capacity and scalability.

**Security Testing Aspects:**

* Perform penetration testing to identify potential security vulnerabilities.
* Review the server's audit logs to ensure proper tracking of user actions.
* Conduct code reviews to identify potential security flaws in the server's implementation.

This test plan provides a comprehensive framework for validating conformance to the Plan-Net FHIR Implementation Guide. By executing these tests, implementers can ensure their servers meet the requirements and provide interoperable and secure data exchange capabilities. 


## Test Plan for Server-SHOULD

## Test Plan for FHIR Plan-Net Implementation Guide

**Version:** 1.0
**Date:** 2023-10-26

### 1. Executive Summary

This document outlines the test plan for validating conformance to the FHIR Plan-Net Implementation Guide. The primary objective is to ensure that FHIR servers adhere to the requirements outlined in the guide, specifically focusing on the interactions and relationships between HealthcareServices, Organizations, Practitioners, Networks, Locations, and Insurance Plans.

**Scope:**

This test plan covers the following aspects of the FHIR Plan-Net Implementation Guide:

* Association of HealthcareServices with Organizations.
* Linking Practitioners and Organizations to Networks.
* Utilization of PractitionerRole and OrganizationAffiliation resources.
* Support for XML format in interactions.
* `vread` interaction support and resource retrieval by version for Endpoint, HealthcareService, InsurancePlan, Location, and Organization resources.

**Key Testing Considerations:**

* This test plan focuses on "SHOULD" level requirements, meaning successful implementation is highly recommended but not mandatory.
* Testing will involve both inspection of resource structures and actual API interactions with a FHIR server.
* Test data will be used to simulate real-world scenarios and edge cases.
* Performance and security testing are out of scope for this test plan.

### 2. Test Environment Requirements

**Infrastructure:**

* A FHIR server compliant with FHIR R4 and the Plan-Net Implementation Guide.
* A testing tool capable of sending FHIR requests and validating responses (e.g., Postman, Insomnia, custom scripts).

**Tools:**

* FHIR validator for validating resource instances against the base FHIR specification and Plan-Net profiles.
* Tool for generating synthetic FHIR data conforming to the Plan-Net Implementation Guide.

**Test Data:**

* A set of synthetic FHIR resources representing HealthcareServices, Organizations, Practitioners, Networks, Locations, and Insurance Plans, adhering to the Plan-Net Implementation Guide.
* Test data should include variations and edge cases to ensure comprehensive testing.

**FHIR Server Configuration:**

* The FHIR server should be configured to support the Plan-Net Implementation Guide profiles and interactions.
* Ensure the server accepts both JSON and XML formats for requests and responses.

### 3. Test Groupings

This section groups related requirements into logical test categories:

**Group 1: Resource Relationships and Associations**

* **REQ-SERVER-SHOULD-01**: Associate HealthcareServices with an Organization.
* **REQ-SERVER-SHOULD-02**: Link Practitioners and Organizations to Networks through PractitionerRole and OrganizationAffiliation.
* **REQ-SERVER-SHOULD-03**: Utilize PractitionerRole and OrganizationAffiliation to associate Practitioners and Organizations with HealthcareServices, Organizations, Networks, and Locations.

**Test Approach:** This group will primarily involve inspection of resource instances. Test data will be loaded onto the FHIR server, and queries will be performed to validate the relationships between resources as specified in the requirements.

**Key Considerations:** Pay close attention to the cardinality and types of references used in the resources.

**Group 2: XML Support**

* **REQ-SERVER-SHOULD-01**: Support XML format for interactions.

**Test Approach:** This group will involve sending FHIR requests in XML format and verifying that the server accepts and processes them correctly. Responses should also be validated for correct XML format.

**Key Considerations:** All interactions defined in the Plan-Net Implementation Guide should be tested with XML formatted requests.

**Group 3: `vread` Interaction and Resource Versioning**

* **REQ-SERVER-SHOULD-01**: Support vread interaction for Endpoint.
* **REQ-SERVER-SHOULD-02**: Return Endpoint resource by ID and version.
* **REQ-SERVER-SHOULD-03**: Support vread interaction for HealthcareService.
* **REQ-SERVER-SHOULD-04**: Return HealthcareService resource by ID and version.
* **REQ-SERVER-SHOULD-05**: Support vread interaction for InsurancePlan.
* **REQ-SERVER-SHOULD-06**: Return InsurancePlan resource by ID and version.
* **REQ-SERVER-SHOULD-01**: Support Location vread interaction.
* **REQ-SERVER-SHOULD-02**: Return Location resource history by version ID.
* **REQ-SERVER-SHOULD-03**: Support Organization vread interaction.
* **REQ-SERVER-SHOULD-04**: Return Organization resource history by version ID.

**Test Approach:** This group will involve sending `vread` requests for each specified resource type and verifying that the server returns the correct resource version based on the provided version ID.

**Key Considerations:** Ensure the server correctly handles invalid or nonexistent version IDs.

### 4. Individual Test Cases

**Group 1: Resource Relationships and Associations**

**Test Case ID:** TC-REQ-SERVER-SHOULD-01

**Requirement ID:** REQ-SERVER-SHOULD-01 (Associate HealthcareServices with an Organization)

**Preconditions:**

* Test data containing HealthcareService and Organization resources is loaded onto the FHIR server.

**Test Steps:**

1. Retrieve a HealthcareService resource from the server.
2. Verify that the `HealthcareService.providedBy` element contains a reference to an Organization resource.

**Expected Result:** The `HealthcareService.providedBy` element should contain a valid reference to an Organization resource.

**Validation Criteria:**

* The reference should point to a resource of type `Organization`.
* The referenced Organization resource should exist on the server.

**Test Case ID:** TC-REQ-SERVER-SHOULD-02

**Requirement ID:** REQ-SERVER-SHOULD-02 (Link Practitioners and Organizations to Networks)

**Preconditions:**

* Test data containing Practitioner, Organization, Network, PractitionerRole, and OrganizationAffiliation resources is loaded onto the FHIR server.

**Test Steps:**

1. Retrieve a PractitionerRole resource from the server.
2. Verify that the `PractitionerRole.network` element contains a reference to a Network resource.
3. Retrieve an OrganizationAffiliation resource from the server.
4. Verify that the `OrganizationAffiliation.network` element contains a reference to a Network resource.

**Expected Result:** Both `PractitionerRole.network` and `OrganizationAffiliation.network` elements should contain valid references to Network resources.

**Validation Criteria:**

* The references should point to resources of type `Network`.
* The referenced Network resources should exist on the server.

**Test Case ID:** TC-REQ-SERVER-SHOULD-03

**Requirement ID:** REQ-SERVER-SHOULD-03 (Utilize PractitionerRole and OrganizationAffiliation for associations)

**Preconditions:**

* Test data containing Practitioner, Organization, HealthcareService, Network, Location, PractitionerRole, and OrganizationAffiliation resources is loaded onto the FHIR server.

**Test Steps:**

1. Retrieve a PractitionerRole resource and verify it contains references to HealthcareService, Organization, Network, and Location resources as appropriate.
2. Retrieve an OrganizationAffiliation resource and verify it contains references to HealthcareService, Organization, Network, and Location resources as appropriate.

**Expected Result:** Both PractitionerRole and OrganizationAffiliation resources should contain valid references to the appropriate resources as defined in their respective profiles within the Plan-Net Implementation Guide.

**Validation Criteria:**

* The references should point to resources of the correct type.
* The referenced resources should exist on the server.

**Group 2: XML Support**

**Test Case ID:** TC-REQ-SERVER-SHOULD-01

**Requirement ID:** REQ-SERVER-SHOULD-01 (Support XML format for interactions)

**Preconditions:**

* The FHIR server is running and configured to accept XML formatted requests.

**Test Steps:**

1. Choose an interaction defined in the Plan-Net Implementation Guide (e.g., read, search, vread).
2. Construct a valid FHIR request for the chosen interaction in XML format.
3. Send the request to the FHIR server.

**Expected Result:**

* The server should return a HTTP status code 200 (OK) indicating successful processing of the request.
* The response body should be in valid XML format.

**Validation Criteria:**

* Verify the HTTP status code of the response.
* Validate the response body against the FHIR XML schema.

**Group 3: `vread` Interaction and Resource Versioning**

This group will follow a similar structure for each resource type (Endpoint, HealthcareService, InsurancePlan, Location, Organization). Below is an example for HealthcareService:

**Test Case ID:** TC-REQ-SERVER-SHOULD-03-04

**Requirement IDs:** 
* REQ-SERVER-SHOULD-03 (Support vread interaction for HealthcareService)
* REQ-SERVER-SHOULD-04 (Return HealthcareService resource by ID and version)

**Preconditions:**

* Test data containing HealthcareService resources with different versions is loaded onto the FHIR server.

**Test Steps:**

1. Retrieve the latest version of a HealthcareService resource and note its ID and version ID.
2. Send a `vread` request to the server using the resource ID and a previous version ID.

**Expected Result:**

* The server should return a HTTP status code 200 (OK).
* The response body should contain the HealthcareService resource with the specified version ID.

**Validation Criteria:**

* Verify the HTTP status code of the response.
* Validate that the returned resource has the correct ID and version ID.

**Pseudocode for automated testing:**

```python
def test_vread_healthcare_service(client, resource_id, version_id):
  """Tests the vread interaction for HealthcareService resources.

  Args:
    client: A FHIR client instance.
    resource_id: The ID of the HealthcareService resource.
    version_id: The version ID of the HealthcareService resource.
  """
  response = client.vread('HealthcareService', resource_id, version_id)
  assert response.status_code == 200
  assert response.resource.id == resource_id
  assert response.resource.meta.versionId == version_id
```

### 5. Special Testing Considerations

**Edge Cases:**

* Test with empty or missing required elements in resources.
* Use boundary values for numeric data types.
* Include special characters and different character encodings in string values.
* Test with very large resources to assess potential performance bottlenecks.

**Performance Considerations:**

* While not the primary focus of this test plan, it's important to monitor the response times of the FHIR server during testing.
* Consider performing load testing with a large number of concurrent requests to assess the server's performance under stress.

**Security Testing Aspects:**

* Ensure the FHIR server is properly configured to authenticate and authorize access to resources.
* Test for common vulnerabilities such as SQL injection and cross-site scripting (XSS).
* Verify that sensitive data is properly protected and not exposed in responses.

This test plan provides a comprehensive framework for validating conformance to the FHIR Plan-Net Implementation Guide. By following this plan, implementers can ensure their FHIR servers correctly implement the requirements and provide interoperable solutions for exchanging healthcare information. 


## Test Plan for Server-MAY

## Test Plan: FHIR Implementation Guide - Location Resource with GeoJSON

**1. Executive Summary**

**1.1 Overview**

This test plan outlines the strategy for validating conformance to the FHIR Implementation Guide requirement related to representing regions using Location resources with GeoJSON data (REQ-SERVER-MAY-01). The plan focuses on verifying that FHIR servers can correctly handle and process Location resources containing GeoJSON data for representing regions.

**1.2 Scope**

This test plan covers the following aspects:

* **Functionality:** Verifying the server's ability to receive, process, and return Location resources with embedded GeoJSON data.
* **Data Integrity:** Ensuring the accuracy and validity of GeoJSON data within the Location resource.
* **Conformance:** Validating the implementation against the specified "MAY" conformance level, meaning the functionality is optional but should be implemented consistently if chosen.

**1.3 Key Testing Considerations**

* **Optional Feature:** As a "MAY" requirement, the test plan should include checks to determine if the server implements this functionality.
* **GeoJSON Validation:**  Tests should validate the structure and content of the GeoJSON data against the GeoJSON specification.
* **Coordinate Reference System:** Ensure the server correctly interprets and handles the Coordinate Reference System (CRS) used in the GeoJSON data.

**2. Test Environment Requirements**

**2.1 Infrastructure**

* **FHIR Server:** A FHIR server compliant with the target FHIR version.
* **Testing Tool:** A tool capable of sending FHIR requests and validating responses (e.g., Postman, Jest).
* **Test Data:** A set of valid and invalid Location resources with embedded GeoJSON data.

**2.2 FHIR Server Configuration**

* The FHIR server should be configured to accept and process Location resources.
* If the server implements the optional GeoJSON functionality, it should be enabled.

**3. Test Groupings**

**3.1 Group 1: Basic Functionality (REQ-SERVER-MAY-01)**

* **Test Approach:** This group will focus on verifying if the server supports the optional functionality of handling GeoJSON data within Location resources.
* **Key Considerations:** 
    * Tests should check for specific HTTP status codes or error messages indicating support or lack thereof.
    * If the server doesn't support the functionality, further tests in this plan might be irrelevant.

**3.2 Group 2: GeoJSON Data Handling**

* **Test Approach:** This group will test the server's ability to correctly process and return Location resources containing valid GeoJSON data.
* **Key Considerations:**
    * Tests should use various GeoJSON geometry types (Point, LineString, Polygon) to represent regions.
    * Data validation should include checking for correct GeoJSON syntax and adherence to the specification.

**3.3 Group 3: Edge Cases and Error Handling**

* **Test Approach:** This group will focus on testing the server's behavior when encountering invalid or unexpected GeoJSON data within Location resources.
* **Key Considerations:**
    * Tests should include scenarios like invalid GeoJSON syntax, unsupported geometry types, or missing CRS information.
    * The server should gracefully handle errors and return appropriate error messages.

**4. Individual Test Cases**

**4.1 REQ-SERVER-MAY-01: Support for GeoJSON in Location Resource**

* **Test Case ID:** TC-MAY-01-01
* **Preconditions:** None
* **Test Steps:**
    1. Send a GET request to the server's capability statement endpoint.
    2. Inspect the capability statement for any indication of support for GeoJSON within Location resources.
* **Expected Results:**
    * **Pass:** The capability statement explicitly mentions support for GeoJSON in Location resources or doesn't explicitly prohibit it.
    * **Fail:** The capability statement explicitly states that GeoJSON within Location resources is not supported.
* **Validation Criteria:** Examination of the capability statement response.

**4.2 REQ-SERVER-MAY-01: Process Valid GeoJSON Data**

* **Test Case ID:** TC-MAY-01-02
* **Preconditions:** TC-MAY-01-01 passed.
* **Test Steps:**
    1. Create a Location resource with valid GeoJSON data representing a region (e.g., a Polygon).
    2. Send a POST request to the server to create the resource.
    3. Retrieve the created resource using its ID.
* **Expected Results:**
    * **Pass:** The server successfully creates the Location resource and returns it with the provided GeoJSON data intact.
    * **Fail:** The server rejects the resource creation or modifies/removes the GeoJSON data.
* **Validation Criteria:** 
    * HTTP status codes (201 Created for successful creation).
    * Comparison of the returned resource with the original request payload.

**4.3 REQ-SERVER-MAY-01: Handle Invalid GeoJSON Data**

* **Test Case ID:** TC-MAY-01-03
* **Preconditions:** TC-MAY-01-01 passed.
* **Test Steps:**
    1. Create a Location resource with invalid GeoJSON data (e.g., incorrect syntax).
    2. Send a POST request to the server to create the resource.
* **Expected Results:**
    * **Pass:** The server rejects the resource creation with an appropriate error message indicating the invalid GeoJSON data.
    * **Fail:** The server accepts the resource with invalid data or throws an unexpected error.
* **Validation Criteria:**
    * HTTP status codes (e.g., 400 Bad Request).
    * Examination of the error message for specific details about the invalid GeoJSON.

**(Add more test cases for different GeoJSON geometry types, CRS variations, and other edge cases.)**

**5. Special Testing Considerations**

**5.1 Edge Cases**

* Test with extremely large and complex GeoJSON data to assess potential performance bottlenecks.
* Use various coordinate reference systems to ensure proper handling.
* Test with empty geometries or geometries with very few coordinates.

**5.2 Performance Considerations**

* Measure the response time for processing Location resources with varying sizes of GeoJSON data.
* Conduct load testing to evaluate the server's performance under high request volumes.

**5.3 Security Testing Aspects**

* If applicable, verify that access to Location resources with GeoJSON data is properly authorized and protected.
* Ensure that malicious or malformed GeoJSON data cannot be used to exploit vulnerabilities in the server. 


## Test Plan for Client (Directory Mobile Application)-SHALL NOT

## Test Plan: FHIR Implementation Guide - Directory App Privacy

**1. Executive Summary**

This test plan outlines the strategy for validating conformance to the FHIR Implementation Guide requirement **REQ-CLIENT-SHALL-NOT-01**, focusing on prohibiting directory mobile applications from sending consumer identifiable information in queries to Plan-Net services. 

**Purpose:** Ensure that directory applications adhere to privacy regulations by preventing the transmission of sensitive consumer data during service queries.

**Scope:** This plan covers testing the client-side behavior of directory mobile applications interacting with the Plan-Net FHIR server.

**Key Testing Considerations:**

* **Test Data:** Utilize realistic but de-identified consumer data for queries.
* **Network Monitoring:** Implement network monitoring tools to inspect data transmitted during queries.
* **Client-Side Manipulation:** Attempt to bypass client-side restrictions through data manipulation.

**2. Test Environment Requirements**

**Infrastructure:**

* **Test Client:** A representative directory mobile application (or simulator) capable of querying the Plan-Net FHIR server.
* **Plan-Net FHIR Server:** A test instance of the Plan-Net FHIR server configured according to the implementation guide.
* **Network Monitoring Tool:** A tool like Wireshark or Fiddler to capture and analyze network traffic.

**Tools:**

* **FHIR Client Library:**  A library compatible with the chosen test client for constructing and sending FHIR queries.
* **Test Data Generator:** A tool or script for generating realistic, de-identified consumer data.

**Test Data:**

* **De-identified Consumer Data:** A dataset containing typical consumer attributes (e.g., name, address, date of birth) with all identifiable information replaced with realistic substitutes.

**FHIR Server Configuration:**

* The Plan-Net FHIR server should be configured to log all incoming requests, including headers and payloads.

**3. Test Groupings**

**Group:** Client Query Validation

**Description:** This group focuses on verifying that the directory mobile application does not transmit consumer identifiable information within FHIR queries.

**Test Approach:**

* **Black-box testing:** Send various queries from the test client, including valid and invalid requests, while monitoring network traffic for any transmission of identifiable information.
* **Client-side manipulation:** Attempt to modify the client application or its data to bypass restrictions and send identifiable information.

**Key Considerations:**

* Test a variety of query types and parameters to ensure comprehensive coverage.
* Focus on data fields that are most likely to contain identifiable information.

**4. Individual Test Cases**

**Test Case ID:** TC-REQ-CLIENT-SHALL-NOT-01-01

**Requirement:** REQ-CLIENT-SHALL-NOT-01

**Preconditions:**

* The test client is configured with de-identified consumer data.
* The network monitoring tool is running and capturing traffic between the client and server.

**Test Steps:**

1. Using the test client, initiate a query to the Plan-Net FHIR server.
2. The query should request resources related to plan information but should not include any consumer identifiable information in the query parameters or body.
3. Capture the network traffic generated by the query.

**Expected Results:**

* The network traffic should not contain any consumer identifiable information in the request headers, query parameters, or request body.

**Validation Criteria:**

* Analyze the captured network traffic using the network monitoring tool to confirm the absence of identifiable information.

**Test Case ID:** TC-REQ-CLIENT-SHALL-NOT-01-02

**Requirement:** REQ-CLIENT-SHALL-NOT-01

**Preconditions:**

* The test client is configured with de-identified consumer data.
* Attempt to modify the client application or its data to include identifiable information in the query.

**Test Steps:**

1. Modify the client application or its data to include consumer identifiable information (e.g., real name, address) in the query parameters or body.
2. Initiate the modified query to the Plan-Net FHIR server.

**Expected Results:**

* The client application should prevent the transmission of the modified query containing identifiable information. 
* Alternatively, the client application might sanitize the query before transmission, removing or replacing identifiable information.

**Validation Criteria:**

* Observe the client application's behavior during the query execution.
* Analyze the captured network traffic to confirm the absence of identifiable information or the presence of sanitized data.

**Automatically Testable Requirements:**

This requirement is suitable for automated testing. Pseudocode for a potential test:

```python
import requests

# Define test data with de-identified consumer information
test_data = {
    "fake_name": "John Doe",
    "fake_address": "123 Main St",
    # ... other de-identified data
}

# Construct FHIR query URL
fhir_server_url = "https://example.com/fhir/Plan"
query_parameters = {"parameter": test_data} 
response = requests.get(fhir_server_url, params=query_parameters)

# Assert that the response does not contain identifiable information
assert "John Doe" not in response.text
assert "123 Main St" not in response.text
# ... other assertions for identifiable information
```

**5. Special Testing Considerations**

**Edge Cases:**

* Test with various data types and formats within the query to ensure robust handling of unexpected input.
* Explore scenarios where identifiable information might be indirectly embedded within the query.

**Performance Considerations:**

* While not the primary focus, assess the performance impact of any client-side data sanitization or validation processes.

**Security Testing Aspects:**

* Conduct penetration testing on the client application to identify vulnerabilities that could expose consumer identifiable information.
* Review the client application's code for potential security flaws related to data handling and transmission. 


## Test Plan for Server (Health Plan API)-SHALL

## Test Plan: FHIR Implementation Guide Conformance

**Version:** 1.0
**Date:** 2023-10-27

**1. Executive Summary**

**1.1 Overview**

This document outlines the test plan for validating conformance to the FHIR Implementation Guide (IG) for Health Plan APIs. The primary objective is to ensure that server implementations adhere to the mandatory requirements outlined in the IG, specifically focusing on the handling of "Must Support" data elements.

**1.2 Scope**

This test plan covers the following aspects:

* Validation of "Must Support" data element population in query responses (REQ-SERVER-SHALL-01).
* Verification of appropriate reason codes for missing "Must Support" data elements with minimum cardinality greater than 0 (REQ-SERVER-SHALL-04).

**1.3 Key Testing Considerations**

* **Automated Testing:**  The plan emphasizes automated testing where feasible, utilizing tools capable of FHIR resource validation and interaction testing.
* **Data Variation:** Test cases will employ diverse datasets to cover various scenarios and edge cases related to data presence and absence.
* **Negative Testing:** The plan includes negative test cases to ensure graceful handling of invalid or unexpected requests.

**2. Test Environment Requirements**

**2.1 Infrastructure**

* **FHIR Server:** A FHIR server compliant with the target FHIR version specified in the IG.
* **Testing Tool:** A FHIR-compatible testing tool capable of:
    * Sending various HTTP requests (GET, POST, etc.)
    * Validating FHIR resources against profiles defined in the IG
    * Supporting assertions for response validation
* **Test Data Management System:** A system or mechanism to manage and provide test data, including synthetic data generation capabilities.

**2.2 FHIR Server Configuration**

* The FHIR server under test must be configured to expose the resources and operations defined in the IG.
* The server should be populated with test data representing various scenarios outlined in the test cases.

**3. Test Groupings**

**3.1 Group 1: Must Support Data Element Population (REQ-SERVER-SHALL-01)**

**Test Approach:** This group focuses on verifying that all "Must Support" data elements are populated in query responses when data is available.

**Key Considerations:**

* Identify all resources and search operations within the IG scope.
* Determine the "Must Support" data elements for each resource.
* Construct test queries that should return resources containing these elements.

**3.2 Group 2: Handling Missing Must Support Data Elements (REQ-SERVER-SHALL-04)**

**Test Approach:** This group validates the server's behavior when "Must Support" data elements with minimum cardinality greater than 0 are not present.

**Key Considerations:**

* Identify "Must Support" elements with minimum cardinality greater than 0.
* Design test scenarios where these elements are intentionally omitted from the data.
* Verify the server returns appropriate reason codes (nullFlavors, dataAbsentReason extension) for the missing data.

**4. Individual Test Cases**

**4.1 Test Case ID: TC-REQ-SERVER-SHALL-01-01**

**Requirement:** REQ-SERVER-SHALL-01

**Preconditions:**

* The FHIR server is running and accessible.
* Test data containing populated "Must Support" elements is loaded.

**Test Steps:**

1. **Send a search request** to the server for a resource within the IG's scope.
2. **Receive the response** from the server.

**Expected Results:**

* **Response Status Code:** 200 (OK)
* **Response Body:** The response body should contain the requested resources.
* **Data Validation:** All "Must Support" data elements for the returned resource(s) should be populated with valid values.

**Validation Criteria:**

* Verify the response status code.
* Validate the presence and value of all "Must Support" data elements in the returned resource(s) against the IG's profile definitions.

**Automated Test Logic (example using pseudocode):**

```
// Assuming 'response' contains the FHIR response object
// and 'resourceType' is the type of resource being tested

function validateMustSupportElements(response, resourceType) {
  // Retrieve the profile for the resource type from the IG
  profile = getProfile(resourceType); 

  // Iterate through each resource in the response bundle
  foreach (resource in response.entry) {
    // Validate the resource against the profile
    validationResult = validateResource(resource, profile); 

    // Assert that there are no errors related to missing "Must Support" elements
    assert(validationResult.errors.length == 0, "Missing Must Support elements detected."); 
  }
}
```

**4.2 Test Case ID: TC-REQ-SERVER-SHALL-04-01**

**Requirement:** REQ-SERVER-SHALL-04

**Preconditions:**

* The FHIR server is running and accessible.
* Test data containing resources with intentionally missing "Must Support" elements (minimum cardinality > 0) is loaded.

**Test Steps:**

1. **Send a search request** to retrieve a resource containing the "Must Support" element with missing data.
2. **Receive the response** from the server.

**Expected Results:**

* **Response Status Code:** 200 (OK)
* **Response Body:** The response body should contain the requested resource.
* **Missing Data Handling:** The "Must Support" element with missing data should either:
    * Contain a valid nullFlavor code from the corresponding value set (if applicable).
    * Utilize the `dataAbsentReason` extension with a valid code.

**Validation Criteria:**

* Verify the response status code.
* Check for the presence of either a valid nullFlavor code or the `dataAbsentReason` extension with a valid code for the missing "Must Support" element.

**Automated Test Logic (example using pseudocode):**

```
// Assuming 'resource' is the FHIR resource object being tested
// and 'elementPath' is the path to the "Must Support" element

function validateMissingDataReason(resource, elementPath) {
  // Check if the element is present in the resource
  if (resource.hasElement(elementPath)) {
    element = resource.getElement(elementPath);

    // Check for nullFlavor code
    if (element.hasValueCodeableConcept() && element.valueCodeableConcept.hasCoding()) {
      // Validate the nullFlavor code against the appropriate value set
      assert(isValidNullFlavor(element.valueCodeableConcept.coding.first().code), "Invalid nullFlavor code.");
    } 
    // Check for dataAbsentReason extension
    else if (element.hasExtension("http://hl7.org/fhir/StructureDefinition/data-absent-reason")) {
      // Validate the dataAbsentReason code
      assert(isValidDataAbsentReason(element.extension.first().valueCodeableConcept.coding.first().code), "Invalid dataAbsentReason code.");
    } 
    else {
      // Neither nullFlavor nor dataAbsentReason is present
      assert(false, "Missing reason for absent data."); 
    }
  } else {
    // The element itself is missing, which might be valid depending on cardinality
    // Add logic to handle this scenario based on the specific element and IG requirements
  }
}
```

**5. Special Testing Considerations**

**5.1 Edge Cases**

* **Minimum Cardinality 0:** Test scenarios where "Must Support" elements with minimum cardinality 0 are both present and absent, ensuring the server handles both cases correctly.
* **Partial Data:** Test cases where some "Must Support" elements within a resource are populated while others are missing, verifying proper reason codes for each missing element.

**5.2 Performance Considerations**

* **Response Times:** Measure and assess response times for various queries, especially those retrieving large datasets or involving complex filtering.
* **Resource Optimization:** Evaluate if the server implements appropriate techniques for resource optimization (e.g., paging, _summary parameters) to ensure efficient data retrieval.

**5.3 Security Testing Aspects**

* **Authentication and Authorization:** Verify that the FHIR server enforces appropriate authentication and authorization mechanisms to protect sensitive patient data.
* **Data Integrity:** Conduct tests to ensure the server protects against data tampering and maintains data integrity throughout interactions.
* **Vulnerability Scanning:** Utilize automated security scanning tools to identify potential vulnerabilities in the FHIR server implementation. 


## Test Plan for Server (Health Plan API)-SHALL NOT

## Test Plan: FHIR Implementation Guide Conformance

**1. Executive Summary**

**1.1. Purpose**

This test plan outlines the strategy for validating conformance to the FHIR Implementation Guide, specifically focusing on requirement REQ-SERVER-SHALL-NOT-03 regarding the exclusion of data elements with minimum cardinality 0 when information is not present. 

**1.2. Scope**

The scope of this test plan encompasses the functionality of the Health Plan API server as it pertains to handling data elements with minimum cardinality 0. It includes testing various scenarios where such data elements may be present or absent in the underlying data and verifying the server's response conforms to the specified requirement.

**1.3. Key Testing Considerations**

* **Data Variety:** Tests will utilize diverse datasets with varying combinations of present and absent data elements to ensure comprehensive coverage.
* **Resource Types:** Testing will cover all relevant FHIR resource types where the requirement applies.
* **Automation:**  Where feasible, automated tests will be developed to improve efficiency and repeatability.
* **Negative Testing:**  The test plan emphasizes negative testing scenarios to validate the system's behavior when handling missing or incomplete data.

**2. Test Environment Requirements**

**2.1. Infrastructure**

* **FHIR Server:** A deployed instance of the Health Plan API server adhering to the FHIR specification.
* **Testing Tool:** A suitable testing tool capable of sending FHIR requests and analyzing responses (e.g., Postman, Jest).
* **Test Data Management:** A mechanism for loading and managing test data within the FHIR server.

**2.2. Tools**

* **FHIR Client:** A tool for constructing and sending FHIR requests (can be integrated with the testing tool).
* **JSON Validator:** A tool for validating the structure and content of FHIR resources returned by the server.

**2.3. Test Data**

* **Synthetic Data:** A set of synthetic FHIR resources representing various clinical scenarios, including instances with missing data elements.
* **Reference Data:**  A set of reference FHIR resources with known data element configurations for comparison.

**2.4. FHIR Server Configuration**

* The FHIR server should be configured to accurately reflect the production environment, including any relevant data access controls and security settings.

**3. Test Groupings**

**3.1. Data Element Exclusion**

This group focuses on verifying the server's adherence to REQ-SERVER-SHALL-NOT-03.

**Test Approach:**

* Execute a series of FHIR read operations targeting resources with known data element configurations.
* Include scenarios where target resources have data elements with minimum cardinality 0 present and absent.
* Analyze the returned resources to confirm the exclusion of data elements with minimum cardinality 0 when information is not present.

**Key Considerations:**

* Test various FHIR resource types where the requirement applies.
* Utilize diverse datasets with varying combinations of present and absent data elements.

**4. Individual Test Cases**

**4.1. REQ-SERVER-SHALL-NOT-03 - Data Element Exclusion**

**Test Case ID:** TC-SERVER-03-01

**Preconditions:**

* The FHIR server is running and accessible.
* Test data containing a Patient resource with a missing "telecom" element (minimum cardinality 0) is loaded.

**Test Steps:**

1. Send a FHIR read request for the Patient resource with the missing "telecom" element.
2. Analyze the returned Patient resource.

**Expected Results:**

* The response status code is 200 (OK).
* The returned Patient resource does not contain the "telecom" element.

**Validation Criteria:**

* Verify the absence of the "telecom" element in the returned JSON response using a JSON validator.

**Automated Test Logic (Pseudocode):**

```
// Send FHIR read request for the Patient resource
response = fhirClient.read('Patient', patientId);

// Assert response status code is 200
assert.equal(response.status, 200);

// Assert "telecom" element is not present in the response body
assert.isUndefined(response.data.telecom); 
```

**5. Special Testing Considerations**

**5.1. Edge Cases**

* Test scenarios with deeply nested data elements having minimum cardinality 0.
* Verify the behavior with different data types for the data element with minimum cardinality 0.

**5.2. Performance Considerations**

* While not the primary focus of this test plan, performance testing can be incorporated to assess the impact of excluding data elements on response times.

**5.3. Security Testing**

* Ensure that excluding data elements does not inadvertently expose sensitive information.
* Verify that access controls are enforced consistently, even when data elements are excluded. 


## Test Plan for Client (Application)-SHALL

## Test Plan: FHIR Implementation Guide Conformance

**1. Executive Summary**

**1.1. Purpose and Scope:**

This test plan outlines the strategy and procedures for validating the conformance of client applications to the FHIR Implementation Guide, specifically focusing on requirements related to handling "Must Support" data elements (REQ-CLIENT-SHALL-02 and REQ-CLIENT-SHALL-03). 

**1.2. Key Testing Considerations:**

* **Focus:** This test plan emphasizes the client application's ability to process and interpret "Must Support" data elements as defined by the Implementation Guide.
* **Methodology:** A combination of automated and manual testing will be employed to ensure comprehensive coverage.
* **Test Data:** Realistic and representative test data will be used, including both valid and invalid instances of resources containing "Must Support" elements.
* **Environment:** Testing will be conducted in a dedicated test environment mirroring the production environment as closely as possible.

**2. Test Environment Requirements**

**2.1. Infrastructure:**

* **Test FHIR Server:** A FHIR server compliant with the target FHIR version and configured according to the Implementation Guide.
* **Client Test Harness:** A testing framework or tool capable of sending FHIR requests and receiving responses. This could be a dedicated FHIR testing tool or a custom-built script.
* **Test Data Management:** A system for generating, storing, and managing test data, including synthetic patient data and resources with "Must Support" elements.

**2.2. Tools:**

* **FHIR Client Library:** A client library compatible with the chosen programming language for interacting with the FHIR server.
* **Test Data Generator:** A tool for generating synthetic FHIR resources conforming to the Implementation Guide's profiles.
* **Assertion Library:** A library for validating FHIR responses and resource content.

**2.3. Test Data:**

* **Valid Resources:**  A set of FHIR resources containing all required and "Must Support" data elements populated with valid values, conforming to the Implementation Guide's profiles.
* **Resources with Missing "Must Support" Elements:** A set of FHIR resources where some or all "Must Support" elements are intentionally omitted.
* **Invalid Resources:** A set of FHIR resources containing invalid data types or values for "Must Support" elements.

**2.4. FHIR Server Configuration:**

* The FHIR server must be configured to support the resources and profiles defined in the Implementation Guide.
* The server should be populated with test data representing various scenarios.
* Logging should be enabled to facilitate debugging and analysis.

**3. Test Groupings**

**3.1. Group 1: Processing "Must Support" Data Elements (REQ-CLIENT-SHALL-02)**

**Test Approach:** This group focuses on verifying that the client application can successfully process resources containing "Must Support" data elements without errors.

* **Test Cases:** Will involve sending valid FHIR resources containing "Must Support" elements to the client application and verifying successful processing.
* **Key Considerations:**
    * Different HTTP methods (e.g., READ, CREATE, UPDATE) should be tested.
    * Various combinations of "Must Support" elements within resources should be included.

**3.2. Group 2: Interpreting Missing "Must Support" Elements (REQ-CLIENT-SHALL-03)**

**Test Approach:** This group verifies that the client correctly interprets missing "Must Support" elements as data not present in the system.

* **Test Cases:** Will involve querying for resources and verifying the client's behavior when "Must Support" elements are absent in the response.
* **Key Considerations:**
    * The client should not throw errors or halt processing.
    * The client should ideally provide a mechanism to identify missing "Must Support" elements (e.g., specific flags or data structures).

**4. Individual Test Cases**

**4.1. REQ-CLIENT-SHALL-02: Process resource instances containing Must Support data elements without errors**

**4.1.1. Test Case ID:** TC-REQ-CLIENT-SHALL-02-01

**Preconditions:**

* The client application is running and connected to the test FHIR server.
* A valid FHIR resource containing "Must Support" elements is available.

**Test Steps:**

1. **Send:** Send a CREATE request to the client application with the valid FHIR resource containing "Must Support" elements.
2. **Receive:** Receive the response from the client application.

**Expected Results:**

* The client application should return a successful HTTP status code (e.g., 201 Created).
* The response should not contain any error messages related to the "Must Support" elements.

**Validation Criteria:**

* Verify the HTTP status code of the response.
* Analyze the response body for any error messages related to "Must Support" elements.

**4.1.2. Test Case ID:** TC-REQ-CLIENT-SHALL-02-02 (Automated)

**(Similar test cases should be created for different HTTP methods and resource types)**

**Pseudocode:**

```python
# Assuming a hypothetical FHIR client library
client = FhirClient(base_url="http://test-fhir-server")

# Load a valid resource with "Must Support" elements
resource = load_fhir_resource("valid_resource.json")

# Send a CREATE request
response = client.create(resource)

# Assert successful creation
assert response.status_code == 201
assert "error" not in response.json()
```

**4.2. REQ-CLIENT-SHALL-03: Interpret missing Must Support data elements as not present in the Health Plan API system**

**4.2.1. Test Case ID:** TC-REQ-CLIENT-SHALL-03-01

**Preconditions:**

* The client application is running and connected to the test FHIR server.
* A FHIR resource is available on the server with one or more "Must Support" elements intentionally omitted.

**Test Steps:**

1. **Query:** Send a READ request to the client application to retrieve the FHIR resource with missing "Must Support" elements.
2. **Receive:** Receive the response from the client application.

**Expected Results:**

* The client application should return a successful HTTP status code (e.g., 200 OK).
* The response should not contain any error messages related to the missing "Must Support" elements.
* The client application should provide a mechanism to identify the missing elements (e.g., specific flags, null values, or dedicated data structures).

**Validation Criteria:**

* Verify the HTTP status code of the response.
* Analyze the response body for any error messages related to "Must Support" elements.
* Inspect the returned resource representation to confirm the client's handling of missing elements.

**5. Special Testing Considerations**

**5.1. Edge Cases:**

* Test with resources containing a large number of "Must Support" elements.
* Test with resources containing nested data structures within "Must Support" elements.
* Test with different data types for "Must Support" elements (e.g., CodeableConcept, Period, Reference).

**5.2. Performance Considerations:**

* Measure the client's response time when processing resources with varying numbers of "Must Support" elements.
* Evaluate the impact of missing "Must Support" elements on the client's performance.

**5.3. Security Testing Aspects:**

* Ensure that the client application handles sensitive data within "Must Support" elements securely.
* Verify that the client application does not expose any sensitive information in error messages or logs related to "Must Support" elements. 


## Test Plan for Client (Application)-SHOULD

## Test Plan: FHIR Implementation Guide Conformance

**Document Version:** 1.0
**Date:** 2023-10-27

## 1. Executive Summary

This document outlines the test plan for validating conformance to the FHIR Implementation Guide, specifically focusing on requirement **REQ-CLIENT-SHOULD-01**. The primary objective is to ensure that client applications interacting with FHIR servers adhering to this guide can effectively handle Must Support data elements.

**Scope:**

This test plan focuses on the functional requirement of displaying or storing Must Support data elements by client applications. It does not cover non-functional requirements like performance, security, or usability.

**Key Testing Considerations:**

* **Variety of Client Applications:** Testing should encompass different types of client applications (e.g., web-based, mobile) to ensure broad compliance.
* **Data Element Coverage:**  A representative set of Must Support data elements from different resource types should be included in the testing.
* **Display and Storage Mechanisms:**  Verification should consider various methods of displaying (e.g., UI rendering) and storing (e.g., databases, file systems) data.

## 2. Test Environment Requirements

**Infrastructure:**

* **FHIR Server:** A FHIR server compliant with the target FHIR version and the implementation guide being tested.
* **Client Applications:**  A selection of client applications representing different types and functionalities.
* **Test Data:**  A set of FHIR resources containing Must Support data elements.

**Tools:**

* **FHIR Client:** A tool for interacting with the FHIR server (e.g., Postman, Insomnia).
* **Test Management Tool:**  For managing test cases, execution, and results (optional).

**FHIR Server Configuration:**

* The FHIR server should be configured to expose the required FHIR resources and profiles defined in the implementation guide.
* Authentication and authorization mechanisms should be configured as needed.

## 3. Test Groupings

**Group 1: Client Display of Must Support Data Elements**

* **Test Approach:**  Simulate user interactions with client applications to retrieve and display FHIR resources containing Must Support data elements.
* **Key Considerations:**
    * Verify correct rendering of data elements in the user interface.
    * Ensure clarity and understandability of displayed information.

**Group 2: Client Storage of Must Support Data Elements**

* **Test Approach:**  Trigger client application functionalities that involve storing retrieved FHIR resources or specific data elements.
* **Key Considerations:**
    * Validate the persistence of Must Support data elements in the chosen storage mechanism.
    * Ensure data integrity and consistency during storage.

## 4. Individual Test Cases

**Test Case ID:** TC-REQ-CLIENT-SHOULD-01-01

**Requirement:** REQ-CLIENT-SHOULD-01

**Group:** Client Display of Must Support Data Elements

**Preconditions:**

* The FHIR server is running and accessible.
* The client application is configured to connect to the FHIR server.
* Test data containing Must Support elements is loaded on the FHIR server.

**Test Steps:**

1. Using the client application, initiate a request to retrieve a FHIR resource containing Must Support data elements.
2. Observe the client application's user interface.

**Expected Results:**

* The client application displays the requested FHIR resource.
* All Must Support data elements within the resource are rendered clearly and accurately in the user interface.

**Validation Criteria:**

* Visual inspection of the client application's user interface.

**Test Case ID:** TC-REQ-CLIENT-SHOULD-01-02

**Requirement:** REQ-CLIENT-SHOULD-01

**Group:** Client Storage of Must Support Data Elements

**Preconditions:**

* The FHIR server is running and accessible.
* The client application is configured to connect to the FHIR server and store data.
* Test data containing Must Support elements is loaded on the FHIR server.

**Test Steps:**

1. Trigger the client application's functionality to retrieve and store a FHIR resource containing Must Support data elements.
2. Access the client application's storage mechanism (database, file system, etc.).

**Expected Results:**

* The retrieved FHIR resource is successfully stored in the client application's designated storage.
* All Must Support data elements within the resource are present and accurately stored.

**Validation Criteria:**

* Inspection of the data stored by the client application in its storage mechanism.

## 5. Special Testing Considerations

**Edge Cases:**

* Test with empty or missing Must Support data elements to ensure graceful handling by client applications.
* Use data exceeding typical length limitations to test for truncation or error handling.

**Performance Considerations:**

* While not the primary focus, observe the time taken to display and store data to identify potential performance bottlenecks.

**Security Testing Aspects:**

* While outside the scope of this test plan, ensure that sensitive data within Must Support elements is handled securely during display and storage. This includes aspects like encryption, access control, and data masking. 


## Test Plan for Client (Consumer App)-SHALL

## Test Plan: FHIR Implementation Guide Conformance

**1. Executive Summary**

**1.1. Purpose**

This test plan outlines the strategy for validating conformance to the FHIR Implementation Guide (FHIR IG), specifically focusing on requirement REQ-CLIENT-SHALL-04 related to client application handling of Must Support data elements asserting missing information. 

**1.2. Scope**

This test plan covers the functional testing of client applications (Consumer Apps) interacting with a FHIR server implementing the specified FHIR IG. The primary focus is on verifying the client's ability to process resource instances containing Must Support data elements that indicate missing information without encountering errors or unexpected behavior.

**1.3. Key Testing Considerations**

* **Test Data:** Realistic FHIR resources with Must Support elements representing various data types and missing information scenarios.
* **Client Applications:** Testing with different client applications (e.g., web-based, mobile) to ensure broad compatibility.
* **FHIR Server Configuration:** The FHIR server should be configured to strictly enforce Must Support requirements as defined in the FHIR IG.

**2. Test Environment Requirements**

**2.1. Infrastructure**

* **FHIR Server:** A FHIR-compliant server supporting the required FHIR version and profiles defined in the FHIR IG.
* **Client Application:** One or more client applications under test, representing typical Consumer App actors.
* **Testing Tools:**
    * **FHIR Client:** A tool for constructing and sending FHIR requests (e.g., Postman, Insomnia).
    * **Test Data Generator:** A tool for generating realistic FHIR resources conforming to the FHIR IG (e.g., Synthea).
    * **Logging and Monitoring Tools:** To capture and analyze client application behavior during testing.

**2.2. Test Data**

* **Realistic FHIR Resources:** Generate test data representing various resource types relevant to the FHIR IG.
* **Must Support Variations:** Include resources with Must Support elements representing different data types (e.g., string, code, reference) and missing information scenarios (e.g., null values, empty strings).

**2.3. FHIR Server Configuration**

* **Must Support Enforcement:** Configure the FHIR server to strictly enforce Must Support requirements as defined in the FHIR IG. This may involve rejecting requests with missing Must Support data elements or returning appropriate error codes.

**3. Test Groupings**

**3.1. Client Handling of Must Support Data Elements**

* **Test Approach:** This group focuses on verifying client application behavior when encountering Must Support data elements asserting missing information.
* **Key Considerations:**
    * Test with various resource types and Must Support element variations.
    * Observe client application behavior for error handling, data display, and user interaction.

**4. Individual Test Cases**

**4.1. REQ-CLIENT-SHALL-04: Process Resource Instances with Missing Must Support Data**

* **Test Case ID:** TC-CLIENT-SHALL-04-01
* **Preconditions:**
    * The FHIR server is running and configured according to the FHIR IG.
    * The client application is connected to the FHIR server.
* **Test Steps:**
    1. **Prepare Test Data:** Create a FHIR resource instance containing a Must Support data element with a value asserting missing information (e.g., null, empty string).
    2. **Send Request:** Using the client application or a FHIR client tool, send a request to the FHIR server to retrieve the prepared resource instance.
    3. **Observe Client Behavior:** Monitor the client application for any errors, warnings, or unexpected behavior.
* **Expected Results:**
    * The client application **SHALL** successfully process the resource instance without throwing errors or displaying misleading information.
    * The client application **MAY** choose to display a visual indicator or message to the user indicating that the specific data element is missing, but this is not mandatory for passing this test case.
* **Validation Criteria:**
    * No error messages related to the Must Support element are displayed to the user.
    * The client application continues to function as expected, allowing further interaction with the FHIR server.

**4.2. Additional Test Cases:**

* Create additional test cases (TC-CLIENT-SHALL-04-02, TC-CLIENT-SHALL-04-03, etc.) to cover various resource types, Must Support data types, and missing information scenarios.

**5. Special Testing Considerations**

**5.1. Edge Cases**

* **Unexpected Data Types:** Test with Must Support elements containing unexpected or invalid data types to ensure graceful handling by the client application.
* **Resource Cardinality:** Test with resources containing multiple instances of the same Must Support element, some with missing information and others with valid data.

**5.2. Performance Considerations**

* **Large Resources:** Test with large FHIR resources containing numerous Must Support elements to assess the client application's performance in handling such data.

**5.3. Security Testing**

* **Data Exposure:** Verify that the client application does not inadvertently expose sensitive information contained within Must Support elements, even when the information is marked as missing.
* **Input Validation:** Test for potential vulnerabilities related to Must Support elements, such as injection attacks, by providing malicious or specially crafted data as input.

This test plan provides a comprehensive framework for validating client application conformance to the FHIR IG requirement related to Must Support data elements. By executing these tests and analyzing the results, you can ensure that your client applications can effectively handle missing information scenarios in a robust and user-friendly manner. 


## Test Plan for Client-SHOULD

## FHIR Implementation Guide Test Plan

**1. Executive Summary**

**1.1. Overview**

This test plan outlines the strategy for validating conformance to the FHIR Implementation Guide, specifically focusing on requirements related to client handling of directory content updates (REQ-CLIENT-SHOULD-02 and REQ-CLIENT-SHOULD-03). The plan emphasizes a combination of automated and manual testing approaches to ensure comprehensive coverage.

**1.2. Key Testing Considerations**

* **Client-side focus:** The tests primarily target client applications interacting with the FHIR server.
* **Caching mechanisms:**  The tests assume clients implement some form of caching for directory content.
* **SHOULD conformance:**  The requirements specify "SHOULD" conformance, implying flexibility in implementation. The test plan acknowledges this by providing guidance rather than strict pass/fail criteria in certain cases.

**2. Test Environment Requirements**

**2.1. Infrastructure**

* **FHIR Server:** A FHIR-compliant server conforming to the target implementation guide.
* **Test Client:** A configurable client application capable of making FHIR API requests and simulating caching behavior.
* **Test Data:** A populated FHIR repository with sample directory resources.

**2.2. Tools**

* **FHIR Client Library:**  A suitable library for the chosen programming language to interact with the FHIR server.
* **Testing Framework:** A framework like JUnit, pytest, or similar for structuring and executing automated tests.
* **HTTP Proxy (Optional):** For inspecting and manipulating requests/responses during testing.

**2.3. FHIR Server Configuration**

* The FHIR server should be configured to support the _lastUpdated search parameter for relevant resources.

**3. Test Groupings**

**3.1. Group 1: Directory Content Update Detection**

* **Requirements:** REQ-CLIENT-SHOULD-02
* **Test Approach:**
    * Simulate client caching of directory content.
    * Modify directory resources on the server.
    * Verify the client utilizes the _lastUpdated parameter to detect and retrieve updated content.

**3.2. Group 2: Cached Data Validation**

* **Requirements:** REQ-CLIENT-SHOULD-03
* **Test Approach:**
    * Simulate client caching of directory content.
    * Delete specific resources on the server.
    * Verify the client periodically queries for cached data using _id and handles potential deletions appropriately.

**4. Individual Test Cases**

**4.1. REQ-CLIENT-SHOULD-02: Utilize lastUpdate timestamp for tracking directory content updates**

**4.1.1. Test Case ID:** TC-02-01

**4.1.2. Preconditions:**

* The client has cached a set of directory resources.

**4.1.3. Test Steps:**

1. **Modify:** Update an existing directory resource on the server.
2. **Query:**  Have the client query for updated content using a filter on the _lastUpdated parameter with a timestamp after the modification.
3. **Validate:** Verify the client receives the updated resource.

**4.1.4. Validation Criteria:**

* The client's query response includes the modified resource.
* The client does not retrieve unmodified resources.

**4.1.5. Test Logic Outline (Pseudocode):**

```
// Client-side logic
function getUpdatedResources(cacheTimestamp) {
  return fhirClient.search({
    resourceType: 'ResourceType',
    searchParams: {
      _lastUpdated: `gt${cacheTimestamp}` 
    }
  });
}
```

**4.2. REQ-CLIENT-SHOULD-03: Periodically verify cached data existence using _id queries**

**4.2.1. Test Case ID:** TC-03-01

**4.2.2. Preconditions:**

* The client has cached a set of directory resources.

**4.2.3. Test Steps:**

1. **Delete:** Delete a cached resource on the server.
2. **Query:** Trigger the client's periodic validation mechanism, which should query for cached resources using their _id.
3. **Validate:** Verify the client detects the deleted resource and handles it appropriately (e.g., removes it from the cache).

**4.2.4. Validation Criteria:**

* The client identifies the deleted resource.
* The client takes appropriate action based on the deletion (e.g., cache invalidation, user notification).

**4.2.5. Test Logic Outline (Pseudocode):**

```
// Client-side logic
function validateCachedData() {
  cachedResources.forEach(resource => {
    fhirClient.read('ResourceType', resource.id)
      .then(response => { 
        // Handle successful retrieval
      })
      .catch(error => {
        if (error.statusCode === 404) {
          // Handle resource deletion
        }
      });
  });
}
```

**5. Special Testing Considerations**

**5.1. Edge Cases**

* **Concurrent Updates:** Test scenarios with multiple simultaneous updates to directory content.
* **Large Datasets:** Evaluate client performance with a high volume of cached resources.
* **Network Interruptions:** Simulate network outages during client validation processes.

**5.2. Performance Considerations**

* **Caching Efficiency:**  Assess the impact of caching on client response times.
* **Query Optimization:** Analyze the efficiency of client queries using the _lastUpdated parameter.

**5.3. Security Testing Aspects**

* **Authorization:** Verify that clients can only access authorized directory content, even when using caching.
* **Data Integrity:** Ensure cached data remains consistent and tamper-proof. 


## Test Plan for Unknown-Unknown

## Test Plan for FHIR Implementation Guide: Organization Resource

**1. Executive Summary**

**1.1. Purpose and Scope**

This test plan outlines the strategy for validating conformance to the FHIR Implementation Guide requirements related to the Organization resource, specifically focusing on the supported _revincludes as defined in requirement REQ-SERVER-SHALL-11. 

**1.2. Key Testing Considerations**

* **Automated Testing:**  The majority of tests outlined in this plan are designed for automated execution using a FHIR testing tool.
* **Test Data:**  Testing will require a populated FHIR server with representative Organization resources and related resources linked via the specified _revincludes.
* **Conformance Tooling:**  Consider leveraging FHIR conformance testing tools like Touchstone or Inferno to supplement manual and automated testing efforts.

**2. Test Environment Requirements**

**2.1. Infrastructure and Tools**

* **FHIR Server:** A FHIR server compliant with the target FHIR version and supporting the required profiles and extensions.
* **Testing Tool:** A FHIR testing tool capable of executing automated tests, e.g., Jest, Mocha, Chai with a FHIR client library.
* **Test Data Generator:** A tool or script for generating synthetic FHIR resources conforming to the implementation guide.

**2.2. FHIR Server Configuration**

* The FHIR server must be configured to enable the _include and _revinclude search parameters.
* Ensure the server enforces any specific security requirements related to accessing Organization resources and linked data.

**3. Test Groupings**

**3.1. Group: Organization _revincludes**

**3.1.1. Test Approach:** This group focuses on validating the server's ability to correctly process and return resources linked to an Organization resource via the specified _revincludes. Tests will involve sending search requests with the defined _revincludes and verifying the response content and structure.

**3.1.2. Key Considerations:**

* **Resource Referencing:** Ensure test data includes valid references between Organization resources and the related resources for each _revincludes.
* **Response Structure:** Validate that the returned Bundle conforms to the FHIR specification for search results with _revincludes.

**4. Individual Test Cases**

**4.1. Test Case ID: TEST-REQ-SERVER-SHALL-11-ENDPOINT**

* **Requirement:** REQ-SERVER-SHALL-11 (_revincludes: Endpoint:organization)
* **Preconditions:**
    * The FHIR server is running and accessible.
    * Test data includes at least one Organization resource with a linked Endpoint resource.
* **Test Steps:**
    1. Send a GET request to the server: `GET [base]/Organization?[parameter=value]&_revinclude=Endpoint:organization`
    2. Replace `[parameter=value]` with a valid search parameter and value to identify the target Organization resource.
* **Expected Results:**
    * The server responds with HTTP status code 200 (OK).
    * The response body is a valid FHIR Bundle containing:
        * The requested Organization resource.
        * The linked Endpoint resource in the `entry` array.
* **Validation Criteria:**
    * Verify the HTTP status code.
    * Validate the response Bundle structure and content against the FHIR specification.
    * Assert that the included Endpoint resource has the correct reference to the Organization resource.

**4.2. Test Case ID: TEST-REQ-SERVER-SHALL-11-HEALTHCARESERVICE**

* **Requirement:** REQ-SERVER-SHALL-11 (_revincludes: HealthcareService:organization)
* **Preconditions, Test Steps, Expected Results, Validation Criteria:**  Follow the same structure as Test Case 4.1, replacing `Endpoint:organization` with `HealthcareService:organization` in the request URL and adjusting the expected linked resource type accordingly.

**4.3. Test Case ID: TEST-REQ-SERVER-SHALL-11-INSURANCEPLAN-ADMINISTERED-BY**

* **Requirement:** REQ-SERVER-SHALL-11 (_revincludes: InsurancePlan:administered-by)
* **Preconditions, Test Steps, Expected Results, Validation Criteria:**  Follow the same structure as Test Case 4.1, replacing `Endpoint:organization` with `InsurancePlan:administered-by` in the request URL and adjusting the expected linked resource type accordingly.

**4.4. Test Case ID: TEST-REQ-SERVER-SHALL-11-INSURANCEPLAN-OWNED-BY**

* **Requirement:** REQ-SERVER-SHALL-11 (_revincludes: InsurancePlan:owned-by)
* **Preconditions, Test Steps, Expected Results, Validation Criteria:**  Follow the same structure as Test Case 4.1, replacing `Endpoint:organization` with `InsurancePlan:owned-by` in the request URL and adjusting the expected linked resource type accordingly.

**4.5. Test Case ID: TEST-REQ-SERVER-SHALL-11-ORGANIZATIONAFFILIATION**

* **Requirement:** REQ-SERVER-SHALL-11 (_revincludes: OrganizationAffiliation:primary-organization)
* **Preconditions, Test Steps, Expected Results, Validation Criteria:**  Follow the same structure as Test Case 4.1, replacing `Endpoint:organization` with `OrganizationAffiliation:primary-organization` in the request URL and adjusting the expected linked resource type accordingly.

**5. Special Testing Considerations**

**5.1. Edge Cases**

* **Missing Linked Resources:** Test scenarios where the requested Organization resource does not have any linked resources for a specific _revincludes. The server should return a valid Bundle with the Organization resource but without any additional resources.
* **Circular References:**  Evaluate scenarios where circular references exist between resources (e.g., Organization A is linked to Organization B, and Organization B is linked back to Organization A). Ensure the server handles these cases gracefully and avoids infinite loops.

**5.2. Performance Considerations**

* **Response Time:** Measure the response time for requests with _revincludes, especially when retrieving multiple linked resources.  Establish acceptable performance thresholds.
* **Resource Limits:**  Test the server's behavior when requests involve a large number of linked resources. Verify compliance with any defined resource limits and error handling.

**5.3. Security Testing Aspects**

* **Authorization:**  Validate that access to Organization resources and linked data is properly authorized based on user roles and permissions.
* **Data Filtering:**  Ensure that sensitive information within linked resources is appropriately filtered or masked based on user access rights. 
