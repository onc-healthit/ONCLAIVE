module Test10_gemini
  class Req08MustSupportElementsDisplayGroup < Inferno::TestGroup
    id :test10_gemini_req_08_must_support_display_group
    title 'REQ-08: Must Support elements display'
    description %(
      This test group addresses REQ-08: "Application Actor SHOULD display
      Must Support data elements for human use or store for other purposes."

      The test within this group requires manual attestation from the user
      to confirm the Application Actor's behavior regarding the display or
      storage of Must Support elements from a specified FHIR resource.
    )

    test do
      id :test10_gemini_req_08_application_displays_must_support_attestation
      title 'Application Actor Attestation for Must Support Elements Handling'
      description %(
        **Requirement REQ-08**: "Application Actor SHOULD display Must Support
        data elements for human use or store for other purposes."

        **Actor**: Application Actor
        **Conformance**: SHOULD

        **Test Purpose**:
        This test verifies, through user attestation, that the Application Actor
        (the system under test) appropriately handles Must Support data elements.
        Specifically, it checks if the application either displays these elements
        for human use or stores them for other purposes.

        **Test Execution Steps**:
        1.  **Specify Resource**: The tester provides a relative reference to a FHIR
            resource instance (e.g., `Patient/123`) that the Application Actor
            is expected to process. This resource should ideally contain
            Must Support elements as defined by relevant FHIR profiles.
        2.  **Fetch Resource**: The test will attempt to read this resource from the
            FHIR server.
        3.  **Identify Must Support Elements**: The tester provides a description of
            the Must Support elements that are relevant for the specified resource
            and should be handled by the Application Actor.
        4.  **Attestation**: The tester attests whether their Application Actor
            correctly displays these Must Support elements for human use or
            stores them for other purposes when processing the fetched resource.

        **Expected Outcome**:
        -   If the resource is fetched successfully and the tester attests 'Yes' (the
            application handles Must Support elements as required), the test will pass.
        -   If the tester attests 'No', the test will issue a warning. This is because
            REQ-08 is a "SHOULD" requirement, indicating a recommendation rather
            than a strict mandate.
        -   The test will fail if the specified resource cannot be fetched or if inputs are missing.
      )

      input :resource_reference,
            title: 'Resource Reference for Test',
            description: 'Provide a relative FHIR resource reference (e.g., Patient/123, Observation/abc). ' \
                         'This resource will be fetched, and you will attest to how your application ' \
                         'handles its Must Support elements.',
            type