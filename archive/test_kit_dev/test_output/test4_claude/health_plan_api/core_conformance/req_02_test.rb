module Test4_claude
  class NoConsumerIdentificationGroup < Inferno::TestGroup
    id :no_consumer_identification_requirement
    title 'REQ-02: No Consumer Identification Requirement'
    description %(
      Verify that the Health Plan API does not require directory mobile applications 
      to send consumer identifying information in queries.
      
      The server SHALL NOT require any consumer identifying information to be included
      in directory queries.
    )

    test do
      id :basic_directory_query_without_consumer_info
      title 'Basic directory query succeeds without consumer information'
      description %(
        Verify that a basic directory query succeeds without including any 
        consumer identifying information.
      )

      input :url
      
      run do
        # Make basic practitioner search without any consumer info
        fhir_client.set_url url
        fhir_search(:practitioner)
        
        assert_response_status(200)
        assert_resource_type(:bundle)
      end
    end

    test do
      id :search_with_standard_parameters
      title 'Directory search with standard parameters succeeds'
      description %(
        Verify that directory searches using standard search parameters succeed
        without requiring consumer information.
      )

      input :url

      run do
        fhir_client.set_url url
        
        # Search with standard parameters
        search_params = {
          specialty: 'cardiology',
          location: '90210',
          _count: 10
        }
        
        fhir_search(:practitioner, params: search_params)
        
        assert_response_status(200)
        assert_resource_type(:bundle)
      end
    end

    test do 
      id :error_responses_without_consumer_info
      title 'Error responses do not indicate missing consumer information'
      description %(
        Verify that when errors occur, they are not due to missing
        consumer identification information.
      )

      input :url
      
      run do
        fhir_client.set_url url

        # Invalid search that should return error
        fhir_search(:practitioner, params: {invalid_param: 'test'})
        
        assert_response_status([400, 422])
        
        begin
          response_body = JSON.parse(response[:body])
          
          if response_body['issue']
            response_body['issue'].each do |issue|
              details = issue['details']&.dig('text') || issue['diagnostics'] || ''
              
              assert !details.downcase.include?('consumer'),
                     'Error message indicates missing consumer information'
              assert !details.downcase.include?('patient'), 
                     'Error message indicates missing patient information'
              assert !details.downcase.include?('member'),
                     'Error message indicates missing member information'
            end
          end
        rescue JSON::ParserError
          # If response isn't JSON, that's fine - we just can't check the error text
          pass 'Non-JSON error response received'
        end
      end
    end
  end
end