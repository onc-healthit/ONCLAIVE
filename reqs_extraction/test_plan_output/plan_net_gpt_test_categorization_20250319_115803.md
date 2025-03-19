# Test Categorization for Plan Net

## Generated on: 2025-03-19 11:59:18

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
| --- | --- | --- | --- | --- |
| REQ-PRIV-001 | Manual | Simple | Access to the Plan-Net service | This requirement is about the absence of authentication. It can be manually verified by attempting to access the service without providing any authentication details. |
| REQ-PRIV-002 | Automatic | Moderate | A conformant Plan-Net service, a directory mobile application | This requirement can be automatically tested by writing a test case where the application attempts to query the service without sending any consumer identifying information. The complexity is moderate because it involves interaction between two systems. |
| REQ-PRIV-003 | Automatic | Moderate | A directory mobile application, a Plan-Net service | Similar to REQ-PRIV-002, this requirement can be automatically tested by writing a test case where the application attempts to query the service without sending any consumer identifiable information. The complexity is moderate because it involves interaction between two systems. |
| REQ-DATA-001 | Automatic | Complex | Health Plan API actors, Must Support data elements | This requirement can be automatically tested by writing test cases to check if the actors populate all Must Support data elements correctly, and handle missing information as specified. The complexity is high because it involves multiple conditions and scenarios. |
| REQ-APP-001 | Hybrid | Complex | Application actors, Must Support data elements, Health Plan API system | This requirement can be partially tested automatically by writing test cases to check if the actors process resource instances containing Must Support data elements without error. However, verifying if the actors are capable of displaying these data elements for human use or storing the information for other purposes may require manual verification. The complexity is high because it involves multiple conditions and scenarios. |


| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
| --- | --- | --- | --- | --- |
| REQ-CONS-001 | Hybrid | Moderate | Consumer App, Test data with Must Support elements asserting missing information | While the requirement can be tested automatically to some extent, manual verification may be needed to ensure the Consumer App is correctly processing the missing information. |
| REQ-DATA-002 | Manual | Simple | Profiles, Inspection tools | This requirement involves inspecting the content of the profile data which is a manual process. The complexity is simple as it only requires checking the presence of the lastUpdate timestamp. |
| REQ-SERV-001 | Automatic | Complex | Plan-Net Server, Implementation Guide, Automated test tools | This requirement can be tested automatically by verifying the server's support for all profiles defined in the Implementation Guide. The complexity is high as it involves testing all profiles. |
| REQ-SERV-002 | Automatic | Moderate | Plan-Net Server, FHIR specification, Automated test tools | This requirement can be tested automatically by verifying the server's RESTful behavior according to the FHIR specification. The complexity is moderate as it involves testing the server's implementation against the FHIR specification. |
| REQ-SERV-003 | Automatic | Moderate | Plan-Net Server, Automated test tools | This requirement can be tested automatically by sending requests that should trigger each of the specified HTTP error responses and verifying the server's responses. The complexity is moderate as it involves testing multiple error conditions. |


| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
| --- | --- | --- | --- | --- |
| REQ-SERV-004 | Hybrid | Moderate | Plan-Net Server, JSON and XML data | While the server's support for JSON and XML formats can be tested automatically, the SHOULD requirement for XML support may require manual verification to ensure proper functioning. |
| REQ-SERV-005 | Manual | Simple | Plan-Net Server, FHIR meta.profile attribute | This requirement involves inspection of the FHIR meta.profile attribute, which is a manual process. It is simple as it only involves checking the presence of supported Plan-Net profiles. |
| REQ-SERV-006 | Automatic | Complex | Plan-Net Server, searchParameters for each profile | This requirement can be automatically tested by executing search queries with different combinations of searchParameters. It is complex due to the need to test each profile individually and in combination. |
| REQ-SERV-007 | Automatic | Complex | Plan-Net Server, search parameters with 'chain' property | This requirement can be automatically tested by executing search queries with chained parameters. It is complex due to the need to test both forward and reverse chaining. |
| REQ-SERV-008 | Automatic | Simple | Plan-Net Server, Unauthorized request | This requirement can be automatically tested by sending unauthorized requests to the server and checking for HTTP 401 response. It is simple as it only involves checking the response code. |

| Requirement ID | Testability | Complexity | Prerequisites | Rationale |
| --- | --- | --- | --- | --- |
| REQ-ENDP-001 | Automatic | Moderate | Plan-Net Server, Plan-Net Endpoint profile | The requirement is about the server supporting a specific profile and interactions. This can be tested automatically by writing test scripts to check if the server responds correctly to the specified interactions. |
| REQ-ENDP-002 | Automatic | Simple | Server, Endpoint resource | The requirement is about the server's ability to return an Endpoint resource. This can be tested automatically by sending a GET request to the server and checking if the returned resource matches the expected output. |
| REQ-ENDP-003 | Automatic | Moderate | Server, Endpoint resource, organization parameter | The requirement is about the server's ability to support a specific operation (_include). This can be tested automatically by sending a GET request with the specified operation and checking if the server returns the expected output. |
| REQ-ENDP-004 | Automatic | Complex | Server, Endpoint resource, search parameters | The requirement is about the server's ability to support specific search parameters. This can be tested automatically by sending GET requests with different search parameters and checking if the server returns the expected output. The complexity is considered high due to the need to test multiple parameters. |
