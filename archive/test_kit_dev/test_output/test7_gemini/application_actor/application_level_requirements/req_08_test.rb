module Test7_gemini
  class REQ08MustSupportElementsDisplayGroup < Inferno::TestGroup
    # Unique identifier for this test group
    id :req_08_must_support_elements_display_group
    # Human-readable title for the test group
    title 'REQ-08: Must Support Elements Display and Storage'
    # Detailed description of the test group, supporting Markdown
    description %(
      **Requirement REQ-08**: "Application Actor SHOULD display Must Support data elements for human use or store for other purposes."

      This group of tests addresses the REQ-08 requirement concerning the application's handling
      of "Must Support" (MS) elements. This is a "SHOULD" requirement for an Application Actor.
      Since verifying an application's display logic or internal storage capabilities typically
      falls outside the scope of direct automated API testing (which Inferno primarily focuses on),
      this test relies on user attestation.

      "Must Support" elements are those elements that an application must be capable of
      processing. These are typically defined within specific FHIR Implementation Guides (IGs).
      The application developer is expected to be aware of the MS elements relevant to the
      IGs their application claims conformance to.
    )

    # Define the individual test case
    test do
      # Unique identifier for this test
      id :req_08_attestation_must_support_display_store
      # Human-readable title for the test
      title 'Attestation: Application Displays or Stores Must Support Elements (REQ-08)'
      # Detailed description of what this test verifies, supporting Markdown
      description %(
        This test requires you to attest whether your application, acting as an "Application Actor",
        fulfills the **REQ-08** requirement.

        **Requirement Details**:
        - **ID**: REQ-08
        - **Description**: "Application Actor SHOULD display Must Support data elements for human use or store for other purposes"
        - **Actor**: Application Actor
        - **Conformance**: SHOULD

        Please consider the "Must Support" elements as defined in the relevant Implementation Guide(s)
        to which your application claims conformance.
        Does your application meet the criteria of REQ-08 by either:
        1. Displaying these Must Support data elements for human use?
        OR
        2. Storing these Must Support data elements for other purposes (e.g., further processing, decision support, etc.)?
      )
      # This test evaluates a "SHOULD" requirement.
      # A 'No' attestation will result in a test failure.
      # The overall test suite's configuration determines how such failures (for SHOULD requirements)
      # are reported (e.g., as a warning or a critical failure).

      # Define an input for user attestation
      input :req_08_attestation,
            title: 'REQ-08 Attestation: Handling of Must Support Elements',
            description: 'Regarding requirement REQ-08, does your application display Must Support data elements for human use OR store them for other purposes?',
            type: 'radio', # Radio button input type for Yes/No
            default_value: 'false', # Default to 'No' to require active user confirmation.
            input_instructions: 'Select "Yes" if your application meets the REQ-08 requirement for handling Must Support elements. Select "No" if it does not.',
            options: {
              list_options: [
                {
                  label: 'Yes, the application meets this "SHOULD" requirement.',
                  value: 'true'
                },
                {
                  label: 'No, the application does not meet this "SHOULD" requirement.',
                  value: 'false'
                }
              ]
            }

      # The run block contains the actual test logic
      run do
        # The assertion checks if the user attested 'Yes'.
        # If 'No' is selected, the assertion fails, indicating the "SHOULD" requirement is not met by attestation.
        assert req_08_attestation == 'true', %(
          **REQ-08 (SHOULD) Not Met by Attestation.**
          User attested that the application does not display Must Support data elements
          for human use or store them for other purposes.
          Requirement (REQ-08): "Application Actor SHOULD display Must Support data elements for human use or store for other purposes."
        )

        # If the assertion passes, it means the user attested 'Yes'.
        # The test result is explicitly set to 'pass' with a success message.
        pass "User attested that the application meets REQ-08: It displays Must Support data elements for human use or stores them for other purposes. This fulfills the 'SHOULD' requirement."
      end
    end
  end
end