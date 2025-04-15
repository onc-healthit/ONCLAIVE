# Consolidated Test Plan for Plan Net

## Generated on: 2025-04-09 11:51:23

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
# Test Specification for Requirement REQ-02

## 1. Requirement ID
- **REQ-02**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Manual
  - The requirement involves ensuring that no Personally Identifiable Information (PII) is sent by the client, which requires inspection of the data being transmitted. This is best assessed through manual inspection or review of logs.

### Complexity
- **Complexity**: Moderate
  - The complexity is moderate as it involves understanding what constitutes PII and ensuring none of it is included in the data payloads sent by the client application.

### Prerequisites
- **System Configurations**: 
  - Access to the client application and the Plan-Net service for testing.
  - Logging or monitoring tools to capture and inspect outgoing requests from the client.
- **Data Setup**: 
  - Ensure that the client application is configured to interact with a test instance of the Plan-Net service.
  - Access to a list of data elements considered PII for reference during inspection.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A set of typical queries that the directory mobile application would send to the Plan-Net service.
- **Expected Outputs**: 
  - The data payloads of these queries should not contain any PII.

### Required FHIR Operations
- **Operations**:
  - `GET` operations to query the Plan-Net service, as specified in the Capability Statement.
  - Ensure that the client supports these operations without including PII in the request payloads.

### Test Data Requirements
- **Test Data**:
  - Simulated user data that does not include PII.
  - A list of data fields that are considered PII to cross-reference during inspection.

### Validation Criteria
- **Validation Checks**:
  - Inspect the outgoing requests from the client to the Plan-Net service.
  - Verify that none of the requests contain PII such as names, social security numbers, addresses, or other identifiable information.
  - Ensure that the requests only include necessary query parameters that do not reveal consumer identity.
  - Confirm that the client application adheres to the requirement by not sending any PII in all tested scenarios.

- **Assertions**:
  - If any PII is detected in the outgoing requests, the test fails.
  - If all outgoing requests are free of PII, the test passes.

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
  - The requirement can be tested automatically by simulating client interactions with a FHIR server and verifying the handling of Must Support data elements.

### Complexity
- **Complexity**: Moderate
  - The complexity arises from the need to ensure that all Must Support elements are processed correctly without causing errors, which may involve multiple resource types and scenarios.

### Prerequisites
- **System Configurations**: 
  - A FHIR client application capable of interacting with a FHIR server.
  - Access to a FHIR server that supports the necessary resources and operations as per the Capability Statement.

- **Data Setup**:
  - The FHIR server must have resources that include Must Support data elements populated.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - FHIR resource instances containing Must Support data elements.

- **Expected Outputs**:
  - The client application processes the resource instances without generating errors or failing.
  - Successful processing logs or status codes indicating no errors occurred.

### Required FHIR Operations
- **FHIR Operations**:
  - `GET [base]/[resourceType]/[id]`: Retrieve specific resource instances.
  - `SEARCH [base]/[resourceType]?parameter=value`: Search for resources with specific criteria.
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - Resource instances of types defined in the Capability Statement, each containing Must Support data elements.
  - Variations of resource instances where Must Support elements are present, absent, or partially populated.

### Validation Criteria
- **Validation Checks**:
  - The client application should not crash or throw errors when processing resources with Must Support elements.
  - Verify that the application logs or user interface indicate successful processing of the resources.
  - Confirm that Must Support elements are handled according to the application's functional requirements (e.g., displayed correctly in the UI, used in decision-making processes).

- **Assertions**:
  - Assert that no exceptions or error messages are generated by the client when processing the resources.
  - Assert that the client application maintains expected functionality and performance when interacting with Must Support elements.

By following this test specification, we can ensure that the client application meets the requirement of processing Must Support data elements without errors, as mandated by REQ-06.
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
  - **Rationale**: The requirement involves human interaction to verify the display of data elements, which necessitates manual inspection.

### Complexity
- **Level**: Moderate
  - **Rationale**: While displaying data is a straightforward task, ensuring that all relevant data elements are correctly displayed or stored involves multiple checks.

### Prerequisites
- **System Configurations**: 
  - The client application must be installed and configured to connect to the FHIR server.
  - Ensure network connectivity between the client and the FHIR server.
- **Data Setup**:
  - The FHIR server must contain a set of test data that includes various FHIR resources with diverse data elements.
- **User Setup**:
  - A test user account with appropriate permissions to access and view the data elements.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A set of FHIR resources (e.g., Patient, Observation, Condition) with populated data elements.
- **Expected Outputs**: 
  - The client application should display the data elements in a human-readable format.
  - Alternatively, the application should store the data elements for other purposes, such as logging or further processing.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Patient/{id}`
  - `GET [base]/Observation/{id}`
  - `GET [base]/Condition/{id}`
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Type of Test Data**:
  - A diverse set of FHIR resources with varying data elements to test the display capabilities.
  - Include resources with optional and mandatory fields to ensure comprehensive testing.

### Validation Criteria
- **Conformance Checks**:
  - Verify that all data elements from the FHIR resources are displayed correctly in the client application.
  - Check that the display format is user-friendly and accessible.
  - Confirm that the application can store the data elements for other purposes, if applicable.
  - Ensure that no data elements are missing or incorrectly represented.
  - Validate that the application handles different data types and structures appropriately.

- **Assertions**:
  - The client application displays each data element as expected.
  - The application logs or stores the data elements without errors.
  - No discrepancies between the source data on the FHIR server and the displayed data on the client.

By following this test specification, testers can ensure that the client application meets the requirements of REQ-07 by effectively displaying or storing FHIR data elements.
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
  - The requirement involves interpretation by the client, which necessitates human inspection to verify correct behavior.

### Complexity
- **Complexity Level**: Moderate
  - While the concept is straightforward, ensuring that the client correctly interprets missing data across various scenarios requires careful inspection.

### Prerequisites
- **System Configurations**: 
  - Access to a Health Plan API that implements the relevant FHIR resources.
  - A client application capable of querying the Health Plan API.
- **Data Setup**:
  - The Health Plan API should have resource instances with missing Must Support data elements.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A set of test queries to the Health Plan API for resources known to have missing Must Support data elements.
- **Expected Outputs**:
  - The client should interpret the absence of Must Support data elements as data not present in the Health Plan API actor's system.

### Required FHIR Operations
- **FHIR Operations**:
  - `GET [base]/[resource-type]?[parameters]`: To query resources from the Health Plan API.
  - Ensure these operations are supported in the Capability Statement for the Health Plan API.

### Test Data Requirements
- **Test Data**:
  - Resource instances from the Health Plan API with intentionally missing Must Support data elements.
  - Examples of resources might include `Coverage`, `PlanDefinition`, or other relevant resources as defined in the Capability Statement.

### Validation Criteria
- **Validation Checks**:
  - Verify that the client application does not generate errors or incorrect assumptions due to missing Must Support data.
  - Confirm that the client logs or displays a message indicating the data is not present in the Health Plan API actor's system.
  - Ensure that the client application continues to function correctly and provides meaningful output to the end-user despite missing data.
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
  - The requirement can be tested using automated test scripts that simulate client processing of FHIR resources with missing information indicators.

### Complexity
- **Complexity Level**: Moderate
  - The complexity arises from the need to handle various FHIR resource types and ensure correct processing of the "Must Support" data elements with missing information indicators.

### Prerequisites
- **System Configurations**: 
  - The Consumer App must be configured to connect to a FHIR server that supports the necessary FHIR operations as per the Capability Statement.
- **Data Setup**: 
  - Access to a FHIR server with test resources that include "Must Support" data elements with missing information indicators.
  - Ensure the FHIR server supports the operations required for the test, such as `read` and `search`.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - FHIR resource instances (e.g., Patient, Observation) containing "Must Support" data elements with missing information indicators (e.g., dataAbsentReason extension).
- **Expected Outputs**: 
  - The Consumer App should correctly interpret and process the missing information indicators without errors, and display or log appropriate messages indicating the absence of data.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Patient/[id]` - To retrieve a Patient resource with missing information indicators.
  - `GET [base]/Observation/[id]` - To retrieve an Observation resource with missing information indicators.
  - These operations must be supported by the FHIR server as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - Create or use existing FHIR resources that include "Must Support" data elements with missing information indicators, such as the `dataAbsentReason` extension.
  - Ensure a variety of resources are tested to cover different scenarios of missing information.

### Validation Criteria
- **Specific Checks**:
  - Verify that the Consumer App can successfully retrieve and process each FHIR resource with missing information indicators.
  - Check that the application logs or displays a message indicating the presence of missing information and the reason for its absence.
  - Assert that no errors occur during the processing of these resources.
  - Confirm that the application adheres to the FHIR specification for handling missing information indicators, particularly the `dataAbsentReason` extension.

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
- **REQ-31**: Client tracking of directory content updates

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Hybrid
  - **Reasoning**: The test involves both automated query execution and manual inspection of results to verify correct tracking of updates.

### Complexity
- **Classification**: Moderate
  - **Reasoning**: The test requires setting up a client to cache results and then perform queries using the `_lastUpdated` parameter, which involves understanding of caching mechanisms and FHIR search parameters.

### Prerequisites
- **System Configurations**: 
  - A FHIR server with directory content that supports the `_lastUpdated` search parameter.
  - A client application capable of caching query results and performing FHIR searches.
- **Data Setup**: 
  - Initial directory content data to be cached by the client.
  - Subsequent updates to the directory content to test tracking capabilities.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  1. Initial query to cache directory content.
  2. Updated directory content with known changes.
  3. Query using `_lastUpdated` parameter to fetch updates.
- **Expected Outputs**:
  - The client should correctly identify and retrieve only the additions or modifications since the last cached state.

### Required FHIR Operations
- **API Calls**:
  1. `GET [base]/[resource]?_lastUpdated=[date]` - To query updates based on the last updated timestamp.
  2. `GET [base]/[resource]` - Initial query to cache directory content.

### Test Data Requirements
- **Test Data**:
  - A set of directory entries with known timestamps.
  - Updated entries with modified timestamps to simulate changes.

### Validation Criteria
- **Specific Checks**:
  1. Verify that the initial query results are cached by the client.
  2. Confirm that the client performs a subsequent query using the `_lastUpdated` parameter.
  3. Ensure that the results of the `_lastUpdated` query only include entries that have been added or modified since the last cache.
  4. Manually inspect the query results to ensure they match expected updates.

- **Assertions**:
  - The client correctly caches the initial query results.
  - The client correctly identifies and retrieves updates using the `_lastUpdated` parameter.
  - The client does not retrieve any entries that have not been updated or added since the last cache.

By following this test specification, we can ensure that clients are correctly tracking and retrieving updates to directory content as per the implementation guidance provided in REQ-31.
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
  - **Rationale**: The requirement specifies a "SHALL NOT" condition, which necessitates a manual inspection of the API requests and responses to ensure that no personally identifiable information (PII) is required or transmitted.

### Complexity
- **Complexity Level**: Simple
  - **Rationale**: The requirement is straightforward, focusing solely on the absence of PII in directory queries.

### Prerequisites
- **System Configurations**: 
  - A FHIR server conforming to the Plan-Net Implementation Guide.
  - Access to the server's directory query endpoints.
- **Data/Setup**:
  - Ensure the server is populated with test data that can be queried.
  - Ensure that the directory mobile application is capable of making queries to the server.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A directory query request from a mobile application without any consumer identifying information.
- **Expected Outputs**:
  - Successful query response from the server without any requirement for PII in the request.

### Required FHIR Operations
- **Supported API Calls**:
  - `GET [base]/Practitioner`
  - `GET [base]/Organization`
  - `GET [base]/Location`
  - Ensure these operations do not require PII as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - Sample directory data for practitioners, organizations, and locations that can be queried.
  - Ensure that the data does not include any PII in the request parameters.

### Validation Criteria
- **Specific Checks**:
  - Inspect the API request logs to verify that no PII is included in the request headers or parameters.
  - Confirm that the server responds to directory queries without requiring any PII.
  - Ensure that the server's response is valid and contains the expected directory information.
- **Assertions**:
  - Assert that no HTTP 4xx or 5xx errors occur due to missing PII.
  - Assert that the response includes the expected directory data without any errors related to authentication or authorization based on PII.

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
- **REQ-03**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement can be tested using automated scripts that query the FHIR server and validate the presence of Must Support data elements in the responses.

### Complexity
- **Complexity Level**: Moderate
  - While the concept of Must Support is straightforward, ensuring all such elements are populated across various resources and scenarios adds complexity.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server must have the necessary configurations to support the Health Plan API.
- **Data Setup**:
  - The server must contain sample data that includes all Must Support elements for the relevant resources.
  - Ensure that the server's Capability Statement is up-to-date and reflects the support for Must Support elements.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A set of predefined FHIR queries targeting resources with Must Support elements.
- **Expected Outputs**:
  - Responses from the server that include all Must Support data elements populated as specified in the Implementation Guide.

### Required FHIR Operations
- **Operations**:
  - `GET [base]/[resource]?parameters` (e.g., `GET [base]/Patient?identifier=12345`)
  - Ensure that the Capability Statement supports these operations for the resources in question.

### Test Data Requirements
- **Test Data**:
  - A diverse dataset that includes instances of all resources with Must Support elements.
  - Data should be realistic and cover various scenarios to ensure comprehensive testing.

### Validation Criteria
- **Validation Checks**:
  - Verify that each Must Support element is present in the response for each queried resource.
  - Check that the values of Must Support elements conform to the expected data types and constraints.
  - Ensure that no Must Support element is missing or left unpopulated in any response.
  - Validate against the Capability Statement to confirm that the server declares support for the required operations and resources.

- **Assertions**:
  - Assertions should be made to confirm the presence and correctness of Must Support elements in the response.
  - Log any discrepancies or missing elements for further analysis.

By following this test specification, testers can systematically verify that the Health Plan API server meets the requirement to populate all Must Support data elements as part of the query results.
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
  - **Rationale**: The requirement involves inspecting the absence of data elements in a resource instance, which is typically verified through manual inspection of the returned resource.

### Complexity
- **Classification**: Moderate
  - **Rationale**: The complexity is moderate due to the need to verify multiple conditions (presence of Must Support data elements, cardinality checks, and conditional absence).

### Prerequisites
- **System Configurations**: 
  - A FHIR server implementing the Health Plan API.
  - Access to the server's Capability Statement to confirm supported operations.
- **Data Setup**: 
  - Test resources with Must Support data elements having minimum cardinality of 0.
  - Ensure the server is configured to handle and return query results.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A query request to the FHIR server for a specific resource type that includes Must Support data elements with a minimum cardinality of 0.
- **Expected Outputs**: 
  - The returned resource instance should not include the Must Support data elements if they are absent.

### Required FHIR Operations
- **API Calls/Operations**: 
  - `GET [base]/[ResourceType]?parameter=value` (e.g., `GET [base]/Patient?name=Smith`)
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**: 
  - Resource instances where Must Support data elements are conditionally absent (i.e., elements with a minimum cardinality of 0 are not present).

### Validation Criteria
- **Specific Checks**:
  - Verify that the resource instance returned does not include absent Must Support data elements with a minimum cardinality of 0.
  - Confirm that the server's response adheres to the FHIR standard and the Implementation Guide's conformance requirements.
  - Check that no errors or warnings are returned by the server indicating non-compliance with the requirement.

- **Assertions**:
  - Assert that the resource instance does not contain the absent Must Support data elements.
  - Assert that the server's response status code is 200 (OK) and the response is valid according to FHIR standards.

By following this test specification, testers can ensure that the server correctly omits absent Must Support data elements with a minimum cardinality of 0, in compliance with the FHIR Implementation Guide requirement REQ-04.
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
  - **Reason**: The requirement involves both automated checks (validating the presence of `dataAbsentReason`) and manual inspection (ensuring the correct application of nullFlavors or extensions).

### Complexity
- **Complexity Level**: Moderate
  - **Reason**: Involves understanding and validating the correct use of extensions and value sets, which requires both automated and manual verification steps.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must support the `dataAbsentReason` extension.
  - The server should have the capability to handle nullFlavors as defined in the value set.
- **Data Setup**: 
  - Ensure there are resources with missing required data elements where `dataAbsentReason` can be applied.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - FHIR resources with missing required data elements.
- **Expected Outputs**: 
  - Resources should include the `dataAbsentReason` extension or appropriate nullFlavors from the specified value set.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resourceType]` to retrieve resources with missing required data.
  - `POST [base]/[resourceType]` to submit resources and verify server response for missing data handling.
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - Create test resources with intentionally missing required fields to trigger the use of `dataAbsentReason`.
  - Include variations to test different nullFlavors where applicable.

### Validation Criteria
- **Automated Checks**:
  - Verify that the `dataAbsentReason` extension is present when required data is missing.
  - Check that the nullFlavors used are part of the specified value set.
- **Manual Inspection**:
  - Ensure that the application of `dataAbsentReason` or nullFlavors is contextually appropriate.
  - Validate that the server's response correctly reflects the handling of missing data as per the requirement.

- **Assertions**:
  - The presence of `dataAbsentReason` in the response for missing required data elements.
  - Correct application of nullFlavors from the value set.
  - Server responses should conform to the expected behavior as outlined in the requirement.

By following this test specification, testers can ensure that the server complies with REQ-05 by correctly handling missing required information using the `dataAbsentReason` extension or appropriate nullFlavors.
```

---

<a id='req-10'></a>

### REQ-10: JSON format support

**Description**: "Support json source formats for all Plan-Net interactions."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for FHIR Implementation Guide Requirement

## 1. Requirement ID
- **REQ-10**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement to support JSON format can be tested automatically by sending requests to the server and verifying the responses.

### Complexity
- **Level**: Simple
  - The requirement is straightforward as it involves checking the server's ability to handle JSON format, which is a standard feature in FHIR servers.

### Prerequisites
- **System Configurations**: 
  - The server must be running and accessible over the network.
  - The server should have the Plan-Net module enabled and properly configured.
  
- **Data/Setup**:
  - Ensure that the server has sample FHIR resources available for Plan-Net interactions (e.g., Practitioner, Organization, HealthcareService).

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - JSON-formatted FHIR requests for each Plan-Net interaction (e.g., GET, POST, PUT, DELETE).
  
- **Expected Outputs**:
  - The server should correctly process the JSON requests and return appropriate JSON-formatted FHIR responses.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Practitioner`
  - `POST [base]/Practitioner`
  - `PUT [base]/Practitioner/{id}`
  - `DELETE [base]/Practitioner/{id}`
  - Similarly, operations for Organization and HealthcareService resources.
  
  Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Type of Test Data**:
  - Valid JSON representations of FHIR resources such as Practitioner, Organization, and HealthcareService.
  - Example JSON payloads for creating, updating, and retrieving resources.

### Validation Criteria
- **Specific Checks**:
  - **Conformance**: Verify that the server accepts JSON requests and returns JSON responses for all Plan-Net interactions.
  - **Response Validation**: Check that the response status codes are appropriate (e.g., 200 for successful GET, 201 for successful POST).
  - **Content Validation**: Ensure the response body is a valid JSON and conforms to the FHIR resource structure.
  - **Error Handling**: Validate that the server returns appropriate error messages in JSON format for invalid requests.
```


---

<a id='req-11'></a>

### REQ-11: RESTful behavior implementation

**Description**: "Implement the RESTful behavior according to the FHIR specification."

**Actor**: Server

**Conformance**: SHALL

# Test Specification for REQ-11: RESTful Behavior Implementation

## 1. Requirement ID
- **REQ-11**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Hybrid
  - **Automatic**: Automated tests can verify the correct implementation of RESTful operations.
  - **Manual**: Inspection of logs and server responses may be required to ensure compliance with the FHIR specification.

### Complexity
- **Complexity**: Moderate
  - The implementation of RESTful behavior involves multiple operations and response handling, requiring a comprehensive test suite.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to expose FHIR RESTful endpoints.
  - Ensure that the server supports the necessary FHIR version as specified in the Capability Statement.
- **Data Setup**:
  - Populate the server with a minimal dataset to allow for meaningful interaction during testing.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - HTTP requests for each supported RESTful operation (e.g., GET, POST, PUT, DELETE) on various FHIR resources.
- **Expected Outputs**: 
  - Correct HTTP status codes (e.g., 200, 201, 204, 400, 404).
  - Properly formatted FHIR resources in responses.
  - Appropriate error messages for invalid requests.

### Required FHIR Operations
- **Supported API Calls/Operations**:
  - `GET [base]/[resourceType]`: Retrieve a list of resources.
  - `GET [base]/[resourceType]/[id]`: Retrieve a specific resource by ID.
  - `POST [base]/[resourceType]`: Create a new resource.
  - `PUT [base]/[resourceType]/[id]`: Update an existing resource.
  - `DELETE [base]/[resourceType]/[id]`: Delete a resource.

### Test Data Requirements
- **Test Data**:
  - A set of valid and invalid FHIR resources for each resource type supported by the server.
  - Example resource IDs for testing retrieval, update, and deletion operations.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server correctly implements each RESTful operation as per the FHIR specification.
  - Confirm that the server returns the correct HTTP status codes for each operation.
  - Ensure that the server responds with valid FHIR resources, including correct headers and content types.
  - Check that error handling is implemented correctly, with appropriate error messages and status codes for invalid requests.
  - Validate that the server's behavior aligns with the declared capabilities in the Capability Statement.

By following this test specification, testers can systematically verify that the server implements RESTful behavior in compliance with the FHIR specification and the relevant Capability Statement.

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
  - The requirement to support all profiles can be tested through automated scripts that validate the server's capability to handle requests conforming to each profile.

### Complexity
- **Complexity**: Complex
  - The complexity arises from the need to validate multiple profiles, each potentially having unique constraints and extensions.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to expose all profiles defined in the Implementation Guide.
- **Data Setup**: 
  - Test data must be available that conforms to each profile.
- **Environment**: 
  - Access to a test server environment that mirrors the production configuration.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A set of FHIR resources conforming to each profile defined in the Implementation Guide.
- **Expected Outputs**: 
  - Successful creation, retrieval, update, and deletion (CRUD operations) of resources that conform to each profile without errors.

### Required FHIR Operations
- **API Calls/Operations**:
  - `POST` to create resources conforming to each profile.
  - `GET` to retrieve resources and verify they conform to the profile.
  - `PUT` to update resources and ensure continued conformance.
  - `DELETE` to remove resources and ensure proper handling.
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Type of Test Data**:
  - Valid FHIR resources for each profile, including edge cases and typical use cases.
  - Resources should cover all mandatory fields and a variety of optional fields.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server correctly processes and stores resources conforming to each profile.
  - Check that the server returns appropriate HTTP status codes (e.g., 200, 201 for success, 400 for bad requests).
  - Ensure that retrieved resources match the profile structure and constraints.
  - Confirm that updates and deletions are correctly handled and reflected in subsequent retrievals.
- **Assertions**:
  - Assertions should include checks for profile-specific constraints, such as required fields, value set bindings, and extensions.
  - Validate that the server's Capability Statement includes support for all profiles as claimed.

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
- **Classification**: Automatic
  - The requirement involves checking server responses to unauthorized requests, which can be automated through scripted API calls and response evaluations.

### Complexity
- **Complexity**: Simple
  - The requirement involves straightforward validation of HTTP status codes in response to unauthorized access attempts.

### Prerequisites
- **System Configurations**: 
  - A FHIR server instance configured to authenticate requests.
  - Access to server logs for additional verification if necessary.
- **Data/Setup**:
  - Ensure the server is running and accessible.
  - No special data setup is required as the test focuses on unauthorized access attempts.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - An HTTP request to the FHIR server without valid authorization credentials.
- **Expected Outputs**:
  - The server should return an HTTP status code of 401 (Unauthorized) or another 4xx status code indicating unauthorized access.

### Required FHIR Operations
- **API Calls/Operations**:
  - Perform a GET request on a FHIR resource endpoint (e.g., `/Patient`) without including valid authorization headers.
  - This operation is supported by the general capabilities of the FHIR server as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - No specific FHIR resource data is required as the test focuses on the server's response to unauthorized access.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server returns an HTTP status code of 401 or another appropriate 4xx code.
  - Ensure that the response includes a WWW-Authenticate header if applicable, indicating the authentication scheme required.
  - Log and report any deviations from the expected response status codes.
- **Assertions**:
  - Assert that the response status code is 401 or a relevant 4xx code.
  - Assert that the response does not contain any sensitive data or resource information.

By following this test specification, the requirement REQ-13 can be effectively validated to ensure that the FHIR server correctly handles unauthorized requests according to the Implementation Guide.
```

---

<a id='req-14'></a>

### REQ-14: Insufficient scope response

**Description**: "Return the following response classes: (Status 403): insufficient scope."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for FHIR Implementation Guide Requirement REQ-14

## 1. Requirement ID
- **REQ-14**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement can be tested using automated scripts that simulate requests with insufficient scope and verify the response.

### Complexity
- **Complexity Level**: Simple
  - The requirement involves checking for a specific HTTP status code (403) and message ("insufficient scope"), which is straightforward.

### Prerequisites
- **System Configurations**: 
  - The server must be configured with OAuth 2.0 or a similar authorization framework that supports scope-based access control.
- **Data**: 
  - Test user accounts with varying scopes of access.
- **Setup**: 
  - Ensure the server is running and accessible.
  - Ensure the Capability Statement includes support for the necessary FHIR operations that will be tested.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - API requests with tokens that have insufficient scope for the requested operation.
- **Expected Outputs**:
  - HTTP response with status code 403.
  - Response body containing a message indicating "insufficient scope."

### Required FHIR Operations
- **API Calls**:
  - Any FHIR operation that requires specific scopes (e.g., `read`, `write`) as per the server's Capability Statement.
  - Example operations could include `GET [base]/Patient`, `POST [base]/Observation`, etc.

### Test Data Requirements
- **Test Data**:
  - OAuth 2.0 tokens with limited scopes.
  - Resource identifiers (e.g., Patient IDs) that the test user attempts to access.

### Validation Criteria
- **Validation Checks**:
  - Verify that the server returns an HTTP 403 status code for requests with insufficient scope.
  - Check the response body for a message explicitly stating "insufficient scope."
  - Confirm that the server's behavior aligns with the Capability Statement regarding scope-based access control.
- **Assertions**:
  - Assert that the response status code is 403.
  - Assert that the response body contains the phrase "insufficient scope."
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
  - The test can be automated by simulating requests with invalid parameters and verifying the server's response.

### Complexity
- **Complexity**: Simple
  - The requirement involves sending requests with invalid parameters and checking for a specific HTTP status code (400).

### Prerequisites
- **System Configurations**: 
  - The server must be running and accessible.
  - The server must support FHIR operations as specified in the Capability Statement.
- **Data or Setup**: 
  - No specific data setup is required, but the server must be capable of processing FHIR requests.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs for the Test
- **Inputs**: 
  - A FHIR request with an invalid parameter (e.g., a parameter not defined in the FHIR specification or a malformed parameter).
- **Expected Outputs**: 
  - The server should return an HTTP status code of 400 with an error message indicating an "invalid parameter."

### Required FHIR Operations
- **API Calls/Operations**:
  - Any FHIR operation that accepts parameters (e.g., `GET [base]/Patient` with invalid query parameters).
  - Ensure these operations are supported in the Capability Statement.

### Test Data Requirements
- **Type of Test Data**: 
  - No specific patient or resource data is required.
  - The focus is on the structure of the request, specifically the parameters.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server returns an HTTP status code of 400.
  - Check the response body for an error message that explicitly mentions "invalid parameter."
  - Ensure that the error message is compliant with the FHIR OperationOutcome resource format, if applicable.
  - Confirm that no other status codes (e.g., 200, 404) are returned for requests with invalid parameters.

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
  - The requirement can be tested using automated scripts that simulate requests to the server and verify the response status code.

### Complexity
- **Complexity Level**: Simple
  - The test involves sending a request to a server for a non-existent resource and checking for a 404 status code, which is straightforward.

### Prerequisites
- **System Configurations**: 
  - The server must be running and accessible.
  - The server must be configured to handle FHIR API requests.
- **Data/Setup**:
  - No specific data setup is required since the test involves requesting a non-existent resource.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Input**: 
  - A request to the FHIR server for a resource that does not exist (e.g., GET request to `/Patient/nonexistent-id`).
- **Expected Output**: 
  - The server should return a response with HTTP status code 404.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resourceType]/[id]`
    - Example: `GET /Patient/nonexistent-id`
  - Ensure that the server's Capability Statement supports the `read` operation for the resource type being tested.

### Test Data Requirements
- **Test Data**:
  - No specific test data is required since the test is for a non-existent resource.

### Validation Criteria
- **Specific Checks**:
  - Verify that the HTTP response status code is 404.
  - Optionally, check the response body for a standard FHIR OperationOutcome resource indicating the resource is unknown.
  - Validate that the server's response time is within acceptable limits for error handling (e.g., < 2 seconds).

- **Assertions**:
  - Assert that the status code is 404.
  - Assert that the response content type is `application/fhir+json` or `application/fhir+xml` as applicable.
  - If an OperationOutcome is returned, assert that it contains an appropriate error message indicating the resource is not found.

```


---

<a id='req-17'></a>

### REQ-17: Deleted resource response

**Description**: "Return the following response classes: (Status 410): deleted resource."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for FHIR Implementation Guide Requirement REQ-17

## 1. Requirement ID
- **REQ-17**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The test can be automated as it involves sending a request to the server and checking the HTTP response status code.

### Complexity
- **Complexity Level**: Simple
  - The requirement involves a straightforward check of the HTTP response status code when accessing a deleted resource.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to handle HTTP requests and return appropriate status codes.
- **Data Setup**:
  - At least one resource must be created and then deleted to test the response for a deleted resource.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Input**: 
  - An HTTP GET request to the server for a resource that has been previously deleted.
- **Expected Output**: 
  - The server should return an HTTP 410 Gone status code indicating the resource has been deleted.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resourceType]/[id]` 
    - This operation should be supported as per the Capability Statement for accessing resources.

### Test Data Requirements
- **Test Data**:
  - A resource of any type (e.g., Patient, Observation) that can be created and subsequently deleted.
  - Ensure the resource ID is known and accessible for testing purposes.

### Validation Criteria
- **Specific Checks**:
  - Verify that the HTTP response status code is 410 when a GET request is made for a deleted resource.
  - Confirm that the response body (if any) aligns with the FHIR standard for a 410 response, which may include an OperationOutcome resource explaining the deletion.
- **Assertions**:
  - Assert that the response status is exactly 410.
  - Optionally, assert that the response includes a valid FHIR OperationOutcome resource if provided.

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
  - The requirement involves verifying the presence of specific profile URIs in the `meta.profile` attribute, which can be programmatically checked using automated scripts.

### Complexity
- **Complexity**: Simple
  - The task involves straightforward verification of metadata in FHIR resource instances.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server should have implemented and exposed the Plan-Net profiles as specified in the Implementation Guide.
- **Data Setup**:
  - Instances of resources that are expected to conform to the Plan-Net profiles should be available on the server.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - FHIR resource instances that are expected to conform to Plan-Net profiles.
- **Expected Outputs**:
  - Each resource instance should contain a `meta.profile` attribute with URIs corresponding to the supported Plan-Net profiles.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resource-type]/[id]`: Retrieve specific resource instances to check for the `meta.profile` attribute.
  - `GET [base]/[resource-type]?profile=[uri]`: Search for resources by profile to ensure they are correctly tagged.

### Test Data Requirements
- **Type of Test Data**:
  - Resource instances that are expected to conform to specific Plan-Net profiles, such as `Practitioner`, `Organization`, `HealthcareService`, etc.
  - Profile URIs that are defined in the Plan-Net Implementation Guide.

### Validation Criteria
- **Specific Checks**:
  - Verify that the `meta.profile` attribute is present in each resource instance.
  - Confirm that the `meta.profile` attribute includes the correct URI(s) for the Plan-Net profiles.
  - Ensure that the server correctly supports search operations by profile, returning the appropriate resources when queried.

- **Assertions**:
  - The `meta.profile` attribute must not be empty and should contain at least one valid Plan-Net profile URI.
  - The server should return successful responses (HTTP 200) for resources queried by profile URI, and the resources should match the expected profile structure.

By following this structured approach, the test will ensure that the server correctly identifies and supports the Plan-Net profiles as required by the Implementation Guide.
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
  - The requirement can be tested using automated scripts that execute search operations and validate responses against expected outcomes.

### Complexity
- **Classification**: Moderate
  - The complexity arises from the need to test multiple search parameters across different profiles, ensuring each is supported individually.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server must have implemented the relevant profiles with search parameter support as per the Capability Statement.
- **Data Setup**:
  - Populate the server with test data that includes resources conforming to the profiles in question.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A list of profiles and their corresponding search parameters as defined in the Implementation Guide.
  - Test queries for each search parameter.

- **Expected Outputs**:
  - Successful execution of search queries returning appropriate resource bundles.
  - Each search parameter should return results consistent with the data setup and profile definitions.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resource]?parameter=value`
  - Ensure the server's Capability Statement includes support for the `search` operation on the relevant resources.

### Test Data Requirements
- **Data Types**:
  - Resources that conform to the profiles being tested.
  - Each resource should have attributes that can be queried using the defined search parameters.

### Validation Criteria
- **Conformance Checks**:
  - Verify that each search operation returns a `200 OK` status code.
  - Validate that the returned resources match the search criteria specified in the query.
  - Ensure the search results are consistent with the expected number of resources and their attributes.
  - Confirm that unsupported search parameters result in an appropriate error response (e.g., `400 Bad Request`).

- **Assertions**:
  - Assert that the response bundle type is `searchset`.
  - Assert that the resources in the response conform to the expected profile.
  - Assert that the server's response time is within acceptable limits for search operations.

By following this test specification, the implementation of individual search parameter support can be thoroughly verified, ensuring compliance with the FHIR Implementation Guide requirements.
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
  - The requirement can be tested using automated scripts that perform search operations with multiple parameters and validate the responses.

### Complexity
- **Classification**: Moderate
  - While the concept of search is straightforward, the combination of multiple search parameters across different profiles adds complexity.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be running and accessible.
  - The server must support the search operations as defined in the Capability Statement.
- **Data Setup**: 
  - The server must have sufficient data populated that aligns with the profiles being tested, ensuring that search operations can return meaningful results.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs for the Test
- **Inputs**: 
  - A set of search parameter combinations for each profile defined in the implementation guide.
  - Example: For a Patient profile, search parameters might include `name`, `birthdate`, and `gender`.
- **Expected Outputs**: 
  - Correct FHIR resources returned that match the search criteria.
  - HTTP status code 200 (OK) for successful searches.
  - Proper handling of no results found, with an empty bundle and status code 200.

### Required FHIR Operations
- **API Calls/Operations**: 
  - `GET [base]/[resourceType]?parameter1=value1&parameter2=value2...`
  - Ensure that the server supports these operations as indicated in the Capability Statement.

### Test Data Requirements
- **Type of Test Data**: 
  - A diverse dataset that includes multiple instances of each profile with varying attributes.
  - Data should be representative of real-world scenarios to ensure comprehensive testing of search functionality.

### Validation Criteria
- **Specific Checks**:
  - Verify that the response contains only resources that match all specified search parameters.
  - Validate the structure and content of the returned FHIR resources against the expected profiles.
  - Confirm that the server correctly handles edge cases, such as no matching resources or invalid parameter values.
  - Check that the response time is within acceptable limits to ensure performance is not degraded by combination searches.
  
- **Assertions**:
  - Assert that the HTTP response status code is 200.
  - Assert that the returned Bundle contains the expected number of entries.
  - Assert that each entry in the Bundle matches the search criteria.
  - Assert that the server logs or error messages (if applicable) do not indicate any processing errors.

This test specification provides a structured approach to validating the combination search parameter support as required by the FHIR Implementation Guide, ensuring that the server meets the conformance criteria.

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
  - The requirement can be tested using automated scripts that simulate client-server interactions and verify the server's response to forward chaining queries.

### Complexity
- **Complexity**: Moderate
  - While the concept of forward chaining is straightforward, ensuring comprehensive coverage across all search parameters that specify the 'chain' property requires careful consideration of various resource types and their interrelations.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be configured to support search operations and forward chaining as specified in the Capability Statement.
- **Data Setup**: 
  - A set of FHIR resources with known relationships that can be used to test forward chaining.
  - Ensure that the server's Capability Statement includes support for the necessary search parameters and chaining.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A series of FHIR search queries utilizing the 'chain' property on various resources (e.g., Patient, Observation, Encounter).
- **Expected Outputs**: 
  - Correctly chained search results that reflect the relationships between resources as specified in the queries.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resource]?[parameter]:[chain]=[value]`
  - Ensure that the server's Capability Statement indicates support for these operations.

### Test Data Requirements
- **Test Data**:
  - A dataset containing interconnected FHIR resources, such as:
    - Patients with linked Observations and Encounters.
    - Practitioners linked to Patients via Encounters.
  - The data should include various scenarios to test different chaining paths.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server returns the correct resources when a forward chaining search is performed.
  - Ensure that the chaining logic respects the relationships defined in the FHIR resources.
  - Assertions:
    - The response contains the expected number of resources.
    - The resources in the response match the criteria specified in the chained search query.
    - The server's response time is within acceptable limits for chained searches.
```


---

<a id='req-22'></a>

### REQ-22: Reverse chaining support

**Description**: "Support reverse chaining on all search parameters that specify the 'chain' property."

**Actor**: Server

**Conformance**: SHALL

```markdown
# Test Specification for FHIR Implementation Guide Requirement

## 1. Requirement ID
- **REQ-22**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement involves validating the server's ability to support reverse chaining, which can be tested programmatically by executing specific search queries and verifying the responses.

### Complexity
- **Classification**: Moderate
  - While the concept of reverse chaining is straightforward, ensuring that it works across all applicable search parameters requires a comprehensive set of tests.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server's Capability Statement must indicate support for search operations and reverse chaining.
- **Data Setup**:
  - The server must have sufficient data populated to test reverse chaining effectively. This includes resources that are linked in a manner that supports chaining.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A set of search queries utilizing reverse chaining on various search parameters that specify the 'chain' property.
- **Expected Outputs**:
  - Responses that correctly reflect the reverse chaining logic, returning the expected resources based on the search criteria.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resource]?_has:[relatedResource]:[searchParameter]:[value]`
  - Ensure these operations are supported as per the server's Capability Statement.

### Test Data Requirements
- **Data Types**:
  - Resources that are interlinked, such as Patient, Observation, and Encounter, where chaining can be applied.
  - Example: Patients linked to Observations, where reverse chaining can be tested by searching for Observations that link back to specific Patients.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server's responses include the correct resources based on the reverse chaining logic.
  - Assertions should check:
    - The presence of expected resources in the response.
    - The absence of resources that do not meet the chaining criteria.
    - Correct handling of edge cases, such as no matches or multiple matches.
  - Ensure that the server's response time and performance are within acceptable limits for search operations.

- **Result Indication**:
  - A test passes if the server returns the correct resources for all tested reverse chaining queries and meets performance expectations.
  - A test fails if any query does not return the expected results or if the server fails to handle the operation efficiently.
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
  - The requirement to support XML format can be tested programmatically by sending requests and validating responses in XML format.

### Complexity
- **Complexity**: Moderate
  - While the support for XML format is straightforward, it involves testing across all Plan-Net interactions, which may include multiple resource types and operations.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to accept and respond with XML formatted data.
- **Data Setup**:
  - Ensure that the server has a variety of Plan-Net resources available for testing.
  - Access to the server's Capability Statement to verify supported operations.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - FHIR requests for each Plan-Net interaction in XML format.
- **Expected Outputs**:
  - FHIR responses for each interaction in XML format, conforming to the FHIR XML schema.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET` requests for reading resources.
  - `POST`, `PUT`, `DELETE` requests for creating, updating, and deleting resources.
  - Ensure these operations are supported as per the server's Capability Statement.

### Test Data Requirements
- **Test Data**:
  - A set of Plan-Net resources (e.g., Practitioner, Organization, HealthcareService) in XML format.
  - Test data should cover various scenarios including valid, invalid, and edge cases for resource attributes.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server correctly processes requests with `Content-Type: application/fhir+xml` and `Accept: application/fhir+xml` headers.
  - Ensure that the server returns valid XML responses that conform to the FHIR XML schema.
  - Validate that all Plan-Net interactions (CRUD operations) are supported in XML format.
  - Confirm that the server's Capability Statement includes XML format support for all relevant interactions.
  - Check for proper error handling and appropriate status codes in XML format for invalid requests.

By following this test specification, the requirement for XML format support across all Plan-Net interactions can be thoroughly validated.
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
  - The requirement involves checking for a specific HTTP response code (401) when unauthorized requests are made, which is straightforward to implement and verify.

### Prerequisites
- **System Configurations**: 
  - The server must be running and accessible over the network.
  - Authentication mechanisms (e.g., OAuth2, Basic Auth) must be configured on the server.
- **Data**: 
  - No specific data setup is required as the test focuses on unauthorized access.
- **Setup**: 
  - Ensure that there are endpoints available that require authentication.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - An HTTP request to a secured FHIR endpoint without valid authentication credentials.
- **Expected Outputs**: 
  - The server responds with an HTTP 401 Unauthorized status code.

### Required FHIR Operations
- **API Calls/Operations**:
  - Perform a GET request on a secured FHIR endpoint (e.g., Patient, Observation) without including authentication credentials.

### Test Data Requirements
- **Test Data**:
  - No specific FHIR resources are needed as the test is focused on authentication rather than data content.

### Validation Criteria
- **Validation Checks**:
  - Verify that the server returns an HTTP 401 Unauthorized status code.
  - Ensure that the response does not include any FHIR resource data.
  - Optionally, check for the presence of a `WWW-Authenticate` header in the response, indicating the authentication method required.

### Additional Considerations
- **Negative Testing**:
  - Attempt to access multiple secured endpoints to ensure consistent behavior across the server.
- **Boundary Testing**:
  - Test with different types of unauthorized requests (e.g., missing token, expired token) to ensure robust rejection mechanisms.

By following this test specification, you can ensure that the server correctly rejects unauthorized requests, maintaining compliance with the FHIR Implementation Guide requirement REQ-24.
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
  - The requirement involves verifying the server's capability to perform read interactions, which can be tested programmatically by making API calls and checking responses.

### Complexity
- **Complexity**: Simple
  - The read interaction is a basic FHIR operation and involves straightforward API requests and responses.

### Prerequisites
- **System Configurations**: 
  - A Plan Net server instance configured to expose FHIR endpoints.
  - Network access to the server for testing purposes.
- **Data Setup**:
  - The server must have pre-loaded resources for each resource type and profile defined in the Plan Net implementation guide.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Resource type and profile identifiers as specified in the Plan Net implementation guide.
  - Valid resource IDs for existing resources on the server.

- **Expected Outputs**:
  - HTTP Status Code 200 (OK) for successful read operations.
  - The response body should contain the resource in the expected FHIR format.
  - The resource should conform to the specified profile.

### Required FHIR Operations
- **FHIR Operation**: 
  - `GET [base]/[resourceType]/[id]`
  - Ensure that the server's Capability Statement includes support for the `read` operation on all relevant resource types.

### Test Data Requirements
- **Test Data**:
  - A set of resource IDs for each resource type and profile that are known to exist on the server.
  - These resources should be pre-validated to conform to the profiles they are associated with.

### Validation Criteria
- **Validation Checks**:
  - Verify that the server returns a 200 HTTP status code for each read operation.
  - Confirm that the returned resource matches the requested resource ID and conforms to the specified profile.
  - Validate that the response includes all mandatory elements defined in the profile.
  - Check that the resource's meta.profile element includes the profile URL, indicating conformance to the profile.
- **Assertions**:
  - Assert that the response is in valid FHIR JSON or XML format.
  - Assert that the resource content matches the expected structure and data types as per the profile definition.
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
  - The verification of the vread interaction can be automated by sending requests to the server and validating responses.

### Complexity
- **Complexity**: Moderate
  - While the vread interaction itself is straightforward, ensuring it works across all resource types and profiles increases complexity.

### Prerequisites
- **System Configurations**: 
  - The server must be running and accessible with the necessary endpoints configured.
- **Data Setup**:
  - The server must have existing resources with known versions to test the vread interaction.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Resource type and ID
  - Specific version ID of the resource
- **Expected Outputs**:
  - HTTP 200 OK status code
  - Resource representation corresponding to the specified version
  - Correct `Last-Modified` and `ETag` headers reflecting the version

### Required FHIR Operations
- **vread Operation**:
  - `GET [base]/[resource-type]/[id]/_history/[version-id]`
  - Ensure that the Capability Statement indicates support for vread for each resource type.

### Test Data Requirements
- **Test Data**:
  - A set of resources with multiple versions available on the server.
  - Each resource should have a known version history to validate the vread interaction.

### Validation Criteria
- **Validation Checks**:
  - Verify that the response status code is 200.
  - Confirm that the returned resource matches the expected version content.
  - Check that the `Last-Modified` header matches the expected modification date of the version.
  - Validate that the `ETag` header reflects the correct version identifier.
  - Ensure that the server's Capability Statement lists vread as a supported operation for the resource type.

- **Assertions**:
  - The server correctly returns the specified version of the resource.
  - The response headers are accurate and conform to FHIR standards.
  - The server's Capability Statement includes vread support for the tested resource types.

By following this test specification, the implementation of the vread interaction can be effectively validated for compliance with the FHIR Implementation Guide requirement REQ-26.
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
- **REQ-27**: Support for _includes

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement can be tested using automated scripts that simulate client-server interactions and verify the server's response to _includes parameters.

### Complexity
- **Complexity Level**: Moderate
  - While the concept of _includes is straightforward, the complexity arises from ensuring that the server correctly processes and returns the appropriate resources as specified in the _includes parameter.

### Prerequisites
- **System Configurations**: 
  - A FHIR server instance that implements the applicable resources and supports search operations.
  - Access to the server's Capability Statement to verify support for _includes.
- **Data Setup**:
  - Pre-populated FHIR resources that can be used to test the _includes functionality, ensuring that linked resources are available for inclusion.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A list of FHIR resource types and their respective _includes parameters as specified in the implementation guide.
  - Search queries using _includes parameters.
- **Expected Outputs**:
  - The server should return a bundle containing the primary resources and the included resources as specified by the _includes parameter.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resource]?_include=[parameter]`
  - `GET [base]/[resource]?_include=[parameter1]&_include=[parameter2]` (for multiple includes)
  - Ensure these operations are supported by checking the server's Capability Statement.

### Test Data Requirements
- **Type of Test Data**:
  - A set of FHIR resources with known relationships that can be used to verify the _includes functionality. For example, Patient resources linked to Encounter resources, where the Encounter resource should be included in the search results.

### Validation Criteria
- **Specific Checks**:
  - Verify that the server's response includes the primary resource and the related resources as specified by the _includes parameter.
  - Check that the response is a valid FHIR Bundle with the correct structure.
  - Confirm that the server's Capability Statement lists support for the _includes parameters being tested.
  - Ensure that the response time is within acceptable limits for performance testing.
  - Validate that no errors are returned by the server during the processing of the _includes parameter.

- **Assertions**:
  - The response bundle contains all expected resources.
  - The included resources are correctly linked to the primary resources.
  - The server's Capability Statement confirms support for the tested _includes parameters.
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
  - This requirement can be tested using automated scripts that perform API calls and validate responses.

### Complexity
- **Complexity Level**: Moderate
  - The complexity arises from the need to handle multiple resource types and ensure that the server correctly processes _revincludes for each.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to support FHIR RESTful interactions.
  - The server's Capability Statement must declare support for _revincludes.
- **Data Setup**:
  - The server must have existing resources that are linked to other resources through references, allowing for _revincludes to be tested.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A list of resource types and their corresponding _revincludes as specified in the requirement.
  - Specific resource IDs or search parameters to initiate the _revincludes search.
- **Expected Outputs**:
  - The server should return a bundle containing the primary resources and the included resources as specified by the _revincludes parameter.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resourceType]?_id=[id]&_revincludes=[relatedResource]`
  - Ensure these operations are supported as per the server's Capability Statement.

### Test Data Requirements
- **Test Data**:
  - A set of resources with known references to other resources (e.g., a Patient resource with references to related Observations or Encounters).
  - Ensure diversity in the data to cover different resource types and relationships.

### Validation Criteria
- **Specific Checks**:
  - Verify that the response bundle includes the primary resource and all related resources as specified by the _revincludes parameter.
  - Check for correct HTTP status codes (e.g., 200 OK).
  - Validate that the included resources are correctly linked to the primary resource.
  - Ensure that the server's response adheres to the FHIR specification for bundles and resource inclusion.
- **Assertions**:
  - The response contains all expected resources.
  - The response structure matches the FHIR specification for a search response with included resources.
  - No unexpected resources are included in the response.
```


---

<a id='req-29'></a>

### REQ-29: Network profile NPI handling

**Description**: "The NPI and CLIA identifier types, which are Must-Support, are clearly intended for provider organizations only and are not expected to be populated for other organization types."

**Actor**: Server

**Conformance**: None (Clarification)

```markdown
# Test Specification for REQ-29: Network Profile NPI Handling

## 1. Requirement ID
- **REQ-29**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement can be tested automatically by querying the FHIR server and verifying the presence or absence of NPI and CLIA identifiers based on the organization type.

### Complexity
- **Complexity**: Moderate
  - The complexity is moderate due to the need to differentiate between provider and non-provider organization types and verify the presence of specific identifiers.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be configured to support the Organization resource and the relevant operations.
- **Data Setup**:
  - The server must have pre-existing Organization resources with varying types (provider and non-provider) for testing.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - FHIR Organization resources with different types (e.g., provider, hospital, lab, etc.).
- **Expected Outputs**:
  - Provider-type organizations should have NPI and CLIA identifiers populated.
  - Non-provider-type organizations should not have NPI and CLIA identifiers populated.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET /Organization` to retrieve organization resources.
  - Ensure these operations are supported as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - At least one Organization resource of type "provider" with NPI and CLIA identifiers.
  - At least one Organization resource of a non-provider type without NPI and CLIA identifiers.

### Validation Criteria
- **Specific Checks**:
  - For each Organization resource of type "provider", assert that:
    - The `identifier` field includes both NPI and CLIA identifiers.
  - For each Organization resource of a non-provider type, assert that:
    - The `identifier` field does not include NPI and CLIA identifiers.
- **Assertions**:
  - The test passes if all provider-type organizations have the required identifiers and all non-provider-type organizations do not have these identifiers.
  - The test fails if any provider-type organization lacks the identifiers or any non-provider-type organization has them.

```
This structured test specification provides a clear and comprehensive approach to verifying the requirement REQ-29 for network profile NPI handling in FHIR implementations.

---

<a id='req-30'></a>

### REQ-30: lastUpdate timestamp requirement

**Description**: "Each profile in this guide requires that the lastUpdate timestamp be provided as part of the profile's data content."

**Actor**: Server

**Conformance**: None (Requirement)

```markdown
# Test Specification for REQ-30: lastUpdate Timestamp Requirement

## 1. Requirement ID
- **REQ-30**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement can be tested programmatically by checking the presence and format of the `lastUpdate` timestamp in the profile's data content.

### Complexity
- **Complexity**: Simple
  - The requirement involves verifying the existence and correct format of a single timestamp field.

### Prerequisites
- **System Configurations**: 
  - The server must be configured to support the FHIR operations required for retrieving profile data.
- **Data Setup**:
  - Profiles must be available on the server for testing.
  - Ensure that the profiles are updated to include the `lastUpdate` timestamp.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - FHIR resource profiles to be tested.
- **Expected Outputs**:
  - Each profile should include a `lastUpdate` timestamp in the correct format (e.g., ISO 8601).

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/[resourceType]/[id]`: Retrieve the specific profile resource by its ID.
  - Ensure the server's Capability Statement supports these operations.

### Test Data Requirements
- **Test Data**:
  - A set of profile resources that are expected to include the `lastUpdate` timestamp.
  - Profiles should be varied to cover different resource types if applicable.

### Validation Criteria
- **Validation Checks**:
  1. **Presence Check**: Verify that the `lastUpdate` timestamp is present in the profile's data content.
  2. **Format Check**: Confirm that the `lastUpdate` timestamp follows the correct format (e.g., ISO 8601).
  3. **Consistency Check**: Ensure that the `lastUpdate` timestamp is consistent with the profile's metadata and reflects the last modification time.

- **Assertions**:
  - The test passes if all profiles include a `lastUpdate` timestamp in the correct format.
  - The test fails if any profile is missing the `lastUpdate` timestamp or if the timestamp is in an incorrect format.
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
  - The requirement involves executing search queries and verifying the results, which can be automated using test scripts.

### Complexity
- **Complexity Level**: Moderate
  - The test involves multiple search parameters and requires validation against specific fields in the `HealthcareService` and `Location` resources.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be configured to support search operations on `HealthcareService` and `Location` resources.
- **Data Setup**: 
  - The system must have pre-existing data for `HealthcareService` resources with categories and specialties related to pharmacies.
  - `Location` resources must be associated with the `HealthcareService` entries to test location-based searches.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - Search queries using the `HealthcareService` resource with filters on `category` and `specialty`.
  - Search queries using the `Location` resource with filters on `address`, `type`, etc.
- **Expected Outputs**: 
  - A list of `HealthcareService` resources that match the search criteria for pharmacies.
  - A list of `Location` resources that correspond to the `HealthcareService` entries.

### Required FHIR Operations
- **API Calls**:
  - `GET /HealthcareService?category=<pharmacy-category>&specialty=<pharmacy-specialty>`
  - `GET /Location?address-city=<city>&address-state=<state>&address-postalcode=<postalcode>`

### Test Data Requirements
- **HealthcareService Data**:
  - Entries with `category` set to pharmacy-related categories.
  - Entries with `specialty` set to pharmacy-related specialties.
- **Location Data**:
  - Entries with valid addresses, including city, state, and postal code.

### Validation Criteria
- **HealthcareService Validation**:
  - Verify that all returned `HealthcareService` entries have `category` and `specialty` fields matching the search criteria.
- **Location Validation**:
  - Confirm that all returned `Location` entries are associated with the `HealthcareService` entries and match the address criteria.
- **Assertions**:
  - The response status code should be `200 OK`.
  - The response should contain a `Bundle` with `entry` elements corresponding to the search criteria.
  - Each `entry` should contain a `resource` of type `HealthcareService` or `Location` as applicable.
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
  - The requirement involves searching for providers by name, which can be automated using FHIR API calls and verifying the responses.

### Complexity
- **Complexity Level**: Moderate
  - The search functionality itself is straightforward, but it involves multiple parameters and potential combinations with location, network, specialty, and role/privileges, increasing complexity.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be configured to support Practitioner and Location resources.
- **Data Setup**:
  - A dataset of Practitioner resources with diverse names, locations, networks, specialties, and roles/privileges.
  - Ensure that the dataset includes practitioners named "Joe Smith" for testing.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Search query for Practitioner resource by name, e.g., `Practitioner?name=Joe+Smith`
- **Expected Outputs**:
  - A list of Practitioner resources matching the name "Joe Smith".
  - The results should include relevant details such as location, network, specialty, and role/privileges if available.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Practitioner?name=Joe+Smith`
  - Optionally, extend searches with additional parameters like location, network, specialty, and role/privileges if supported.

### Test Data Requirements
- **Practitioner Data**:
  - Practitioners with varying names, including "Joe Smith".
  - Practitioners associated with different locations, networks, specialties, and roles/privileges.
- **Location Data**:
  - Locations associated with practitioners to test location-based filtering.

### Validation Criteria
- **Conformance Checks**:
  - Verify that the search returns only practitioners with the name "Joe Smith".
  - Validate that the returned Practitioner resources include correct and complete data for fields such as location, network, specialty, and role/privileges.
  - Ensure that the search response adheres to the FHIR standard for Practitioner resources.
  - Confirm that the search supports the required search parameters as specified in the Capability Statement.
- **Assertions**:
  - The response status code should be 200 (OK).
  - The response should contain a `Bundle` of type `searchset`.
  - Each entry in the Bundle should be a Practitioner resource with the name "Joe Smith".
  - Validate that the search results are consistent with the expected dataset and configurations.

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
  - The requirement can be tested using automated scripts that perform search operations and validate responses.

### Complexity
- **Level**: Simple
  - The search operation by name is a straightforward query and involves basic string matching.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be running and accessible.
  - The server must support the Organization resource and the relevant search parameters as per the Capability Statement.
  
- **Data Setup**:
  - Ensure the server has a diverse set of Organization resources with varying names, including "Montgomery Cardiology" and "CVS".
  - Include Organizations with different locations, networks, and specialties to validate the qualifications of the search.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Input**: 
  - FHIR search query for Organization resource using the `name` search parameter.
  - Example: `GET [base]/Organization?name=Montgomery%20Cardiology`
  
- **Expected Output**:
  - A list of Organization resources that match the search name "Montgomery Cardiology".
  - Each returned Organization should have the `name` field containing the search term.
  - Validate that the search results are filtered correctly based on the `name` parameter.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Organization?name=[search-term]`
  - Ensure the server supports the `name` search parameter as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - Organization resources with names including "Montgomery Cardiology", "CVS", and other variations to test partial and exact matches.
  - Organizations should have associated locations, networks, and specialties to test the qualifications of the search.

### Validation Criteria
- **Specific Checks**:
  - Verify that the search results include only those Organizations whose `name` field matches the search term.
  - Check that the response is a valid FHIR Bundle with a `Bundle.type` of `searchset`.
  - Ensure that the search respects FHIR search parameter rules, including case insensitivity and partial matching.
  - Confirm that the response contains all necessary metadata, such as `total` count and `link` elements for pagination if applicable.
- **Assertions**:
  - Assert that the HTTP response status code is 200 (OK).
  - Assert that the `Bundle.entry` contains at least one Organization resource for known search terms.
  - Assert that each Organization in the `Bundle.entry` has a `name` field that includes the search term.

By following this structured test specification, the requirement REQ-34 can be effectively validated to ensure compliance with the FHIR Implementation Guide.

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
  - The requirement can be tested using automated scripts that perform API calls and validate responses.

### Complexity
- **Complexity Level**: Moderate
  - The test involves multiple search parameters and requires validation of search results based on specialty, location, network, and name.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be configured to support the PractitionerRole resource and its associated search parameters.
- **Data Setup**:
  - Populate the FHIR server with test data that includes multiple PractitionerRole resources with various specialties, locations, networks, and names.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Search query with `PractitionerRole.specialty` set to a specific specialty (e.g., Cardiologist).
  - Optional filters: `location`, `network`, `name`.
- **Expected Outputs**:
  - A list of PractitionerRole resources where the `specialty` matches the search query.
  - Resources should be filtered correctly based on additional parameters if provided.

### Required FHIR Operations
- **API Calls**:
  - `GET [base]/PractitionerRole?specialty=[specialty]&location=[location]&network=[network]&name=[name]`
  - Ensure the server supports these operations as per the Capability Statement.

### Test Data Requirements
- **Test Data**:
  - PractitionerRole resources with various specialties, including at least one with the specialty "Cardiologist".
  - Resources should have diverse locations, networks, and names to test filtering capabilities.

### Validation Criteria
- **Conformance Checks**:
  - Verify that the response contains only PractitionerRole resources with the specified specialty.
  - If additional filters are applied (location, network, name), ensure the results are accurately filtered.
  - Validate that the response adheres to the FHIR standard for PractitionerRole resources.
  - Check for proper handling of edge cases, such as no results found or invalid search parameters.
  - Confirm that the search operation completes within acceptable performance thresholds.

- **Assertions**:
  - The response status code should be 200 (OK).
  - The response body should contain a `Bundle` of type `searchset`.
  - Each entry in the bundle should be a PractitionerRole resource with the correct specialty.
  - If filters are applied, ensure that all entries meet the criteria specified in the search parameters.
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
  - The requirement involves executing FHIR search operations, which can be automated using test scripts.

### Complexity
- **Complexity**: Moderate
  - The test involves multiple search parameters and requires validation of search results based on specialty and additional qualifiers.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be configured to support the Organization, Location, and OrganizationAffiliation resources.
  - The server must support the search parameters as outlined in the Capability Statement.

- **Data Setup**:
  - The test environment must have pre-populated data including Organizations, Locations, and OrganizationAffiliations with various specialties, including "Compounding Pharmacy".

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs for the Test
- **Inputs**:
  - Search query for OrganizationAffiliation with specialty set to "Compounding Pharmacy".
  - Optional qualifiers: location, network, name.

- **Expected Outputs**:
  - A list of Organization resources that match the search criteria, specifically those affiliated with the "Compounding Pharmacy" specialty.
  - The search results should correctly filter based on any additional qualifiers provided.

### Required FHIR Operations
- **Search Operations**:
  - Perform a search on the `OrganizationAffiliation` resource using the `specialty` search parameter.
  - Utilize additional search parameters as needed: `location`, `network`, `name`.

### Test Data Requirements
- **Test Data**:
  - OrganizationAffiliation instances with various specialties, including "Compounding Pharmacy".
  - Associated Organization and Location resources that can be referenced in searches.

### Validation Criteria
- **Conformance Checks**:
  - Verify that the search results include only those Organization resources that have an affiliation with the specified specialty.
  - Ensure that the search results are correctly filtered when additional qualifiers (location, network, name) are used.
  - Confirm that the response structure adheres to the FHIR standard for search results.

- **Assertions**:
  - The response should contain a `Bundle` of type `searchset`.
  - Each entry in the Bundle should be an `Organization` resource that meets the search criteria.
  - The search operation should return a `200 OK` status code.
  - Validate that the search parameters are correctly interpreted by the server and reflected in the search results.

This test specification outlines the approach to verify the functionality of searching Organizations by specialty, ensuring compliance with the FHIR Implementation Guide requirements and the applicable Capability Statement.
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
- **REQ-37**: Search for active practitioners and organizations

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatic
  - The requirement involves executing FHIR search queries and verifying the responses, which can be automated using test scripts.

### Complexity
- **Classification**: Moderate
  - The test involves multiple resources and search parameters, requiring careful setup and validation of responses.

### Prerequisites
- **System Configurations**: 
  - Access to a FHIR server that supports the required resources and search parameters as per the Capability Statement.
- **Data Setup**:
  - Ensure that the FHIR server contains data for Practitioners and Organizations with various active and inactive statuses.
  - Date fields in PractitionerRole and OrganizationAffiliation must be appropriately populated for testing date-based queries.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - Current date for the search queries.
  - URLs for the FHIR server endpoints for PractitionerRole and OrganizationAffiliation.
- **Expected Outputs**:
  - Responses containing only active Practitioners and Organizations as of the current date.

### Required FHIR Operations
- **API Calls**:
  - `GET /PractitionerRole?_include=PractitionerRole:date=ge<current-date>`
  - `GET /OrganizationAffiliation?_include=OrganizationAffiliation:date=ge<current-date>`

### Test Data Requirements
- **PractitionerRole Data**:
  - Practitioners with roles that have varying active dates, including some with dates before and some after the current date.
- **OrganizationAffiliation Data**:
  - Organizations with affiliations that have varying active dates, including some with dates before and some after the current date.

### Validation Criteria
- **Response Validation**:
  - Verify that all returned PractitionerRole resources have a `date` field greater than or equal to the current date.
  - Verify that all returned OrganizationAffiliation resources have a `date` field greater than or equal to the current date.
  - Ensure that the responses conform to the FHIR standard and include the necessary resource elements as per the Capability Statement.
- **Assertions**:
  - Assert that no inactive practitioners or organizations are included in the response.
  - Assert that the response status code is 200 (OK).
  - Validate that the response format is JSON and adheres to the FHIR specification.

```


---

<a id='req-38'></a>

### REQ-38: Network contact handling for departments

**Description**: "When the contact is a department name, rather than a human (e.g., patient help line), include a blank family and given name, and provide the department name in contact.name.text."

**Actor**: Server

**Conformance**: None (Implementation guidance)

```markdown
# Test Specification for Requirement REQ-38

## 1. Requirement ID
- **REQ-38**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Manual
  - The requirement involves inspecting the structure of contact information, specifically the handling of department names in a FHIR resource. This requires human verification to ensure the correct fields are populated as per the guidance.

### Complexity
- **Complexity**: Simple
  - The requirement involves checking the presence or absence of specific fields within a FHIR resource, which is straightforward.

### Prerequisites
- **System Configurations**: 
  - The FHIR server must be operational and accessible.
  - The server must support the relevant FHIR resources that include contact information, such as `Organization` or `Practitioner`.

- **Data Setup**:
  - The server should have at least one resource instance where the contact is a department name (e.g., a patient help line).

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**:
  - A FHIR resource (e.g., `Organization`) with contact information where the contact is a department name.

- **Expected Outputs**:
  - The `contact.name.text` field should contain the department name.
  - The `contact.name.family` and `contact.name.given` fields should be blank.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Organization/{id}`: Retrieve an `Organization` resource by ID.
  - Ensure the server's Capability Statement supports the `read` operation for the `Organization` resource.

### Test Data Requirements
- **Test Data**:
  - An `Organization` resource with a contact entry where the contact is a department, such as a "patient help line".

### Validation Criteria
- **Specific Checks**:
  - Verify that `contact.name.text` is populated with the department name.
  - Verify that `contact.name.family` is empty.
  - Verify that `contact.name.given` is empty.

- **Assertions**:
  - The test passes if the `contact.name.text` field correctly contains the department name and both `contact.name.family` and `contact.name.given` fields are blank.
  - The test fails if any of these conditions are not met.

```
This test specification outlines the steps needed to manually verify that department contacts in FHIR resources are handled according to the implementation guide's requirements. It ensures that department names are correctly represented in the `contact.name.text` field while leaving `contact.name.family` and `contact.name.given` fields blank.

---

<a id='req-39'></a>

### REQ-39: Organization contact handling for departments

**Description**: "When the contact is a department name, rather than a human (e.g., patient help line), include a blank family and given name, and provide the department name in contact.name.text."

**Actor**: Server

**Conformance**: None (Implementation guidance)

```markdown
# Test Specification for REQ-39: Organization Contact Handling for Departments

## 1. Requirement ID
- **REQ-39**

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Manual
  - **Rationale**: This requirement involves verifying the structure of the Organization resource, specifically the contact details, which is best inspected manually to ensure that the department name is correctly placed in `contact.name.text` and that `family` and `given` names are blank.

### Complexity
- **Level**: Simple
  - **Rationale**: The requirement involves straightforward validation of the presence and structure of specific fields within the Organization resource.

### Prerequisites
- **System Configurations**: 
  - A FHIR server that implements the Organization resource as per the Capability Statement.
- **Data Setup**: 
  - At least one Organization resource with a contact representing a department (e.g., a patient help line).

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs for the Test
- **Input**: 
  - A request to retrieve an Organization resource that includes a contact for a department.
- **Expected Output**: 
  - The `contact.name.text` should contain the department name.
  - The `contact.name.family` and `contact.name.given` should be blank.

### Required FHIR Operations
- **API Calls/Operations**:
  - `GET [base]/Organization?_id=[organization-id]`: Retrieve the specific Organization resource by its ID.
  - `GET [base]/Organization?name=[department-name]`: Search for the Organization by department name to ensure it is correctly indexed.

### Test Data Requirements
- **Test Data**:
  - An Organization resource with:
    - `contact.name.text` populated with a department name (e.g., "Patient Help Line").
    - `contact.name.family` and `contact.name.given` fields left blank.

### Validation Criteria
- **Specific Checks**:
  - **Check 1**: Verify that `contact.name.text` is populated with the correct department name.
  - **Check 2**: Ensure that `contact.name.family` is blank.
  - **Check 3**: Ensure that `contact.name.given` is blank.
  - **Check 4**: Confirm that the Organization resource can be retrieved using the `name` search parameter with the department name.
- **Assertions**:
  - The department name is correctly displayed in `contact.name.text`.
  - The `family` and `given` fields are not populated.
  - The Organization resource is retrievable via search using the department name.

```


---

<a id='req-40'></a>

### REQ-40: Practitioner qualification coding

**Description**: "When the value set for the coded concept in qualification is insufficient, the qualification can be provided in the text field of the codeableConcept."

**Actor**: Server

**Conformance**: None (Implementation guidance)

```markdown
# Test Specification for Requirement REQ-40

## 1. Requirement ID
- **REQ-40**: Practitioner qualification coding

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Manual
  - **Rationale**: The requirement involves inspecting the text field of a CodeableConcept when the coded concept is insufficient, which requires human judgment to assess the appropriateness of the text content.

### Complexity
- **Classification**: Moderate
  - **Rationale**: The requirement involves understanding the context of qualifications and ensuring that the text field is used appropriately when the coded values are insufficient.

### Prerequisites
- **System Configurations**: 
  - A FHIR server that supports the Practitioner resource and adheres to the specified Capability Statement.
- **Data Setup**: 
  - Practitioner resources with qualifications that have both coded and text fields populated.

## 3. Test Implementation Strategy

### Required Inputs and Expected Outputs
- **Inputs**: 
  - A Practitioner resource with a qualification where the coded concept is insufficient, and the text field is populated.
- **Expected Outputs**: 
  - Verification that the text field provides a meaningful and contextually appropriate description of the qualification when the coded concept is insufficient.

### Required FHIR Operations
- **Operations**: 
  - `GET [base]/Practitioner?_id=[id]`
  - `GET [base]/Practitioner?name=[name]`
  - `GET [base]/Practitioner?family=[family]`
  - `GET [base]/Practitioner?given=[given]`
  - `GET [base]/Practitioner?_lastUpdated=[date]`
  - These operations are supported as per the Capability Statement and will be used to retrieve Practitioner resources for inspection.

### Test Data Requirements
- **Test Data**: 
  - Practitioner resources with varying qualifications, including those where the coded concept is insufficient and the text field is used to provide additional context.

### Validation Criteria
- **Checks**:
  - Ensure that when the coded concept in a qualification is insufficient, the text field of the CodeableConcept is populated.
  - Verify that the text field provides a clear and relevant description of the qualification.
  - Confirm that the text field is used appropriately and not redundantly when the coded concept is sufficient.
- **Assertions**:
  - The text field must not be empty when the coded concept is insufficient.
  - The content of the text field should be coherent and provide additional clarity or context to the qualification.
  - The test passes if the text field is appropriately used and provides meaningful information when the coded concept is insufficient.

```


---



