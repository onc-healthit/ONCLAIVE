# frozen_string_literal: true

module Test4_gemini
  class NoAuthenticationRequirementTest < Inferno::Test
    id :req_01_no_authentication_requirement
    title 'Health Plan API SHALL NOT require authentication for Plan-Net service access'
    description %(
      Health Plan API SHALL NOT require authentication for Plan-Net service access.
      This test verifies that a request made without authentication will result in a success (2xx) response code.
    )

    run do
      fhir_client.set_bearer_token(nil)
      fhir_read(:capability_statement)
      assert_response_status(200), 'Authentication should not be required for Plan-Net service access'
    end
  end
end
