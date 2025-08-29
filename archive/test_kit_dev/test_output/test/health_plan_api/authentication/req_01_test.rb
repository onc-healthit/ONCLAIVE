module Test
  class NoAuthTestGroup < Inferno::TestGroup
    id :no_auth_required
    title 'No Authentication Required'
    description %(
      Verify that the Health Plan API does not require authentication 
      for Plan-Net service access as specified in REQ-01.
    )

    fhir_client do
      url :url
    end

    test do
      id :test_no_auth_required
      title 'Server accepts requests without authentication'
      description %(
        This test verifies that the server accepts API requests without requiring
        any authentication credentials or tokens.
      )

      input :url,
            title: 'Health Plan API Base URL',
            description: 'The base URL for the Health Plan API server',
            type: 'text'

      run do
        fhir_get_capability_statement
        assert_response_status(200),
          "Server rejected request without authentication. Expected 200 OK but received #{response[:code]}"

        auth_header = response[:headers].find { |header, _| header.downcase == 'www-authenticate' }&.last

        assert auth_header.nil?,
          'Server requires authentication - WWW-Authenticate header present'

        fhir_read(:organization, 'example')
        assert_response_status([200, 404]),
          'Server rejected unauthenticated resource request'
      end
    end
  end
end