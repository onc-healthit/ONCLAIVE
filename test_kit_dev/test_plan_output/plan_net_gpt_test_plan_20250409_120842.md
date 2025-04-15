# Consolidated Test Plan for Plan Net

## Generated on: 2025-04-09 12:09:02

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
- **Classification**: Manual
  - **Rationale**: The requirement specifies that no Personally Identifiable Information (PII) should be sent by clients. This requires inspection of the data being sent, which is best verified through manual review of the data payloads.

### Complexity
- **Complexity Level**: Moderate
  - **Rationale**: While the concept of not sending PII is straightforward, identifying and verifying the absence of all forms of PII in data payloads can be intricate due to the variety of data types and potential edge cases.

### Prerequisites
- **System Configurations**: 
  - Access to the directory mobile application that interfaces with the Plan-Net service.
  - Access to network monitoring tools to capture data payloads sent by the client.
- **Data Setup**:
  - A configured Plan-Net service endpoint that the client application will query.
  - Test user accounts or profiles set up in the mobile application without PII.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - Network traffic data from the mobile application when querying the Plan-Net service.
- **Expected Outputs**: 
  - Data payloads should not contain any PII such as names, social security numbers, addresses, phone numbers, or any other identifiable information.

### Required FHIR Operations
- **FHIR Operations**: 
  - The Capability Statement should support the following operations for the Plan-Net service:
    - `GET` operations for querying resources such as `Practitioner`, `Organization`, `Location`, etc.
  - Ensure these operations do not include PII in their request payloads.

### Test Data Requirements
- **Test Data**: 
  - Use synthetic or anonymized data that mimics real-world scenarios but does not contain PII.
  - Ensure that the test data set includes various types of queries that the mobile application might perform.

### Validation Criteria
- **Specific Checks**:
  - Capture and inspect the HTTP request payloads sent by the client application.
  - Verify that the payloads do not include any fields or values that can be classified as PII.
  - Confirm that the application adheres to the requirement by not sending PII in any scenario, including edge cases.
  - Document any instances where PII is detected and ensure corrective actions are taken.
```


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
  - The requirement can be tested automatically by simulating client interactions with FHIR resources containing Must Support data elements.

### Complexity
- **Complexity**: Moderate
  - The test involves verifying that the client can process various resource instances without errors, which requires a comprehensive set of test cases to cover different scenarios.

### Prerequisites
- **System Configurations**: 
  - The client application must be deployed and configured to connect to a FHIR server.
  - The FHIR server must support the necessary operations as per the Capability Statement.
  
- **Data Setup**:
  - Access to a FHIR server with resources that include Must Support data elements.
  - Test user credentials with appropriate access permissions to read resources.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A set of FHIR resource instances (e.g., Patient, Observation) that include Must Support data elements.
  
- **Expected Outputs**:
  - The client application processes the resource instances without generating errors or causing application failures.
  - The client application should correctly display or handle the Must Support data elements as per its functional requirements.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Patient/[id]`
  - `GET [base]/Observation/[id]`
  - Any other resource operations that include Must Support elements as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - Resource instances with Must Support elements populated with valid data.
  - Resource instances with Must Support elements left empty or with null values to test handling of optional data.

### Validation Criteria
- **Specific Checks**:
  - Verify that the client application does not crash or throw exceptions when processing resources with Must Support elements.
  - Assert that Must Support elements are correctly processed and displayed by the client, even if they are empty or null.
  - Confirm that the client application logs any issues related to Must Support elements in a non-disruptive manner.
  - Ensure that the client application maintains overall functionality and user experience when encountering Must Support elements.

- **Assertions**:
  - No unhandled exceptions or application crashes occur during the test.
  - The client application correctly interprets and displays Must Support elements.
  - Logs or error messages, if any, are informative and do not disrupt application flow.
```


---

<a id='req-07'></a>

### REQ-07: Client display of data elements

**Description**: "Application actors SHOULD be capable of displaying the data elements for human use or storing the information for other purposes."

**Actor**: Client

**Conformance**: SHOULD

```markdown
# Test Specification for FHIR Implementation Guide Requirement REQ-07

## 1. Requirement ID
- **REQ-07**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Manual
  - **Rationale**: The requirement involves human interaction for verifying the display of data elements, which necessitates manual inspection to ensure that data is presented correctly and is human-readable.

### Complexity
- **Complexity Level**: Moderate
  - **Rationale**: While the requirement itself is straightforward, verifying that all relevant data elements are displayed correctly across different scenarios and data types can add complexity.

### Prerequisites
- **System Configurations**: 
  - The client application must be installed and configured to connect to the FHIR server.
  - The application should have access to a test environment that mimics the production setup.
- **Data Setup**: 
  - A set of FHIR resources (e.g., Patient, Observation, Condition) should be available on the FHIR server for testing purposes.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A set of test FHIR resources with various data elements that the client application should display.
- **Expected Outputs**:
  - The client application should correctly display the data elements in a human-readable format.
  - The application should also have the capability to store the information for other purposes, if applicable.

### Required FHIR Operations
- **Supported API Calls**:
  - `GET [base]/Patient/{id}`
  - `GET [base]/Observation/{id}`
  - `GET [base]/Condition/{id}`
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Type of Test Data**:
  - A diverse set of FHIR resources with varying data elements, including:
    - Patients with different demographics
    - Observations with different types and values
    - Conditions with varying severity and status

### Validation Criteria
- **Display Verification**:
  - Verify that the client application displays all relevant data elements from the FHIR resources in a clear and readable format.
  - Check that data elements such as names, dates, codes, and values are presented correctly.
- **Storage Capability**:
  - Confirm that the application can store the displayed information for future retrieval or other purposes, if applicable.
- **Conformance Check**:
  - Ensure that the application meets the "SHOULD" conformance level by demonstrating the capability to display and store data elements as described.
- **Inspection**:
  - Conduct a manual inspection of the user interface to ensure compliance with the requirement.

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
  - The requirement involves interpretation by the client application, which is best verified through inspection and manual testing.

### Complexity
- **Complexity Level**: Moderate
  - While the concept is straightforward, verifying the correct interpretation of missing data requires careful inspection of client behavior and potentially complex test scenarios.

### Prerequisites
- **System Configurations**: 
  - Access to a Health Plan API actor with a known set of resources.
  - A client application capable of querying the Health Plan API.
- **Data Setup**:
  - Resource instances in the Health Plan API actor that have missing Must Support data elements.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A set of FHIR resource instances from the Health Plan API actor where some Must Support data elements are intentionally omitted.
- **Expected Outputs**:
  - The client application should interpret these missing elements as data not present in the Health Plan API actor's system, without generating errors or incorrect assumptions.

### Required FHIR Operations
- **FHIR Operations**:
  - `GET [base]/[resource]`: Retrieve resource instances from the Health Plan API actor.
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - A variety of FHIR resources (e.g., Coverage, ExplanationOfBenefit) with some Must Support elements missing.
  - Ensure the test data represents realistic scenarios where data might be missing.

### Validation Criteria
- **Specific Checks**:
  - Verify that the client application does not generate errors when encountering missing Must Support elements.
  - Confirm that the client application does not attempt to infer or fabricate data for missing elements.
  - Ensure that the client application logs or documents the absence of data appropriately, if applicable.
  - Inspect the client application's user interface or logs to ensure compliance with the requirement.

- **Assertions**:
  - The client application SHALL interpret missing Must Support data elements as data not present in the system.
  - No errors or incorrect data assumptions should be made by the client application.

By following this test specification, testers can ensure that the client application correctly handles missing Must Support data elements as required by the FHIR Implementation Guide.
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
- **REQ-09**: Client processing of missing information indicators

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement involves processing data elements that can be programmatically verified.

### Complexity
- **Level**: Moderate
  - The complexity arises from handling various resource types and ensuring all Must Support elements with missing information are correctly processed.

### Prerequisites
- **System Configurations**: 
  - The Consumer App must be configured to connect to a FHIR server that supports the necessary operations.
- **Data Setup**:
  - The FHIR server must contain resource instances with Must Support elements marked as missing.
  - The server must support the Capability Statement indicating the ability to handle Must Support elements.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - FHIR resource instances containing Must Support data elements with missing information indicators (e.g., `dataAbsentReason`).
- **Expected Outputs**:
  - The Consumer App should correctly identify and process the missing information indicators without errors.
  - The app should log or display a message indicating the presence of missing information.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resourceType]` to retrieve resource instances.
  - Ensure the server supports these operations as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - Resource instances (e.g., Patient, Observation) with Must Support elements containing `dataAbsentReason` extensions.
  - Examples:
    - A Patient resource with a missing `birthDate` element, using `dataAbsentReason` to indicate why it is missing.
    - An Observation resource with a missing `valueQuantity`, using `dataAbsentReason`.

### Validation Criteria
- **Specific Checks**:
  - Verify that the Consumer App correctly identifies Must Support elements with `dataAbsentReason`.
  - Confirm that the app processes these elements without throwing errors or exceptions.
  - Check that the app logs or displays appropriate messages indicating the presence of missing information.
  - Ensure that the app's behavior aligns with the expected handling of missing information as defined in the FHIR Implementation Guide.

- **Assertions**:
  - The app processes the resource without errors.
  - The app logs/display messages for each Must Support element with missing information.
  - The app's user interface or logs reflect the correct handling of missing data as per the requirement.

```

---

<a id='req-31'></a>

### REQ-31: Client tracking of directory content updates

**Description**: "Clients that cache query results can track additions or modifications to directory content through queries that filter content using the _lastUpdated search parameter."

**Actor**: Client

**Conformance**: None (Implementation guidance)

```markdown
# Test Specification for Requirement REQ-31

## 1. Requirement ID
- **REQ-31**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Hybrid
  - The requirement involves both automated queries and manual inspection of results.

### Complexity
- **Complexity Level**: Moderate
  - Involves understanding and implementing FHIR search parameters and evaluating changes over time.

### Prerequisites
- **System Configurations**: 
  - A FHIR server with directory content that supports the `_lastUpdated` search parameter.
  - Client application capable of caching query results and performing FHIR queries.
- **Data Setup**: 
  - Initial dataset with known timestamps for directory content entries.
  - Ability to modify or add entries to the directory content to simulate updates.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Initial query to cache directory content with known `_lastUpdated` timestamps.
  - Subsequent queries using the `_lastUpdated` parameter to detect changes.
- **Expected Outputs**:
  - Accurate identification of additions or modifications to the directory content since the initial query.

### Required FHIR Operations
- **Supported API Calls**:
  - `GET [base]/[resource]?_lastUpdated=[date]`
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - Directory content with a variety of resources and known `_lastUpdated` timestamps.
  - Simulated updates to the directory content by adding new resources or modifying existing ones.

### Validation Criteria
- **Specific Checks**:
  - Verify that the client correctly identifies new or updated resources when queried with `_lastUpdated`.
  - Ensure that no unchanged resources are returned in the query results.
  - Confirm that the timestamps of returned resources are greater than or equal to the `_lastUpdated` parameter used in the query.
- **Assertions**:
  - The number of resources returned matches the expected number of updates.
  - The content of returned resources reflects the latest state of the directory.
  - Manual inspection to ensure that the client application correctly updates its cache based on query results.
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
# Test Specification for REQ-01

## 1. Requirement ID
- **REQ-01**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Manual
  - **Rationale**: The requirement involves verifying that no personally identifiable information (PII) is required for directory queries, which may involve inspecting API request logs and configurations rather than automated testing.

### Complexity
- **Classification**: Simple
  - **Rationale**: The requirement is straightforward as it involves checking the absence of PII in the requests made to the server.

### Prerequisites
- **System Configurations**: 
  - The server must be set up to handle directory queries.
  - The mobile application should be configured to make directory queries without sending PII.
- **Data Setup**: 
  - Ensure that the directory service is populated with test data that can be queried.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A directory query request from a mobile application.
- **Expected Outputs**: 
  - The server processes the query without requiring any consumer identifying information (PII) in the request.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Directory` or equivalent operation for querying the directory.
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Type of Test Data**:
  - Directory entries that can be queried without needing PII.
  - Ensure test data is anonymized and does not contain any PII.

### Validation Criteria
- **Specific Checks**:
  - Inspect the API request logs to ensure no PII is included in the request parameters or headers.
  - Verify that the server responds to the directory query successfully without requiring PII.
  - Confirm that the server's response does not contain any error indicating missing PII.
- **Assertions**:
  - The request does not contain fields such as name, address, phone number, or other identifying information.
  - The server's response status code should be 200 (OK) or appropriate success code.
  - No error messages related to missing PII should be present in the server's response.

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
  - The requirement can be tested using automated scripts to verify the presence and correct population of Must Support data elements in the query results.

### Complexity
- **Complexity**: Moderate
  - The complexity arises from the need to handle various resource types and ensure that all Must Support elements are populated correctly across these resources.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to expose the Health Plan API with all relevant endpoints enabled.
- **Data Setup**: 
  - The server must have a dataset that includes all resources with Must Support elements.
  - Test user accounts with appropriate access rights to query the data.
- **Environment**: 
  - A test environment that mirrors the production setup to ensure accurate testing conditions.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A set of queries designed to retrieve resources that include Must Support data elements.
- **Expected Outputs**: 
  - Query results where all Must Support data elements are populated according to the FHIR profiles defined in the Implementation Guide.

### Required FHIR Operations
- **FHIR Operations**:
  - `GET [base]/[resource]?[parameters]` - To retrieve resources with Must Support elements.
  - `GET [base]/metadata` - To verify that the server's Capability Statement supports the required operations.

### Test Data Requirements
- **Test Data**:
  - A comprehensive dataset that includes instances of each resource type with Must Support elements.
  - Test cases should cover a variety of scenarios, including edge cases where Must Support elements are conditionally populated.

### Validation Criteria
- **Validation Checks**:
  - Verify that each Must Support data element is present in the query results.
  - Ensure that the data elements are populated with valid and expected values.
  - Check that the server's Capability Statement includes support for the necessary operations and resources.
- **Assertions**:
  - All Must Support elements are present and correctly populated in the returned resources.
  - The server responds with a 200 HTTP status code for successful queries.
  - The Capability Statement confirms support for the required operations and resources.

By following this test specification, testers can systematically verify that the Health Plan API actors meet the requirement to populate Must Support data elements as specified in the FHIR Implementation Guide.
```

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
  - **Rationale**: The requirement involves inspecting the absence of data elements in FHIR resource instances, which may require human judgment to verify that the absence is appropriate given the context of the data.

### Complexity
- **Classification**: Moderate
  - **Rationale**: While the requirement itself is straightforward, verifying it involves understanding the context and ensuring that data elements are correctly omitted based on their cardinality and presence in the data.

### Prerequisites
- **System Configurations**: The server must be configured to handle FHIR requests and support the relevant resources and operations as specified in the Capability Statement.
- **Data Setup**: The server must have access to a dataset where certain Must Support data elements have a minimum cardinality of 0 and are conditionally absent.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A FHIR query request to the Health Plan API for a resource that includes Must Support data elements with a minimum cardinality of 0.
- **Expected Outputs**: 
  - The returned FHIR resource instance should not include the Must Support data elements that are absent in the dataset.

### Required FHIR Operations
- **API Calls/Operations**: 
  - `GET [base]/[resource]?[parameters]` - Retrieve the resource instances that are expected to have absent Must Support data elements.
  - Ensure that these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Type of Test Data**: 
  - Resource instances with Must Support elements that have a minimum cardinality of 0 and are conditionally absent.
  - Example resources could include `Patient`, `Coverage`, or other relevant resources as specified in the Capability Statement.

### Validation Criteria
- **Specific Checks**:
  - Verify that the response does not include the Must Support data elements that are absent in the dataset.
  - Confirm that the server correctly omits these elements in accordance with the requirement when the minimum cardinality is 0.
  - Ensure that no unexpected data elements are present in the response.
- **Assertions**:
  - The absence of specific Must Support data elements in the response is correct and aligns with the dataset and requirement.
  - The server's behavior complies with the SHALL NOT conformance requirement by not including absent data elements.

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
- **Classification**: Hybrid
  - **Reason**: The test involves both automated checks to ensure the presence of the `dataAbsentReason` extension and manual inspection to verify the appropriate use of nullFlavors or other values from the value set.

### Complexity
- **Complexity**: Moderate
  - **Reason**: While the presence of the `dataAbsentReason` can be automatically checked, verifying the correct application of values from a value set requires a deeper understanding of the context and potentially manual inspection.

### Prerequisites
- **System Configurations**: The server must be configured to support the dataAbsentReason extension and the relevant value set for nullFlavors.
- **Data Setup**: The server must have resources with data elements where the minimum cardinality is greater than 0, and some of these elements should intentionally have missing information.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A FHIR resource with a data element that has a minimum cardinality >0 and is missing information.
- **Expected Outputs**: 
  - The resource should include the `dataAbsentReason` extension or a value from the specified value set indicating the reason for the absence of data.

### Required FHIR Operations
- **FHIR Operations**: 
  - `GET` operation to retrieve resources from the server.
  - `POST` or `PUT` operation to create or update resources with missing data elements to test the server's response.

### Test Data Requirements
- **Test Data**: 
  - Resources with required elements that are intentionally left blank to trigger the use of `dataAbsentReason`.
  - Examples of resources could include Patient, Observation, or any other resource with mandatory fields.

### Validation Criteria
- **Validation Checks**:
  1. **Presence Check**: Verify that the `dataAbsentReason` extension is present for any required data element that is missing.
  2. **Value Set Check**: Confirm that the value used for `dataAbsentReason` is from the specified value set (e.g., nullFlavors).
  3. **Conformance Check**: Ensure that the server's response conforms to the FHIR specification and the implementation guide's requirements.
  4. **Manual Inspection**: Review a sample of resources to ensure that the reasons for missing data are appropriate and correctly applied.

- **Assertions**:
  - Assert that the `dataAbsentReason` extension is correctly applied for all missing required data elements.
  - Assert that the values used are valid according to the specified value set.
  - Assert that the server correctly processes and returns resources with missing data elements and appropriate `dataAbsentReason` extensions.

By following this test specification, the conformance to the REQ-05 requirement can be effectively verified.
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
  - The requirement to support JSON format for all Plan-Net interactions can be tested using automated scripts that validate JSON responses from the server.

### Complexity
- **Complexity Level**: Moderate
  - While JSON format support is a standard feature, ensuring that all Plan-Net interactions consistently support JSON requires comprehensive testing across multiple endpoints.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to handle HTTP requests and respond with JSON formatted data.
- **Data Setup**:
  - A set of predefined Plan-Net resources must be available on the server to test against.
- **Environment**:
  - Access to a test environment where the server is deployed and accessible.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - HTTP GET requests to all Plan-Net interaction endpoints.
- **Expected Outputs**:
  - HTTP responses with a status code of 200 (OK) and a body formatted in JSON.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/PlanDefinition`
  - `GET [base]/HealthcareService`
  - `GET [base]/Location`
  - `GET [base]/Organization`
  - `GET [base]/Practitioner`
  - `GET [base]/PractitionerRole`
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - A variety of Plan-Net resources (e.g., PlanDefinition, HealthcareService) with different attributes to ensure comprehensive testing of JSON output.

### Validation Criteria
- **Specific Checks**:
  - Verify that each response is in JSON format by checking the `Content-Type` header is `application/json`.
  - Validate that the JSON response is well-formed and adheres to the expected FHIR resource structure.
  - Ensure that all required fields for each resource type are present and correctly populated.
  - Confirm that the server handles invalid requests gracefully, returning appropriate error messages in JSON format.
- **Assertions**:
  - Assert that the response status code is 200 for valid requests.
  - Assert that the JSON response matches the expected schema for each Plan-Net resource type.
  - Assert that error responses for invalid requests are also in JSON format with appropriate error details.

```


---

<a id='req-11'></a>

### REQ-11: RESTful behavior implementation

**Description**: "Implement the RESTful behavior according to the FHIR specification."

**Actor**: Server

**Conformance**: SHALL

# Test Specification for Requirement REQ-11

## 1. Requirement ID
- **REQ-11**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Hybrid
  - **Reasoning**: While many aspects of RESTful behavior can be tested automatically through API calls and responses, some elements may require manual inspection to ensure adherence to the FHIR specification, such as correct implementation of HTTP methods and status codes.

### Complexity
- **Complexity**: Moderate
  - **Reasoning**: Implementing RESTful behavior involves multiple HTTP methods and status codes, each with specific requirements according to the FHIR specification. This requires a comprehensive understanding of the FHIR RESTful API guidelines.

### Prerequisites
- **System Configurations**: 
  - A FHIR server instance configured to support RESTful operations.
  - Network access to the server for testing.
- **Data Setup**:
  - Preloaded FHIR resources on the server to test various RESTful operations (e.g., Patient, Observation).
- **Setup**:
  - Ensure the server is running and accessible.
  - Ensure that the server's Capability Statement is available and reflects support for required RESTful operations.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - HTTP requests for each RESTful operation (GET, POST, PUT, DELETE) on various FHIR resources.
- **Expected Outputs**:
  - Correct HTTP status codes (e.g., 200, 201, 204, 400, 404).
  - Correct resource representations in the response body.
  - Appropriate handling of errors and exceptions.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resourceType]` - Retrieve a list of resources.
  - `GET [base]/[resourceType]/[id]` - Retrieve a specific resource by ID.
  - `POST [base]/[resourceType]` - Create a new resource.
  - `PUT [base]/[resourceType]/[id]` - Update an existing resource.
  - `DELETE [base]/[resourceType]/[id]` - Delete a specific resource by ID.

### Test Data Requirements
- **Test Data**:
  - Sample FHIR resources for each type being tested (e.g., Patient, Observation).
  - Valid and invalid resource representations to test error handling.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server responds with the correct HTTP status codes for each operation.
  - Confirm that resource representations in responses match the FHIR specification.
  - Check that the server's Capability Statement includes support for the tested operations.
  - Ensure that error responses include appropriate OperationOutcome resources as per FHIR guidelines.
  - Validate that the server correctly handles conditional requests (e.g., If-None-Match, If-Modified-Since headers).

By following this test specification, testers can systematically verify the implementation of RESTful behavior on a FHIR server, ensuring compliance with the FHIR specification and the server's Capability Statement.

---

<a id='req-12'></a>

### REQ-12: Support for all Implementation Guide profiles

**Description**: "Support all profiles defined in this Implementation Guide."

**Actor**: Server

**Conformance**: SHALL

# Test Specification for Requirement REQ-12

## 1. Requirement ID
- **REQ-12**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement to support all profiles can be tested automatically by validating the server's capability to handle requests and responses according to the profiles defined in the Implementation Guide.

### Complexity
- **Complexity Level**: Complex
  - The complexity arises from the need to validate multiple profiles, each potentially having different structures, constraints, and validation rules.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to expose all the profiles defined in the Implementation Guide.
  - The server's CapabilityStatement must list all supported profiles.
- **Data Setup**: 
  - Test data must be available for each profile to ensure comprehensive testing.
  - The server must have access to a FHIR-compliant data store.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A list of all profiles defined in the Implementation Guide.
  - Sample FHIR resources conforming to each profile.
- **Expected Outputs**:
  - Successful validation of resources against each profile.
  - The server's CapabilityStatement correctly lists all profiles.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/metadata`: To retrieve the server's CapabilityStatement and verify supported profiles.
  - `POST [base]/[ResourceType]`: To create resources and test profile conformance.
  - `GET [base]/[ResourceType]/[id]`: To retrieve resources and verify they conform to the expected profiles.

### Test Data Requirements
- **Test Data**:
  - Valid FHIR resources for each profile defined in the Implementation Guide.
  - Resources should cover various scenarios, including edge cases, to ensure thorough testing.

### Validation Criteria
- **Conformance Verification**:
  - The server's CapabilityStatement must list all profiles defined in the Implementation Guide.
  - Each test resource must be successfully created and retrieved, conforming to its respective profile.
  - The server should return appropriate error messages for resources that do not conform to the profiles.
- **Assertions**:
  - Assert that the server supports all profiles by checking the CapabilityStatement.
  - Assert that resources can be created and retrieved while maintaining conformance to their profiles.
  - Assert that non-conforming resources are rejected with detailed error messages.

By following this test specification, we ensure that the server meets the requirement to support all profiles defined in the Implementation Guide, thereby achieving interoperability and compliance with the specified FHIR standards.

---

<a id='req-13'></a>

### REQ-13: Unauthorized request response

**Description**: "Return the following response classes: (Status 401/4xx): unauthorized request."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for FHIR Implementation Guide Requirement

## 1. Requirement ID
- **REQ-13**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - This requirement can be tested automatically by simulating unauthorized requests and verifying the server's response.

### Complexity
- **Complexity Level**: Simple
  - The requirement involves checking for a specific HTTP status code, which is straightforward.

### Prerequisites
- **System Configurations**: 
  - The server must be running and accessible.
  - The server should be configured to require authentication for access to protected resources.
- **Data Setup**: 
  - No specific data setup is required, as the test focuses on unauthorized access.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - An HTTP request to a protected FHIR resource without valid authentication credentials.
- **Expected Outputs**: 
  - The server should return an HTTP response with a status code of 401 (Unauthorized) or another 4xx status code indicating unauthorized access.

### Required FHIR Operations
- **API Calls/Operations**:
  - Perform a `GET` operation on a protected FHIR resource endpoint without including authentication headers or with invalid credentials.
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**: 
  - No specific patient or resource data is required since the test focuses on authentication failure.
  - Use generic resource endpoints that require authentication.

### Validation Criteria
- **Specific Checks**:
  - Verify that the HTTP status code in the response is 401 or another appropriate 4xx code for unauthorized access.
  - Check that the response includes a WWW-Authenticate header indicating the type of authentication required (if applicable).
  - Ensure no sensitive data is returned in the response body when unauthorized access is attempted.
```


---

<a id='req-14'></a>

### REQ-14: Insufficient scope response

**Description**: "Return the following response classes: (Status 403): insufficient scope."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for FHIR Implementation Guide Requirement

## 1. Requirement ID
- **REQ-14**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The test can be automated by simulating API requests and checking the HTTP response status code.

### Complexity
- **Complexity**: Simple
  - The requirement involves checking for a specific HTTP response status, which is straightforward.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to enforce scope-based access control.
- **Data**: 
  - User accounts with varying scopes of access.
- **Setup**: 
  - Ensure that the server is running and accessible.
  - Ensure that the server's capability statement includes support for scope-based access control.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - API request with insufficient scope (e.g., a request with a token that lacks the necessary permissions).
- **Expected Outputs**:
  - HTTP response with status code 403 and a message indicating "insufficient scope."

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resource]` (e.g., `GET /Patient`) with an authorization token that has insufficient scope.
  - Ensure these operations are supported as per the server's capability statement.

### Test Data Requirements
- **Test Data**:
  - Authorization tokens with varying scopes:
    - Token with sufficient scope (for control comparison).
    - Token with insufficient scope (for testing the requirement).

### Validation Criteria
- **Specific Checks**:
  - Verify that the server returns an HTTP 403 status code when a request is made with insufficient scope.
  - Check that the response body contains a message or indication of "insufficient scope."
  - Ensure that requests with sufficient scope do not return a 403 status code, confirming correct scope handling.
```


---

<a id='req-15'></a>

### REQ-15: Invalid parameter response

**Description**: "Return the following response classes: (Status 400): invalid parameter."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for Requirement REQ-15

## 1. Requirement ID
- **REQ-15**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement can be tested programmatically by sending requests with invalid parameters and verifying the server's response.

### Complexity
- **Complexity**: Simple
  - The requirement involves straightforward validation of server response to invalid input.

### Prerequisites
- **System Configuration**: 
  - The FHIR server must be operational and accessible.
  - The server must support the operations specified in the Capability Statement.
- **Data/Setup**: 
  - No specific data setup is required as the test involves invalid parameters.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A set of API requests with intentionally invalid parameters.
- **Expected Outputs**: 
  - HTTP status code 400 with a response indicating "invalid parameter."

### Required FHIR Operations
- **FHIR Operations**:
  - Any FHIR operation that accepts parameters (e.g., `search`, `read`, `update`, `create`) as supported by the server's Capability Statement.

### Test Data Requirements
- **Test Data**:
  - Construct requests with parameters that are:
    - Not defined in the FHIR specification.
    - Incorrectly formatted (e.g., wrong data type).
    - Out of valid range if applicable.

### Validation Criteria
- **Validation Checks**:
  - Verify that the server returns a 400 HTTP status code.
  - Check the response body for an OperationOutcome resource indicating the nature of the invalid parameter.
  - Ensure that the error message clearly states "invalid parameter" and provides details on the parameter issue.
```


---

<a id='req-16'></a>

### REQ-16: Unknown resource response

**Description**: "Return the following response classes: (Status 404): unknown resource."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for Requirement REQ-16

## 1. Requirement ID
- **REQ-16**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement involves verifying the server's response to a specific condition (unknown resource), which can be efficiently tested using automated scripts.

### Complexity
- **Complexity**: Simple
  - The test involves a straightforward verification of HTTP status code and message when accessing a non-existent resource.

### Prerequisites
- **System Configurations**: 
  - A FHIR server instance must be available and accessible for testing.
  - The server must be configured to handle HTTP requests and return appropriate status codes.
- **Data/Setup**:
  - No specific data setup is required as the test involves accessing a non-existent resource.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Input**: 
  - An HTTP GET request to a non-existent FHIR resource endpoint (e.g., `/Patient/nonexistent-id`).
- **Expected Output**: 
  - HTTP Status Code: 404
  - Response Body: A message indicating "unknown resource" or similar wording as per server implementation.

### Required FHIR Operations
- **API Calls/Operations**:
  - HTTP GET operation on a resource that does not exist in the server's database.
  - Ensure the server supports the GET operation as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - No actual FHIR resource data is required since the test targets a non-existent resource.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server returns an HTTP 404 status code when a request is made to a non-existent resource.
  - Check that the response body contains a message indicating the resource is unknown.
  - Ensure the response conforms to the FHIR standard for error responses, including appropriate headers and structure.

- **Assertions**:
  - Assert that the HTTP status code is 404.
  - Assert that the response body includes an error message related to an unknown resource.
  - Assert that the response format adheres to FHIR error response standards.

By following this test specification, testers can ensure that the FHIR server correctly handles requests for unknown resources, thereby conforming to the specified requirement.
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
  - The test can be automated as it involves verifying HTTP response status codes.

### Complexity
- **Complexity**: Simple
  - The test involves straightforward HTTP status code verification.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server must support the DELETE operation as per the Capability Statement.
- **Data Setup**:
  - A resource that can be safely deleted for testing purposes.
  - Ensure the resource is initially present on the server.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Input**: 
  - A valid FHIR resource ID that exists on the server and can be deleted.
- **Expected Output**: 
  - HTTP Status Code 410 (Gone) when attempting to access the deleted resource.

### Required FHIR Operations
- **FHIR Operations**:
  - `DELETE [base]/[resourceType]/[id]`: To delete the resource.
  - `GET [base]/[resourceType]/[id]`: To attempt retrieval of the deleted resource and verify the response.

### Test Data Requirements
- **Test Data**:
  - A resource of any type (e.g., Patient, Observation) that is pre-existing on the server and can be used for deletion testing.

### Validation Criteria
- **Validation Checks**:
  1. **Delete Operation**: 
     - Perform a DELETE operation on the specified resource.
     - Verify that the DELETE operation returns a successful status code (e.g., 204 No Content or 200 OK).
  2. **Access Deleted Resource**:
     - Perform a GET operation on the same resource ID after deletion.
     - Assert that the server returns HTTP Status Code 410 (Gone).
     - Ensure that the response does not contain the resource data.

- **Assertions**:
  - The server must return a 410 status code when accessing a deleted resource, indicating conformance to the requirement.
```


---

<a id='req-18'></a>

### REQ-18: Profile identification in meta attribute

**Description**: "Identify the Plan-Net profiles supported as part of the FHIR meta.profile attribute for each instance."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for REQ-18: Profile Identification in Meta Attribute

## 1. Requirement ID
- **REQ-18**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement involves verifying the presence and correctness of profile URIs in the `meta.profile` attribute, which can be automated through API testing tools.

### Complexity
- **Complexity**: Simple
  - The test involves straightforward validation of the `meta.profile` attribute in FHIR resource instances.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server should have implemented the Plan-Net profiles.

- **Data Setup**:
  - Instances of resources that are expected to conform to the Plan-Net profiles should be available on the server.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - FHIR resource instances that are expected to conform to Plan-Net profiles.

- **Expected Outputs**:
  - Each resource instance should contain the correct Plan-Net profile URI(s) in the `meta.profile` attribute.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resourceType]/[id]` to retrieve specific resource instances.
  - `GET [base]/[resourceType]` to search and retrieve multiple resource instances.

### Test Data Requirements
- **Test Data**:
  - Resource instances that are supposed to conform to specific Plan-Net profiles.
  - The profiles should be clearly defined and documented, with their URIs available for validation.

### Validation Criteria
- **Specific Checks**:
  - Verify that the `meta.profile` attribute is present in the resource instance.
  - Validate that the `meta.profile` attribute contains the correct URI(s) for the Plan-Net profiles.
  - Ensure that the profile URIs are valid and match the expected format and value as per the Plan-Net specification.

- **Assertions**:
  - Assert that the `meta.profile` attribute is not empty.
  - Assert that all required Plan-Net profile URIs are included in the `meta.profile` attribute.
  - Assert that the profile URIs are correctly formatted and resolve to the expected profiles.

By following this test specification, the conformance of the FHIR server to the requirement of identifying Plan-Net profiles in the `meta.profile` attribute can be effectively validated.
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
  - The requirement can be tested using automated scripts to verify the support of search parameters on each profile.

### Complexity
- **Classification**: Moderate
  - While the implementation of search parameters is straightforward, verifying them across multiple profiles requires comprehensive test coverage.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server must have the necessary profiles implemented as per the FHIR Implementation Guide.
- **Data Setup**:
  - The server must contain sample data for each profile to ensure search operations can be performed.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A list of profiles supported by the server.
  - A list of search parameters defined for each profile.
- **Expected Outputs**:
  - Successful execution of search operations using each search parameter on the respective profile.
  - Correct and expected search results returned by the server.

### Required FHIR Operations
- **API Calls**:
  - `GET [base]/[resource]?parameter=value`
    - Ensure the server's Capability Statement includes support for the `search` operation on each profile.
  - `GET [base]/metadata`
    - Retrieve the server's Capability Statement to confirm supported profiles and operations.

### Test Data Requirements
- **Data Types**:
  - Sample resources for each profile with varied attributes to test different search parameters.
  - Data should cover edge cases, such as maximum and minimum values, and typical use cases.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server returns a `200 OK` status code for each search operation.
  - Confirm that the search results match the expected output based on the provided search parameters.
  - Check that unsupported search parameters result in an appropriate error message (e.g., `400 Bad Request`).
  - Ensure that the Capability Statement lists all profiles and their supported search parameters.
  - Validate that the search results are consistent with the data present in the server for the given profile.

By following this test specification, you can systematically verify that the FHIR server supports search parameters on each profile individually, as required by the Implementation Guide.
```

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
- **Classification**: Automatic
  - The requirement involves verifying the server's ability to handle combination search parameters, which can be tested using automated scripts to perform and validate search operations.

### Complexity
- **Complexity Level**: Moderate
  - While the concept of search is straightforward, the combination of multiple search parameters across different profiles adds complexity to the testing process.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server must have implemented the necessary search capabilities as outlined in its Capability Statement.
- **Data Setup**:
  - The server must contain sufficient data for each profile to test various combinations of search parameters effectively.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A set of search parameter combinations for each profile defined in the FHIR Implementation Guide.
  - Example search queries that combine multiple parameters (e.g., `Patient?name=John&birthdate=1980-01-01`).

- **Expected Outputs**:
  - A list of resources that match the search criteria for each combination of search parameters.
  - The response should conform to the FHIR search response format, including correct status codes and resource bundles.

### Required FHIR Operations
- **FHIR Operations**:
  - `GET [base]/[resource]?[parameters]`: Perform search operations using the combination of search parameters.
  - Ensure that the server supports these operations as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - A diverse dataset that includes multiple instances of each profile type with varying attributes to test different search parameter combinations.
  - Ensure that the dataset includes edge cases, such as resources with missing or null values for certain attributes.

### Validation Criteria
- **Validation Checks**:
  - Verify that the server returns the correct resources matching the search criteria for each combination of parameters.
  - Check that the response includes the expected HTTP status code (e.g., 200 OK for successful searches).
  - Ensure that the response bundle structure adheres to the FHIR specification.
  - Validate that the search results are consistent with the data in the server, including correct handling of edge cases and null values.
  - Confirm that the server handles invalid or unsupported parameter combinations gracefully, returning appropriate error messages or status codes.

By following this structured test specification, testers can systematically verify the server's compliance with the combination search parameter requirement, ensuring robust support for complex search scenarios.

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
- **Classification**: Automatic
  - The requirement can be tested using automated scripts to verify the server's ability to handle forward chaining on search parameters.

### Complexity
- **Complexity Level**: Moderate
  - While the concept of forward chaining is straightforward, ensuring comprehensive coverage across all search parameters with the 'chain' property requires careful planning and execution.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to support search operations as per the FHIR specification.
- **Data Setup**: 
  - The server must have sufficient data that includes resources with relationships that can be used to demonstrate forward chaining.
  - Ensure that the Capability Statement of the server indicates support for search operations and chaining.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A set of FHIR search queries that utilize the 'chain' property on various search parameters.
- **Expected Outputs**: 
  - Successful execution of search queries with correct results that demonstrate the ability to follow resource references as specified by the chain.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resource]?parameter.chain=...`
  - Ensure these operations are supported in the server's Capability Statement under the search interaction.

### Test Data Requirements
- **Test Data**:
  - Resources with known relationships that can be used to test chaining, such as:
    - Patients with linked Observations
    - Practitioners with linked Encounters
    - Conditions with linked Medications

### Validation Criteria
- **Specific Checks**:
  - Verify that the server returns the correct resources when a chained search is performed.
  - Ensure that the server handles multiple levels of chaining correctly.
  - Confirm that the server returns appropriate error messages or status codes if chaining is not supported or if the chain is invalid.
  - Assertions should include:
    - The response status code is `200 OK`.
    - The response contains the expected resources.
    - The response time is within acceptable limits for performance.
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
- **Classification**: Automatic
  - The requirement can be tested using automated scripts that perform API calls and validate responses against expected results.

### Complexity
- **Complexity**: Moderate
  - While the concept of reverse chaining is straightforward, ensuring comprehensive coverage across all applicable search parameters adds complexity.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be configured to support reverse chaining as per the implementation guide.
- **Data Setup**: 
  - The server must have sufficient data that includes resources with relationships that can be used to test reverse chaining.
  - Ensure that the FHIR server's Capability Statement includes support for the search parameters with the 'chain' property.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A list of search parameters that specify the 'chain' property.
  - Example FHIR resources that can be used to demonstrate reverse chaining (e.g., Patient, Observation, Encounter).
- **Expected Outputs**:
  - Correctly filtered and linked resources in response to reverse chaining search queries.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resource]?_has:[relatedResource]:[searchParam]:[value]`
  - Verify that the server supports these operations as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - A set of FHIR resources with known relationships, such as:
    - Patients with linked Observations
    - Encounters linked to specific Patients
  - Ensure that the data includes various scenarios to test different reverse chaining paths.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server returns the correct resources when a reverse chaining query is executed.
  - Assertions should include:
    - The response contains the expected resources based on the reverse chain.
    - The response status code is `200 OK`.
    - The response structure conforms to the FHIR specification.
  - Check for performance and response time to ensure the server handles reverse chaining efficiently.
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
- **Classification**: Automatic
  - The requirement to support XML format can be tested programmatically by sending requests and verifying responses in XML format.

### Complexity
- **Complexity Level**: Moderate
  - While the task of supporting XML is straightforward, ensuring that all Plan-Net interactions are correctly formatted and validated in XML adds a layer of complexity.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to accept and respond with XML formatted data.
- **Data Setup**: 
  - Access to a test environment where Plan-Net interactions can be executed.
- **Setup**: 
  - Ensure that the server's Capability Statement includes support for XML format in the 'format' element.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A set of Plan-Net interaction requests formatted in XML.
- **Expected Outputs**: 
  - Responses from the server in XML format, correctly structured according to the FHIR XML schema.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET` and `POST` operations for Plan-Net resources (e.g., `Location`, `HealthcareService`, `Organization`) as specified in the Capability Statement.
  - Ensure these operations are listed as supported in the server's Capability Statement.

### Test Data Requirements
- **Test Data**:
  - Sample XML requests for each Plan-Net interaction type.
  - Valid Plan-Net resource instances in XML format to be used in requests.

### Validation Criteria
- **Conformance Checks**:
  - Verify that the server's response is in XML format.
  - Validate the XML response against the FHIR XML schema to ensure it is well-formed and adheres to the FHIR standard.
  - Check that the server's Capability Statement lists XML as a supported format under the 'format' element.
  - Ensure that all required elements for each Plan-Net interaction are present and correctly populated in the XML response.
  - Confirm that the server handles XML requests and responses without errors.

- **Assertions**:
  - The server returns HTTP status code 200 for successful XML interactions.
  - The XML response matches the expected structure and content for the requested Plan-Net interaction.
  - Any error responses should be correctly formatted in XML and provide meaningful error messages.

By following this test specification, the requirement for XML format support in all Plan-Net interactions can be systematically verified.
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
  - The requirement can be tested using automated scripts that simulate unauthorized requests to the server and verify the response.

### Complexity
- **Complexity**: Simple
  - The requirement involves checking for a specific HTTP response code, which is straightforward to implement and verify.

### Prerequisites
- **System Configurations**: 
  - The server must be running and accessible over the network.
  - The server should have authentication mechanisms configured.
- **Data/Setup**:
  - Ensure that there are no valid authentication tokens or credentials used in the request.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - An HTTP request to the FHIR server without authentication credentials or with invalid credentials.
- **Expected Outputs**:
  - The server responds with an HTTP 401 Unauthorized status code.

### Required FHIR Operations
- **API Calls/Operations**:
  - Any FHIR RESTful operation (e.g., `GET`, `POST`, `PUT`, `DELETE`) can be used to test unauthorized access. Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - No specific FHIR resource data is required since the test focuses on authentication. However, a known endpoint (e.g., `/Patient`) should be used for the request.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server returns an HTTP 401 Unauthorized response code.
  - Check that the response does not include any sensitive information.
  - Ensure that the response includes the `WWW-Authenticate` header, as per HTTP standards, indicating the authentication scheme used by the server.

- **Assertions**:
  - Assert that the response status code is 401.
  - Assert that the `WWW-Authenticate` header is present in the response.
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
  - The requirement is suitable for automated testing as it involves verifying the server's ability to perform read interactions on various resource types and profiles.

### Complexity
- **Complexity**: Moderate
  - While the read interaction itself is straightforward, the need to test across multiple resource types and profiles increases the complexity.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to expose the FHIR API endpoints for all resource types and profiles defined in the implementation guide.
- **Data Setup**: 
  - Ensure that the server contains a representative set of FHIR resources for each type and profile to be tested.
  - The server should have valid authentication and authorization mechanisms in place if required.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - FHIR resource identifiers (IDs) for each resource type and profile.
- **Expected Outputs**: 
  - Successful HTTP status code (200 OK) and a valid FHIR resource in the response body for each read interaction.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resourceType]/[id]` for each resource type and profile.
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - A set of FHIR resource IDs for each resource type and profile that are expected to exist on the server.
  - Each resource should be in a valid state and conform to the specified profile.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server returns a 200 OK status code for each read operation.
  - Validate that the returned resource matches the expected resource type and conforms to the specified profile.
  - Ensure the resource content is complete and correctly formatted according to FHIR standards.
  - Check that any required elements defined in the profiles are present in the returned resource.

- **Assertions**:
  - The server responds with a valid FHIR resource for each read request.
  - The resource content matches the expected structure and data as per the profile.
  - No unexpected errors or status codes are returned during the read operations.
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
  - The vread interaction can be tested programmatically by issuing HTTP requests and evaluating the responses.

### Complexity
- **Complexity Level**: Moderate
  - While the vread interaction itself is straightforward, testing it across multiple resource types and profiles increases complexity.

### Prerequisites
- **System Configurations**: 
  - Access to a Plan Net server with vread capabilities enabled.
  - Network access to the server for sending HTTP requests.
- **Data Setup**:
  - Ensure that the server has resources available for each type and profile that support vread.
  - Each resource should have at least one versioned instance available.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Resource type and ID
  - Specific version ID of the resource
- **Expected Outputs**:
  - HTTP Status Code: 200 OK
  - Resource: The specific version of the resource matching the requested version ID
  - Correct FHIR resource format and content as per the requested version

### Required FHIR Operations
- **vread Operation**:
  - HTTP GET request to `[base]/[resourceType]/[id]/_history/[versionId]`
  - Ensure the Capability Statement includes support for the vread operation for applicable resources.

### Test Data Requirements
- **Test Data**:
  - A set of resources for each type and profile that support vread, each with multiple versions.
  - Version IDs for each resource to test specific version retrieval.

### Validation Criteria
- **HTTP Response Validation**:
  - Verify the response status code is 200 OK.
  - Confirm the response body contains the correct version of the resource.
  - Validate the resource content against the expected FHIR profile and version.
- **Error Handling**:
  - Test for proper error responses (e.g., 404 Not Found) when requesting non-existent resource versions.
- **Conformance Check**:
  - Ensure the server's Capability Statement lists vread as a supported interaction for the tested resource types.

```
This test specification outlines the necessary steps and considerations to verify that a Plan Net server supports the vread interaction for each resource type and profile, in accordance with the FHIR Implementation Guide requirement REQ-26. The test is designed to be automated, leveraging HTTP requests to validate server behavior against expected outcomes.

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
- **Classification**: Automatic
  - The requirement can be tested using automated scripts that execute FHIR API calls and validate responses.

### Complexity
- **Classification**: Moderate
  - Testing involves multiple FHIR resources and verifying the inclusion of related resources in the response.

### Prerequisites
- **System Configurations**: 
  - A FHIR server with the capability to process `_include` parameters.
  - Access to the server's Capability Statement to verify supported resources and operations.
- **Data Setup**: 
  - Pre-existing FHIR resources that are linked (e.g., Patient, Encounter, Observation) to test the `_include` functionality.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - FHIR search queries with `_include` parameters for various resources.
- **Expected Outputs**: 
  - Responses that include the primary resource and the specified related resources.

### Required FHIR Operations
- **Operations**:
  - `GET [base]/[resource]?_include=[relatedResource]`
  - Ensure the server's Capability Statement lists support for the `_include` parameter for the relevant resources.

### Test Data Requirements
- **Test Data**:
  - A set of FHIR resources with known relationships. For example:
    - A Patient resource with linked Encounter resources.
    - An Encounter resource with linked Observation resources.

### Validation Criteria
- **Criteria**:
  - The server returns a bundle containing the primary resource and the related resources specified by the `_include` parameter.
  - Verify that the response bundle contains all expected included resources.
  - Check that the server's response time is within acceptable limits for performance.
  - Confirm that the server's Capability Statement correctly advertises support for the `_include` parameter for the tested resources.

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
  - The requirement can be tested automatically by executing FHIR API calls and validating responses against expected outcomes.

### Complexity
- **Complexity**: Moderate
  - While the concept of _revincludes is straightforward, ensuring comprehensive coverage across all specified resources adds complexity.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to support FHIR API interactions.
  - Ensure the server's Capability Statement indicates support for _revincludes.
- **Data Setup**:
  - Populate the server with a diverse set of FHIR resources that have relationships suitable for testing _revincludes.
  - Ensure resources are linked appropriately to test reverse inclusion.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A list of FHIR resource types to test _revincludes on.
  - Specific _revincludes parameters to be tested, as defined in the Implementation Guide.
- **Expected Outputs**:
  - The server should return resources that are linked back to the primary resource through the specified _revincludes parameter.

### Required FHIR Operations
- **FHIR Operations**:
  - `GET [base]/[resource]?_id=[id]&_revincludes=[parameter]`
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - A set of FHIR resources with known relationships that can be used to test _revincludes.
  - Example: Patients with related Observations, Encounters, or other linked resources.

### Validation Criteria
- **Validation Checks**:
  - Verify that the response includes the primary resource and all resources that reference it via the specified _revincludes parameter.
  - Confirm that the response structure adheres to FHIR standards.
  - Check for correct handling of edge cases, such as no resources matching the _revincludes criteria.
  - Ensure performance and response time are within acceptable limits for the server's specifications.

- **Assertions**:
  - The response contains the expected number of resources.
  - The resources returned are correctly linked as per the _revincludes parameter.
  - The server returns appropriate error messages for unsupported _revincludes parameters.

By following this test specification, we can ensure that the server meets the requirement to support _revincludes as mandated by the FHIR Implementation Guide.
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
  - The requirement can be tested automatically by querying the server for Organization resources and verifying the presence or absence of NPI and CLIA identifiers based on the organization type.

### Complexity
- **Complexity**: Moderate
  - The complexity arises from the need to differentiate between provider organizations and other organization types, and to verify the correct handling of NPI and CLIA identifiers.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server must support the necessary FHIR operations as per the Capability Statement.
- **Data Setup**:
  - The server must have Organization resources with varying types (e.g., provider organizations and non-provider organizations).

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A query to retrieve Organization resources from the FHIR server.
- **Expected Outputs**:
  - Provider organizations should have NPI and CLIA identifiers populated.
  - Non-provider organizations should not have NPI and CLIA identifiers populated.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Organization` - Retrieve all Organization resources.
  - `GET [base]/Organization/{id}` - Retrieve specific Organization resources by ID if needed for detailed verification.

### Test Data Requirements
- **Test Data**:
  - A diverse set of Organization resources that include:
    - At least one provider organization with NPI and CLIA identifiers.
    - At least one non-provider organization without NPI and CLIA identifiers.

### Validation Criteria
- **Specific Checks**:
  - For each Organization resource retrieved:
    - If the organization type is a provider, assert that NPI and CLIA identifiers are present and correctly formatted.
    - If the organization type is not a provider, assert that NPI and CLIA identifiers are absent.
- **Assertions**:
  - The test passes if all provider organizations have the required identifiers and all non-provider organizations do not have these identifiers.
  - The test fails if any provider organization lacks the identifiers or any non-provider organization has them.

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
- **Classification**: Automatic
  - The requirement can be tested using automated scripts to verify the presence of the `lastUpdate` timestamp in the profile's data content.

### Complexity
- **Complexity Level**: Simple
  - The requirement involves checking for the presence of a timestamp field, which is straightforward.

### Prerequisites
- **System Configurations**: 
  - The server must be running and accessible with the necessary FHIR profiles implemented.
- **Data Setup**: 
  - Profiles that are expected to contain the `lastUpdate` timestamp must be available on the server.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - FHIR profiles from the server that are specified in the implementation guide.
- **Expected Outputs**: 
  - Each profile must include a `lastUpdate` timestamp in its data content.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[ProfileType]/[id]` - Retrieve specific profiles to check for the `lastUpdate` timestamp.
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - A set of profiles that are expected to be compliant with the implementation guide.
  - Profiles should be varied to ensure comprehensive coverage (e.g., different resource types, different states of data).

### Validation Criteria
- **Checks**:
  - Verify that each retrieved profile contains a `lastUpdate` field.
  - The `lastUpdate` field should be a valid timestamp format (e.g., ISO 8601).
  - Ensure that the `lastUpdate` field is not null or empty.
  
- **Assertions**:
  - Assert that the `lastUpdate` timestamp is present in the profile data.
  - Assert that the timestamp is in a valid format.
  - Assert that the timestamp reflects a reasonable and expected update time (e.g., not a future date).

By following this test specification, the requirement REQ-30 can be effectively validated to ensure compliance with the FHIR Implementation Guide.
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
- **REQ-32**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - This requirement involves verifying search functionality, which can be tested programmatically using automated scripts to simulate search requests and validate responses.

### Complexity
- **Complexity Level**: Moderate
  - The requirement involves multiple search parameters and conditions that need to be validated, making it moderately complex.

### Prerequisites
- **System Configurations**: 
  - A FHIR server implementing the Plan-Net design with the necessary resources (HealthcareService, Location) and search capabilities.
- **Data Setup**:
  - Pre-loaded test data including HealthcareService resources with various categories and specialties, and Location resources with different addresses and networks.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Search requests for HealthcareService resources with specified `category` and `specialty`.
  - Optional search qualifiers: `Location` and `network`.

- **Expected Outputs**:
  - Correct subset of HealthcareService resources that match the search criteria.
  - Responses should include resources with the specified `category` and `specialty`, filtered by `Location` and `network` if provided.

### Required FHIR Operations
- **FHIR Operations**:
  - `GET [base]/HealthcareService?category=[value]&specialty=[value]`
  - `GET [base]/HealthcareService?category=[value]&specialty=[value]&location=[reference]`
  - `GET [base]/HealthcareService?category=[value]&specialty=[value]&network=[reference]`

### Test Data Requirements
- **HealthcareService Resources**:
  - At least one resource for each category and specialty combination to be tested.
  - Resources should be associated with different locations and networks.

- **Location Resources**:
  - Resources with varying `address-city`, `address-state`, and `address-postalcode` to test location-based filtering.

### Validation Criteria
- **Conformance Checks**:
  - Verify that the search results include only HealthcareService resources matching the specified `category` and `specialty`.
  - Ensure that additional filters by `Location` and `network` correctly narrow down the search results.
  - Validate that the response structure adheres to FHIR standards and includes necessary elements like `resourceType`, `id`, and `meta`.

- **Assertions**:
  - Assert that the response status code is `200 OK`.
  - Assert that the number of resources returned matches the expected count based on the test data setup.
  - Assert that each returned resource contains the specified `category` and `specialty` values.

By following this structured test specification, the implementation of the general search functionality for pharmacies can be thoroughly validated against the FHIR Implementation Guide requirements.
```

---

<a id='req-33'></a>

### REQ-33: Provider search by name

**Description**: "The Plan-Net design is based around the following types of searches: Provider by Name - Example: Joe Smith - Focal Resource and Field: Practitioner.name - Qualifications of Search: Location, network, specialty, role/privileges."

**Actor**: Server

**Conformance**: None (Design requirement)

```markdown
# Test Specification for Requirement REQ-33

## 1. Requirement ID
- **REQ-33**: Provider search by name

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement can be tested using automated scripts to perform searches and verify results.

### Complexity
- **Complexity Level**: Moderate
  - The test involves multiple search parameters and requires validation against specific criteria such as location, network, specialty, and role/privileges.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server must support the Practitioner resource and the specified search parameters.
- **Data Setup**:
  - The server must have Practitioner resources populated with diverse data, including names, locations, networks, specialties, and roles/privileges.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Search query for Practitioner by name, e.g., "Joe Smith".
  - Optional filters: location, network, specialty, role/privileges.
- **Expected Outputs**:
  - A list of Practitioner resources matching the search criteria.
  - Each result should include relevant details such as name, location, network, specialty, and role/privileges.

### Required FHIR Operations
- **API Calls**:
  - `GET [base]/Practitioner?name=[name]`
  - Optional: Add filters such as location, network, specialty, and role/privileges if supported by the server.

### Test Data Requirements
- **Practitioner Data**:
  - Practitioners with varying names, including "Joe Smith".
  - Practitioners associated with different locations, networks, specialties, and roles/privileges.
- **Location Data**:
  - Locations with diverse attributes to test filtering capabilities.

### Validation Criteria
- **Conformance Checks**:
  - Verify that the search returns Practitioners with the specified name.
  - Check that optional filters (location, network, specialty, role/privileges) refine the search results correctly.
  - Ensure that the response conforms to the FHIR Practitioner resource structure.
  - Validate that the server supports the required search parameters (`name`, `family`, `given`) as per the Capability Statement.
- **Assertions**:
  - The response should include a `200 OK` status code.
  - The number of returned results should match the expected count based on the input criteria.
  - Each Practitioner in the response should have the `name` field matching the search query and include relevant details for location, network, specialty, and role/privileges if applicable.

```


---

<a id='req-34'></a>

### REQ-34: Organization search by name

**Description**: "The Plan-Net design is based around the following types of searches: Organization by Name - Example: Montgomery Cardiology or CVS - Focal Resource and Field: Organization.name - Qualifications of Search: Location, network, specialty."

**Actor**: Server

**Conformance**: None (Design requirement)

# Test Specification for Requirement REQ-34

## 1. Requirement ID
- **REQ-34**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement involves searching for organizations by name, which can be automated using API calls and response validation.

### Complexity
- **Level**: Simple
  - The search functionality is straightforward and involves basic query parameters.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server must support the Organization resource and the search parameter `name`.
- **Data Setup**:
  - Ensure the FHIR server contains sample Organization resources with varying names, including "Montgomery Cardiology" and "CVS".
  - Ensure that related Location, network, and specialty data are populated for comprehensive testing.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Search query parameter: `name`
  - Example search values: "Montgomery Cardiology", "CVS"
- **Expected Outputs**:
  - A list of Organization resources that match the search criteria by name.
  - The response should include relevant details such as organization name, address, and any associated locations or specialties.

### Required FHIR Operations
- **API Calls**:
  - Perform a GET request on the Organization resource with the search parameter `name`:
    ```
    GET [base]/Organization?name=Montgomery Cardiology
    GET [base]/Organization?name=CVS
    ```

### Test Data Requirements
- **Organization Data**:
  - At least two Organization resources with names "Montgomery Cardiology" and "CVS".
  - Additional Organization resources with similar names to test partial matches and ensure precise search functionality.
- **Associated Data**:
  - Location, network, and specialty data linked to the organizations for extended validation.

### Validation Criteria
- **Response Validation**:
  - Verify that the response status code is 200 (OK).
  - Confirm that the response contains Organization resources where the `name` field matches the search criteria.
  - Check that the returned resources include expected fields such as `name`, `address`, and any linked `Location` or `specialty`.
- **Assertions**:
  - Assert that the number of returned resources matches the expected count for the given search criteria.
  - Validate that no unrelated Organization resources are included in the response.
- **Error Handling**:
  - Ensure that invalid search queries return appropriate error messages or status codes (e.g., 400 Bad Request for malformed queries).

By following this structured test specification, the implementation of the FHIR server's search functionality for organizations by name can be thoroughly validated to meet the requirements outlined in REQ-34.

---

<a id='req-35'></a>

### REQ-35: Provider search by specialty

**Description**: "The Plan-Net design is based around the following types of searches: Provider by Specialty - Example: Cardiologist - Focal Resource and Field: PractitionerRole.specialty - Qualifications of Search: Location, network, name."

**Actor**: Server

**Conformance**: None (Design requirement)

```markdown
# Test Specification for Requirement REQ-35

## 1. Requirement ID
- **REQ-35**: Provider search by specialty

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement can be tested using automated scripts that perform FHIR API calls to search for providers by specialty.

### Complexity
- **Level**: Moderate
  - While the search functionality itself is straightforward, ensuring all relevant parameters (specialty, location, network, and name) are correctly implemented and tested adds complexity.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be configured to support PractitionerRole searches.
- **Data Setup**: 
  - The system must have pre-loaded data for practitioners with various specialties, including "Cardiologist".
  - Location, network, and name data should be available and linked to PractitionerRole resources.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - Search query for PractitionerRole with `specialty=Cardiologist`
  - Optional filters: `location`, `network`, `name`
- **Expected Outputs**: 
  - A list of PractitionerRole resources where the `specialty` is "Cardiologist".
  - The results should be filtered correctly based on any additional parameters provided (e.g., location, network, name).

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/PractitionerRole?specialty=Cardiologist`
  - Optional: Add parameters such as `&location=[location_id]`, `&network=[network_id]`, `&name=[name]`

### Test Data Requirements
- **PractitionerRole Resources**:
  - At least one PractitionerRole with the specialty "Cardiologist".
  - PractitionerRole resources with various locations, networks, and names to test filtering.
- **Location and Network Resources**:
  - Relevant Location and Network resources linked to PractitionerRole resources.

### Validation Criteria
- **Conformance Checks**:
  - Verify that the response contains PractitionerRole resources with the `specialty` field set to "Cardiologist".
  - Check that filtering by location, network, and name returns the correct subset of results.
  - Ensure that the response conforms to FHIR standards (correct resource types, valid JSON format).
- **Assertions**:
  - The number of results matches the expected count based on the test data setup.
  - Each returned PractitionerRole resource has a valid reference to a Practitioner and associated Location/Network if specified.
  - The server responds with a 200 HTTP status code and the correct FHIR bundle structure.
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
- **Classification**: Automatic
  - The requirement involves searching and retrieving data from a FHIR server, which can be automated using scripts or testing tools.

### Complexity
- **Classification**: Moderate
  - The requirement involves multiple search parameters and the interaction between different resources (Organization, OrganizationAffiliation, Location).

### Prerequisites
- **System Configurations**: 
  - A FHIR server implementing the Plan-Net design.
  - The server must support the Organization, OrganizationAffiliation, and Location resources.
- **Data Setup**:
  - Pre-loaded test data including Organizations with various specialties.
  - OrganizationAffiliation resources linking Organizations with their specialties.
  - Location resources associated with Organizations.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Search query for Organization by specialty, e.g., `OrganizationAffiliation.specialty=Compounding Pharmacy`.
  - Additional search qualifiers: Location, network, name.
- **Expected Outputs**:
  - A list of Organizations that match the specified specialty and any additional qualifiers.
  - Each Organization should include relevant details such as name, location, and network.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/OrganizationAffiliation?specialty=[specialty]&location=[location]&network=[network]&name=[name]`
  - Ensure the server supports these search parameters as per the Capability Statement.

### Test Data Requirements
- **Type of Test Data**:
  - Organizations with various specialties, including "Compounding Pharmacy".
  - OrganizationAffiliation resources linking these Organizations with their specialties.
  - Location resources with different attributes (city, state, postal code) linked to Organizations.
  - Network and name attributes for Organizations to test additional qualifiers.

### Validation Criteria
- **Specific Checks**:
  - Verify that the search results include only Organizations with the specified specialty.
  - Ensure that additional qualifiers (location, network, name) filter results correctly.
  - Confirm that the returned data includes all necessary fields (e.g., Organization name, location).
  - Validate the response status code is 200 (OK) for successful searches.
  - Check that the response conforms to the FHIR standard for Organization and related resources.
  - Ensure no unexpected errors or warnings are returned by the server.

- **Assertions**:
  - The number of returned Organizations matches the expected count based on the test data setup.
  - Each returned OrganizationAffiliation resource includes the correct specialty and links to the correct Organization.
  - The search results are consistent across multiple test runs with the same input parameters.
```


---

<a id='req-37'></a>

### REQ-37: Search for active practitioners and organizations

**Description**: "Sample query to search for currently active Practitioners (replace date in query with current date): http://davinci-plan-net-ri.logicahealth.org/fhir/PractitionerRole?_include=PractitionerRole:date=ge2021-10-25. Sample query to search for currently active Organizations (replace date in query with current date): http://davinci-plan-net-ri.logicahealth.org/fhir/OrganizationAffiliation?_include=OrganizationAffiliation:date=ge2021-10-25."

**Actor**: Server

**Conformance**: None (Implementation example)

```markdown
# Test Specification for REQ-37

## 1. Requirement ID
- **REQ-37**: Search for active practitioners and organizations

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement involves executing FHIR search queries and validating the responses, which can be automated using test scripts.

### Complexity
- **Complexity**: Moderate
  - The complexity arises from the need to handle date-based filtering and ensure the correct inclusion of related resources.

### Prerequisites
- **System Configurations**: 
  - Access to a FHIR server that supports the required resources and search parameters.
  - Network configuration allowing HTTP requests to the server.
  
- **Data Setup**:
  - Ensure the FHIR server has data for Practitioners, PractitionerRoles, Organizations, and OrganizationAffiliations with varying active statuses and dates.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Current date for filtering active resources.
  - FHIR search queries for PractitionerRole and OrganizationAffiliation.

- **Expected Outputs**:
  - Responses containing only currently active Practitioners and Organizations.
  - Correct inclusion of related resources as specified by `_include` parameters.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET /PractitionerRole?_include=PractitionerRole:date=ge<current-date>`
  - `GET /OrganizationAffiliation?_include=OrganizationAffiliation:date=ge<current-date>`

### Test Data Requirements
- **Practitioner Data**:
  - Practitioners with varying active statuses and associated PractitionerRoles.
  
- **Organization Data**:
  - Organizations with varying active statuses and associated OrganizationAffiliations.

### Validation Criteria
- **Conformance Checks**:
  - Ensure the response includes only active Practitioners and Organizations.
  - Validate the inclusion of related resources as specified by `_include`.
  - Verify that the search parameters used are supported as per the Capability Statement.
  - Confirm that the responses adhere to FHIR standards and include expected fields.

- **Assertions**:
  - Response status code is 200 (OK).
  - All returned resources have active status as true.
  - The `_include` parameter correctly fetches related resources.
  - The date filter correctly limits results to those active on or after the specified date.
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
**REQ-38**

## 2. Requirement Analysis

- **Testability Assessment**: 
  - **Type**: Manual
  - **Rationale**: The requirement involves inspecting the structure of the contact information, specifically the presence of a blank family and given name, and the correct placement of the department name in `contact.name.text`. This requires manual inspection of the data returned by the server.

- **Complexity**: 
  - **Level**: Simple
  - **Rationale**: The requirement is straightforward, focusing on the presence and correct placement of specific fields in the contact resource.

- **Prerequisites**: 
  - Ensure the FHIR server is operational and accessible.
  - The server should have at least one contact entry where the contact is a department (e.g., patient help line).
  - Access to the server's API documentation to understand how to retrieve contact information.

## 3. Test Implementation Strategy

- **Required Inputs and Expected Outputs**:
  - **Input**: Request to retrieve contact information from the FHIR server.
  - **Expected Output**: A contact resource with:
    - `contact.name.family` and `contact.name.given` fields as empty.
    - `contact.name.text` containing the department name.

- **Required FHIR Operations**:
  - **Operation**: `GET [base]/ContactPoint` or equivalent operation to retrieve contact resources.
  - **Capability Statement Reference**: Ensure the server supports the `ContactPoint` resource retrieval operation.

- **Test Data Requirements**:
  - At least one contact entry where the contact is a department, not a human. This entry should be pre-loaded into the server's database.

- **Validation Criteria**:
  - **Check 1**: Verify that `contact.name.family` is empty.
  - **Check 2**: Verify that `contact.name.given` is empty.
  - **Check 3**: Verify that `contact.name.text` contains the department name (e.g., "Patient Help Line").
  - **Assertion**: All checks must pass for the test to be considered successful.

### Additional Notes:
- This test does not require conformance to a specific FHIR profile, as it is implementation guidance.
- The test is conditional, meaning it only applies when the contact is a department.
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
  - **Rationale**: The requirement involves inspection of the `Organization` resource to ensure that when a contact is a department, the `family` and `given` names are blank, and the department name is correctly placed in `contact.name.text`. This requires human verification to ensure the correct interpretation of the data.

### Complexity
- **Complexity**: Simple
  - **Rationale**: The requirement is straightforward, involving a simple check of the `Organization` resource's contact fields.

### Prerequisites
- **System Configurations**: 
  - A FHIR server that implements the `Organization` resource.
- **Data Setup**: 
  - At least one `Organization` resource with a contact entry representing a department (e.g., "patient help line").

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs for the Test
- **Inputs**: 
  - An `Organization` resource with a contact entry where the contact is a department.
- **Expected Outputs**: 
  - The `contact.name.family` and `contact.name.given` fields should be blank.
  - The `contact.name.text` field should contain the department name.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Organization?_id=[organization-id]`: Retrieve the specific `Organization` resource by its ID.
  - `GET [base]/Organization?name=[department-name]`: Search for the `Organization` resource by department name.

### Test Data Requirements
- **Test Data**:
  - An `Organization` resource with:
    - `contact.name.family` and `contact.name.given` fields set to blank.
    - `contact.name.text` field containing a valid department name (e.g., "Patient Help Line").

### Validation Criteria
- **Specific Checks**:
  - **Check 1**: Verify that the `contact.name.family` field is empty.
  - **Check 2**: Verify that the `contact.name.given` field is empty.
  - **Check 3**: Verify that the `contact.name.text` field contains the expected department name.
- **Assertions**:
  - The test passes if all checks are satisfied for the `Organization` resource under inspection.
  - The test fails if any of the checks are not satisfied, indicating non-conformance with the requirement.

This structured test specification ensures that the requirement REQ-39 is thoroughly tested through manual inspection, verifying the correct handling of department contacts within the `Organization` resource.

---

<a id='req-40'></a>

### REQ-40: Practitioner qualification coding

**Description**: "When the value set for the coded concept in qualification is insufficient, the qualification can be provided in the text field of the codeableConcept."

**Actor**: Server

**Conformance**: None (Implementation guidance)

# Test Specification for Requirement REQ-40

## 1. Requirement ID
- **REQ-40**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Manual
  - The requirement involves inspecting the text field of a `CodeableConcept` when the coded concept is insufficient, which requires human judgment to verify the appropriateness of the text.

### Complexity
- **Classification**: Moderate
  - The requirement involves understanding the context of qualifications and determining when the text field should be used, which requires domain knowledge.

### Prerequisites
- **System Configurations**: 
  - A FHIR server capable of storing and retrieving Practitioner resources.
- **Data Setup**:
  - Practitioner resources with various qualifications, including some where the coded concept is insufficient and text is provided.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Practitioner resources with qualifications where the coded concept is insufficient.
- **Expected Outputs**:
  - Practitioner resources should have a `CodeableConcept` for qualifications where the `text` field is populated appropriately when the coded concept is insufficient.

### Required FHIR Operations
- **GET**: Retrieve Practitioner resources using supported search parameters such as `name`, `_id`, `family`, `given`.
  - Example: `GET [base]/Practitioner?name=[name]`

### Test Data Requirements
- **Test Data**:
  - Practitioner resources with various qualifications.
  - At least one resource where the qualification code is insufficient, and the text field is used to provide additional information.

### Validation Criteria
- **Specific Checks**:
  - Verify that Practitioner resources with qualifications have a `CodeableConcept` where the `text` field is used when the coded concept is insufficient.
  - Ensure that the `text` field provides meaningful and relevant information that complements the coded concept.
- **Assertions**:
  - The `text` field should not be empty when the coded concept is insufficient.
  - The content of the `text` field should be relevant and descriptive of the qualification.
- **Inspection**:
  - Manually inspect the `text` field to ensure it provides appropriate additional information when the coded concept is insufficient.

---



