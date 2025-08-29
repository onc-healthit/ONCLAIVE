module Test6_claude
  class NoPiiSendingTest < Inferno::TestGroup
    id :no_pii_sending_test
    title 'No PII Sending by Clients'
    description %(
      Validates that a directory mobile application does not send consumer 
      identifiable information when querying a Plan-Net service.
      
      Requirement: A directory mobile application SHALL NOT send consumer 
      identifiable information when querying a Plan-Net service.
    )

    test do
      id :check_practitioner_search_params
      title 'Verify no PII in Practitioner search'
      description %(
        This test verifies that Practitioner searches do not include PII 
        search parameters like identifier, name, birthdate, etc.
      )
      
      input :plannet_server_url
      
      run do
        # Get search params from request
        search_request = fhir_search(:practitioner)
        params = search_request.request.uri.query_values || {}

        restricted_params = [
          'identifier',
          'name',
          'given',
          'family', 
          'birthdate',
          'email',
          'phone',
          'address'
        ]

        restricted_params.each do |param|
          assert !params.key?(param), 
            "Search included restricted PII parameter: #{param}"
        end

        pass 'No PII parameters found in Practitioner search'
      end
    end

    test do
      id :check_organization_search_params  
      title 'Verify no PII in Organization search'
      description %(
        This test verifies that Organization searches do not include PII
        search parameters like identifier, name, email, etc.
      )

      input :plannet_server_url

      run do
        search_request = fhir_search(:organization)
        params = search_request.request.uri.query_values || {}

        restricted_params = [
          'identifier',
          'name',
          'email',
          'phone',
          'address'
        ]

        restricted_params.each do |param|
          assert !params.key?(param),
            "Search included restricted PII parameter: #{param}"
        end

        pass 'No PII parameters found in Organization search'
      end
    end

    test do
      id :check_location_search_params
      title 'Verify no PII in Location search' 
      description %(
        This test verifies that Location searches do not include PII
        search parameters like identifier, name, etc.
      )

      input :plannet_server_url

      run do
        search_request = fhir_search(:location)
        params = search_request.request.uri.query_values || {}

        restricted_params = [
          'identifier',
          'name',
          'email',
          'phone',
          'address'
        ]

        restricted_params.each do |param|
          assert !params.key?(param),
            "Search included restricted PII parameter: #{param}"
        end

        pass 'No PII parameters found in Location search'
      end
    end
  end
end