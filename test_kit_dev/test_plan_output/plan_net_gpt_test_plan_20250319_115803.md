# Comprehensive Test Plan for Plan Net

## Generated on: 2025-03-19 12:01:36



## Test Plan for Server-SHOULD

1. Executive Summary
   - This test plan aims to validate the conformance of the FHIR Implementation Guide to the requirement REQ-PRIV-001, which stipulates that the Plan-Net service should not require authentication and should not maintain records associating the consumer with queried entities.
   - Key testing considerations include server configuration, privacy, and security aspects.

2. Test Environment Requirements
   - A FHIR server with the Plan-Net service installed and configured.
   - Test data to simulate consumer queries.
   - Tools to inspect server logs and data storage for verification.

3. Test Groupings
   - Group 1: Authentication Requirements
     - This group tests the server's behavior when a consumer attempts to access the Plan-Net service. The server should not require authentication.
   - Group 2: Privacy Considerations
     - This group tests the server's data storage and logging practices. The server should not maintain records associating the consumer with queried entities.

4. Individual Test Cases
   - Test Case ID: REQ-PRIV-001-TC1
     - Preconditions: The FHIR server is running with the Plan-Net service.
     - Test Steps: Attempt to access the Plan-Net service without providing authentication.
     - Expected Results: The server allows access to the Plan-Net service without requiring authentication.
     - Validation Criteria: The server does not prompt for authentication and provides access to the Plan-Net service.
     - Test Logic: 
       ```
       Access Plan-Net service
       If authentication prompt, then test fail
       Else, test pass
       ```
   - Test Case ID: REQ-PRIV-001-TC2
     - Preconditions: The FHIR server is running with the Plan-Net service. A consumer query has been made.
     - Test Steps: Inspect the server logs and data storage for records associating the consumer with the queried entities.
     - Expected Results: The server does not maintain records associating the consumer with the queried entities.
     - Validation Criteria: No records found associating the consumer with the queried entities.
     - Test Logic: 
       ```
       Inspect server logs and data storage
       If records found associating consumer with queried entities, then test fail
       Else, test pass
       ```

5. Special Testing Considerations
   - Edge Cases: Test with multiple concurrent consumer queries to ensure the server maintains privacy considerations under load.
   - Performance Considerations: Monitor server performance during testing to ensure it can handle the load without requiring authentication.
   - Security Testing Aspects: Ensure that even though authentication is not required, the server does not expose sensitive data or allow unauthorized actions.

## Test Plan for Server-SHALL NOT

1. Executive Summary
   - This test plan is designed to verify the conformance of a Plan-Net service to the FHIR Implementation Guide, specifically the requirement that the service should not require consumer identifying information for content queries. The plan will use a systematic approach to validate the service's functionality, performance, security, and privacy considerations.

2. Test Environment Requirements
   - The test environment will require a configured FHIR server, a directory mobile application for testing, and a set of test data that includes both consumer identifying and non-identifying information. The FHIR server should be configured to log all incoming queries for further analysis.

3. Test Groupings
   - Privacy Requirements: This group will focus on testing the requirement that the service should not require consumer identifying information. The test approach will involve sending queries with and without consumer identifying information and comparing the responses.

4. Individual Test Cases
   - Test Case ID: REQ-PRIV-002
     - Preconditions: The FHIR server is configured and the directory mobile application is ready for testing.
     - Test Steps with Expected Results: 
       1. Send a query from the directory mobile application to the Plan-Net service without including consumer identifying information. The service should respond with the requested content.
       2. Send a query from the directory mobile application to the Plan-Net service with consumer identifying information included. The service should respond with the same content as in step 1, indicating that the consumer identifying information was not required.
     - Validation Criteria: The responses in both steps should be identical and should not indicate any requirement for consumer identifying information.
     - Test Logic Outline: 
       ```
       // pseudocode
       queryWithoutIdentifyingInfo = sendQueryWithoutIdentifyingInfo()
       queryWithIdentifyingInfo = sendQueryWithIdentifyingInfo()
       assert(queryWithoutIdentifyingInfo == queryWithIdentifyingInfo)
       ```

5. Special Testing Considerations
   - Edge Cases: Test with minimal and excessive amounts of non-identifying information in the query to ensure the service can handle a variety of query sizes.
   - Performance Considerations: Monitor the response times of the service to ensure it can handle the queries in a timely manner.
   - Security Testing Aspects: Review the server logs to ensure that no consumer identifying information is being stored or logged when queries are made.

## Test Plan for Server-SHALL

**1. Executive Summary**
   - **Purpose and Scope**: The purpose of this test plan is to verify the conformance of the FHIR server to the Implementation Guide. The scope includes testing the server's ability to manage profiles, implement RESTful behavior, return HTTP error responses, support search parameters, and reject unauthorized requests.
   - **Key Testing Considerations**: The test plan will focus on both functional and non-functional requirements, including security and performance aspects.

**2. Test Environment Requirements**
   - **Infrastructure, Tools and Test Data**: A FHIR server, a testing tool such as Postman or Insomnia, and test data conforming to the profiles defined in the Implementation Guide.
   - **FHIR Server Configuration Requirements**: The server should be configured to support all profiles defined in the Implementation Guide.

**3. Test Groupings**
   - **Profile Management**: Test cases will verify the server's ability to manage profiles, including lastUpdate timestamp and identifying supported profiles in the meta.profile attribute.
   - **RESTful Behavior**: Test cases will verify the server's implementation of RESTful behavior and support for search parameters.
   - **Error Handling**: Test cases will verify the server's ability to return standard HTTP error responses and reject unauthorized requests.

**4. Individual Test Cases**
   - **Test Case REQ-DATA-002**: 
     - **Preconditions**: A profile exists on the server.
     - **Test Steps**: Retrieve the profile and check for the lastUpdate timestamp.
     - **Expected Results**: The lastUpdate timestamp is present in the profile's data content.
     - **Validation Criteria**: The profile's data content includes a lastUpdate timestamp.
   - **Test Case REQ-SERV-001**: 
     - **Preconditions**: The server is running.
     - **Test Steps**: Send a request to the server to retrieve all supported profiles.
     - **Expected Results**: The server returns a list of all profiles defined in the Implementation Guide.
     - **Validation Criteria**: The server supports all profiles defined in the Implementation Guide.
   - **Test Case REQ-SERV-002**: 
     - **Preconditions**: The server is running.
     - **Test Steps**: Send a request to the server and check the response for RESTful behavior.
     - **Expected Results**: The server returns a response that conforms to the FHIR specification.
     - **Validation Criteria**: The server implements RESTful behavior according to the FHIR specification.
   - **Test Case REQ-SERV-003**: 
     - **Preconditions**: The server is running.
     - **Test Steps**: Send requests to the server that should return each of the specified HTTP error responses.
     - **Expected Results**: The server returns the correct HTTP error response for each request.
     - **Validation Criteria**: The server returns the specified HTTP error responses.

**5. Special Testing Considerations**
   - **Edge Cases**: Test cases will include edge cases, such as requests for non-existent resources and unauthorized requests.
   - **Performance Considerations**: The server's performance will be tested under high load conditions to verify its ability to handle multiple simultaneous requests.
   - **Security Testing Aspects**: The server's security features will be tested, including its ability to reject unauthorized requests and return appropriate HTTP error responses.

## Test Plan for Server-SHALL/SHOULD

**Test Plan**

1. **Executive Summary**
   - **Purpose and Scope**: This test plan aims to validate the conformance of the Plan-Net Server to the FHIR Implementation Guide, focusing on JSON and XML support, Endpoint resource profile and interactions, and Endpoint retrieval by ID and version.
   - **Key Testing Considerations**: The test plan will address the requirements' conformance levels (SHALL/SHOULD), the server's role, and the verification method (Test). 

2. **Test Environment Requirements**
   - **Infrastructure, Tools and Test Data**: A FHIR server, HTTP client for sending requests, JSON and XML data for testing different formats, and a database with sample Endpoint resources.
   - **FHIR Server Configuration Requirements**: The server should be configured to support the Plan-Net profile and interactions.

3. **Test Groupings**
   - **Group 1: Data Format Support**
     - **Test Approach**: Validate the server's ability to handle JSON and XML formats.
     - **Key Considerations**: The server SHALL support JSON and SHOULD support XML.
   - **Group 2: Endpoint Resource Support**
     - **Test Approach**: Validate the server's support for the Endpoint resource profile and interactions.
     - **Key Considerations**: The server SHALL support search-type and read interactions and SHOULD support vread interaction.
   - **Group 3: Endpoint Retrieval**
     - **Test Approach**: Validate the server's ability to retrieve an Endpoint by ID and version.
     - **Key Considerations**: The server SHALL support GET [base]/Endpoint/[id] and SHOULD support GET [base]/Endpoint/[id]/_history/vid.

4. **Individual Test Cases**
   - **Test Case ID: REQ-SERV-004**
     - **Preconditions**: The server is running and accessible.
     - **Test Steps**: Send requests in both JSON and XML formats and validate the responses.
     - **Validation Criteria**: The server should correctly process JSON requests and optionally XML requests.
   - **Test Case ID: REQ-ENDP-001**
     - **Preconditions**: The server is running, accessible, and configured to support the Endpoint resource profile.
     - **Test Steps**: Perform search-type, read, and vread interactions and validate the responses.
     - **Validation Criteria**: The server should correctly process search-type and read interactions and optionally vread interaction.
   - **Test Case ID: REQ-ENDP-002**
     - **Preconditions**: The server is running, accessible, and contains Endpoint resources.
     - **Test Steps**: Send GET requests for an Endpoint by ID and version and validate the responses.
     - **Validation Criteria**: The server should correctly return the requested Endpoint resource and optionally its version history.

5. **Special Testing Considerations**
   - **Edge Cases**: Test with invalid or non-existent Endpoint IDs, unsupported data formats, and unsupported interactions.
   - **Performance Considerations**: Test with large data sets and high request rates to evaluate the server's performance.
   - **Security Testing Aspects**: Test the server's handling of unauthorized or malicious requests.

## Test Plan for Client-SHALL NOT

1. Executive Summary
   - This test plan aims to verify the conformance of a directory mobile application to the FHIR Implementation Guide, specifically the requirement REQ-PRIV-003. The test will focus on ensuring the application does not send consumer identifiable information when querying a Plan-Net service.
   - Key testing considerations include data privacy, application functionality, and conformance to the FHIR standard.

2. Test Environment Requirements
   - The test will require a controlled environment with a configured FHIR server, a directory mobile application, and test data. Tools needed include a network traffic analyzer (like Wireshark) and a FHIR client for sending requests.
   - The FHIR server should be configured to log all incoming requests for detailed analysis.

3. Test Groupings
   - The test will focus on the Privacy Considerations category, specifically the handling of consumer identifiable information.
   - The test approach involves simulating queries from the directory mobile application to the Plan-Net service and analyzing the sent data.

4. Individual Test Cases
   - Test Case ID: TC-REQ-PRIV-003
   - Preconditions: The directory mobile application is installed and configured correctly. The FHIR server is up and running.
   - Test Steps with Expected Results:
     1. Launch the directory mobile application.
     2. Initiate a query to the Plan-Net service.
     3. Capture the outgoing network traffic using the network traffic analyzer.
     4. Analyze the captured data for any consumer identifiable information.
     5. Expected Result: No consumer identifiable information is found in the sent data.
   - Validation Criteria: The test is passed if no consumer identifiable information is found in the sent data.
   - Test Logic Outline:
     ```
     Start directory mobile application
     Initiate Plan-Net service query
     Capture outgoing network traffic
     Analyze captured data
     If consumer identifiable information is found:
         Test failed
     Else:
         Test passed
     ```

5. Special Testing Considerations
   - Edge Cases: Consider testing with different types of queries and varying amounts of consumer data.
   - Performance Considerations: Monitor the application and server performance during the test. High network traffic should not affect the application's performance.
   - Security Testing Aspects: Ensure the application uses secure communication protocols when sending queries to the Plan-Net service.

## Test Plan for Health Plan API-SHALL

1. Executive Summary
   - This test plan is designed to verify the conformance of the Health Plan API with the FHIR Implementation Guide, specifically focusing on the handling of Must Support data elements. The scope of the test includes the ability of the API actors to populate all Must Support data elements in the query results and the correct handling of missing information.
   - Key testing considerations include the correct population of data elements, the handling of missing information, and the use of appropriate values or extensions when information is not present.

2. Test Environment Requirements
   - The test environment requires a configured FHIR server, a test database populated with sample patient data, and testing tools capable of sending API requests and validating responses.
   - The FHIR server should be configured to support the Health Plan API and all Must Support data elements.

3. Test Groupings
   - Data Elements Handling: This group tests the ability of the API actors to populate all Must Support data elements in the query results.
   - Missing Information Handling: This group tests the handling of missing information, including the use of appropriate values or extensions.

4. Individual Test Cases
   - REQ-DATA-001
     - Preconditions: The FHIR server is configured correctly, and the test database is populated with sample patient data.
     - Test Steps: Send an API request to the Health Plan API. Validate that all Must Support data elements are included in the response when information is present. When information is not present, validate that data elements are not included when minimum cardinality is 0, and that the reason for missing information is sent when minimum cardinality is >0.
     - Expected Results: The API response includes all Must Support data elements when information is present. When information is not present, data elements are not included when minimum cardinality is 0, and the reason for missing information is sent when minimum cardinality is >0.
     - Validation Criteria: The API response matches the expected results.
     - Test Logic: 
       ```
       if (dataElement is present) {
         assert(dataElement is in API response);
       } else {
         if (minimum cardinality == 0) {
           assert(dataElement is not in API response);
         } else {
           assert(reason for missing information is in API response);
         }
       }
       ```

5. Special Testing Considerations
   - Edge Cases: Test with data that has minimum cardinality >0 but is not present in the database. Validate that the reason for missing information is sent in the API response.
   - Performance Considerations: Measure the response time of the API requests to ensure that the addition of Must Support data elements does not significantly impact performance.
   - Security Testing Aspects: Validate that the API does not expose sensitive patient data in the response when the data is not present.

## Test Plan for Application-SHALL

1. Executive Summary
   - This test plan is designed to validate the conformance of applications to the FHIR Implementation Guide, specifically focusing on the processing of Must Support elements. The scope includes testing the application's ability to process, interpret, display, and store Must Support data elements.
   - Key testing considerations include the application's error handling, data interpretation, and data display/storage capabilities.

2. Test Environment Requirements
   - The test environment will require a FHIR server, a test application, and test data containing Must Support data elements. The FHIR server should be configured to support the necessary resource instances.
   - FHIR server configuration requirements include the ability to handle Must Support data elements and simulate missing data elements.

3. Test Groupings
   - Requirement Group: Must Support Data Elements
     - Test Approach: Validate the application's ability to process, interpret, display, and store Must Support data elements.
     - Key Considerations: Focus on error handling, data interpretation, and data display/storage capabilities.

4. Individual Test Cases
   - REQ-APP-001
     - Preconditions: The application is running and connected to the FHIR server. The FHIR server is populated with test data.
     - Test Steps with Expected Results:
       1. Send a request to the FHIR server to retrieve a resource instance containing Must Support data elements.
       2. Verify the application processes the retrieved data without error.
       3. Remove a Must Support data element from the resource instance.
       4. Send a request to the FHIR server to retrieve the modified resource instance.
       5. Verify the application interprets the missing Must Support data element as data not present.
       6. Verify the application is capable of displaying the retrieved data for human use or storing the information for other purposes.
     - Validation Criteria: The application should process the data without error, interpret missing data as not present, and be capable of displaying or storing the data.
     - Test Logic Outline:
       ```
       function test_REQ_APP_001() {
         let resource = getResourceWithMustSupportElements();
         assert(application.process(resource) == NO_ERROR);
         
         resource.removeMustSupportElement();
         assert(application.process(resource) == DATA_NOT_PRESENT);
         
         assert(application.display(resource) == SUCCESS || application.store(resource) == SUCCESS);
       }
       ```

5. Special Testing Considerations
   - Edge Cases: Test with resource instances that have multiple missing Must Support data elements.
   - Performance Considerations: Monitor the application's performance when processing large resource instances.
   - Security Testing Aspects: Ensure the application securely handles, displays, and stores the Must Support data elements.

## Test Plan for Consumer App-SHALL

1. Executive Summary
   - This test plan aims to validate the conformance of consumer applications to the FHIR Implementation Guide, specifically focusing on the requirement that they can process Must Support elements with missing information.
   - Key testing considerations include the robustness of the application in handling missing data, the accuracy of the processing, and the conformance to the FHIR standards.

2. Test Environment Requirements
   - The test environment will require a FHIR server, a consumer application, and a set of test data with varying levels of completeness.
   - The FHIR server should be configured to allow the consumer application to access and process the test data.

3. Test Groupings
   - The primary test group for this requirement is "Handling Missing Data". This group will focus on the application's ability to process Must Support elements with missing information.
   - The test approach will involve providing the application with test data that has missing Must Support elements and observing how it processes the data.

4. Individual Test Cases
   - Test Case ID: TC-REQ-CONS-001
   - Preconditions: The consumer application is able to access the FHIR server and the test data.
   - Test Steps with Expected Results: 
     1. Provide the application with a resource instance that has a missing Must Support element.
     2. The application should process the resource instance without any errors.
   - Validation Criteria: The application successfully processes the resource instance and handles the missing Must Support element as per the FHIR standards.
   - Test Logic Outline: 
     ```
     if (resourceInstance.contains(mustSupportElement) == false) {
       try {
         consumerApp.process(resourceInstance);
         assert(consumerApp.processedWithoutErrors() == true);
       } catch (Exception e) {
         fail("Application was unable to process resource instance with missing Must Support element");
       }
     }
     ```

5. Special Testing Considerations
   - Edge Cases: Test data should include resource instances with multiple missing Must Support elements, as well as instances where all Must Support elements are missing.
   - Performance Considerations: The application's performance in processing resource instances with missing Must Support elements should be monitored and compared to its performance with complete data.
   - Security Testing Aspects: The application's security measures should not be compromised when processing resource instances with missing Must Support elements.