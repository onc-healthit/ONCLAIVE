# Consolidated Test Plan for Plan Net

## Generated on: 2025-04-09 14:11:09

## Capability Statement

This test plan incorporates constraints and requirements from the Plan Net Capability Statement.

## Table of Contents

- [Client](#client)
  - [REQ-02: No PII sending by clients](#req-02)
  - [REQ-06: Client handling of Must Support data elements](#req-06)
  - [REQ-07: Client display of data elements](#req-07)
  - [REQ-08: Client interpretation of missing Must Support data](#req-08)
  - [REQ-09: Client processing of missing information indicators](#req-09)
  - [REQ-31: Client tracking of directory content updates](#req-31)
- [Server](#server)
  - [REQ-01: No PII requirement for directory queries](#req-01)
  - [REQ-03: Population of Must Support data elements](#req-03)
  - [REQ-04: Not including absent data elements](#req-04)
  - [REQ-05: Using dataAbsentReason for missing required information](#req-05)
  - [REQ-10: JSON format support](#req-10)
  - [REQ-11: RESTful behavior implementation](#req-11)
  - [REQ-12: Support for all Implementation Guide profiles](#req-12)
  - [REQ-13: Unauthorized request response](#req-13)
  - [REQ-14: Insufficient scope response](#req-14)
  - [REQ-15: Invalid parameter response](#req-15)
  - [REQ-16: Unknown resource response](#req-16)
  - [REQ-17: Deleted resource response](#req-17)
  - [REQ-18: Profile identification in meta attribute](#req-18)
  - [REQ-19: Individual search parameter support](#req-19)
  - [REQ-20: Combination search parameter support](#req-20)
  - [REQ-21: Forward chaining support](#req-21)
  - [REQ-22: Reverse chaining support](#req-22)
  - [REQ-23: XML format support](#req-23)
  - [REQ-24: Rejection of unauthorized requests](#req-24)
  - [REQ-25: Support for read interaction](#req-25)
  - [REQ-26: Support for vread interaction](#req-26)
  - [REQ-27: Support for _includes](#req-27)
  - [REQ-28: Support for _revincludes](#req-28)
  - [REQ-29: Network profile NPI handling](#req-29)
  - [REQ-30: lastUpdate timestamp requirement](#req-30)
  - [REQ-32: General Search for Pharmacy](#req-32)
  - [REQ-33: Provider search by name](#req-33)
  - [REQ-34: Organization search by name](#req-34)
  - [REQ-35: Provider search by specialty](#req-35)
  - [REQ-36: Organization search by specialty](#req-36)
  - [REQ-37: Search for active practitioners and organizations](#req-37)
  - [REQ-38: Network contact handling for departments](#req-38)
  - [REQ-39: Organization contact handling for departments](#req-39)
  - [REQ-40: Practitioner qualification coding](#req-40)

## Test Specifications

<a id='client'></a>

## Client

<a id='req-02'></a>

### REQ-02: No PII sending by clients

**Description**: "A directory mobile application SHALL NOT send consumer identifiable information when querying a Plan-Net service."

**Actor**: Client

**Conformance**: SHALL NOT

```markdown
# Test Specification for REQ-02

## 1. Requirement ID
- **REQ-02**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Attestation
  - This requirement is best verified through inspection and attestation since it involves ensuring that no personally identifiable information (PII) is sent by the client application. Automated testing can be challenging due to the nature of PII, which requires human judgment to identify.

### Complexity
- **Complexity**: Moderate
  - While the requirement itself is straightforward, ensuring compliance involves understanding what constitutes PII and verifying that none is sent, which can be nuanced.

### Prerequisites
- **System Configurations**: 
  - The directory mobile application must be configured to connect to the Plan-Net service.
  - Access to the application's source code or logs to inspect outgoing data payloads.
- **Data Setup**: 
  - Test data that does not include PII should be prepared for use by the client application during testing.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - None specifically required, as the test focuses on the absence of PII rather than specific FHIR resources.
- **Expected Outputs**: 
  - Confirmation that no PII is present in any data sent by the client application when querying the Plan-Net service.

### Required FHIR Operations
- **API Calls/Operations**: 
  - `GET` operations to query the Plan-Net service.
  - Ensure that these operations are supported as per the Capability Statement of the Plan-Net service.

### Validation Criteria
- **Specific Checks**:
  - Inspect the payload of requests sent by the client application to the Plan-Net service.
  - Verify that no fields contain PII such as names, social security numbers, addresses, phone numbers, or any other identifiable information.
  - Check logs or use network monitoring tools to capture and review outgoing requests.
  - Ensure compliance through a checklist or attestation form signed by the development team, confirming that no PII is sent.
- **Assertions**:
  - Assert that all outgoing requests from the client application contain only non-identifiable information.
  - Assert that any identifiable information is either anonymized or removed before sending.

This test specification ensures that the directory mobile application complies with the requirement to not send PII when querying the Plan-Net service, aligning with the applicable Capability Statement information.
```

---

<a id='req-06'></a>

### REQ-06: Client handling of Must Support data elements

**Description**: "Application actors SHALL be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."

**Actor**: Client

**Conformance**: SHALL

# Test Specification for Requirement REQ-06

## 1. Requirement ID
- **REQ-06**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies that client applications must handle Must Support data elements without errors or failures. This can be tested by providing resource instances containing Must Support elements and observing the client's behavior.

### Complexity
- **Complexity Level**: Moderate
- **Rationale**: While the requirement is straightforward, it involves testing multiple resource types and ensuring that the client handles each Must Support element correctly, which may vary across resources.

### Prerequisites
- **System Configurations**: 
  - The client application must be installed and configured to interact with a FHIR server.
  - Access to a FHIR server that supports the relevant resources and operations.
- **Data Setup**: 
  - A set of FHIR resource instances that include Must Support elements as defined in the Implementation Guide.
  - A list of Must Support elements for each resource type to be tested.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - A collection of resource instances (e.g., Patient, Observation, Encounter) that include Must Support elements.
- **Expected Outputs**: 
  - The client processes the resource instances without generating errors or causing application failures.
  - Logs or reports indicating successful processing of Must Support elements.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resourceType]/[id]` to retrieve resource instances containing Must Support elements.
  - `POST [base]/[resourceType]` or `PUT [base]/[resourceType]/[id]` to test client handling of Must Support elements during resource creation or update.

### Validation Criteria
- **Specific Checks**:
  - **No Errors**: Verify that the client application does not produce any error messages or exceptions when processing resources with Must Support elements.
  - **Successful Processing**: Confirm that the client can successfully display, store, or otherwise handle the Must Support elements as intended.
  - **Log Verification**: Check application logs for any warnings or errors related to Must Support elements.
  - **User Interface**: If applicable, ensure that Must Support elements are correctly rendered in the client’s user interface.
- **Assertions**:
  - The client application logs should not contain any error entries related to Must Support elements.
  - The client should acknowledge the presence of Must Support elements, either through UI display or internal processing logs.

---

<a id='req-07'></a>

### REQ-07: Client display of data elements

**Description**: "Application actors SHOULD be capable of displaying the data elements for human use or storing the information for other purposes."

**Actor**: Client

**Conformance**: SHOULD

```markdown
# Test Specification for REQ-07: Client Display of Data Elements

## 1. Requirement ID
- **REQ-07**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Attestation
  - This requirement is primarily concerned with the capability of displaying or storing data elements, which is subjective and reliant on user interface design and user experience considerations. It is best verified through inspection or attestation rather than automated testing.

### Complexity
- **Complexity**: Moderate
  - While the requirement itself is straightforward, testing it involves verifying both the display and storage capabilities, which may require multiple steps and considerations.

### Prerequisites
- **System Configurations**: 
  - The client application must be installed and configured to access the FHIR server.
  - User interface components capable of displaying FHIR data elements must be available.
  
- **Data**:
  - Access to a FHIR server with sample data elements that the client application can retrieve.
  - Sample FHIR resources such as Patient, Observation, and Condition should be available for testing.

- **Setup**:
  - Ensure the client application is connected to the FHIR server and has the necessary permissions to retrieve and display data.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**:
  - Patient
  - Observation
  - Condition

- **Expected Outputs**:
  - The client application should display the data elements retrieved from the FHIR server in a human-readable format.
  - The application should also demonstrate the capability to store the retrieved data for other purposes, such as logging or further processing.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Patient/{id}`
  - `GET [base]/Observation/{id}`
  - `GET [base]/Condition/{id}`
  - These operations must be supported as per the Capability Statement.

### Validation Criteria
- **Display Verification**:
  - Verify that the client application correctly displays the data elements from the retrieved FHIR resources.
  - Check that the display includes key elements such as patient name, observation values, and condition descriptions.

- **Storage Verification**:
  - Confirm that the application can store the retrieved data elements for purposes beyond immediate display.
  - This could be verified by checking logs, database entries, or other storage mechanisms used by the application.

- **Conformance Check**:
  - Ensure that the application adheres to the "SHOULD" conformance level by demonstrating the capability to display and store data, even if not mandatory.

- **Inspection**:
  - Conduct a manual inspection of the client application to verify that it meets the requirement of displaying and storing data elements effectively.

```


---

<a id='req-08'></a>

### REQ-08: Client interpretation of missing Must Support data

**Description**: "When querying Health Plan API actors, Application actors SHALL interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."

**Actor**: Client

**Conformance**: SHALL

```markdown
# Test Specification for Requirement REQ-08

## 1. Requirement ID
- **REQ-08**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Attestation
  - The requirement involves interpreting missing data, which is subjective and requires confirmation from the client application actor. This makes it suitable for attestation rather than automated testing.

### Complexity
- **Complexity Level**: Moderate
  - While the concept of interpreting missing data is straightforward, ensuring consistent interpretation across different client implementations adds complexity.

### Prerequisites
- **System Configurations**: 
  - Access to a Health Plan API that supports querying for resources with Must Support data elements.
  - A client application capable of querying the Health Plan API and interpreting the data.
- **Data Requirements**:
  - Sample FHIR resources from the Health Plan API with some Must Support data elements intentionally missing.
- **Setup**:
  - Ensure the client application is configured to connect to the Health Plan API and has necessary permissions.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - Patient, Coverage, and ExplanationOfBenefit resources with missing Must Support data elements.
- **Expected Outputs**:
  - Confirmation from the client application that missing Must Support data elements are interpreted as data not present in the Health Plan API actor's system.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Patient/{id}`
  - `GET [base]/Coverage/{id}`
  - `GET [base]/ExplanationOfBenefit/{id}`
  - These operations should be supported as per the Capability Statement of the Health Plan API.

### Validation Criteria
- **Specific Checks**:
  - Verify that the client application logs or provides a report indicating the interpretation of missing Must Support data elements.
  - Confirm that the client application does not generate errors or incorrect assumptions when Must Support data elements are missing.
  - Ensure that the client application behavior aligns with the requirement description, treating missing data as not present in the Health Plan API actor's system.

- **Assertions**:
  - The client application SHALL provide documentation or logs showing the interpretation of missing Must Support elements.
  - The client SHALL not attempt to infer or fabricate missing Must Support data elements.
```


---

<a id='req-09'></a>

### REQ-09: Client processing of missing information indicators

**Description**: "Consumer App actors SHALL be able to process resource instances containing Must Support data elements asserting missing information."

**Actor**: Client

**Conformance**: SHALL

```markdown
# Test Specification for Requirement REQ-09

## 1. Requirement ID
- **REQ-09**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies that Consumer App actors must process resource instances with Must Support data elements indicating missing information. This can be tested by providing such resource instances and verifying the app's response.

### Complexity
- **Classification**: Moderate
- **Rationale**: While the requirement is straightforward, it involves understanding and processing Must Support data elements, which may vary across different resource types.

### Prerequisites
- **System Configurations**: 
  - The Consumer App must be deployed and accessible for testing.
  - The app must have access to a FHIR server that supports the necessary resources and operations.
- **Data Setup**: 
  - Resource instances with Must Support data elements set to indicate missing information (e.g., using the `data-absent-reason` extension).

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - Examples of FHIR resources (e.g., Patient, Observation) with Must Support elements indicating missing information using the `data-absent-reason` extension.
- **Expected Outputs**: 
  - The Consumer App should correctly identify and handle the missing information indicators, possibly by displaying a notification or logging the occurrence.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Patient/[id]` or `GET [base]/Observation/[id]` to retrieve resource instances with missing information indicators.
  - Ensure these operations are supported as per the Capability Statement.

### Validation Criteria
- **Specific Checks**:
  - Verify that the Consumer App successfully retrieves the resource instances containing Must Support elements with missing information indicators.
  - Confirm that the app processes these indicators correctly, such as by displaying a message or logging the event.
  - Check that the app does not crash or exhibit unexpected behavior when encountering missing information indicators.
  - Ensure that the app's response aligns with any user interface or logging requirements specified in the implementation guide.

- **Assertions**:
  - The app logs or displays a message indicating the presence of missing information.
  - The app maintains functionality and does not produce errors when processing these resource instances.
```


---

<a id='req-31'></a>

### REQ-31: Client tracking of directory content updates

**Description**: "Clients that cache query results can track additions or modifications to directory content through queries that filter content using the _lastUpdated search parameter."

**Actor**: Client

**Conformance**: None (Implementation guidance)

```markdown
# Test Specification for REQ-31: Client Tracking of Directory Content Updates

## 1. Requirement ID
- **REQ-31**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement involves specific operations (queries using the `_lastUpdated` search parameter) that can be programmatically executed and verified.

### Complexity
- **Complexity Level**: Moderate
- **Rationale**: The test involves setting up a client to cache query results and then perform subsequent queries to detect updates, which requires a moderate level of setup and validation.

### Prerequisites
- **System Configurations**: 
  - A FHIR server with directory content that supports the `_lastUpdated` search parameter.
  - A client system capable of caching query results and performing subsequent queries.
- **Data Setup**: 
  - Initial directory content with known timestamps.
  - Ability to modify or add directory content to test updates.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - Directory resources (e.g., `Practitioner`, `Organization`, `Location`) with known `_lastUpdated` timestamps.
- **Expected Outputs**: 
  - Successful retrieval of updated or newly added directory content based on the `_lastUpdated` parameter.

### Required FHIR Operations
- **Search Operation**: 
  - Perform a search query on directory resources using the `_lastUpdated` search parameter.
  - Example API Call: `GET [base]/[resource]?_lastUpdated=[date-time]`

### Validation Criteria
- **Initial Query**: 
  - Execute a query to cache the current state of directory resources.
  - Validate that the initial query returns expected resources with correct `_lastUpdated` timestamps.

- **Update Simulation**: 
  - Simulate an update or addition to the directory content.
  - Ensure the `_lastUpdated` timestamp of updated/new resources is correctly set.

- **Subsequent Query**: 
  - Perform a query using the `_lastUpdated` parameter to retrieve only the updated or newly added resources.
  - Validate that the query returns only the resources with `_lastUpdated` timestamps greater than the initial query.

- **Assertions**:
  - Confirm that the client correctly identifies and retrieves only the modified or newly added resources.
  - Verify that no resources with unchanged `_lastUpdated` timestamps are returned in the subsequent query.

- **Inspection**: 
  - Manually inspect logs or client cache to ensure correct tracking of updates.
```


---



<a id='server'></a>

## Server

<a id='req-01'></a>

### REQ-01: No PII requirement for directory queries

**Description**: "A conformant Plan-Net service SHALL NOT require a directory mobile application to send consumer identifying information in order to query content."

**Actor**: Server

**Conformance**: SHALL NOT

```markdown
# Test Specification for Requirement REQ-01

## 1. Requirement ID
- **REQ-01**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies that no consumer identifying information should be required for directory queries, which can be verified by inspecting the API request and response patterns.

### Complexity
- **Classification**: Simple
- **Rationale**: The requirement involves checking the absence of specific data elements (PII) in API requests, which is straightforward to validate.

### Prerequisites
- **System Configurations**: 
  - A conformant Plan-Net server must be available for testing.
  - The server must have a directory service endpoint as specified in the Capability Statement.
- **Data Setup**: 
  - Ensure the directory service is populated with test data that can be queried without requiring PII.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: None required as input since the test focuses on the absence of PII in the request.
- **Expected Outputs**: Successful query responses from the directory service without requiring PII in the request.

### Required FHIR Operations
- **API Calls/Operations**:
  - Perform a `GET` request on the directory service endpoint (e.g., `/Plan-Net/Directory`) without including any consumer identifying information in the request headers or body.
  - Ensure the server supports the `GET` operation on the directory service as per the Capability Statement.

### Validation Criteria
- **Specific Checks**:
  - **Request Inspection**: Verify that the request does not include any consumer identifying information such as name, date of birth, social security number, or any other PII.
  - **Response Validation**: Confirm that the server responds with a valid directory listing without requiring any PII in the request.
  - **Conformance Assertion**: The test passes if the server successfully returns directory information without any PII being present in the request, adhering to the "SHALL NOT" conformance requirement.
```


---

<a id='req-03'></a>

### REQ-03: Population of Must Support data elements

**Description**: "Health Plan API actors SHALL be capable of populating all Must Support data elements as part of the query results."

**Actor**: Server

**Conformance**: SHALL

# Test Specification for REQ-03

## 1. Requirement ID
REQ-03

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies that Health Plan API actors must populate all Must Support data elements in query results, which can be verified through automated testing by querying the server and checking the response for the presence of these elements.

### Complexity
- **Classification**: Moderate
- **Rationale**: While the requirement is straightforward in terms of checking for the presence of Must Support elements, it requires a comprehensive understanding of which elements are marked as Must Support in the profiles being tested.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to respond to queries with the appropriate FHIR resources that include Must Support elements.
- **Data**: 
  - Test data must be available on the server that includes all Must Support elements for the relevant FHIR profiles.
- **Setup**: 
  - Access to the server's API endpoint with necessary authentication credentials.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - Identify the specific FHIR profiles and resources that include Must Support elements (e.g., Patient, Coverage, ExplanationOfBenefit).
- **Expected Outputs**: 
  - Query responses should include all Must Support elements populated as per the FHIR profiles.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Patient/{id}`
  - `GET [base]/Coverage/{id}`
  - `GET [base]/ExplanationOfBenefit/{id}`
  - Ensure these operations are supported as per the Capability Statement.

### Validation Criteria
- **Presence of Must Support Elements**:
  - Verify that each Must Support element is present in the response for the relevant resources.
- **Correctness of Data**:
  - Ensure that the data within the Must Support elements is valid and conforms to the expected data types and constraints.
- **Assertions**:
  - For each resource type, assert that all Must Support elements are included in the response.
  - Log any missing Must Support elements as a failure.
- **Result Indication**:
  - A test passes if all Must Support elements are present and correctly populated in the response for each queried resource.

---

<a id='req-04'></a>

### REQ-04: Not including absent data elements

**Description**: "In situations where information on a particular Must Support data element is not present and the minimum cardinality is 0, the Health Plan API actors SHALL NOT include the data elements in the resource instance returned as part of the query results."

**Actor**: Server

**Conformance**: SHALL NOT

```markdown
# Test Specification for Requirement REQ-04

## 1. Requirement ID
- **REQ-04**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies a clear condition (absence of data elements with minimum cardinality 0) and a clear expected behavior (SHALL NOT include those elements). This can be programmatically verified by inspecting the returned resource instance.

### Complexity
- **Classification**: Simple
- **Rationale**: The requirement involves checking the presence or absence of data elements in a resource, which is straightforward to implement and verify.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to support the Health Plan API as per the Capability Statement.
- **Data**: 
  - Test resources must be available with optional (min cardinality 0) Must Support elements that may or may not have data.
- **Setup**: 
  - Ensure the server is running and accessible for API calls.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - A set of test resources (e.g., Coverage, ExplanationOfBenefit) with Must Support elements that have a minimum cardinality of 0.
- **Expected Outputs**: 
  - The returned resource instance should not include the Must Support data elements if they are absent.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[ResourceType]?parameter=value`: Perform a query operation to retrieve the resource instances.
  - Ensure these operations are supported as per the Capability Statement.

### Validation Criteria
- **Specific Checks**:
  - Inspect the returned resource instance for the presence of Must Support elements with a minimum cardinality of 0.
  - **Assertion 1**: If the Must Support data element is absent, it SHALL NOT appear in the resource instance.
  - **Assertion 2**: Verify that the server response does not include any empty or null fields for these elements.
  - **Assertion 3**: Confirm that the response adheres to the FHIR resource structure and does not include unexpected elements.

- **Result Indication**:
  - **Pass**: The resource instance does not include absent Must Support elements with a minimum cardinality of 0.
  - **Fail**: The resource instance includes absent Must Support elements, indicating non-conformance.
```


---

<a id='req-05'></a>

### REQ-05: Using dataAbsentReason for missing required information

**Description**: "In situations where information on a particular data element is not present and the minimum cardinality is >0, SHALL send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for Requirement REQ-05

## 1. Requirement ID
- **REQ-05**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies a clear condition (use of `dataAbsentReason`) that can be programmatically checked in FHIR resources when required data is missing.

### Complexity
- **Complexity Level**: Moderate
- **Rationale**: While the concept of `dataAbsentReason` is straightforward, ensuring its correct application across various resources with different cardinalities requires thorough testing.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must support the `dataAbsentReason` extension.
  - The server must have implemented the relevant profiles that specify minimum cardinalities for elements.
- **Data Setup**: 
  - Test data should include instances of FHIR resources where certain required elements are intentionally left absent.
  - Ensure the server is configured to handle and return `dataAbsentReason` values.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - Select resources with elements having a minimum cardinality >0 (e.g., Patient, Observation).
  - Create test instances where these elements are missing.
- **Expected Outputs**: 
  - The server should return the resource with the `dataAbsentReason` extension applied to missing required elements.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET` requests to retrieve resources with missing required elements.
  - `POST` or `PUT` requests to submit resources with missing required elements to check server handling.
  - Ensure these operations are supported as per the Capability Statement.

### Validation Criteria
- **Specific Checks**:
  - Verify that for each resource with missing required elements, the `dataAbsentReason` extension is present.
  - Check that the `dataAbsentReason` uses appropriate values from the specified value set (e.g., nullFlavors).
  - Confirm that the server does not reject resources solely due to missing required elements if `dataAbsentReason` is correctly applied.
- **Assertions**:
  - Assert that the response status is successful (e.g., HTTP 200 or 201 for successful retrieval or submission).
  - Assert that the `dataAbsentReason` extension is correctly populated in the response.
  - Assert that the values used in `dataAbsentReason` are valid according to the specified value set.

```


---

<a id='req-10'></a>

### REQ-10: JSON format support

**Description**: "Support json source formats for all Plan-Net interactions."

**Actor**: Server

**Conformance**: SHALL

# Test Specification for Requirement REQ-10

## 1. Requirement ID
- **REQ-10**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies support for JSON format in all Plan-Net interactions, which can be verified through automated testing by sending requests in JSON format and checking for successful processing.

### Complexity
- **Classification**: Simple
- **Rationale**: The requirement involves verifying the acceptance and processing of JSON formatted requests, which is a straightforward test of format support.

### Prerequisites
- **System Configurations**: 
  - The server must be running and accessible.
  - The server must have Plan-Net interactions implemented.
- **Data/Setup**:
  - A set of valid FHIR resources in JSON format for Plan-Net interactions.
  - Access credentials if required for API access.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - A sample set of FHIR resources relevant to Plan-Net interactions (e.g., Practitioner, Organization, HealthcareService) formatted in JSON.
- **Expected Outputs**: 
  - Successful HTTP status codes (e.g., 200 OK) for valid JSON requests.
  - Correct processing and response of the server indicating successful handling of the JSON input.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET` requests to retrieve resources in JSON format.
  - `POST`, `PUT`, or `PATCH` requests to create or update resources using JSON format.
  - Ensure these operations are supported by the server's Capability Statement.

### Validation Criteria
- **Specific Checks**:
  - **HTTP Response Code**: Verify that the server responds with a 2xx status code for requests made in JSON format.
  - **Content-Type Header**: Check that the `Content-Type` header in the request is set to `application/fhir+json` and that the server accepts this format.
  - **Response Validation**: Confirm that the server's response is correctly formatted in JSON and matches expected resource structures.
  - **Error Handling**: Ensure that the server provides appropriate error messages if JSON format is incorrect or if there are other issues with the request.
- **Assertions**:
  - Assert that all Plan-Net interactions support JSON format as required.
  - Assert that the server processes and returns data correctly when JSON formatted requests are made.

By following this structured approach, the test specification ensures comprehensive coverage of the requirement to support JSON format for all Plan-Net interactions, verifying both acceptance and correct processing of JSON data by the server.

---

<a id='req-11'></a>

### REQ-11: RESTful behavior implementation

**Description**: "Implement the RESTful behavior according to the FHIR specification."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for REQ-11: RESTful Behavior Implementation

## 1. Requirement ID
- **REQ-11**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
  - The requirement to implement RESTful behavior according to the FHIR specification can be tested through automated API testing tools that verify RESTful operations.

### Complexity
- **Complexity Level**: Moderate
  - While the basic RESTful operations (CRUD) are straightforward, ensuring compliance with the full FHIR RESTful specification, including error handling and interaction with various resource types, adds complexity.

### Prerequisites
- **System Configurations**: 
  - A FHIR server instance that supports RESTful operations.
  - Access credentials for the server if authentication is required.
- **Data Setup**:
  - Pre-existing FHIR resources on the server to test read, update, and delete operations.
  - Capability Statement of the server to verify supported operations.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - A set of sample FHIR resources (e.g., Patient, Observation) for CRUD operations.
- **Expected Outputs**:
  - Successful HTTP status codes (e.g., 200, 201) for valid operations.
  - Appropriate error codes (e.g., 400, 404) for invalid operations.

### Required FHIR Operations
- **API Calls**:
  - `GET [base]/[resourceType]` for read operations.
  - `POST [base]/[resourceType]` for create operations.
  - `PUT [base]/[resourceType]/[id]` for update operations.
  - `DELETE [base]/[resourceType]/[id]` for delete operations.
  - `GET [base]/metadata` to retrieve the Capability Statement for supported operations verification.

### Validation Criteria
- **Conformance Checks**:
  - Verify that the server responds with the correct HTTP status codes for each operation.
  - Confirm that the server supports all CRUD operations as per the FHIR RESTful specification.
  - Ensure that the server's Capability Statement lists all supported operations and resource types.
  - Validate that the server correctly handles invalid requests with appropriate error messages and codes.
  - Check that resources are correctly created, read, updated, and deleted as expected.

- **Assertions**:
  - The server SHALL return a 200 status code for successful `GET` requests.
  - The server SHALL return a 201 status code for successful `POST` requests.
  - The server SHALL return a 200 status code for successful `PUT` requests.
  - The server SHALL return a 204 status code for successful `DELETE` requests.
  - The server SHALL return a 404 status code when a resource is not found.
  - The server SHALL return a 400 status code for malformed requests.
```


---

<a id='req-12'></a>

### REQ-12: Support for all Implementation Guide profiles

**Description**: "Support all profiles defined in this Implementation Guide."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for Requirement REQ-12

## 1. Requirement ID
- **REQ-12**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically Testable
  - This requirement is automatically testable as it involves verifying the server's capability to support all profiles defined in the Implementation Guide. This can be done using automated tools that check profile conformance.

### Complexity
- **Complexity**: Moderate
  - The complexity is moderate as it involves multiple profiles and ensuring that each is supported by the server. It requires a comprehensive understanding of the profiles and their constraints.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to expose all profiles defined in the Implementation Guide.
  - Access to the server's Capability Statement to verify declared support for profiles.
  
- **Data/Setup**:
  - Access to the Implementation Guide to identify all profiles.
  - Test data conforming to each profile to be used in validation.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**:
  - A list of all profiles defined in the Implementation Guide.
  - Test instances for each profile to be used in validation.

- **Expected Outputs**:
  - Confirmation that the server supports each profile as per the Implementation Guide.
  - Validation results indicating conformance or non-conformance for each profile.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/metadata`: Retrieve the Capability Statement to verify declared support for profiles.
  - `POST [base]/[ResourceType]`: Submit test instances for each profile to the server to verify support.
  - `GET [base]/[ResourceType]/_search`: Search operations to verify that resources conform to the profiles.

### Validation Criteria
- **Specific Checks**:
  - Verify that the Capability Statement lists all profiles from the Implementation Guide under `rest.resource.supportedProfile`.
  - For each profile, submit a test instance and check:
    - The server accepts the resource without errors.
    - The resource is stored and retrievable.
    - The resource conforms to the profile constraints (using a FHIR validator).
  - Ensure that search operations return results conforming to the profiles.
  - Assertions:
    - All profiles are listed in the Capability Statement.
    - Test instances conform to profiles without validation errors.
    - Search results are consistent with profile constraints.
```


---

<a id='req-13'></a>

### REQ-13: Unauthorized request response

**Description**: "Return the following response classes: (Status 401/4xx): unauthorized request."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for Requirement REQ-13

## 1. Requirement ID
- **REQ-13**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies a clear expected behavior (returning a 401/4xx status code) that can be programmatically verified through automated testing.

### Complexity
- **Level**: Simple
- **Rationale**: The requirement involves checking for a specific HTTP status code in response to an unauthorized request, which is a straightforward validation.

### Prerequisites
- **System Configurations**: 
  - The server must be running and accessible over the network.
  - The server must be configured to require authentication for access to protected resources.
- **Data/Setup**: 
  - Ensure that there are resources on the server that require authentication to access.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - Any resource that requires authentication to access (e.g., Patient, Observation).
- **Expected Outputs**: 
  - HTTP response with status code 401 (Unauthorized) or another 4xx status code indicating an unauthorized request.

### Required FHIR Operations
- **API Calls/Operations**: 
  - Perform a `GET` request on a protected FHIR resource endpoint without providing authentication credentials.

### Validation Criteria
- **Specific Checks**:
  - **Assertion 1**: The server returns an HTTP status code of 401 or another 4xx code indicating unauthorized access.
  - **Assertion 2**: The response should include a `WWW-Authenticate` header if applicable, indicating the authentication scheme required.
  - **Assertion 3**: The response body, if present, should contain an OperationOutcome resource providing details about the unauthorized access.

- **Passing Criteria**:
  - The test passes if the server returns the expected 401/4xx status code and meets all specified assertions.

```


---

<a id='req-14'></a>

### REQ-14: Insufficient scope response

**Description**: "Return the following response classes: (Status 403): insufficient scope."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for Requirement REQ-14

## 1. Requirement ID
- **REQ-14**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies a clear response class (HTTP Status 403) for a specific condition (insufficient scope), which can be programmatically verified through automated testing.

### Complexity
- **Classification**: Simple
- **Rationale**: The requirement involves checking the HTTP response status code, which is straightforward and does not involve complex logic or multiple steps.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to enforce scope-based access control.
- **Data**:
  - A valid FHIR client application with limited access scopes that do not cover the requested operation.
- **Setup**:
  - Ensure that the FHIR server is operational and accessible.
  - Ensure that the client application is registered with the FHIR server and has a valid but limited access token.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: None specifically required for the test, but the operation should target a resource or endpoint that the client does not have sufficient scope to access.
- **Expected Outputs**: 
  - HTTP Status Code: 403
  - Response Body: A message indicating "insufficient scope" (optional but recommended for clarity).

### Required FHIR Operations
- **API Call**: 
  - Perform a FHIR operation (e.g., read, search, or update) using the client application with limited scopes.
  - Ensure that the operation targets a resource or endpoint that requires a scope not included in the client's access token.

### Validation Criteria
- **HTTP Status Code**: Verify that the server returns a 403 status code.
- **Response Content**: Optionally, check that the response body contains a message indicating "insufficient scope."
- **Log Verification**: Ensure that server logs (if accessible) indicate the reason for the 403 response was due to insufficient scope.
- **Repeatability**: The test should consistently produce the same results under the same conditions.

By following this test specification, testers can ensure that the FHIR server correctly implements scope-based access control by returning the appropriate HTTP status code when a client attempts to perform an operation without sufficient scope.
```

---

<a id='req-15'></a>

### REQ-15: Invalid parameter response

**Description**: "Return the following response classes: (Status 400): invalid parameter."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for REQ-15: Invalid Parameter Response

## 1. Requirement ID
- **REQ-15**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies a clear expected behavior (HTTP Status 400) when invalid parameters are used in a request. This can be tested programmatically by sending requests with known invalid parameters and verifying the response.

### Complexity
- **Complexity Level**: Simple
- **Rationale**: The test involves sending requests with invalid parameters and checking for a specific HTTP status code, which is straightforward.

### Prerequisites
- **System Configurations**: 
  - A running instance of the FHIR server that implements the relevant Capability Statement.
  - Access to the server's API endpoints.
- **Data Setup**: 
  - No specific data setup is required as the test focuses on the response to invalid parameters rather than data content.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - Any FHIR resource type that the server supports and is relevant to the operations being tested.
- **Invalid Parameters**: 
  - Construct requests with parameters that are known to be invalid according to the FHIR specification or the server's implementation guide.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resource]?invalidParam=value`
  - `POST [base]/[resource]` with invalid query parameters in the URL or body
  - Ensure these operations are supported as per the Capability Statement.

### Validation Criteria
- **Expected Output**: 
  - The server MUST return an HTTP 400 status code.
- **Assertions**:
  - Verify that the response status code is 400.
  - Optionally, check the response body for an OperationOutcome resource that provides additional details about the invalid parameter error.
- **Pass/Fail Criteria**:
  - **Pass**: The server returns a 400 status code for requests with invalid parameters.
  - **Fail**: The server returns any status code other than 400 or does not provide an appropriate error message.

```


---

<a id='req-16'></a>

### REQ-16: Unknown resource response

**Description**: "Return the following response classes: (Status 404): unknown resource."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for REQ-16: Unknown Resource Response

## 1. Requirement ID
- **REQ-16**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies a clear expected behavior (returning a 404 status code) when an unknown resource is requested, which can be programmatically verified.

### Complexity
- **Complexity Level**: Simple
- **Rationale**: The requirement involves a straightforward check of the HTTP response status code when accessing a non-existent resource.

### Prerequisites
- **System Configurations**: 
  - The server must be running and accessible.
  - The server must have no existing resource with the ID that will be used for testing.
- **Data/Setup**:
  - Ensure that the test environment does not have the resource ID that will be used to simulate the unknown resource request.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resource**: Use a non-existent resource ID for any resource type supported by the server.
- **Expected Output**: HTTP status code 404 with a message indicating "unknown resource."

### Required FHIR Operations
- **API Call**: Perform a `GET` request on a FHIR resource endpoint using a non-existent resource ID.
  - Example: `GET [base]/Patient/unknown-id`
- **Capability Statement Support**: Ensure the server's Capability Statement indicates support for the `GET` operation on the resource type being tested.

### Validation Criteria
- **HTTP Status Code**: The server must return a 404 status code.
- **Response Body**: Optionally, the response body should include an OperationOutcome resource with a message indicating the resource is unknown.
- **Assertions**:
  - Assert that the HTTP status code is 404.
  - If an OperationOutcome is returned, assert that it contains a message related to the unknown resource.
- **Pass/Fail Criteria**:
  - **Pass**: If the server returns a 404 status code and, if applicable, an appropriate OperationOutcome message.
  - **Fail**: If the server returns any status code other than 404 or an inappropriate response message.

By following this test specification, the conformance of the server to the requirement REQ-16 can be effectively validated.
```

---

<a id='req-17'></a>

### REQ-17: Deleted resource response

**Description**: "Return the following response classes: (Status 410): deleted resource."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for Requirement REQ-17

## 1. Requirement ID
- **REQ-17**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies a clear expected behavior (HTTP Status 410 for deleted resources) that can be programmatically verified through automated testing.

### Complexity
- **Classification**: Simple
- **Rationale**: The requirement involves a straightforward HTTP status code check in response to a specific condition (accessing a deleted resource).

### Prerequisites
- **System Configuration**: 
  - The server must be configured to support resource deletion operations.
  - The server must be capable of returning HTTP status codes as per the FHIR specification.
- **Data Setup**: 
  - A resource that can be deleted must exist in the server prior to the test.
  - Ensure that the resource is deleted before attempting to access it for the test.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resource**: 
  - A reference to a resource that has been deleted (e.g., Patient, Observation).
- **Expected Output**: 
  - HTTP response with status code 410 (Gone).

### Required FHIR Operations
- **API Calls/Operations**:
  - `DELETE [base]/[resourceType]/[id]`: To delete the resource.
  - `GET [base]/[resourceType]/[id]`: To attempt to access the deleted resource and verify the response.

### Validation Criteria
- **HTTP Status Code**: 
  - Verify that the server returns an HTTP 410 status code when accessing a deleted resource.
- **Response Body**:
  - Optionally, verify that the response body contains appropriate information or an OperationOutcome resource indicating the resource is gone.
- **Log Verification**:
  - Ensure that the server logs (if accessible) reflect the deletion operation and the subsequent access attempt.

### Test Steps
1. **Setup**: Create a resource on the server.
2. **Delete**: Perform a DELETE operation on the created resource.
3. **Access**: Attempt a GET operation on the deleted resource.
4. **Verify**: Check that the response status code is 410.
5. **Cleanup**: Ensure no residual data or configurations remain post-test.

This test ensures that the server conforms to the requirement of returning a 410 status code for deleted resources, as specified in the FHIR Implementation Guide.
```

---

<a id='req-18'></a>

### REQ-18: Profile identification in meta attribute

**Description**: "Identify the Plan-Net profiles supported as part of the FHIR meta.profile attribute for each instance."

**Actor**: Server

**Conformance**: SHALL

# Test Specification for Requirement REQ-18

## 1. Requirement ID
- **REQ-18**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement involves checking the `meta.profile` attribute of FHIR resources, which can be programmatically verified by inspecting the resource metadata.

### Complexity
- **Classification**: Simple
- **Rationale**: The test involves straightforward verification of the presence and correctness of profile URIs in the `meta.profile` attribute.

### Prerequisites
- **System Configurations**: 
  - A FHIR server that supports the Plan-Net profiles.
- **Data Setup**: 
  - Instances of FHIR resources that are expected to conform to Plan-Net profiles.
  - Knowledge of the specific Plan-Net profile URIs that should be present in the `meta.profile` attribute.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: Instances of resources that are expected to conform to specific Plan-Net profiles (e.g., Practitioner, Organization, Location).
- **Expected Outputs**: 
  - Each resource instance should have the correct Plan-Net profile URI(s) listed in its `meta.profile` attribute.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resourceType]/[id]` - Retrieve specific resource instances by ID.
  - `GET [base]/[resourceType]` - Search for resource instances, potentially with query parameters to filter by profile.

### Validation Criteria
- **Presence Check**: Verify that the `meta.profile` attribute is present in the resource metadata.
- **Correctness Check**: 
  - Ensure that the `meta.profile` attribute contains the correct Plan-Net profile URI(s).
  - Compare the profile URIs in the `meta.profile` attribute against the expected list of Plan-Net profile URIs.
- **Conformance Assertion**: 
  - The test passes if all retrieved resource instances have the correct Plan-Net profile URI(s) in their `meta.profile` attribute.
  - The test fails if any resource instance is missing the `meta.profile` attribute or contains incorrect profile URIs.

By following this test specification, testers can ensure that the FHIR server correctly identifies and supports the Plan-Net profiles as required by the implementation guide.

---

<a id='req-19'></a>

### REQ-19: Individual search parameter support

**Description**: "Support the searchParameters on each profile individually."

**Actor**: Server

**Conformance**: SHALL

# Test Specification for REQ-19

## 1. Requirement ID
- **REQ-19**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies that the server must support search parameters on each profile individually, which can be verified through automated testing by executing search operations with various parameters.

### Complexity
- **Classification**: Moderate
- **Rationale**: Testing involves executing multiple search operations across different profiles, requiring a comprehensive understanding of the search parameters applicable to each profile.

### Prerequisites
- **System Configurations**: 
  - A FHIR server with implemented profiles and search capabilities as per the Capability Statement.
- **Data Requirements**: 
  - A dataset containing instances of resources for each profile to be tested.
  - Knowledge of the search parameters applicable to each profile.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - Instances of resources for each profile defined in the implementation guide.
- **Expected Outputs**: 
  - Correct search results for each executed search operation, matching the criteria specified by the search parameters.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resource]?parameter=value` for each search parameter applicable to the profile.
  - Ensure these operations are supported as per the Capability Statement.

### Validation Criteria
- **Specific Checks**:
  - **Check 1**: Verify that the server returns a `200 OK` HTTP status code for each search operation.
  - **Check 2**: Validate that the search results contain only resources that match the specified search parameters.
  - **Check 3**: Confirm that the server supports all required search parameters for each profile as defined in the implementation guide.
  - **Check 4**: Ensure that the search results are consistent with the expected output, based on the dataset and search criteria.
- **Assertions**:
  - Each search operation should return results that are filtered according to the search parameters.
  - The server should not return any error messages related to unsupported search parameters for the profiles being tested.

---

<a id='req-20'></a>

### REQ-20: Combination search parameter support

**Description**: "Support the searchParameters on each profile in combination."

**Actor**: Server

**Conformance**: SHALL

# Test Specification for Requirement REQ-20

## 1. Requirement ID
- **REQ-20**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies that the server must support search parameters on each profile in combination, which can be tested by executing search queries and verifying the responses.

### Complexity
- **Classification**: Moderate
- **Rationale**: While the basic search operation is straightforward, testing combinations of search parameters across different profiles requires a more nuanced approach to ensure all combinations are supported.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to support the necessary search operations as per the FHIR specification.
  - Access to the server's API endpoint with appropriate authentication if required.

- **Data Setup**:
  - A set of FHIR resources that conform to the profiles specified in the Implementation Guide.
  - Resources must include a variety of data to ensure comprehensive testing of search parameter combinations.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - A collection of resources that conform to the profiles defined in the Implementation Guide. These may include Patient, Observation, Encounter, etc., depending on the profiles.
  - Each resource should have diverse data to test different search parameter combinations effectively.

- **Expected Outputs**:
  - Correctly filtered search results based on the combination of search parameters.
  - Responses should conform to the FHIR search response format, including correct resource counts and pagination if applicable.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resource]?parameter1=value1&parameter2=value2...`
  - Ensure the server supports these operations as per the Capability Statement.

### Validation Criteria
- **Specific Checks**:
  - **Correctness**: Verify that the search results match the expected set of resources based on the combination of search parameters used.
  - **Conformance**: Ensure that the search results conform to the FHIR resource structure and profiles specified in the Implementation Guide.
  - **Performance**: The server should respond within an acceptable time frame for search operations.
  - **Error Handling**: Verify that invalid combinations of search parameters return appropriate error messages as per the FHIR specification.
  - **Pagination**: If the search results exceed the server's page size, ensure that pagination is correctly implemented and navigable.

By following this structured test specification, the requirement REQ-20 can be thoroughly validated to ensure that the server supports combination search parameters as required by the FHIR Implementation Guide.

---

<a id='req-21'></a>

### REQ-21: Forward chaining support

**Description**: "Support forward chaining on all search parameters that specify the 'chain' property."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for REQ-21: Forward Chaining Support

## 1. Requirement ID
- **REQ-21**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically Testable
  - The requirement specifies a clear behavior (support for forward chaining on search parameters with the 'chain' property) that can be programmatically verified through API interactions.

### Complexity
- **Complexity**: Moderate
  - Forward chaining involves understanding the relationships between resources and requires multiple API calls to verify proper chaining behavior.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server must have implemented the search parameter chaining as per the FHIR specification.
  
- **Data Setup**:
  - Populate the server with a dataset that includes resources with known relationships. For example, Patient, Observation, and Practitioner resources where Observations are linked to Patients, and Patients are linked to Practitioners.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**:
  - A set of Patient resources with linked Observation resources.
  - Practitioner resources linked to the Patients.
  
- **Expected Outputs**:
  - Successful search responses that demonstrate the ability to chain search parameters across related resources.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Observation?subject:Patient.name=Smith`
  - `GET [base]/Patient?general-practitioner:Practitioner.name=Jones`
  - Ensure these operations are supported as per the Capability Statement.

### Validation Criteria
- **Specific Checks**:
  - **Check 1**: Execute a search query using a chained parameter (e.g., `Observation?subject:Patient.name=Smith`) and verify that the response includes Observations linked to Patients with the name "Smith".
  - **Check 2**: Execute a search query using a chained parameter (e.g., `Patient?general-practitioner:Practitioner.name=Jones`) and verify that the response includes Patients whose general practitioner has the name "Jones".
  - **Assertions**:
    - The response should include the expected resources based on the chaining logic.
    - The response should not include resources that do not meet the chained search criteria.
    - Verify that the server returns a status code of 200 for successful searches.
    - Ensure that the response conforms to the FHIR search result format.

By following this test specification, the implementation of forward chaining support can be systematically verified to ensure compliance with the FHIR Implementation Guide requirement REQ-21.
```

---

<a id='req-22'></a>

### REQ-22: Reverse chaining support

**Description**: "Support reverse chaining on all search parameters that specify the 'chain' property."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for REQ-22: Reverse Chaining Support

## 1. Requirement ID
- **REQ-22**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies a clear behavior (support for reverse chaining on search parameters with the 'chain' property) that can be programmatically verified through API calls.

### Complexity
- **Complexity Level**: Moderate
- **Rationale**: While the concept of reverse chaining is straightforward, it involves understanding the relationships between resources and ensuring that the server correctly implements the chaining logic across potentially multiple resource types.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be configured to support search operations.
  - The server's Capability Statement must indicate support for reverse chaining.
- **Data Setup**:
  - Populate the server with a set of interconnected FHIR resources that include search parameters with the 'chain' property. For example, Patient, Encounter, and Observation resources where Observations are linked to Encounters, and Encounters are linked to Patients.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - A set of resources that demonstrate relationships, such as:
    - `Patient` resources
    - `Encounter` resources linked to `Patient`
    - `Observation` resources linked to `Encounter`
- **Expected Outputs**:
  - Successful execution of reverse chaining queries that return correct and expected results based on the resource relationships.

### Required FHIR Operations
- **API Calls**:
  - Perform a search operation using reverse chaining. For example:
    - `/Observation?_has:Encounter:subject:Patient.identifier=12345`
    - This query should return Observations linked to Encounters that are associated with a Patient having the identifier `12345`.

### Validation Criteria
- **Specific Checks**:
  - **Correctness**: Verify that the search results include only those resources that meet the reverse chaining criteria.
  - **Completeness**: Ensure that all applicable resources are returned by the query.
  - **Performance**: Confirm that the server responds to reverse chaining queries within an acceptable time frame.
  - **Conformance**: Check that the server's response conforms to the FHIR specification for search results, including correct resource types and structures.

- **Assertions**:
  - The search response contains the expected number of resources.
  - Each resource in the response is correctly linked according to the reverse chaining logic.
  - The server's Capability Statement includes support for the necessary search operations and reverse chaining.

By following this test specification, testers can ensure that the FHIR server meets the requirement for supporting reverse chaining on search parameters with the 'chain' property.
```

---

<a id='req-23'></a>

### REQ-23: XML format support

**Description**: "Support xml source formats for all Plan-Net interactions."

**Actor**: Server

**Conformance**: SHOULD

```markdown
# Test Specification for Requirement REQ-23

## 1. Requirement ID
- **REQ-23**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically Testable
  - The requirement to support XML format for all Plan-Net interactions can be verified by executing automated tests that check the server's ability to handle XML input and output.

### Complexity
- **Complexity**: Moderate
  - While the requirement is straightforward, it involves verifying multiple interactions across the Plan-Net API, which requires a comprehensive set of test cases to ensure coverage.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to accept and process XML format requests.
  - The server must be capable of returning responses in XML format.
- **Data Setup**:
  - A set of valid FHIR resources that are part of the Plan-Net interactions must be available for testing.
  - Test user accounts and permissions configured to access the server endpoints.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**:
  - A collection of FHIR resources relevant to Plan-Net interactions, such as `Practitioner`, `Organization`, `Location`, etc., in XML format.
- **Expected Outputs**:
  - Correctly formatted XML responses for each interaction.
  - HTTP status codes indicating success (e.g., 200 OK) for valid requests.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET` requests for retrieving resources in XML format.
  - `POST` requests for creating resources with XML payloads.
  - `PUT` requests for updating resources using XML format.
  - `DELETE` requests to ensure XML responses are correctly formatted when applicable.

### Validation Criteria
- **Conformance Checks**:
  - Verify that the server accepts XML payloads for all Plan-Net interactions.
  - Confirm that the server returns responses in XML format for all Plan-Net interactions.
  - Validate the structure and content of the XML responses against the FHIR XML schema.
  - Ensure that the server correctly handles XML-specific errors and returns appropriate error messages and status codes.
  - Check that the server's Capability Statement indicates support for XML format in the `format` element.

- **Assertions**:
  - The server must correctly parse and process XML input without errors.
  - The server must produce valid XML output that conforms to the FHIR XML schema.
  - All interactions must be successfully executed with XML format, and any deviations must be logged as failures.

This test specification ensures that the server meets the requirement to support XML format for all Plan-Net interactions, providing a robust framework for automated testing.
```

---

<a id='req-24'></a>

### REQ-24: Rejection of unauthorized requests

**Description**: "A server SHALL reject any unauthorized requests by returning an HTTP 401 unauthorized response code."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for Requirement REQ-24

## 1. Requirement ID
- **REQ-24**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies a clear expected behavior (HTTP 401 response) that can be programmatically verified.

### Complexity
- **Complexity Level**: Simple
- **Rationale**: The requirement involves a straightforward verification of HTTP response status code.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to authenticate requests using a method such as OAuth 2.0, Basic Authentication, or another supported mechanism.
- **Data**: 
  - No specific FHIR resources are required as input since the test focuses on unauthorized access.
- **Setup**: 
  - Ensure the server is running and accessible over the network.
  - Ensure that there are no valid authentication tokens or credentials included in the request.

## 3. Test Implementation Strategy

### Required Inputs
- **HTTP Request**: 
  - An HTTP request to the FHIR server's endpoint without any authentication credentials or with invalid credentials.
- **Expected Output**: 
  - The server should return an HTTP 401 Unauthorized response.

### Required FHIR Operations
- **API Calls**: 
  - Perform a GET request to a FHIR resource endpoint (e.g., `/Patient`) without authentication.
  - Optionally, perform a POST request to a FHIR resource endpoint with invalid credentials to verify consistent behavior.

### Validation Criteria
- **HTTP Status Code**: 
  - Verify that the server returns an HTTP 401 Unauthorized status code.
- **Response Body**: 
  - Optionally, check that the response body contains a standard error message or OperationOutcome resource indicating unauthorized access.
- **Headers**: 
  - Verify that the `WWW-Authenticate` header is present in the response, indicating the authentication scheme (e.g., `Bearer`, `Basic`).

### Additional Notes
- **Security Considerations**: 
  - Ensure that the test does not inadvertently expose sensitive information or credentials.
- **Repeatability**: 
  - The test should be repeatable and should not alter the server's state or data.
```


---

<a id='req-25'></a>

### REQ-25: Support for read interaction

**Description**: "For each resource type and profile, a Plan Net server SHALL support the read interaction."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for FHIR Implementation Guide Requirement REQ-25

## 1. Requirement ID
- **REQ-25**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies that the server must support the read interaction for each resource type and profile, which can be verified through automated API testing.

### Complexity
- **Level**: Moderate
- **Rationale**: The requirement involves testing multiple resource types and profiles, requiring a comprehensive set of test cases to ensure coverage.

### Prerequisites
- **System Configurations**: 
  - A FHIR server instance configured to support the Plan Net Implementation Guide.
  - Access credentials for the FHIR server if authentication is required.
- **Data Setup**: 
  - A set of FHIR resources available on the server for each resource type and profile defined in the Plan Net Implementation Guide.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: A list of resource types and profiles as defined in the Plan Net Implementation Guide. Examples include:
  - `Practitioner`
  - `Organization`
  - `Location`
  - `HealthcareService`
- **Expected Outputs**: 
  - Successful HTTP 200 responses for valid read requests.
  - Correct resource data returned that matches the requested resource ID and conforms to the specified profile.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resourceType]/[id]` for each resource type and profile.
  - Ensure these operations are supported as per the Capability Statement.

### Validation Criteria
- **HTTP Status Code**: 
  - Verify that the server returns a 200 OK status for valid read requests.
- **Resource Conformance**: 
  - Validate that the returned resource conforms to the specified profile using FHIR validation tools.
- **Data Integrity**: 
  - Ensure the returned resource data matches the expected data for the given resource ID.
- **Error Handling**: 
  - Verify that the server returns appropriate error codes (e.g., 404 Not Found) for invalid resource IDs.

By following this structured test specification, testers can ensure that the Plan Net server meets the requirement to support the read interaction for each resource type and profile as mandated by the Implementation Guide.
```

---

<a id='req-26'></a>

### REQ-26: Support for vread interaction

**Description**: "For each resource type and profile, a Plan Net server SHOULD support the vread interaction."

**Actor**: Server

**Conformance**: SHOULD

```markdown
# Test Specification for Requirement REQ-26

## 1. Requirement ID
- **REQ-26**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically Testable
  - The requirement is automatically testable as it involves verifying the server's support for the `vread` interaction, which can be tested through API calls.

### Complexity
- **Complexity Level**: Simple
  - The `vread` interaction is a straightforward operation that retrieves a specific version of a resource, making the test simple in nature.

### Prerequisites
- **System Configurations**: 
  - The server must be running and accessible via a network.
  - The server must have FHIR resources stored with multiple versions available for testing the `vread` interaction.
- **Data Setup**: 
  - Ensure that there are multiple versions of at least one instance of each resource type and profile that the server supports.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - A list of resource types and profiles supported by the server.
  - Specific resource IDs and version IDs for each resource type to test `vread`.

- **Expected Outputs**:
  - Successful HTTP 200 responses for valid `vread` requests.
  - Correct resource version returned in the response body.
  - Appropriate error codes (e.g., 404) for invalid resource or version IDs.

### Required FHIR Operations
- **API Calls/Operations**:
  - Perform a `vread` operation for each resource type and profile using the endpoint pattern: `[base]/[resourceType]/[id]/_history/[vid]`
  - Ensure that the server's Capability Statement indicates support for the `vread` interaction for the tested resources.

### Validation Criteria
- **Conformance Checks**:
  - Verify that the server returns a 200 HTTP status code for valid `vread` requests.
  - Confirm that the response contains the correct version of the resource as specified in the request.
  - Validate that the `meta.versionId` in the response matches the requested version ID.
  - Check that the server returns a 404 HTTP status code for requests with non-existent resource IDs or version IDs.
  - Ensure that the server's Capability Statement includes the `vread` interaction for each resource type tested.

- **Assertions**:
  - Assert that the `vread` interaction is supported as described in the Capability Statement.
  - Assert that the server correctly handles both valid and invalid `vread` requests according to FHIR specifications.
```


---

<a id='req-27'></a>

### REQ-27: Support for _includes

**Description**: "[For each resource] A Server SHALL be capable of supporting the following _includes [list]."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for REQ-27: Support for _includes

## 1. Requirement ID
- **REQ-27**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies that the server must support certain _includes functionality, which can be verified through automated API testing by executing queries with _includes parameters and checking the responses.

### Complexity
- **Complexity Level**: Moderate
- **Rationale**: While the basic test involves executing queries with _includes parameters, the complexity arises from ensuring that all specified resources and their relationships are correctly handled by the server.

### Prerequisites
- **System Configurations**: 
  - A FHIR server instance that is compliant with the applicable Capability Statement.
  - Access to the server's API endpoints.
- **Data Setup**:
  - Preloaded FHIR resources that are relevant to the _includes parameters being tested.
  - Ensure that relationships between resources are established as per the _includes specifications.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - A list of resources that are specified in the _includes list.
  - Example resources might include Patient, Encounter, Observation, etc., depending on the specific _includes requirements.
- **Expected Outputs**:
  - Responses from the server that include the requested resources and their related resources as specified by the _includes parameters.

### Required FHIR Operations
- **API Calls/Operations**:
  - HTTP GET requests with _includes parameters on the relevant FHIR resource endpoints.
  - Example: `GET [base]/Patient?_include=Patient:organization`

### Validation Criteria
- **Specific Checks**:
  - Verify that the server returns HTTP status code 200 for requests with _includes parameters.
  - Check that the response contains the main resource and the included resources as specified by the _includes parameter.
  - Ensure that the included resources are correctly linked to the main resource as per the FHIR specification.
  - Validate that the server's response adheres to the FHIR JSON or XML format as expected.
  - Confirm that the server's capability statement lists support for the _includes functionality.

- **Assertions**:
  - The response includes all specified related resources.
  - The relationships between the main and included resources are correctly represented.
  - No unexpected errors or omissions in the response data.

By following this structured approach, the test will ensure that the server conforms to the requirement of supporting _includes functionality as specified in the FHIR Implementation Guide.
```


---

<a id='req-28'></a>

### REQ-28: Support for _revincludes

**Description**: "[For each resource] A Server SHALL be capable of supporting the following _revincludes: [list]."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for Requirement REQ-28

## 1. Requirement ID
- **REQ-28**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies that the server must support certain `_revincludes`, which can be verified through automated API calls and response validation.

### Complexity
- **Classification**: Moderate
- **Rationale**: While the concept of `_revincludes` is straightforward, the test must ensure that the server correctly handles multiple resource types and potential edge cases.

### Prerequisites
- **System Configurations**: 
  - The server must be running and accessible via a network.
  - The server must have a valid FHIR endpoint supporting the necessary operations.
- **Data Setup**:
  - Populate the server with a set of FHIR resources that have relationships allowing for `_revincludes`.
  - Ensure there are resources of each type mentioned in the `_revincludes` list.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - A list of resources that are expected to be included in the `_revincludes` query, e.g., `Patient`, `Observation`, `Encounter`.
  - Example resources with known relationships that can be used to test `_revincludes`.
  
- **Expected Outputs**:
  - Responses containing the primary resource and the correctly included related resources as specified by the `_revincludes` parameter.

### Required FHIR Operations
- **API Calls**:
  - Perform a `GET` request on the FHIR server for each resource type with the `_revincludes` parameter, e.g., `/Patient?_revincludes=Observation:subject`.
  - Ensure these operations are supported as per the Capability Statement.

### Validation Criteria
- **Response Validation**:
  - **Status Code**: Ensure the HTTP response status code is `200 OK`.
  - **Content Validation**:
    - Verify that the response bundle includes the primary resource and the expected related resources as specified by the `_revincludes` parameter.
    - Check that each included resource has the correct relationship to the primary resource.
  - **Performance**:
    - Ensure the server responds within an acceptable time frame, typically under 2 seconds for a standard query.
  - **Error Handling**:
    - Test for proper error messages and status codes when invalid `_revincludes` parameters are used.

- **Assertions**:
  - Assert that the number of included resources matches the expected count.
  - Assert that the included resources are of the correct type and have the correct references to the primary resource.

This test specification ensures that the server's support for `_revincludes` is thoroughly validated across different resource types and scenarios.
```


---

<a id='req-29'></a>

### REQ-29: Network profile NPI handling

**Description**: "The NPI and CLIA identifier types, which are Must-Support, are clearly intended for provider organizations only and are not expected to be populated for other organization types."

**Actor**: Server

**Conformance**: None (Clarification)

```markdown
# Test Specification for Requirement REQ-29

## 1. Requirement ID
- **REQ-29**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically Testable
  - The requirement specifies that NPI and CLIA identifiers should only be populated for provider organizations, making it possible to automate checks against organization types.

### Complexity
- **Complexity**: Moderate
  - The test involves checking organization types and verifying the presence or absence of specific identifiers, which requires some logic but is not overly complex.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server should have implemented the Organization resource with Must-Support elements for NPI and CLIA identifiers.
  
- **Data Setup**:
  - A dataset of Organization resources with varying types, including provider organizations and non-provider organizations, must be available.
  - Ensure that some provider organizations have NPI and CLIA identifiers populated, while non-provider organizations do not.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - A collection of `Organization` resources with diverse organization types.
  
- **Expected Outputs**:
  - Provider organizations should have NPI and CLIA identifiers populated.
  - Non-provider organizations should not have NPI and CLIA identifiers populated.

### Required FHIR Operations
- **API Calls**:
  - `GET /Organization` to retrieve all organization resources.
  - `GET /Organization/{id}` to retrieve specific organization resources if needed for detailed checks.

### Validation Criteria
- **Specific Checks**:
  - For each `Organization` resource retrieved:
    - **Check 1**: If the organization type is a provider, verify that the `identifier` field includes an NPI and/or CLIA identifier.
    - **Check 2**: If the organization type is not a provider, verify that the `identifier` field does not include an NPI or CLIA identifier.
  
- **Assertions**:
  - **Assertion 1**: All provider organizations have at least one identifier of type NPI or CLIA.
  - **Assertion 2**: No non-provider organizations have identifiers of type NPI or CLIA.

- **Result Indication**:
  - The test passes if all provider organizations meet the identifier criteria and all non-provider organizations do not have these identifiers.
  - The test fails if any provider organization lacks the required identifiers or if any non-provider organization has these identifiers.

```


---

<a id='req-30'></a>

### REQ-30: lastUpdate timestamp requirement

**Description**: "Each profile in this guide requires that the lastUpdate timestamp be provided as part of the profile's data content."

**Actor**: Server

**Conformance**: None (Requirement)

```markdown
# Test Specification for Requirement REQ-30

## 1. Requirement ID
- **REQ-30**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
  - The requirement specifies a clear condition (presence of `lastUpdate` timestamp) that can be programmatically verified.

### Complexity
- **Complexity Level**: Simple
  - The requirement involves checking for the presence of a single element (`lastUpdate` timestamp) in the profile's data content.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to expose FHIR resources as defined in the Implementation Guide.
- **Data Setup**: 
  - Profiles must be available on the server with data content that includes the `lastUpdate` timestamp.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - A list of profiles defined in the Implementation Guide that are expected to include the `lastUpdate` timestamp.
- **Expected Outputs**: 
  - Each profile's data content should include a `lastUpdate` timestamp.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[ProfileType]/[id]` - Retrieve specific instances of the profiles to verify the presence of the `lastUpdate` timestamp.
  - Ensure these operations are supported by the server's Capability Statement.

### Validation Criteria
- **Presence Check**:
  - Verify that the `lastUpdate` timestamp is present in the response for each profile instance.
- **Format Verification**:
  - Ensure that the `lastUpdate` timestamp is in the correct FHIR dateTime format (ISO 8601).
- **Assertions**:
  - Assert that the `lastUpdate` element is not null or empty.
  - Assert that the `lastUpdate` element adheres to the expected dateTime format.
- **Pass Criteria**:
  - All profiles retrieved must include a valid `lastUpdate` timestamp in their data content.
```


---

<a id='req-32'></a>

### REQ-32: General Search for Pharmacy

**Description**: "The Plan-Net design is based around the following types of searches: General Search - Example: Pharmacy - Focal Resource and Field: HealthcareService.category, HealthcareService.specialty - Qualifications of Search: Location, network."

**Actor**: Server

**Conformance**: None (Design requirement)

```markdown
# Test Specification for Requirement REQ-32

## 1. Requirement ID
- **Requirement ID**: REQ-32
- **Summary**: General Search for Pharmacy

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically Testable
  - The requirement specifies a search functionality that can be tested by executing search queries and verifying the results against expected outcomes.

### Complexity
- **Complexity**: Moderate
  - The requirement involves multiple search parameters and cross-referencing between different FHIR resources, which adds a layer of complexity.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must support the necessary search parameters as outlined in the Capability Statement.
- **Data Setup**:
  - Populate the FHIR server with sample data including `HealthcareService` resources with `category` and `specialty` fields populated.
  - Ensure `Location` resources are linked to `HealthcareService` resources.
  - Ensure `Network` information is available and linked appropriately.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**:
  - `HealthcareService` with `category` set to "Pharmacy" and various `specialty` values.
  - `Location` resources linked to the `HealthcareService`.
  - `Organization` and `Network` data linked to `HealthcareService` and `Location`.

- **Expected Outputs**:
  - A list of `HealthcareService` resources that match the search criteria, including correct `category` and `specialty`, and linked `Location` and `Network` information.

### Required FHIR Operations
- **Search Operations**:
  - `GET [base]/HealthcareService?category=pharmacy`
  - `GET [base]/HealthcareService?specialty=[specialty-code]`
  - `GET [base]/HealthcareService?location=[location-id]`
  - `GET [base]/HealthcareService?organization=[organization-id]`

### Validation Criteria
- **Conformance Checks**:
  - Verify that the server returns `HealthcareService` resources where `category` is "Pharmacy".
  - Confirm that the `HealthcareService` resources include the specified `specialty` values.
  - Ensure that returned resources are linked to valid `Location` and `Network` data.
  - Validate that the search results are consistent with the `Location` search parameters (e.g., `address-city`, `address-state`).

- **Assertions**:
  - The response should have a status code of 200 (OK).
  - The response should contain a `Bundle` of type `searchset`.
  - Each entry in the `Bundle` should be a `HealthcareService` resource with the expected `category` and `specialty`.
  - Cross-reference `Location` and `Network` data to ensure they match the search criteria.

This structured test specification provides a comprehensive approach to verifying the implementation of the general search functionality for pharmacies as described in requirement REQ-32.
```

---

<a id='req-33'></a>

### REQ-33: Provider search by name

**Description**: "The Plan-Net design is based around the following types of searches: Provider by Name - Example: Joe Smith - Focal Resource and Field: Practitioner.name - Qualifications of Search: Location, network, specialty, role/privileges."

**Actor**: Server

**Conformance**: None (Design requirement)

```markdown
# Test Specification for REQ-33: Provider Search by Name

## 1. Requirement ID
- **REQ-33**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies a search functionality that can be tested using automated scripts to verify the search results against expected outcomes.

### Complexity
- **Classification**: Moderate
- **Rationale**: While the search functionality is straightforward, the requirement to filter results based on qualifications such as location, network, specialty, and role/privileges adds complexity.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server must support the Practitioner resource and the specified search parameters.
- **Data Setup**:
  - Practitioner resources with varying names, locations, networks, specialties, and roles/privileges must be pre-loaded into the system.
  - Location resources associated with practitioners must be available.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**:
  - Practitioner resources with diverse `name`, `location`, `network`, `specialty`, and `role/privileges` attributes.
  - Location resources linked to practitioners.
- **Expected Outputs**:
  - A list of Practitioner resources matching the search criteria (e.g., name "Joe Smith") and filtered by the specified qualifications.

### Required FHIR Operations
- **Search Operation**:
  - `GET [base]/Practitioner?name=Joe%20Smith`
  - Additional search queries to test filtering:
    - `GET [base]/Practitioner?name=Joe%20Smith&location=[location-id]`
    - `GET [base]/Practitioner?name=Joe%20Smith&network=[network-id]`
    - `GET [base]/Practitioner?name=Joe%20Smith&specialty=[specialty-id]`
    - `GET [base]/Practitioner?name=Joe%20Smith&role=[role-id]`

### Validation Criteria
- **Search Results**:
  - Verify that the search results include only practitioners with the name "Joe Smith".
- **Filtering**:
  - Confirm that additional filters (location, network, specialty, role/privileges) correctly narrow down the search results.
- **Response Format**:
  - Ensure the response is a valid FHIR Bundle with Practitioner resources.
- **Performance**:
  - Validate that the search operation completes within an acceptable time frame.
- **Error Handling**:
  - Check that appropriate error messages are returned for invalid search parameters or when no results are found.
```


---

<a id='req-34'></a>

### REQ-34: Organization search by name

**Description**: "The Plan-Net design is based around the following types of searches: Organization by Name - Example: Montgomery Cardiology or CVS - Focal Resource and Field: Organization.name - Qualifications of Search: Location, network, specialty."

**Actor**: Server

**Conformance**: None (Design requirement)

```markdown
# Test Specification for REQ-34: Organization Search by Name

## 1. Requirement ID
- **REQ-34**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies a clear search operation (Organization by Name) that can be tested using FHIR search parameters.

### Complexity
- **Classification**: Simple
- **Rationale**: The search operation involves a single parameter (`name`) and is supported by the Capability Statement.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server must support the `Organization` resource and the `name` search parameter as per the Capability Statement.
- **Data Setup**:
  - Ensure the FHIR server contains `Organization` resources with diverse `name` values, including examples like "Montgomery Cardiology" and "CVS".

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - `Organization` resources with varying `name` attributes.
- **Search Parameter**: 
  - `name` (string)

### Expected Outputs
- **Successful Search Results**: 
  - A list of `Organization` resources that match the search criteria by `name`.

### Required FHIR Operations
- **Search Operation**: 
  - HTTP GET request to `[base]/Organization?name=[search-string]`
  - Example: `[base]/Organization?name=Montgomery Cardiology`

### Validation Criteria
- **Response Code**: 
  - The server must return a 200 HTTP status code.
- **Content Verification**: 
  - The response should include `Organization` resources where the `name` field matches the search string.
  - Verify that the returned `Organization` resources contain the expected `name` values (e.g., "Montgomery Cardiology" or "CVS").
- **Conformance to Capability Statement**: 
  - Ensure the server supports the `name` search parameter as indicated in the Capability Statement.
- **Edge Cases**:
  - Test with partial matches and case sensitivity (e.g., "montgomery cardiology" vs "Montgomery Cardiology").
  - Test with no matching results to ensure the server handles such cases gracefully.

### Additional Considerations
- **Performance**: 
  - Measure response times to ensure they meet acceptable thresholds for search operations.
- **Security**: 
  - Verify that the search operation adheres to any security protocols or authentication requirements.
```


---

<a id='req-35'></a>

### REQ-35: Provider search by specialty

**Description**: "The Plan-Net design is based around the following types of searches: Provider by Specialty - Example: Cardiologist - Focal Resource and Field: PractitionerRole.specialty - Qualifications of Search: Location, network, name."

**Actor**: Server

**Conformance**: None (Design requirement)

```markdown
# Test Specification for REQ-35: Provider Search by Specialty

## 1. Requirement ID
- **REQ-35**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies a search functionality that can be tested by executing search queries and verifying the results against expected outcomes.

### Complexity
- **Complexity Level**: Moderate
- **Rationale**: The search involves multiple parameters (specialty, location, network, name) and requires validation of the search results against these criteria.

### Prerequisites
- **System Configurations**: 
  - FHIR server must be operational and accessible.
  - The server must support the PractitionerRole resource and the required search parameters as per the Capability Statement.
- **Data Setup**: 
  - Test data must include PractitionerRole resources with various specialties, locations, networks, and names.
  - Ensure there are practitioners with the specialty "Cardiologist" and associated location and network data.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - PractitionerRole resources with the specialty "Cardiologist".
  - Location and network data associated with the practitioners.
- **Expected Outputs**: 
  - A list of PractitionerRole resources filtered by the specialty "Cardiologist" and optionally by location, network, and name.

### Required FHIR Operations
- **API Calls**:
  - `GET [base]/PractitionerRole?specialty=[specialty-code]`: To search for practitioners by specialty.
  - Optionally include parameters for location, network, and name as needed.

### Validation Criteria
- **Conformance Checks**:
  - Verify that the search results include only PractitionerRole resources with the specified specialty "Cardiologist".
  - If additional parameters (location, network, name) are used, ensure the results match these criteria.
  - Check that the server responds with a valid FHIR Bundle containing the expected resources.
  - Validate that the search operation conforms to the FHIR search parameter requirements as specified in the Capability Statement.
- **Assertions**:
  - The response status code should be `200 OK`.
  - The response should contain a `Bundle` resource with entries matching the search criteria.
  - Each entry in the response should have a `PractitionerRole.specialty` field that matches the specified specialty code for "Cardiologist".
```


---

<a id='req-36'></a>

### REQ-36: Organization search by specialty

**Description**: "The Plan-Net design is based around the following types of searches: Organization by specialty - Example: Compounding Pharmacy - Focal Resource and Field: OrganizationAffiliation.specialty - Qualifications of Search: Location, network, name."

**Actor**: Server

**Conformance**: None (Design requirement)

```markdown
# Test Specification for REQ-36: Organization Search by Specialty

## 1. Requirement ID
- **REQ-36**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies a search capability that can be tested by executing a search query and verifying the results against expected criteria.

### Complexity
- **Complexity Level**: Moderate
- **Rationale**: The test involves multiple search parameters and requires validation of the results based on the specialty and other qualifiers.

### Prerequisites
- **System Configurations**: 
  - FHIR server must be operational and accessible.
  - The server must support the Organization, Location, and OrganizationAffiliation resources as per the Capability Statement.
- **Data Setup**:
  - Test data must include Organizations with various specialties, including at least one "Compounding Pharmacy".
  - OrganizationAffiliation resources must link these Organizations with their specialties.
  - Locations and networks should be defined for these Organizations.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**:
  - `Organization`
  - `OrganizationAffiliation`
  - `Location`
- **Search Parameters**:
  - `OrganizationAffiliation.specialty` with value "Compounding Pharmacy"
  - Optional qualifiers: `Location`, `network`, `name`

### Required FHIR Operations
- **API Calls**:
  - `GET [base]/OrganizationAffiliation?specialty=Compounding Pharmacy`
  - Optionally include qualifiers: `&location=[location_id]`, `&network=[network_id]`, `&name=[organization_name]`

### Validation Criteria
- **Conformance Checks**:
  - Verify that the search returns Organizations with the specified specialty "Compounding Pharmacy".
  - Validate that each returned OrganizationAffiliation resource includes the `specialty` field with the correct value.
  - If qualifiers are used, ensure the results are filtered accordingly:
    - **Location**: Check that the returned Organizations are associated with the specified Location.
    - **Network**: Verify that the Organizations belong to the specified network.
    - **Name**: Confirm that the Organization names match the specified name filter.
- **Assertions**:
  - The response should have a status code of 200 (OK).
  - The response body should contain a list of OrganizationAffiliation resources.
  - Each resource should include a valid reference to an Organization with the specified specialty.
  - The total number of returned resources should match the expected count based on the test data setup.

```


---

<a id='req-37'></a>

### REQ-37: Search for active practitioners and organizations

**Description**: "Sample query to search for currently active Practitioners (replace date in query with current date): http://davinci-plan-net-ri.logicahealth.org/fhir/PractitionerRole?_include=PractitionerRole:date=ge2021-10-25. Sample query to search for currently active Organizations (replace date in query with current date): http://davinci-plan-net-ri.logicahealth.org/fhir/OrganizationAffiliation?_include=OrganizationAffiliation:date=ge2021-10-25."

**Actor**: Server

**Conformance**: None (Implementation example)

```markdown
# Test Specification for Requirement REQ-37

## 1. Requirement ID
- **REQ-37**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement involves executing specific FHIR search queries and verifying the results, which can be automated.

### Complexity
- **Complexity Level**: Moderate
- **Rationale**: The test involves multiple resources and search parameters, requiring validation of both query execution and response content.

### Prerequisites
- **System Configurations**: 
  - Access to a FHIR server implementing the Da Vinci Plan Net Implementation Guide.
  - Ensure the server supports the necessary search parameters as per the Capability Statement.

- **Data Setup**:
  - Populate the FHIR server with sample PractitionerRole and OrganizationAffiliation resources that include active practitioners and organizations with appropriate dates.
  - Ensure that the resources have dates that allow for testing of the "active" status based on the current date.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: 
  - PractitionerRole
  - OrganizationAffiliation

- **Expected Outputs**:
  - A list of PractitionerRole resources where the practitioner is active as of the current date.
  - A list of OrganizationAffiliation resources where the organization is active as of the current date.

### Required FHIR Operations
- **API Calls**:
  - Search for active practitioners:
    ```
    GET /PractitionerRole?_include=PractitionerRole:date=ge<current-date>
    ```
  - Search for active organizations:
    ```
    GET /OrganizationAffiliation?_include=OrganizationAffiliation:date=ge<current-date>
    ```

### Validation Criteria
- **Response Validation**:
  - Ensure the HTTP status code is 200 (OK) for both queries.
  - Verify that the returned resources are not empty and contain the expected number of entries.
  - Check that each PractitionerRole resource returned has a date indicating activity on or after the current date.
  - Check that each OrganizationAffiliation resource returned has a date indicating activity on or after the current date.

- **Assertions**:
  - Assert that all returned PractitionerRole resources have a valid practitioner reference.
  - Assert that all returned OrganizationAffiliation resources have a valid organization reference.
  - Validate that the search parameters used are supported as per the Capability Statement.

- **Edge Cases**:
  - Test with no active practitioners or organizations to ensure the system returns an empty result set appropriately.
  - Test with boundary dates to ensure the system correctly includes or excludes resources based on the date.

```

This test specification outlines a structured approach to verify the implementation of the requirement to search for active practitioners and organizations using FHIR resources. It includes detailed steps and criteria for validating the system's conformance to the requirement.

---

<a id='req-38'></a>

### REQ-38: Network contact handling for departments

**Description**: "When the contact is a department name, rather than a human (e.g., patient help line), include a blank family and given name, and provide the department name in contact.name.text."

**Actor**: Server

**Conformance**: None (Implementation guidance)

```markdown
# Test Specification for REQ-38: Network Contact Handling for Departments

## 1. Requirement ID
- **REQ-38**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
  - The requirement specifies clear conditions for how the contact information should be structured when dealing with department names.

### Complexity
- **Complexity**: Simple
  - The requirement involves straightforward validation of the contact name fields in the FHIR resource.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server must support the `ContactPoint` and `Organization` resources as per the Capability Statement.

- **Data Setup**:
  - At least one `Organization` resource with a contact that represents a department (e.g., patient help line) should be available.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**:
  - `Organization` resource with a contact entry where the contact is a department.

- **Expected Outputs**:
  - The `Organization` resource should have the `contact.name.text` populated with the department name.
  - The `contact.name.family` and `contact.name.given` fields should be empty.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Organization/[id]`: Retrieve the `Organization` resource to inspect the contact details.

### Validation Criteria
- **Specific Checks**:
  1. **Check Contact Name Text**:
     - Verify that `contact.name.text` is populated with the department name (e.g., "Patient Help Line").

  2. **Check Family and Given Names**:
     - Verify that `contact.name.family` is empty.
     - Verify that `contact.name.given` is empty.

- **Assertions**:
  - The test passes if the `Organization` resource's contact details conform to the specified structure:
    - `contact.name.text` is not empty and contains the department name.
    - `contact.name.family` and `contact.name.given` are both empty.

- **Inspection Method**:
  - Manually inspect the retrieved `Organization` resource or use automated scripts to validate the fields as per the criteria above.
```


---

<a id='req-39'></a>

### REQ-39: Organization contact handling for departments

**Description**: "When the contact is a department name, rather than a human (e.g., patient help line), include a blank family and given name, and provide the department name in contact.name.text."

**Actor**: Server

**Conformance**: None (Implementation guidance)

```markdown
# Test Specification for Requirement REQ-39

## 1. Requirement ID
- **REQ-39**: Organization contact handling for departments

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Rationale**: The requirement specifies a clear condition for the structure of the `Organization.contact` element when representing a department, which can be programmatically verified.

### Complexity
- **Complexity Level**: Simple
- **Rationale**: The requirement involves straightforward validation of the `Organization.contact` structure for specific fields.

### Prerequisites
- **System Configurations**: The FHIR server must be operational and accessible with the capability to store and retrieve `Organization` resources.
- **Data Setup**: At least one `Organization` resource with a contact representing a department must be present in the system for testing.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**: `Organization` resource with a `contact` element where the contact is a department.
- **Expected Outputs**: 
  - The `contact.name.family` and `contact.name.given` fields should be blank.
  - The `contact.name.text` field should contain the department name.

### Required FHIR Operations
- **Search Operation**: Use the `name` search parameter to retrieve `Organization` resources by department name.
  - Example: `GET [base]/Organization?name=[department_name]`
- **Read Operation**: Retrieve specific `Organization` resources by ID.
  - Example: `GET [base]/Organization/[id]`

### Validation Criteria
- **Check 1**: Verify that the `contact.name.family` field is blank.
- **Check 2**: Verify that the `contact.name.given` field is blank.
- **Check 3**: Verify that the `contact.name.text` field contains the department name.
- **Pass Criteria**: All checks must be satisfied for the test to pass, indicating that the `Organization` resource correctly represents a department contact as per the requirement.

### Additional Notes
- Ensure that the FHIR server supports the required search and read operations as specified in the Capability Statement.
- The test should be repeated for multiple `Organization` resources to ensure consistent handling of department contacts.
```


---

<a id='req-40'></a>

### REQ-40: Practitioner qualification coding

**Description**: "When the value set for the coded concept in qualification is insufficient, the qualification can be provided in the text field of the codeableConcept."

**Actor**: Server

**Conformance**: None (Implementation guidance)

```markdown
# Test Specification for REQ-40: Practitioner Qualification Coding

## 1. Requirement ID
- **REQ-40**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Attestation
  - This requirement is primarily guidance on how to handle situations where the coded concept is insufficient. It is best verified through inspection of documentation or manual review rather than automated testing.

### Complexity
- **Complexity**: Moderate
  - While the requirement itself is straightforward, verifying that the text field is used appropriately when the coded concept is insufficient requires a nuanced understanding of the context and the data.

### Prerequisites
- **System Configurations**: 
  - A FHIR server capable of storing and retrieving Practitioner resources.
- **Data Setup**: 
  - Practitioner resources with qualifications where the coded concept is insufficient, necessitating the use of the text field.

## 3. Test Implementation Strategy

### Required Inputs
- **FHIR Resources**:
  - Practitioner resources with qualifications.
- **Expected Outputs**:
  - Practitioner resources where the qualification text field is populated when the coded concept is insufficient.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Practitioner?_id=[id]`: Retrieve specific Practitioner resources using their unique identifier.
  - `GET [base]/Practitioner?name=[name]`: Search for Practitioner resources by name.
  - `GET [base]/Practitioner?family=[family]`: Search for Practitioner resources by family name.
  - `GET [base]/Practitioner?given=[given]`: Search for Practitioner resources by given name.

### Validation Criteria
- **Specific Checks**:
  - Verify that the Practitioner resource's qualification element includes a text field populated with a meaningful description when the coded concept is insufficient.
  - Ensure that the qualification coding is present and correctly structured according to FHIR standards.
  - Confirm that the text field is used only when necessary, i.e., when the coded concept does not fully capture the qualification.
  - Inspect the Practitioner resource to ensure that all mandatory fields are populated and valid.

- **Assertions**:
  - The text field in the qualification element should not be empty if the coded concept is insufficient.
  - The qualification element should include both a code and a text field when applicable.
  - The Practitioner resource should be retrievable using supported search parameters as outlined in the Capability Statement.

By following this test specification, the implementation of REQ-40 can be verified through a combination of manual inspection and validation of resource data against expected criteria.
```

---



