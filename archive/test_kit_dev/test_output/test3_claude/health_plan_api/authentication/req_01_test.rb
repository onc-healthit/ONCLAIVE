module Test3_claude
  class NoAuthTestGroup < Inferno::TestGroup
    id :no_auth_required
    title 'Health Plan API Authentication Requirements'
    description %(
      Verify that the Health Plan API does not require authentication for Plan-Net service access.
      
      Requirement REQ-01: Health Plan API SHALL NOT require authentication for Plan-Net service access.
    )

    test do
      id :test_no_auth_required
      title 'Server accepts requests without authentication'
      description %(
        This test verifies that the server accepts FHIR API requests without requiring any 
        authentication credentials. It makes a basic read request without authentication 
        and validates that the server responds successfully.
      )

      input :server_url

      run do
        # Configure FHIR client without any auth
        fhir_client do
          url server_url
        end

        # Make request to capability statement endpoint which should always be accessible
        get capability_statement_url

        assert_response_status([200, 201], "Server rejected request without auth. Expected 200/201 status but got #{response.code}")

        # Validate we got back a capability statement
        assert_resource_type(:capability_statement)
        capability_statement = resource

        # Verify no security extension requiring auth
        security = capability_statement.rest&.first&.security
        if security&.service&.any? { |s| s.coding&.any? { |c| c.code == 'SMART-on-FHIR' } }
          fail_message = 'Server indicates it requires SMART-on-FHIR authentication in capability statement'
          assert false, fail_message
        end

        pass 'Successfully accessed FHIR endpoint without authentication'
      end
    end
  end
end