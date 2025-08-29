module Test5_claude
  class NoPiiSendingTest < Inferno::TestGroup
    id :no_pii_sending_test
    title 'No PII Sending by Clients'
    description %(
      Verify that directory mobile applications do not send consumer identifiable 
      information when querying a Plan-Net service, as specified in REQ-02.
      
      The test examines outgoing requests to ensure no PII fields are included
      in query parameters or request bodies.
    )

    test do
      id :search_with_pii_parameters
      title 'Search requests must not include PII parameters'
      description %(
        This test verifies that search requests do not include any parameters
        containing personally identifiable information.
      )

      input :server_url

      run do
        # Define PII-related parameters that should not be used
        prohibited_params = [
          'patient.identifier',
          'patient.name',
          'patient.birthdate',
          'patient.telecom',
          'patient.address',
          'patient.email',
          'patient.phone'
        ]

        # Perform a practitioner search with prohibited parameters
        prohibited_params.each do |param|
          test_value = 'test_value'
          
          # Attempt search with prohibited parameter
          fhir_search(:practitioner, params: { param => test_value })
          
          assert_response_status([400, 422], 
            "Server should reject search with PII parameter: #{param}")

          # Verify error response indicates invalid parameter
          assert_resource_type(:operationoutcome)
          assert resource.issue&.any? { |issue| 
            issue.severity == 'error' && 
            issue.code == 'invalid'
          }, "Server should return error for PII parameter: #{param}"
        end

        pass "Successfully verified that PII parameters are rejected"
      end
    end

    test do
      id :create_update_with_pii
      title 'Create/Update requests must not include PII data'
      description %(
        This test verifies that resource create/update operations do not
        include PII data in the request body.
      )

      input :server_url
      
      run do
        # Attempt to create practitioner with PII
        pii_practitioner = FHIR::Practitioner.new(
          identifier: [
            {
              system: 'http://example.com/id',
              value: '12345'
            }
          ],
          name: [
            {
              family: 'Smith',
              given: ['John']
            }
          ],
          telecom: [
            {
              system: 'phone',
              value: '555-123-4567'
            },
            {
              system: 'email', 
              value: 'john@example.com'
            }
          ],
          address: [
            {
              line: ['123 Main St'],
              city: 'Anytown',
              state: 'ST',
              postalCode: '12345'
            }
          ]
        )

        fhir_create(pii_practitioner)
        
        assert_response_status([400, 422],
          'Server should reject create with PII data')

        assert_resource_type(:operationoutcome)
        assert resource.issue&.any? { |issue|
          issue.severity == 'error' &&
          issue.code == 'invalid'
        }, 'Server should return error for PII data in request body'

        pass "Successfully verified that PII data is rejected in request bodies"
      end
    end
  end
end