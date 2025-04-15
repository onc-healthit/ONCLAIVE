# Consolidated Test Plan for Plan Net

## Generated on: 2025-04-09 12:27:41

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

# Test Specification for Requirement REQ-02

## 1. Requirement ID
**REQ-02**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Manual
  - **Rationale**: The requirement involves ensuring that no personally identifiable information (PII) is sent by clients, which requires inspection of the data payloads sent during API requests. This is best verified through manual inspection or using tools that can simulate and capture API requests for review.

### Complexity
- **Classification**: Moderate
  - **Rationale**: While the task of checking for PII in outgoing requests is straightforward, the complexity arises from the need to understand what constitutes PII and ensuring that all potential data fields are checked.

### Prerequisites
- **System Configurations**: Access to the directory mobile application and the Plan-Net service environment.
- **Data/Setup**: 
  - A configured test environment where the mobile application can interact with the Plan-Net service.
  - Access to network monitoring tools or logging mechanisms to capture outgoing requests from the client.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A series of API requests initiated by the directory mobile application to the Plan-Net service.
- **Expected Outputs**: 
  - API requests should not contain any consumer identifiable information such as names, addresses, phone numbers, social security numbers, or any other data that can be used to identify an individual.

### Required FHIR Operations
- **FHIR Operations**: 
  - `GET` operations for querying Plan-Net service endpoints.
  - Ensure that these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**: 
  - Simulated user profiles without PII.
  - Test scenarios that mimic real-world usage of the mobile application querying the Plan-Net service.

### Validation Criteria
- **Specific Checks**:
  - Capture the API request payloads sent by the client.
  - Manually inspect the payloads to ensure no fields contain PII.
  - Verify that all requests adhere to the expected data structure as defined by the Plan-Net service.
  - Assertions:
    - The request payload does not include any fields that can be classified as PII.
    - The request headers and parameters do not contain PII.
    - The payload adheres to the expected schema without deviations that might include PII.

By following this test specification, testers can effectively verify that the directory mobile application complies with the requirement to avoid sending PII when querying the Plan-Net service.

---

<a id='req-06'></a>

### REQ-06: Client handling of Must Support data elements

**Description**: "Application actors SHALL be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."

**Actor**: Client

**Conformance**: SHALL

```markdown
# Test Specification for REQ-06: Client Handling of Must Support Data Elements

## 1. Requirement ID
- **REQ-06**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement can be tested using automated test scripts that simulate client interactions with FHIR resources containing Must Support data elements.

### Complexity
- **Complexity**: Moderate
  - The complexity is moderate due to the need to handle various resource types and ensure the client processes Must Support elements correctly without errors.

### Prerequisites
- **System Configurations**: 
  - The client application must be configured to interact with a FHIR server that supports the relevant resources and Must Support elements.
- **Data Setup**: 
  - Access to a FHIR server with pre-loaded resources containing Must Support data elements.
- **Environment**: 
  - A test environment where the client application can be executed and monitored for errors.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - FHIR resource instances containing Must Support data elements (e.g., Patient, Observation).
- **Expected Outputs**: 
  - The client processes the resources without errors or application failures.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [resource]`: Retrieve resources from the FHIR server to test client processing.
  - `POST [resource]`: Optionally, create resources to verify the client's ability to handle Must Support elements during creation.

### Test Data Requirements
- **Test Data**:
  - Resource instances with Must Support elements populated, including edge cases such as:
    - Missing optional elements
    - Various data types (e.g., strings, dates, codes)
    - Boundary values for numerical data

### Validation Criteria
- **Specific Checks**:
  - The client application should not produce any errors or exceptions when processing resources with Must Support elements.
  - Log files or output should indicate successful processing of Must Support elements.
  - Verify that the client correctly displays or utilizes the Must Support data elements in its user interface or internal processing logic.
  - Ensure no application crashes or unexpected behavior occurs during the processing of these resources.

- **Assertions**:
  - Confirm the absence of error messages related to Must Support elements in client logs.
  - Validate that the client maintains expected functionality and performance when handling these elements.
```


---

<a id='req-07'></a>

### REQ-07: Client display of data elements

**Description**: "Application actors SHOULD be capable of displaying the data elements for human use or storing the information for other purposes."

**Actor**: Client

**Conformance**: SHOULD

```markdown
# Test Specification for Requirement REQ-07

## 1. Requirement ID
- **REQ-07**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Manual
  - The requirement involves visual inspection of data display, which is inherently a manual process.

### Complexity
- **Complexity Level**: Moderate
  - While displaying data is a straightforward task, ensuring that all relevant data elements are correctly displayed or stored for other purposes can involve multiple data types and formats.

### Prerequisites
- **System Configurations**: 
  - The client application must be installed and configured to connect to the FHIR server.
  - User interface components for data display must be operational.
- **Data Setup**: 
  - Access to a FHIR server with sample data that includes a variety of data elements.
  - User credentials with appropriate permissions to access the data.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A set of FHIR resources (e.g., Patient, Observation, Condition) containing diverse data elements.
- **Expected Outputs**: 
  - Visual confirmation that the client application displays the data elements correctly for human use.
  - Verification that the application can store the information for other purposes if required.

### Required FHIR Operations
- **FHIR Operations**:
  - `GET [base]/Patient/{id}`
  - `GET [base]/Observation/{id}`
  - `GET [base]/Condition/{id}`
  - These operations must be supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - A diverse set of FHIR resources with varying data elements, including:
    - Patient demographics
    - Vital signs and laboratory results (Observation)
    - Diagnoses and conditions (Condition)
  - Ensure data includes edge cases such as missing or null values.

### Validation Criteria
- **Conformance Checks**:
  - **Display Verification**: Confirm that all relevant data elements from the FHIR resources are displayed on the client interface.
  - **Storage Verification**: If applicable, verify that the application can store the data elements for other purposes, such as logging or further processing.
  - **User Interface Checks**: Ensure that the data is presented in a user-friendly and accessible manner.
  - **Error Handling**: Verify that the application handles any missing or null data elements gracefully without crashing or displaying errors.
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
- **Classification**: Manual
  - The requirement involves interpretation by the client application, which typically requires human inspection to verify correct behavior.

### Complexity
- **Complexity**: Moderate
  - The requirement involves understanding the behavior of client applications in response to missing data, which requires careful setup and inspection.

### Prerequisites
- **System Configurations**: 
  - Access to a Health Plan API that supports the relevant FHIR resources and operations.
  - A client application capable of querying the Health Plan API.
- **Data Setup**:
  - Ensure that the Health Plan API actor has resources with missing Must Support data elements.
  - Configure the client application to query these resources.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A set of FHIR resource instances from the Health Plan API with missing Must Support data elements.
  - A client application configured to query these resources.
- **Expected Outputs**:
  - The client application should interpret the missing Must Support data elements as data not present in the Health Plan API actor's system.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resourceType]?[parameters]` to query resources from the Health Plan API.
  - Ensure that these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - FHIR resources (e.g., Coverage, Claim) with intentionally omitted Must Support elements.
  - Example: A Coverage resource without a `subscriberId` if `subscriberId` is marked as Must Support.

### Validation Criteria
- **Validation Checks**:
  - Verify that the client application does not throw errors or exceptions when encountering resources with missing Must Support elements.
  - Confirm that the client application logs or displays a message indicating that the data is not present in the Health Plan API actor's system.
  - Ensure that the client application continues to function correctly and processes other available data elements.

- **Assertions**:
  - The client application should not attempt to infer or fabricate missing data.
  - The client application should handle the absence of Must Support data gracefully, without disrupting the user experience or data processing workflow.
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
- **Classification**: Automatic
  - The requirement involves processing data elements that assert missing information, which can be programmatically verified by checking the presence and handling of specific indicators in the data.

### Complexity
- **Complexity**: Moderate
  - The complexity arises from the need to correctly interpret and process "Must Support" data elements that indicate missing information, which may vary across different resource types.

### Prerequisites
- **System Configurations**: 
  - The Consumer App must be configured to connect to a FHIR server that supports the relevant resources and operations.
- **Data Setup**:
  - The FHIR server must contain resource instances with "Must Support" data elements that assert missing information.
- **Environment**:
  - Access to a test environment where the Consumer App can interact with the FHIR server.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Resource instances from the FHIR server containing "Must Support" data elements with missing information indicators (e.g., `dataAbsentReason`).
- **Expected Outputs**:
  - The Consumer App should correctly interpret and handle these indicators, potentially logging or displaying a message indicating the presence of missing information.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[ResourceType]` to retrieve resource instances with missing information indicators.
  - Ensure that the Capability Statement indicates support for `GET` operations on the relevant resource types.

### Test Data Requirements
- **Type of Test Data**:
  - Resource instances (e.g., Patient, Observation) with "Must Support" elements that include missing information indicators such as `dataAbsentReason`.

### Validation Criteria
- **Specific Checks**:
  - Verify that the Consumer App retrieves resource instances with missing information indicators.
  - Confirm that the app processes these indicators correctly by:
    - Logging an appropriate message or displaying a user notification.
    - Ensuring no application errors occur during processing.
  - Assertions:
    - The presence of a log entry or user notification for each resource instance with missing information.
    - No exceptions or errors in the application logs related to processing these indicators.

```
This test specification outlines a structured approach to verify that Consumer App actors can process resource instances with missing information indicators, as required by the FHIR Implementation Guide. The strategy includes automated testing with specific inputs, operations, and validation criteria to ensure compliance.

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
- **Classification**: Manual
  - The requirement involves inspecting the behavior of the client application in response to directory updates, which typically requires manual verification of the application's response to changes in data.

### Complexity
- **Complexity Level**: Moderate
  - While the concept of using the `_lastUpdated` search parameter is straightforward, ensuring comprehensive coverage across different scenarios (e.g., additions, modifications, and deletions) adds complexity.

### Prerequisites
- **System Configurations**: 
  - Access to a FHIR server that supports the `_lastUpdated` search parameter.
  - A client application capable of caching query results and performing subsequent queries using `_lastUpdated`.

- **Data Setup**:
  - Initial dataset in the directory that can be queried and cached by the client.
  - Ability to simulate or perform updates (additions, modifications) to the directory content.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Initial query results cached by the client.
  - Subsequent directory updates (additions, modifications).

- **Expected Outputs**:
  - Client should correctly identify and retrieve only the updated or newly added entries based on the `_lastUpdated` parameter.

### Required FHIR Operations
- **Search Operation**: 
  - `GET [base]/[resource]?_lastUpdated=[date]`
  - Ensure the FHIR server supports this operation as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - A set of directory entries with known `lastUpdated` timestamps.
  - Entries to be added or modified with updated `lastUpdated` timestamps.

### Validation Criteria
- **Specific Checks**:
  - Verify that the client caches the initial query results correctly.
  - Confirm that the client performs a subsequent query using the `_lastUpdated` parameter.
  - Ensure that the client retrieves only the entries that have been added or modified since the last query.
  - Validate that the client correctly updates its cache with the new or modified entries.
  - Check for any errors or exceptions during the query process and ensure they are handled gracefully.

- **Assertions**:
  - The client should not retrieve entries that have not been updated since the last query.
  - The client should accurately reflect the current state of the directory after processing updates.

By following this test specification, testers can ensure that client applications correctly track and update their cached directory content in response to changes, as guided by the FHIR Implementation Guide requirement REQ-31.
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
# Test Specification for REQ-01: No PII Requirement for Directory Queries

## 1. Requirement ID
- **REQ-01**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Manual
  - **Rationale**: The requirement involves verifying that no consumer identifying information is required, which is best assessed through inspection of API request and response logs, and possibly server-side configurations.

### Complexity
- **Complexity**: Simple
  - **Rationale**: The requirement is straightforward, focusing on the absence of PII in directory queries.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to handle directory queries.
- **Data Setup**:
  - Ensure the directory service is populated with test data that can be queried.
- **Access**:
  - Access to API request/response logs or server configuration files to verify the absence of PII requirements.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A directory query request from a mobile application that does not include any consumer identifying information.
- **Expected Outputs**:
  - The server processes the query and returns the appropriate directory content without requiring any consumer identifying information.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Practitioner`
  - `GET [base]/Organization`
  - `GET [base]/Location`
  - `GET [base]/HealthcareService`
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - Directory entries for practitioners, organizations, locations, and healthcare services that can be queried.
  - Ensure the test data does not include any consumer identifying information.

### Validation Criteria
- **Specific Checks**:
  - **Assertion 1**: Verify that the directory query request does not include any fields that could contain consumer identifying information.
  - **Assertion 2**: Confirm through inspection that the server does not reject the query due to missing consumer identifying information.
  - **Assertion 3**: Ensure the server returns valid directory content in response to the query.
  - **Assertion 4**: Review server-side logs or configurations to confirm no PII is required for processing directory queries.

- **Result Indication**:
  - The test passes if all assertions are met, indicating that the server conforms to the requirement by not requiring consumer identifying information for directory queries.
```


---

<a id='req-03'></a>

### REQ-03: Population of Must Support data elements

**Description**: "Health Plan API actors SHALL be capable of populating all Must Support data elements as part of the query results."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for Requirement REQ-03

## 1. Requirement ID
**REQ-03**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement can be tested using automated scripts that query the server and validate the presence of Must Support data elements in the response.

### Complexity
- **Level**: Moderate
  - While the requirement involves straightforward validation of data elements, the variability in data types and potential volume of data necessitates careful test design.

### Prerequisites
- **System Configurations**: 
  - The Health Plan API server must be deployed and accessible.
  - The server must support the necessary FHIR operations as outlined in the Capability Statement.
- **Data Setup**: 
  - The server must have a dataset that includes all Must Support data elements populated for testing purposes.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - FHIR queries targeting resources that include Must Support data elements.
- **Expected Outputs**: 
  - Responses from the server must include all Must Support data elements populated as specified in the FHIR profiles.

### Required FHIR Operations
- **Supported Operations**:
  - `GET [base]/[resource]?[parameters]` - To retrieve resources and check for Must Support elements.
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Data Types**:
  - A comprehensive dataset that includes instances of each resource type with Must Support data elements populated.
  - Test data should cover different scenarios, including edge cases for each Must Support element.

### Validation Criteria
- **Specific Checks**:
  - Verify that each Must Support data element is present in the response for each queried resource.
  - Validate the correctness of the data format and values for Must Support elements.
  - Assertions should include:
    - Presence of Must Support elements in the response.
    - Correctness of data types and cardinality as per the FHIR profile.
    - Conformance to any value set bindings or constraints specified for Must Support elements.

- **Result Indication**:
  - A test passes if all Must Support data elements are present and correctly populated in the response.
  - A test fails if any Must Support element is missing or incorrectly populated.

```
This structured test specification provides a clear framework for verifying the conformance of a Health Plan API server to the requirement of populating Must Support data elements, ensuring interoperability and data completeness in healthcare applications.

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
- **Classification**: Manual
  - **Rationale**: The requirement involves inspecting the absence of data elements in the returned resource instances, which is best verified through manual inspection of the API response.

### Complexity
- **Complexity Level**: Moderate
  - **Rationale**: While the requirement is straightforward, ensuring that all Must Support elements with a minimum cardinality of 0 are correctly omitted when absent requires careful inspection across various resource types.

### Prerequisites
- **System Configurations**: 
  - The Health Plan API server must be operational and accessible.
  - The server should have implemented the capability to conditionally exclude absent data elements.
- **Data Setup**: 
  - Ensure that the server has resources with Must Support elements that have a minimum cardinality of 0.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A query request to the Health Plan API for resources that include Must Support data elements with a minimum cardinality of 0.
- **Expected Outputs**: 
  - The response should not include the Must Support data elements that are absent and have a minimum cardinality of 0.

### Required FHIR Operations
- **API Calls/Operations**:
  - Use the `GET` operation to retrieve resources from the Health Plan API.
  - Ensure that the API supports search and retrieval operations as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - Resources that include Must Support data elements with a minimum cardinality of 0.
  - Test cases should cover a variety of resources to ensure comprehensive testing.

### Validation Criteria
- **Specific Checks**:
  - Verify that the response does not include any Must Support data elements that are absent and have a minimum cardinality of 0.
  - Confirm that the response adheres to the FHIR resource structure and does not contain empty or null fields for these elements.
- **Assertions**:
  - Assert that the absence of data elements is consistent with the requirement.
  - Validate that the server's behavior aligns with the SHALL NOT conformance requirement.

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
- **Classification**: Manual
  - **Rationale**: Verification by inspection implies a manual review process to ensure that the dataAbsentReason is correctly applied in scenarios where mandatory data is missing.

### Complexity
- **Classification**: Moderate
  - **Rationale**: While the concept of using dataAbsentReason is straightforward, ensuring its correct application across all relevant data elements with minimum cardinality >0 adds complexity.

### Prerequisites
- **System Configurations**: The FHIR server must support the dataAbsentReason extension.
- **Data Setup**: A dataset with missing required information for elements with minimum cardinality >0.
- **Capability Statement**: The server's Capability Statement must include support for the dataAbsentReason extension.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A FHIR resource instance with missing required data elements that have a minimum cardinality >0.
- **Expected Outputs**: 
  - The resource instance should include the dataAbsentReason extension or a suitable nullFlavor from the value set.

### Required FHIR Operations
- **API Calls**:
  - `GET` operation to retrieve a FHIR resource instance for inspection.
  - `POST` or `PUT` operation to submit a resource with missing data elements to verify server response.

### Test Data Requirements
- **Test Data**: 
  - A sample FHIR resource (e.g., Patient, Observation) with intentionally missing required fields.
  - Ensure that these fields have a minimum cardinality >0 and are annotated with dataAbsentReason.

### Validation Criteria
- **Specific Checks**:
  - Verify that for each missing required data element with minimum cardinality >0, the dataAbsentReason extension is present.
  - Confirm that the value of dataAbsentReason is from the specified value set (e.g., nullFlavors).
  - Ensure that the server's response includes the dataAbsentReason extension when queried.
- **Assertions**:
  - Assert that all required fields with missing data have a corresponding dataAbsentReason.
  - Assert that the server does not return an error for missing data when dataAbsentReason is correctly applied.

```


---

<a id='req-10'></a>

### REQ-10: JSON format support

**Description**: "Support json source formats for all Plan-Net interactions."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for Requirement REQ-10

## 1. Requirement ID
- **REQ-10**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement can be tested automatically by sending requests and verifying responses in JSON format.

### Complexity
- **Complexity Level**: Simple
  - The requirement involves verifying JSON format support, which is straightforward given the standard nature of JSON parsing and validation.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to handle HTTP requests and responses.
  - Ensure that the server is operational and accessible over the network.
- **Data Setup**: 
  - Access to a test environment where Plan-Net interactions can be executed.
  - Ensure that the server has Plan-Net resources available for interaction.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A set of HTTP requests targeting Plan-Net interactions (e.g., search, read, create) formatted in JSON.
- **Expected Outputs**: 
  - HTTP responses with a status code indicating success (e.g., 200 OK for read/search, 201 Created for create).
  - Response bodies should be in valid JSON format and conform to the expected FHIR resource structure.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/PlanDefinition` for search interactions
  - `GET [base]/PlanDefinition/[id]` for read interactions
  - `POST [base]/PlanDefinition` for create interactions
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - Sample PlanDefinition resources in JSON format for testing read and create operations.
  - Query parameters for testing search operations.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server accepts requests with `Content-Type: application/json` and `Accept: application/json` headers.
  - Confirm that the server returns responses with `Content-Type: application/json`.
  - Validate that the JSON response body is correctly formatted and contains all expected fields as per the FHIR PlanDefinition resource specification.
  - Check for correct HTTP status codes in the response.
  - Ensure that the server handles invalid JSON gracefully, returning appropriate error messages and status codes (e.g., 400 Bad Request).

```


---

<a id='req-11'></a>

### REQ-11: RESTful behavior implementation

**Description**: "Implement the RESTful behavior according to the FHIR specification."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for FHIR Implementation Guide Requirement

## 1. Requirement ID
- **REQ-11**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Hybrid
  - **Reasoning**: While some aspects of RESTful behavior can be automatically tested (e.g., response codes, headers), others may require manual inspection (e.g., correct implementation of business logic).

### Complexity
- **Classification**: Moderate
  - **Reasoning**: Implementing RESTful behavior involves multiple aspects such as correct HTTP methods, response codes, and adherence to FHIR resource operations. This requires a comprehensive understanding of the FHIR RESTful API.

### Prerequisites
- **System Configurations**: 
  - A FHIR server instance configured to handle RESTful operations.
  - Network access to the server for testing purposes.
- **Data Setup**:
  - Pre-existing FHIR resources on the server to test read, update, and delete operations.
  - User credentials with appropriate permissions for testing secured endpoints.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - HTTP requests for each FHIR RESTful operation (GET, POST, PUT, DELETE).
  - Valid FHIR resource identifiers for testing resource-specific operations.
- **Expected Outputs**:
  - Correct HTTP response codes (e.g., 200, 201, 204, 400, 404).
  - Valid FHIR resource representations in the response body for read operations.
  - Appropriate response headers (e.g., Content-Type, Location).

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resourceType]`
  - `POST [base]/[resourceType]`
  - `PUT [base]/[resourceType]/[id]`
  - `DELETE [base]/[resourceType]/[id]`
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Type of Test Data**:
  - Sample FHIR resources (e.g., Patient, Observation) in JSON format.
  - Resource identifiers for existing resources on the server.
  - Test data should include both valid and invalid scenarios to test error handling.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server responds with the correct HTTP status codes for each operation.
  - Confirm that the response body contains valid FHIR resources for read operations.
  - Check that the server correctly implements CRUD operations as per FHIR specifications.
  - Validate the presence and correctness of HTTP headers in the responses.
  - Ensure that error conditions (e.g., invalid resource IDs) result in appropriate error responses.

- **Assertions**:
  - Assert that a `GET` request returns a 200 status code and a valid resource.
  - Assert that a `POST` request returns a 201 status code and the Location header.
  - Assert that a `PUT` request returns a 200 or 204 status code.
  - Assert that a `DELETE` request returns a 204 status code.
  - Assert that invalid requests return appropriate error codes (e.g., 400, 404).

This test specification aims to ensure that the FHIR server implements RESTful behavior in accordance with the FHIR specification, as required by REQ-11.
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
- **Classification**: Automatic
  - The requirement can be tested automatically by executing a series of API calls to verify the server's support for all profiles defined in the Implementation Guide.

### Complexity
- **Classification**: Moderate
  - While the test involves multiple profiles, the complexity is moderate as it primarily involves verifying profile support through standard FHIR operations.

### Prerequisites
- **System Configurations**: The server must be running and accessible with all profiles from the Implementation Guide implemented.
- **Data Setup**: Test data conforming to each profile must be available or generated for testing purposes.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A list of all profiles defined in the Implementation Guide.
  - Sample FHIR resources conforming to each profile.
- **Expected Outputs**: 
  - Successful creation, read, update, and delete (CRUD) operations for each profile.
  - Validation of resource instances against the profiles without errors.

### Required FHIR Operations
- **API Calls/Operations**:
  - `POST` to create resources conforming to each profile.
  - `GET` to retrieve resources and verify they conform to the profiles.
  - `PUT` to update resources and ensure they still conform.
  - `DELETE` to remove resources and confirm successful deletion.
  - `CapabilityStatement` to verify the server declares support for each profile.

### Test Data Requirements
- **Type of Test Data**:
  - Valid FHIR resource instances for each profile, ensuring they meet all constraints and extensions defined in the profiles.
  - Invalid resource instances to test the server's ability to reject non-conforming resources.

### Validation Criteria
- **Specific Checks**:
  - **Profile Support Verification**: The server's CapabilityStatement must list each profile under supported profiles.
  - **CRUD Operations**: Each operation (create, read, update, delete) must succeed without errors for valid resources.
  - **Validation Against Profiles**: Resources must validate successfully against their respective profiles using the `$validate` operation.
  - **Error Handling**: The server must return appropriate error messages for invalid resources or unsupported operations.

```


---

<a id='req-13'></a>

### REQ-13: Unauthorized request response

**Description**: "Return the following response classes: (Status 401/4xx): unauthorized request."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for Unauthorized Request Response

## 1. Requirement ID
- **REQ-13**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement can be tested using automated scripts to simulate unauthorized requests and verify the server's response.

### Complexity
- **Classification**: Simple
  - The test involves basic HTTP status code verification and does not require complex logic or multiple steps.

### Prerequisites
- **System Configurations**: 
  - The server must be running and accessible over the network.
  - Ensure that the server's security configurations are set to require authentication for access to protected resources.
- **Data Setup**: 
  - No specific data setup is required as the test focuses on unauthorized access.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - An HTTP request to a protected FHIR resource endpoint without valid authentication credentials.
- **Expected Outputs**: 
  - The server should return an HTTP response with a status code of 401 (Unauthorized) or another 4xx status code indicating unauthorized access.

### Required FHIR Operations
- **API Calls/Operations**: 
  - Perform a GET, POST, PUT, or DELETE operation on a FHIR resource endpoint that requires authentication.
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**: 
  - No specific FHIR resource data is necessary as the test focuses on the server's response to unauthorized requests.

### Validation Criteria
- **Specific Checks**:
  - Verify that the HTTP response status code is 401 or another 4xx code indicating unauthorized access.
  - Check that the response includes appropriate error messages or headers indicating the nature of the unauthorized request.
  - Ensure that no sensitive data is exposed in the response body.

- **Assertions**:
  - Assert that the response status code is 401.
  - Assert that the response contains a `WWW-Authenticate` header if applicable.
  - Assert that the response body does not contain any sensitive information.

By following this test specification, testers can ensure that the server correctly handles unauthorized requests by returning the appropriate HTTP status codes and messages, thus conforming to the requirement REQ-13.
```

---

<a id='req-14'></a>

### REQ-14: Insufficient scope response

**Description**: "Return the following response classes: (Status 403): insufficient scope."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for REQ-14: Insufficient Scope Response

## 1. Requirement ID
- **REQ-14**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - This requirement can be tested automatically by simulating requests with insufficient scope and checking the server's response.

### Complexity
- **Complexity**: Simple
  - The requirement involves verifying a specific HTTP status code response, which is straightforward.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to enforce scope-based access control.
  - An OAuth2 authorization server must be available to issue tokens with varying scopes.
- **Data/Setup**:
  - Test user accounts with different scope permissions.
  - Client application credentials to request tokens from the authorization server.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A valid FHIR API endpoint URL.
  - An access token with insufficient scope for the requested operation.
- **Expected Outputs**:
  - HTTP Status Code: 403
  - Response Body: A FHIR OperationOutcome resource indicating "insufficient scope."

### Required FHIR Operations
- **API Calls**:
  - Any FHIR read, write, or search operation that requires specific scopes as per the Capability Statement.
  - Example: `GET [base]/Patient/[id]` or `POST [base]/Observation`.

### Test Data Requirements
- **Test Data**:
  - Access tokens with varying scopes, including one with insufficient scope for the operation being tested.
  - FHIR resources (e.g., Patient, Observation) that the test will attempt to access or modify.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server returns a 403 HTTP status code.
  - Confirm that the response includes a FHIR OperationOutcome resource.
  - Check that the OperationOutcome contains a suitable error message indicating "insufficient scope."
  - Ensure that no unauthorized data is accessed or modified during the test.

- **Assertions**:
  - Assert that the HTTP status code is 403.
  - Assert that the response body is a valid FHIR OperationOutcome.
  - Assert that the OperationOutcome contains an issue with severity "error" and code "forbidden."

By following this test specification, we can ensure that the server correctly handles requests with insufficient scope by returning the appropriate response.
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
- **Classification**: Automatic
  - The requirement can be tested using automated scripts that simulate invalid parameter requests and verify the server's response.

### Complexity
- **Complexity Level**: Simple
  - The requirement involves verifying a single response status code for invalid parameters, which is straightforward.

### Prerequisites
- **System Configurations**: 
  - The server must be running and accessible via its FHIR API endpoint.
  - The server must support the operations as defined in the Capability Statement.
- **Data or Setup**:
  - No specific data setup is required since the test focuses on invalid parameter handling.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A set of API requests with intentionally invalid parameters.
- **Expected Outputs**: 
  - HTTP Status Code 400 with an error message indicating an invalid parameter.

### Required FHIR Operations
- **API Calls/Operations**:
  - Any FHIR operation that accepts parameters (e.g., `GET [base]/Patient`, `GET [base]/Observation`) can be used to test invalid parameter handling.
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Type of Test Data**:
  - Invalid parameters such as:
    - Non-existent query parameters (e.g., `GET [base]/Patient?unknownParam=value`)
    - Incorrect data types for parameters (e.g., `GET [base]/Patient?_count=invalidNumber`)
    - Malformed parameter values (e.g., `GET [base]/Patient?birthdate=notADate`)

### Validation Criteria
- **Specific Checks**:
  - The server returns an HTTP Status Code 400.
  - The response body includes an OperationOutcome resource with:
    - An issue of type `invalid` or `structure`.
    - A diagnostic message indicating the nature of the invalid parameter.
- **Assertions**:
  - Verify that the status code is exactly 400.
  - Validate the presence and correctness of the OperationOutcome resource in the response.
  - Check that the error message is clear and informative regarding the invalid parameter.

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
- **Classification**: Automatic
  - This requirement can be tested using automated scripts that simulate requests to the server and check for the expected HTTP status codes.

### Complexity
- **Complexity**: Simple
  - The requirement involves checking the server's response to a specific condition (requesting an unknown resource), which is straightforward to implement and verify.

### Prerequisites
- **System Configurations**: 
  - The server must be up and running, accessible via the network.
  - The server should be configured to handle FHIR requests and return appropriate HTTP status codes.
- **Data/Setup**:
  - No specific data setup is required since the test involves requesting a non-existent resource.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A request to the FHIR server for a resource that does not exist (e.g., GET request to `/Patient/unknown-id`).
- **Expected Outputs**:
  - The server should return an HTTP status code of 404 with a message indicating "unknown resource."

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resourceType]/[id]`
    - Example: `GET [base]/Patient/unknown-id`
  - Ensure that the server supports the `GET` operation for resource retrieval as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - No specific test data is required since the test involves accessing a non-existent resource. The focus is on the server's response to this condition.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server responds with an HTTP status code of 404.
  - Check the response body (if applicable) to ensure it contains a message indicating "unknown resource."
  - Confirm that the response conforms to the FHIR standard for error responses, including any OperationOutcome details if provided.
  - Ensure that the response headers are correctly set, particularly `Content-Type` as `application/fhir+json` or `application/fhir+xml` depending on the request.

By following this test specification, the conformance to REQ-16 can be effectively validated, ensuring that the server correctly handles requests for unknown resources.
```

---

<a id='req-17'></a>

### REQ-17: Deleted resource response

**Description**: "Return the following response classes: (Status 410): deleted resource."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for REQ-17: Deleted Resource Response

## 1. Requirement ID
- **REQ-17**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The test can be automated as it involves verifying HTTP response codes from the server.

### Complexity
- **Level**: Simple
  - The test involves a straightforward check of the HTTP status code returned when accessing a deleted resource.

### Prerequisites
- **System Configurations**: 
  - The server must be running and accessible.
  - The server must support the FHIR RESTful API operations as specified in the Capability Statement.
- **Data Setup**:
  - Ensure there is at least one resource that can be deleted.
  - The resource must be deleted prior to executing the test to ensure the server returns the correct status code.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - The URL of a previously deleted FHIR resource.
- **Expected Outputs**:
  - HTTP Status Code: 410 (Gone)

### Required FHIR Operations
- **FHIR Operations**:
  - `DELETE [base]/[resourceType]/[id]`: To delete a resource.
  - `GET [base]/[resourceType]/[id]`: To attempt to access the deleted resource and verify the response.

### Test Data Requirements
- **Test Data**:
  - A valid resource of any type that can be deleted (e.g., Patient, Observation).
  - The resource ID of the deleted resource for verification.

### Validation Criteria
- **Specific Checks**:
  - Ensure that the server returns an HTTP 410 status code when a GET request is made to a deleted resource's URL.
  - Verify that the response does not contain any resource data, only the status code indicating the resource is gone.
  - Confirm that the server's behavior aligns with the SHALL conformance requirement, meaning this behavior is mandatory and must be consistently demonstrated.

```


---

<a id='req-18'></a>

### REQ-18: Profile identification in meta attribute

**Description**: "Identify the Plan-Net profiles supported as part of the FHIR meta.profile attribute for each instance."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for Requirement REQ-18

## 1. Requirement ID
- **REQ-18**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement involves checking the presence and correctness of profile URLs in the `meta.profile` attribute, which can be verified programmatically.

### Complexity
- **Complexity Level**: Simple
  - The task involves straightforward validation of metadata attributes within FHIR resources.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server must support the relevant FHIR resources and operations as per the Capability Statement.
- **Data Setup**: 
  - Instances of FHIR resources that are expected to include the `meta.profile` attribute.
  - The server must have implemented Plan-Net profiles.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - FHIR resource instances from the server that are expected to support Plan-Net profiles.
- **Expected Outputs**:
  - Each resource instance should have the `meta.profile` attribute populated with the correct Plan-Net profile URLs.

### Required FHIR Operations
- **FHIR Operations**:
  - `GET [base]/[resourceType]/[id]`: Retrieve specific resource instances.
  - `GET [base]/[resourceType]`: Search for resource instances to verify multiple instances.

### Test Data Requirements
- **Test Data**:
  - A set of resource instances that are expected to conform to Plan-Net profiles.
  - The test data should include a variety of resource types that are part of the Plan-Net implementation.

### Validation Criteria
- **Validation Checks**:
  - Verify that the `meta.profile` attribute is present in each resource instance.
  - Confirm that the `meta.profile` attribute contains the correct Plan-Net profile URL(s).
  - Ensure that the profile URLs are valid and correspond to the Plan-Net profiles defined in the Implementation Guide.
- **Assertions**:
  - The test passes if all resource instances include the `meta.profile` attribute with the correct profile URLs.
  - The test fails if any resource instance lacks the `meta.profile` attribute or contains incorrect profile URLs.
```


---

<a id='req-19'></a>

### REQ-19: Individual search parameter support

**Description**: "Support the searchParameters on each profile individually."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for FHIR Implementation Guide Requirement REQ-19

## 1. Requirement ID
- **REQ-19**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement involves verifying the server's ability to support search parameters on each profile, which can be tested using automated scripts to perform search operations and validate responses.

### Complexity
- **Classification**: Moderate
  - While the concept of searching is straightforward, the need to test each profile individually and validate the correct application of search parameters adds some complexity.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be running and accessible.
  - The server should have implemented the relevant profiles and search parameters as per the Capability Statement.
- **Data Setup**: 
  - The server must have sufficient test data loaded that conforms to the profiles being tested. This data should cover various scenarios to ensure comprehensive testing.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A list of profiles and their associated search parameters as defined in the server's Capability Statement.
  - Search queries for each profile using its search parameters.
- **Expected Outputs**: 
  - Correct HTTP status codes (e.g., 200 OK for successful searches).
  - Responses containing resources that match the search criteria.
  - Responses that do not include resources that do not match the search criteria.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resource]?parameter=value`
  - Ensure these operations are supported by checking the server's Capability Statement for the `search` interaction on each resource type.

### Test Data Requirements
- **Type of Test Data**:
  - A diverse set of resources for each profile, ensuring coverage of different search parameters.
  - Test data should include edge cases, such as boundary values for numerical parameters or special characters in string parameters.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server returns the correct set of resources that match the search criteria.
  - Check that the server does not return resources that do not match the search parameters.
  - Validate that the server handles invalid search parameters gracefully, returning appropriate error messages.
  - Confirm that the search results are consistent with the definitions in the profiles and the Capability Statement.
  - Ensure that performance metrics (e.g., response time) are within acceptable limits for search operations.
```


---

<a id='req-20'></a>

### REQ-20: Combination search parameter support

**Description**: "Support the searchParameters on each profile in combination."

**Actor**: Server

**Conformance**: SHALL

# Test Specification for REQ-20: Combination Search Parameter Support

## 1. Requirement ID
- **REQ-20**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement can be tested using automated scripts that execute search queries with multiple parameters and verify the responses.

### Complexity
- **Complexity Level**: Moderate
  - While the basic execution of search queries is straightforward, ensuring the correct combination of parameters and validating diverse responses increases complexity.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be running and accessible.
  - The server must have implemented the search functionality as per the FHIR specification.
- **Data Setup**:
  - The server must have sufficient data populated that aligns with the profiles defined in the Implementation Guide.
  - Ensure the data includes various combinations of attributes to test different search parameter combinations.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A list of search parameter combinations defined in the profiles.
  - Sample FHIR resources that match the criteria for each search combination.
- **Expected Outputs**:
  - The server returns correct and complete sets of resources that match the search criteria.
  - The response should include HTTP status code 200 for successful searches.
  - The response should include appropriate error codes for invalid combinations or unsupported parameters.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[ResourceType]?parameter1=value1&parameter2=value2...`
  - Ensure these operations are supported as per the Capability Statement's RESTful interactions.

### Test Data Requirements
- **Type of Test Data**:
  - Diverse resource instances that cover all possible combinations of search parameters.
  - Data should include edge cases such as:
    - Resources with only one of the parameters.
    - Resources with all parameters.
    - Resources with none of the parameters.

### Validation Criteria
- **Specific Checks**:
  - Verify that the response contains only resources that match all specified search parameters.
  - Confirm that the response does not include resources that do not meet the search criteria.
  - Check that the response adheres to the FHIR search result structure, including pagination if applicable.
  - Validate that unsupported parameter combinations return an appropriate error message.
- **Assertions**:
  - Assert that the HTTP response code is 200 for successful searches.
  - Assert that the returned resources' attributes match the search criteria.
  - Assert that the server handles invalid search combinations gracefully, returning appropriate error codes (e.g., 400 Bad Request).

This test specification ensures that the FHIR server meets the requirement for supporting combination search parameters as outlined in the Implementation Guide, verifying both functionality and compliance.

---

<a id='req-21'></a>

### REQ-21: Forward chaining support

**Description**: "Support forward chaining on all search parameters that specify the 'chain' property."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for Requirement REQ-21

## 1. Requirement ID
- **REQ-21**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement involves verifying the server's ability to support forward chaining in search parameters, which can be tested programmatically by executing specific API calls and validating the responses.

### Complexity
- **Classification**: Moderate
  - While the concept of chaining is straightforward, ensuring that all search parameters with the 'chain' property are correctly implemented requires a comprehensive understanding of the server's search capabilities and potential variations in resource types.

### Prerequisites
- **System Configurations**: The FHIR server must be configured to support search operations and chaining as per the FHIR specification.
- **Data Setup**: The server must have a sufficient dataset with linked resources to test forward chaining effectively. This includes resources that have references to other resources, allowing for chaining.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A set of FHIR search queries that utilize forward chaining on parameters with the 'chain' property.
  - Example: A search query on the `Patient` resource that chains to `Observation` (e.g., `Patient?_has:Observation:patient:code=XYZ`).

- **Expected Outputs**: 
  - The server should return a correct and complete set of resources that match the chained search criteria.
  - The response should include HTTP status code 200 for successful queries and appropriate error codes for failures.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resource]?[_has:Resource:parameter:chain=criteria]`
  - Ensure these operations are supported as per the Capability Statement under the search capabilities.

### Test Data Requirements
- **Type of Test Data**:
  - A dataset containing multiple resources with interlinked references. For example, `Patient` resources linked to `Observation` resources via the `patient` reference.
  - Ensure diversity in data to cover various chaining scenarios.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server correctly interprets and processes the chain parameter in search queries.
  - Check that the response includes all expected resources that meet the chained criteria.
  - Validate the response structure against the FHIR specification to ensure compliance.
  - Confirm the server's response time is within acceptable limits for performance testing.
  - Ensure no unexpected errors occur during the execution of chained searches.

- **Assertions**:
  - Assert that the returned resources match the criteria specified in the chained search.
  - Assert that the server handles edge cases, such as no matching resources, gracefully.
  - Assert that the server supports all search parameters with the 'chain' property as documented in the Capability Statement.

By following this test specification, testers can systematically verify the server's compliance with the forward chaining requirement, ensuring robust support for complex search operations in FHIR.
```

---

<a id='req-22'></a>

### REQ-22: Reverse chaining support

**Description**: "Support reverse chaining on all search parameters that specify the 'chain' property."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for Requirement REQ-22

## 1. Requirement ID
- **REQ-22**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement can be tested programmatically by executing FHIR search operations and verifying the results.

### Complexity
- **Complexity**: Moderate
  - While reverse chaining is a well-defined FHIR feature, ensuring comprehensive coverage across all search parameters with the 'chain' property requires careful test design.

### Prerequisites
- **System Configurations**: 
  - A FHIR server that supports the specified version and has reverse chaining capabilities enabled.
- **Data Setup**:
  - The server must have resources with relationships that can be used to test reverse chaining (e.g., Patient, Observation, Practitioner).
  - Ensure that the resources are linked in a manner that supports reverse chaining queries.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A set of FHIR search queries utilizing reverse chaining on various resources and search parameters.
- **Expected Outputs**:
  - Correct resources returned that satisfy the reverse chaining criteria specified in the queries.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resource]?_has:[relatedResource]:[parameter]:[value]`
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - A collection of FHIR resources that include:
    - Patients with linked Observations and Practitioners.
    - Observations linked to specific Patients.
    - Practitioners linked to specific Observations.
  - Ensure the data includes multiple instances to test various chaining scenarios.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server returns the correct set of resources when a reverse chain search is performed.
  - Assertions should include:
    - The number of resources returned matches the expected count.
    - The resources returned are the correct type and contain expected relationships.
    - Performance metrics to ensure the server handles reverse chaining efficiently.
  - Example Assertion:
    - For a query `GET [base]/Patient?_has:Observation:subject:code=12345`, verify that all returned Patient resources have at least one Observation with the code `12345`.

```


---

<a id='req-23'></a>

### REQ-23: XML format support

**Description**: "Support xml source formats for all Plan-Net interactions."

**Actor**: Server

**Conformance**: SHOULD

```markdown
# Test Specification for REQ-23: XML Format Support

## 1. Requirement ID
- **REQ-23**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement to support XML format can be tested using automated tools that send and receive FHIR resources in XML format.

### Complexity
- **Complexity Level**: Moderate
  - While XML parsing and validation are straightforward, ensuring all interactions support XML requires comprehensive coverage across different endpoints and resource types.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to accept and process requests in XML format.
- **Data Setup**:
  - Ensure that the server has sample data for all Plan-Net interactions to facilitate testing.
- **Environment**:
  - A test environment that mirrors production settings to ensure accurate testing results.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - FHIR requests for each Plan-Net interaction in XML format.
- **Expected Outputs**:
  - Successful processing of requests with appropriate HTTP status codes (e.g., 200 OK for successful GET requests, 201 Created for successful POST requests).
  - Correct XML response structure as per FHIR standards.

### Required FHIR Operations
- **FHIR Operations**:
  - `GET` for retrieving resources
  - `POST` for creating resources
  - `PUT` for updating resources
  - `DELETE` for deleting resources
  - Ensure these operations are supported in the Capability Statement for the relevant Plan-Net interactions.

### Test Data Requirements
- **Test Data**:
  - Valid XML representations of FHIR resources relevant to Plan-Net interactions (e.g., Practitioner, Organization, HealthcareService).
  - Edge cases with minimal and maximal data sets to test boundary conditions.

### Validation Criteria
- **Validation Checks**:
  - Verify that the server correctly parses and processes XML requests.
  - Ensure that the server returns valid XML responses conforming to FHIR XML schema.
  - Check for correct HTTP status codes and response headers.
  - Validate the integrity and correctness of the data in the response against the input data.
  - Confirm that error handling is correctly implemented for malformed XML inputs.

By following this test specification, you can ensure that the server supports XML format for all Plan-Net interactions as outlined in the requirement REQ-23.
```


---

<a id='req-24'></a>

### REQ-24: Rejection of unauthorized requests

**Description**: "A server SHALL reject any unauthorized requests by returning an HTTP 401 unauthorized response code."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for REQ-24: Rejection of Unauthorized Requests

## 1. Requirement ID
- **REQ-24**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement can be tested using automated scripts to simulate unauthorized requests and verify the server's response.

### Complexity
- **Complexity Level**: Simple
  - The requirement involves straightforward verification of HTTP response codes for unauthorized requests.

### Prerequisites
- **System Configurations**: 
  - The server must be running and accessible over the network.
  - Authentication mechanisms must be configured on the server.
- **Data Setup**:
  - No specific data setup is required, as the test focuses on unauthorized access.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - An HTTP request to the FHIR server without any authentication credentials or with invalid credentials.
- **Expected Outputs**: 
  - The server should return an HTTP 401 Unauthorized response code.

### Required FHIR Operations
- **API Calls/Operations**:
  - Any FHIR RESTful operation (e.g., `GET`, `POST`, `PUT`, `DELETE`) can be used to test unauthorized access. The Capability Statement should support these operations.

### Test Data Requirements
- **Test Data**:
  - No specific FHIR resources are required for this test. The focus is on the server's response to unauthorized requests.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server returns an HTTP 401 Unauthorized status code for requests without valid authentication.
  - Ensure that the response does not contain any sensitive data.
  - Confirm that the response includes appropriate headers indicating the need for authentication (e.g., `WWW-Authenticate` header).

- **Assertions**:
  - The HTTP status code of the response should be `401`.
  - The response body should not contain any FHIR resource data.
  - The `WWW-Authenticate` header should be present in the response, indicating the authentication method required.

By following this test specification, the requirement for rejecting unauthorized requests can be effectively validated, ensuring compliance with the FHIR Implementation Guide.
```

---

<a id='req-25'></a>

### REQ-25: Support for read interaction

**Description**: "For each resource type and profile, a Plan Net server SHALL support the read interaction."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for Requirement REQ-25

## 1. Requirement ID
- **REQ-25**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement involves verifying the server's support for the read interaction, which can be tested programmatically by sending HTTP GET requests and evaluating responses.

### Complexity
- **Complexity Level**: Simple
  - The read interaction is a fundamental FHIR operation, and testing it involves straightforward HTTP GET requests and response validation.

### Prerequisites
- **System Configurations**: 
  - The server must be running and accessible over the network.
  - The server must have the necessary FHIR resources and profiles implemented as per the Plan Net specification.
- **Data Setup**:
  - Ensure that the server has a variety of resources available for each resource type and profile defined in the Plan Net specification.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - HTTP GET requests for each resource type and profile defined in the Plan Net specification.
- **Expected Outputs**:
  - HTTP 200 OK status code for successful reads.
  - Correct resource representation in the response body matching the requested resource type and profile.

### Required FHIR Operations
- **FHIR Operations**:
  - `GET [base]/[resourceType]/[id]`
    - Ensure that the server's Capability Statement includes support for the `read` operation on all applicable resource types.

### Test Data Requirements
- **Test Data**:
  - A set of resource instances for each resource type and profile, with known identifiers, that can be used to perform read operations.

### Validation Criteria
- **Validation Checks**:
  - Verify that the server returns a 200 OK status code for each read request.
  - Confirm that the response body contains a valid FHIR resource of the correct type.
  - Ensure that the resource conforms to the expected profile, including required elements and constraints.
  - Validate that the resource ID in the response matches the ID used in the request.
  - Check that the server's Capability Statement explicitly lists support for the read operation for each resource type.

By following this test specification, testers can ensure that the Plan Net server meets the requirement to support the read interaction for all specified resource types and profiles.
```

---

<a id='req-26'></a>

### REQ-26: Support for vread interaction

**Description**: "For each resource type and profile, a Plan Net server SHOULD support the vread interaction."

**Actor**: Server

**Conformance**: SHOULD

```markdown
# Test Specification for REQ-26: Support for vread Interaction

## 1. Requirement ID
- **REQ-26**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The vread interaction can be tested programmatically by making HTTP requests to the server and verifying the responses.

### Complexity
- **Level**: Simple
  - The vread interaction involves straightforward HTTP requests and responses, making it relatively simple to test.

### Prerequisites
- **System Configurations**: 
  - A running instance of the Plan Net server with vread interaction capability.
  - Access to the server's FHIR API endpoint.
- **Data Setup**:
  - At least one resource of each type and profile that the server supports must be available in the server's database with known version IDs.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Resource type and ID for each resource to be tested.
  - Specific version ID of the resource.
- **Expected Outputs**:
  - A successful HTTP response with status code 200.
  - The response body should contain the resource in the requested version.
  - The resource should match the expected structure and content for the specified version.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resource-type]/[id]/_history/[version-id]`
  - Ensure that the server's Capability Statement includes support for the vread operation for each resource type.

### Test Data Requirements
- **Type of Test Data**:
  - A set of resources with multiple versions stored on the server.
  - Known version IDs for each resource to be used in the vread requests.

### Validation Criteria
- **Specific Checks**:
  - Verify that the HTTP response status code is 200.
  - Confirm that the returned resource matches the requested version ID.
  - Ensure that the resource conforms to the expected structure and profile.
  - Check that the server's response time is within acceptable limits for performance.
  - Validate that the response headers include appropriate metadata, such as `Last-Modified` and `ETag`.

```


---

<a id='req-27'></a>

### REQ-27: Support for _includes

**Description**: "[For each resource] A Server SHALL be capable of supporting the following _includes [list]."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for Requirement REQ-27

## 1. Requirement ID
- **REQ-27**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement involves checking server capabilities, which can be tested programmatically by sending requests and evaluating responses.

### Complexity
- **Complexity Level**: Moderate
  - Testing the support for `_includes` involves verifying multiple resource types and ensuring correct inclusion of related resources, which requires a moderate level of complexity.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be running and accessible.
  - The server must have the relevant resources populated with data that can be used for testing `_includes`.
- **Data Setup**:
  - Ensure that there are linked resources (e.g., Patient and related Observations) available in the server to test `_includes`.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - FHIR Search requests for each resource type specified in the requirement, including `_includes` parameters.
- **Expected Outputs**:
  - Responses that include the primary resource and the related resources specified by the `_includes` parameter.

### Required FHIR Operations
- **FHIR Operations**:
  - `GET [base]/[resource]?_include=[relatedResource]`
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - A set of resources with known relationships, e.g., a Patient resource with linked Observations, Encounters, or other related resources.
  - Ensure that the data includes various relationship types that can be referenced using `_includes`.

### Validation Criteria
- **Validation Checks**:
  - Verify that the server returns a response with a 200 HTTP status code.
  - Confirm that the response bundle includes both the primary resource and the related resources specified by the `_includes` parameter.
  - Check that the related resources are correctly linked to the primary resource as expected.
  - Ensure that the response conforms to the FHIR standard for resource bundles, including correct use of resource types and relationships.
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
- **Classification**: Automatic
  - The requirement can be tested using automated scripts that perform API calls and validate responses.

### Complexity
- **Complexity Level**: Moderate
  - Testing involves multiple FHIR operations and validation of response structures, which requires a moderate level of complexity.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to support FHIR operations as per the Capability Statement.
- **Data Setup**: 
  - Ensure the server has a populated dataset with resources that have relationships allowing for reverse includes.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - FHIR API requests using the `_revincludes` parameter for specified resources.
- **Expected Outputs**: 
  - Responses should include the resource and all related resources as specified by the `_revincludes` parameter.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resource]?_revincludes=[parameter]`
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - A dataset containing resources with known relationships that can be queried using `_revincludes`.
  - Example: Patients with linked Observations, Encounters, or other related resources.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server returns the primary resource along with all related resources as specified by the `_revincludes` parameter.
  - Check that the response includes the correct number and type of related resources.
  - Validate that the relationships in the response match the expected relationships defined in the test data.
  - Ensure that the response conforms to FHIR standards and the server's Capability Statement.
  - Confirm that the server handles requests efficiently and within acceptable performance thresholds.

- **Assertions**:
  - The response status code should be 200 (OK).
  - The response should include all expected related resources.
  - The response should not include unrelated resources.
  - The response should be in valid FHIR format.

By following this test specification, testers can ensure that the server meets the requirement to support `_revincludes` as specified in REQ-28.
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
- **Classification**: Automatic
  - The requirement can be tested using automated scripts that query the FHIR server and validate the presence or absence of specific identifiers based on organization type.

### Complexity
- **Complexity**: Moderate
  - The test involves checking multiple conditions related to organization types and their identifiers, which requires a nuanced understanding of organization profiles.

### Prerequisites
- **System Configurations**: 
  - Access to a FHIR server that implements the relevant profiles.
  - The server must support the Organization resource and the necessary search operations.
- **Data Setup**:
  - A dataset of Organization resources with varying types, including provider organizations and other types.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A set of Organization resources with different types (e.g., provider, non-provider).
- **Expected Outputs**:
  - Provider organizations should have NPI and CLIA identifiers populated.
  - Non-provider organizations should not have NPI and CLIA identifiers populated.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Organization` to retrieve organization resources.
  - `GET [base]/Organization/[id]` to retrieve specific organization details.
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - Organization resources with the following attributes:
    - `type`: Must include both provider and non-provider organization types.
    - `identifier`: Must include NPI and CLIA for provider organizations.

### Validation Criteria
- **Specific Checks**:
  - For each organization resource retrieved:
    - If `type` indicates a provider organization, assert that `identifier` includes NPI and CLIA.
    - If `type` indicates a non-provider organization, assert that `identifier` does not include NPI and CLIA.
- **Assertions**:
  - Pass if all provider organizations have the required identifiers and all non-provider organizations do not.
  - Fail if any provider organization lacks the required identifiers or any non-provider organization has them.

```

---

<a id='req-30'></a>

### REQ-30: lastUpdate timestamp requirement

**Description**: "Each profile in this guide requires that the lastUpdate timestamp be provided as part of the profile's data content."

**Actor**: Server

**Conformance**: None (Requirement)

```markdown
# Test Specification for FHIR Implementation Guide Requirement

## 1. Requirement ID
- **REQ-30**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement can be tested automatically by querying the server and verifying the presence of the `lastUpdate` timestamp in the profile's data content.

### Complexity
- **Complexity Level**: Simple
  - The requirement involves checking for the presence of a single timestamp field, which is straightforward.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server must have implemented the profiles as specified in the Implementation Guide.
- **Data**: 
  - Profiles with data content need to be available on the server for testing.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A list of profiles defined in the Implementation Guide.
- **Expected Outputs**:
  - Each profile's data content should include a `lastUpdate` timestamp.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[ProfileType]/[id]`: Retrieve the resource instance of each profile type to check for the `lastUpdate` timestamp.
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - Instances of each profile type defined in the Implementation Guide.
  - The data should be realistic and reflect typical usage scenarios.

### Validation Criteria
- **Specific Checks**:
  - For each profile retrieved, verify that the `lastUpdate` timestamp is present in the resource's metadata.
  - The `lastUpdate` timestamp should conform to the FHIR dateTime format (e.g., `YYYY-MM-DDThh:mm:ss.sssZ`).
- **Assertions**:
  - Assert that the `lastUpdate` field is not null or empty.
  - Assert that the `lastUpdate` field is formatted correctly according to the FHIR dateTime standard.
  - If any profile does not include a `lastUpdate` timestamp, the test should fail, indicating non-conformance.

```

---

<a id='req-32'></a>

### REQ-32: General Search for Pharmacy

**Description**: "The Plan-Net design is based around the following types of searches: General Search - Example: Pharmacy - Focal Resource and Field: HealthcareService.category, HealthcareService.specialty - Qualifications of Search: Location, network."

**Actor**: Server

**Conformance**: None (Design requirement)

```markdown
# Test Specification for REQ-32: General Search for Pharmacy

## 1. Requirement ID
- **REQ-32**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement can be tested using automated scripts to perform searches and validate responses.

### Complexity
- **Level**: Moderate
  - Involves multiple search parameters and requires validation against expected search results.

### Prerequisites
- **System Configurations**: 
  - A FHIR server that implements the Plan-Net design and supports the required search parameters.
- **Data Setup**:
  - The server must have HealthcareService and Location resources populated with relevant data, including categories, specialties, and location details.
- **Network Configuration**:
  - Ensure network configurations are in place to access the FHIR server.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Search queries using the HealthcareService resource with parameters such as `category`, `specialty`, and location-based parameters.
- **Expected Outputs**:
  - Correctly filtered list of HealthcareService resources representing pharmacies, based on the search criteria.

### Required FHIR Operations
- **FHIR Operations**:
  - `GET [base]/HealthcareService?category=[value]&specialty=[value]&location=[value]`
  - Ensure support for search parameters as specified in the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - HealthcareService resources with various categories and specialties, including pharmacy-related entries.
  - Location resources with diverse address details to test location-based filtering.

### Validation Criteria
- **Validation Checks**:
  - Verify that the search results include only those HealthcareService resources that match the specified `category` and `specialty`.
  - Confirm that location-based searches return resources within the specified geographic area.
  - Ensure that all required search parameters are supported and return expected results.
  - Validate that the response conforms to FHIR standards, including correct resource types and structure.
  - Check for correct handling of edge cases, such as no results found or invalid search parameters.

- **Assertions**:
  - The response status code should be `200 OK`.
  - The response should include a `Bundle` of type `searchset`.
  - Each entry in the response should be a valid `HealthcareService` resource with the expected attributes.
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
- **Classification**: Automatic
  - The requirement involves searching for providers by name using a FHIR API, which can be automated through scripted tests.

### Complexity
- **Complexity Level**: Moderate
  - While the basic search functionality is straightforward, the inclusion of qualifications such as location, network, specialty, and role/privileges adds moderate complexity to the test scenario.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be running and accessible.
  - The server must support the Practitioner resource and the specified search parameters.

- **Data Setup**:
  - The system must have pre-loaded Practitioner resources with diverse names, locations, networks, specialties, and roles/privileges to validate search accuracy.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Search query using the `name` parameter (e.g., `Practitioner?name=Joe Smith`).
  - Optional qualifiers for location, network, specialty, and role/privileges.

- **Expected Outputs**:
  - A list of Practitioner resources matching the search criteria.
  - Each returned Practitioner should have the name "Joe Smith" and meet any specified qualifiers.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Practitioner?name={name}`: To search for practitioners by name.
  - Additional queries may include qualifiers such as location, network, specialty, and role/privileges if supported by the server.

### Test Data Requirements
- **Test Data**:
  - Practitioner resources with varied names including "Joe Smith".
  - Resources should have associated data for location, network, specialty, and role/privileges to test qualifiers.

### Validation Criteria
- **Specific Checks**:
  - Verify that the response status code is `200 OK`.
  - Assert that the response contains Practitioner resources with the name "Joe Smith".
  - Check that the number of returned resources matches the expected count based on the test data setup.
  - Validate that any specified qualifiers (e.g., location, specialty) are correctly applied in the search results.
  - Ensure that no extraneous resources are returned that do not match the search criteria.

- **Assertions**:
  - The `name` field in each returned Practitioner resource must include "Joe Smith".
  - If qualifiers are used, verify that the corresponding fields in the Practitioner resource match the expected values.

This structured test specification provides a comprehensive approach to verifying the Provider search by name functionality as outlined in REQ-33.
```

---

<a id='req-34'></a>

### REQ-34: Organization search by name

**Description**: "The Plan-Net design is based around the following types of searches: Organization by Name - Example: Montgomery Cardiology or CVS - Focal Resource and Field: Organization.name - Qualifications of Search: Location, network, specialty."

**Actor**: Server

**Conformance**: None (Design requirement)

# Test Specification for REQ-34: Organization Search by Name

## 1. Requirement ID
- **REQ-34**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The search functionality can be tested programmatically by executing FHIR search queries and validating the responses.

### Complexity
- **Complexity Level**: Moderate
  - The test involves executing search queries and validating responses against multiple criteria (e.g., name, location, network, specialty).

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be configured to support the Organization resource and its search parameters as specified in the Capability Statement.
- **Data Setup**:
  - The system must have pre-loaded data for organizations, including names like "Montgomery Cardiology" and "CVS" with associated locations, networks, and specialties.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Search query for Organization resource using the `name` search parameter.
  - Example search terms: "Montgomery Cardiology", "CVS".
- **Expected Outputs**:
  - A list of Organization resources matching the search term in the `name` field.
  - The response should include relevant details such as location, network, and specialty if applicable.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Organization?name=[search-term]`
  - Ensure that the `name` search parameter is supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - Organization records with distinct names, including "Montgomery Cardiology" and "CVS".
  - Associated data for location, network, and specialty to verify the qualifications of the search.

### Validation Criteria
- **Specific Checks**:
  - Verify that the response status code is `200 OK`.
  - Confirm that the returned resources include the `Organization` resource type.
  - Validate that the `name` field in the returned resources matches the search term.
  - Check that the response includes relevant details such as location, network, and specialty if specified in the search query.
  - Ensure that the search results are consistent with the data loaded in the system.

By following this structured test specification, you can ensure that the Organization search by name functionality is thoroughly tested and conforms to the requirements outlined in the FHIR Implementation Guide and Capability Statement.

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
- **Classification**: Automatic
  - The requirement can be tested using automated scripts that perform API calls and validate responses.

### Complexity
- **Level**: Moderate
  - While the search functionality is straightforward, the requirement involves multiple search parameters and validation of results, which adds some complexity.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be configured to support the PractitionerRole resource and its search parameters.
- **Data Setup**: 
  - The system must have pre-existing data for practitioners with various specialties, including Cardiologists.
  - Locations, networks, and names associated with these practitioners must be available.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Search query for PractitionerRole with the `specialty` parameter set to "Cardiologist".
  - Optional filters like `location`, `network`, and `name` to refine the search.
- **Expected Outputs**:
  - A list of PractitionerRole resources where the `specialty` is "Cardiologist".
  - The results should be filtered according to any additional parameters provided (e.g., location, network).

### Required FHIR Operations
- **API Calls**:
  - `GET /PractitionerRole?specialty=Cardiologist`
  - `GET /PractitionerRole?specialty=Cardiologist&location=[location-id]`
  - `GET /PractitionerRole?specialty=Cardiologist&network=[network-id]`
  - `GET /PractitionerRole?specialty=Cardiologist&name=[practitioner-name]`

### Test Data Requirements
- **PractitionerRole Data**:
  - Practitioners with the specialty "Cardiologist".
  - Associated locations, networks, and names for comprehensive testing.
- **Location Data**:
  - Valid location identifiers that can be used in conjunction with the PractitionerRole search.
- **Network Data**:
  - Valid network identifiers to test network-based filtering.

### Validation Criteria
- **Conformance Checks**:
  - Verify that the returned PractitionerRole resources have the `specialty` field set to "Cardiologist".
  - Ensure that additional filters (location, network, name) correctly limit the results.
  - Confirm that the response status code is 200 (OK) and that the response structure adheres to the FHIR standard.
  - Validate that the search results include all relevant fields as per the PractitionerRole resource definition.
- **Assertions**:
  - The number of results matches the expected count based on the test data setup.
  - Each result in the response contains valid references to Practitioner, Location, and Network resources where applicable.
```


---

<a id='req-36'></a>

### REQ-36: Organization search by specialty

**Description**: "The Plan-Net design is based around the following types of searches: Organization by specialty - Example: Compounding Pharmacy - Focal Resource and Field: OrganizationAffiliation.specialty - Qualifications of Search: Location, network, name."

**Actor**: Server

**Conformance**: None (Design requirement)

```markdown
# Test Specification for Requirement REQ-36

## 1. Requirement ID
- **REQ-36**: Organization search by specialty

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement can be tested using automated scripts that perform searches and validate responses.

### Complexity
- **Level**: Moderate
  - The complexity arises from the need to validate multiple search parameters and ensure correct filtering by specialty.

### Prerequisites
- **System Configurations**:
  - A FHIR server that supports the Organization, OrganizationAffiliation, and Location resources.
  - The server must implement the search parameters as specified in the Capability Statement.
  
- **Data Setup**:
  - Ensure the FHIR server has pre-loaded data including:
    - Organizations with various specialties, including "Compounding Pharmacy".
    - OrganizationAffiliations linking organizations with specialties.
    - Locations associated with organizations.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Search query for organizations by specialty, e.g., `OrganizationAffiliation?specialty=Compounding Pharmacy`
  - Additional search qualifiers: location, network, name (if applicable)

- **Expected Outputs**:
  - A list of organizations that match the specified specialty.
  - The response should include relevant details like organization name, location, and specialty.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/OrganizationAffiliation?specialty=[specialty]`
  - Optionally include qualifiers: `location`, `network`, `name`

### Test Data Requirements
- **Test Data**:
  - Organizations with different specialties, including "Compounding Pharmacy".
  - OrganizationAffiliations linking these organizations to their specialties.
  - Locations and networks associated with the organizations.

### Validation Criteria
- **Specific Checks**:
  - Verify that the response includes only organizations with the specified specialty.
  - Validate that the returned organizations have valid and correct OrganizationAffiliation.specialty fields.
  - Check that the response adheres to the FHIR standard format.
  - Ensure that the search respects additional qualifiers if provided (e.g., location, network, name).
  - Confirm that the server returns appropriate HTTP status codes (e.g., 200 for success, 400 for bad requests).

- **Assertions**:
  - The number of returned organizations matches the expected count based on the test data.
  - Each organization in the response contains the expected specialty.
  - The response time is within acceptable limits for performance testing.

By following this structured test specification, the requirement REQ-36 can be thoroughly tested to ensure compliance with the FHIR Implementation Guide.
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
- **Classification**: Automatic
  - The requirement involves executing FHIR search queries, which can be automated using test scripts or tools that can interact with FHIR APIs.

### Complexity
- **Complexity Level**: Moderate
  - The requirement involves understanding and executing FHIR search operations with specific parameters and interpreting the results to verify active status.

### Prerequisites
- **System Configurations**: 
  - Access to a FHIR server that implements the Da Vinci Plan-Net Implementation Guide.
  - Ensure the server supports the PractitionerRole and OrganizationAffiliation resources as per the Capability Statement.
- **Data Setup**:
  - The server must have data for Practitioners and Organizations with varying active statuses and dates.
  - Ensure the data includes entries that are both active and inactive for comprehensive testing.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Input**: 
  - FHIR search query for PractitionerRole with date parameter set to current date.
  - FHIR search query for OrganizationAffiliation with date parameter set to current date.
- **Expected Output**: 
  - A list of PractitionerRole resources that are active as of the current date.
  - A list of OrganizationAffiliation resources that are active as of the current date.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET /PractitionerRole?_include=PractitionerRole:date=ge{current_date}`
  - `GET /OrganizationAffiliation?_include=OrganizationAffiliation:date=ge{current_date}`
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **PractitionerRole Data**:
  - Include Practitioners with roles that have varying start and end dates.
- **OrganizationAffiliation Data**:
  - Include Organizations with affiliations that have varying start and end dates.

### Validation Criteria
- **Conformance Checks**:
  - Verify that the search results only include PractitionerRole and OrganizationAffiliation resources that are active as of the current date.
  - Ensure the returned resources match the expected structure and contain the necessary attributes (e.g., active status, valid dates).
- **Assertions**:
  - Confirm that no inactive resources are returned in the search results.
  - Validate that the response status is HTTP 200 OK.
  - Check that the search results are consistent with the server's data setup and the expected active statuses.

```


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
- **Classification**: Manual
  - **Rationale**: The requirement involves inspecting the representation of contact information, which is best verified through manual inspection of the FHIR resource output to ensure the correct fields are populated as per the guidance.

### Complexity
- **Complexity**: Simple
  - **Rationale**: The requirement involves straightforward data field checks within a FHIR resource, specifically focusing on the presence and content of certain fields.

### Prerequisites
- **System Configurations**: The FHIR server must be operational and accessible for testing.
- **Data Setup**: The server must have existing data entries where contacts are represented as department names.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A FHIR resource (e.g., Organization, PractitionerRole) that includes a contact with a department name.
- **Expected Outputs**: 
  - The `contact.name.text` field should contain the department name.
  - The `contact.name.family` and `contact.name.given` fields should be blank.

### Required FHIR Operations
- **API Calls**: 
  - `GET [base]/Organization/{id}` or `GET [base]/PractitionerRole/{id}`
  - Ensure these operations are supported in the Capability Statement under the "read" interaction.

### Test Data Requirements
- **Type of Test Data**: 
  - FHIR resources where the contact is a department, such as a patient help line or administrative department.
  - Ensure the test data includes a variety of department names to validate consistent handling.

### Validation Criteria
- **Specific Checks**:
  1. Verify that the `contact.name.text` field is populated with the department name.
  2. Confirm that the `contact.name.family` and `contact.name.given` fields are empty.
  3. Check that the resource conforms to the general FHIR structure and any additional constraints specified in the Implementation Guide.
- **Assertions**:
  - The department name must be correctly placed in the `contact.name.text` field.
  - Both `contact.name.family` and `contact.name.given` fields must be absent or empty to pass the test.

```


---

<a id='req-39'></a>

### REQ-39: Organization contact handling for departments

**Description**: "When the contact is a department name, rather than a human (e.g., patient help line), include a blank family and given name, and provide the department name in contact.name.text."

**Actor**: Server

**Conformance**: None (Implementation guidance)

# Test Specification for REQ-39: Organization Contact Handling for Departments

## 1. Requirement ID
- **REQ-39**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Manual
  - **Rationale**: The requirement involves inspecting the presence and correct placement of data in specific fields, which is best verified through manual inspection of the FHIR resource.

### Complexity
- **Complexity Level**: Simple
  - **Rationale**: The requirement involves straightforward data placement within a FHIR resource without complex logic or dependencies.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server should support the Organization resource as per the capability statement.
- **Data Setup**: 
  - An Organization resource with a contact that represents a department (e.g., patient help line) must be present in the system.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Input**: 
  - An Organization resource with a contact intended to represent a department.
- **Expected Output**: 
  - The contact's `name.text` field should contain the department name.
  - The contact's `name.family` and `name.given` fields should be blank.

### Required FHIR Operations
- **GET [base]/Organization/{id}**: 
  - Retrieve the Organization resource by its ID to inspect the contact details.
- **GET [base]/Organization?name={department-name}**: 
  - Search for the Organization resource using the department name to ensure it is correctly indexed and retrievable.

### Test Data Requirements
- **Test Data**: 
  - An Organization resource with at least one contact entry where the contact is a department (e.g., "Patient Help Line").
  - Ensure the department name is unique enough to be searchable.

### Validation Criteria
- **Validation Checks**:
  1. **Presence Check**: Verify that the Organization resource contains a contact entry.
  2. **Field Content Check**: 
     - Confirm that `contact.name.text` contains the department name.
     - Confirm that `contact.name.family` and `contact.name.given` are both empty.
  3. **Search Functionality Check**: 
     - Perform a search using the department name and ensure the correct Organization resource is returned.
  4. **Conformance Check**: 
     - Ensure the resource conforms to the general capabilities and supported search parameters as specified in the capability statement.

By following this test specification, the implementation of the requirement can be verified for correctness and adherence to the FHIR Implementation Guide.

---

<a id='req-40'></a>

### REQ-40: Practitioner qualification coding

**Description**: "When the value set for the coded concept in qualification is insufficient, the qualification can be provided in the text field of the codeableConcept."

**Actor**: Server

**Conformance**: None (Implementation guidance)

# Test Specification for Requirement REQ-40

## 1. Requirement ID
**REQ-40: Practitioner Qualification Coding**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Manual
- **Rationale**: The requirement involves inspecting the use of text fields in codeableConcepts when the value set is insufficient, which requires human judgment to assess the appropriateness of the text provided.

### Complexity
- **Classification**: Moderate
- **Rationale**: While the inspection of text fields is straightforward, ensuring that the text appropriately supplements the coded concept requires understanding of clinical qualifications and context.

### Prerequisites
- **System Configurations**: 
  - A FHIR server that supports the Practitioner resource and the specified search parameters.
- **Data Setup**:
  - Practitioner resources with qualifications that include both coded concepts and text fields.
  - A value set that is known to be insufficient for certain qualifications, necessitating the use of text.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A Practitioner resource with a qualification that uses a codeableConcept with both a code and a text field.
- **Expected Outputs**:
  - The text field should provide meaningful and contextually appropriate information that supplements the coded concept.

### Required FHIR Operations
- **Operations**:
  - `GET [base]/Practitioner?_id=[id]`: Retrieve a specific Practitioner resource by ID.
  - `GET [base]/Practitioner?name=[name]`: Search for Practitioner resources by name.
  - `GET [base]/Practitioner?family=[family]`: Search for Practitioner resources by family name.
  - `GET [base]/Practitioner?given=[given]`: Search for Practitioner resources by given name.
  - `GET [base]/Practitioner?_lastUpdated=[date]`: Retrieve Practitioner resources updated on a specific date.

### Test Data Requirements
- **Practitioner Resource**:
  - At least one Practitioner with a qualification that includes a codeableConcept with an insufficient value set, supplemented by a descriptive text.
- **Value Set**:
  - A known value set that lacks certain qualifications, requiring textual supplementation.

### Validation Criteria
- **Conformance Checks**:
  - Verify that the Practitioner resource includes a qualification with a codeableConcept.
  - Check that when the code is insufficient, the text field is populated with appropriate and meaningful information.
  - Ensure the text field does not duplicate the coded information but provides additional context or clarification.
- **Assertions**:
  - The text field should not be empty when the value set is insufficient.
  - The text should be relevant to the qualification and understandable to a human reader.
- **Inspection**:
  - Manually review the text field to confirm it provides necessary context or clarification for the qualification.

---



