# frozen_string_literal: true

module Test3
  # Test Group for REQ-09: Missing Must Support interpretation
  #
  # Description: "Application Actor SHALL interpret missing Must Support data elements
  #               as data not present in Health Plan API system"
  # Actor: Application Actor
  # Conformance: SHALL
  #
  # This group contains tests to address the client-side requirement REQ-09.
  # Since Inferno acts as the client (Application Actor) during testing,
  # this test primarily serves as an informational check or requires manual attestation,
  # as automated verification of external client interpretation logic is typically not feasible.
  class Req09MustSupportInterpretationGroup < Inferno::TestGroup
    id :test3_req_09_must_support_interpretation_group
    title 'REQ-09: Missing Must Support Interpretation'
    description %(
      ### Requirement REQ-09
      **Description**: "Application Actor SHALL interpret missing Must Support data elements as data not present in Health Plan API system"

      **Actor**: Application Actor

      **Conformance**: SHALL

      This test addresses the requirement REQ-09 concerning how an Application Actor
      (the client application connecting to the Health Plan API) should handle situations
      where data elements marked as "Must Support" in the relevant FHIR Implementation Guide profiles
      are missing from the resources returned by the API server.

      The requirement mandates that the client application must interpret such missing elements
      simply as data that is not present or not available in the server's system. The client
      should not assume a default value, infer information, or treat the absence of a Must Support
      element as an error in itself.

      **Testing Approach**:
      Direct automated testing of an external client application's internal interpretation logic
      is generally outside the scope of server-focused testing frameworks like Inferno.
      Inferno itself, when acting as a client, inherently follows FHIR processing rules,
      but this test cannot automatically verify the behavior of the separate Application Actor system under test.

      Therefore, this test serves as an informational confirmation point. It highlights the
      client's responsibility. Compliance might be verified through manual review, client
      testing logs, or attestation.
    )
    # No specific FHIR client configuration needed here as it's informational,
    # but it might inherit from a parent group if part of a larger suite.

    test do
      id :test3_req_09_missing_must_support_interpretation_info
      title 'Application Actor Interpretation of Missing Must Support Elements'
      description %(
        **Requirement**: Application Actor SHALL interpret missing Must Support data elements as data not present in Health Plan API system.

        **Purpose**: This test confirms understanding and acknowledgement of the client-side requirement REQ-09.

        **Process**: This test does not perform any FHIR interactions. It serves as a placeholder
        to document the requirement that the Application Actor (client) must correctly interpret
        the absence of Must Support elements.

        **Evaluation**: The test passes to indicate that the requirement is acknowledged. Actual compliance
        must be ensured within the Application Actor's implementation and potentially verified manually
        or through other means specific to the client application's testing procedures.
      )
      # No inputs or outputs are needed for this informational test.

      run do
        # This test is informational. It confirms the requirement REQ-09 applies to the
        # Application Actor (client). Automated verification of the client's internal
        # interpretation logic by Inferno is not feasible.
        # Passing this test signifies acknowledgement of this client-side responsibility.
        pass %(
          Requirement REQ-09 mandates that the Application Actor (client) must interpret
          missing Must Support data elements as data not present in the Health Plan API system.
          This test passes as an acknowledgement of this requirement. Ensure the client application
          adheres to this interpretation rule. Manual verification or client-specific testing
          may be necessary to confirm compliance.
        )
      end
    end
  end
end