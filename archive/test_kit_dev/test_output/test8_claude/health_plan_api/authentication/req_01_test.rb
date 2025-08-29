module Test8_claude
  class NoAuthenticationRequirementGroup < Inferno::TestGroup
    id :no_authentication_requirement
    title 'No Authentication Requirements for Plan-Net API'
    description %(
      Verify that the Health Plan API does not require authentication 
      for accessing Plan-Net services.

      This test confirms that requests can be made successfully without 
      any authentication credentials.
    )

    fhir_client do
      url :url  
    end

    test do
      id :verify_no_auth_required
      title 'Server allows access without authentication'
      description %(
        Verify that the server accepts requests without any authentication
        credentials and returns successful responses.
      )

      input :url,
            title: 'Health Plan API Base URL',
            description: 'The base URL for the Health Plan API',
            type: :text

      makes_request :unauthenticated_metadata

      run do
        fhir_get_capability_statement(name: :unauthenticated_metadata)

        assert_response_status(200)
        assert_resource_type(:capability_statement)

        auth_header = nil
        response[:headers].each do |header, value|
          auth_header = value if header.downcase == 'www-authenticate'
        end

        assert auth_header.nil?,
               'Server returned WWW-Authenticate header indicating authentication is required'

        security = resource.rest&.first&.security
        
        assert security.nil? || security.service.empty?,
               'CapabilityStatement indicates security requirements are present'
      end
    end

    test do
      id :verify_rejected_auth
      title 'Server ignores provided authentication'
      description %(
        Verify that the server still works correctly even when authentication
        credentials are provided, confirming they are truly not required.
      )

      input :url,
            title: 'Health Plan API Base URL',
            description: 'The base URL for the Health Plan API',
            type: :text

      fhir_client do
        url :url
        bearer_token 'invalid_token'
      end

      run do
        fhir_get_capability_statement

        assert_response_status(200)
        assert_resource_type(:capability_statement)
      end
    end
  end
end