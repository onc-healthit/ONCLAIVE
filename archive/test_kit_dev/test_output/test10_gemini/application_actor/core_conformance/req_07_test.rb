module Test10_gemini
  class Req07MustSupportElementsProcessingGroup < Inferno::TestGroup
    id :req_07_must_support_elements_processing_group
    title 'REQ-07: Must Support Elements Processing'
    description %(
      This test group addresses REQ-07: "Application Actor SHALL process
      resource instances containing Must Support data elements without errors
      or application failure."

      It verifies that the server (acting as the Application Actor) can
      successfully receive and process a resource instance, provided by the tester,
      that is presumed to contain all relevant Must Support data elements.
      The test performs a FHIR create operation with the provided resource.
      Successful processing is indicated by a 201 Created HTTP response from the server.
    )
    # Requirement