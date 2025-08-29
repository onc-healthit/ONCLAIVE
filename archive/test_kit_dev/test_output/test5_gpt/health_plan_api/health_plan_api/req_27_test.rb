module Test5Gpt
  class SupportForIncludesTestGroup < Inferno::TestGroup
    id :req_27_support_for_includes
    title 'Support for _includes'
    description %(
      This test group verifies that the Health Plan API server supports the _includes
      parameter for various FHIR resources as required by the specification.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :req_27_patient_include_test
      title 'Server supports _includes for Patient resource'
      description %(
        Verify that the server supports the _includes parameter for the Patient resource.
      )
      input :patient_id

      run do
        fhir_search(:patient, params: { _id: patient_id, _include: 'Patient:organization' })
        
        assert_response_status(200)
        assert_bundle_response

        included_resources = resource.entry.map(&:resource).select { |res| res.resourceType == 'Organization' }
        assert included_resources.any?, 'Expected at least one Organization resource included in the response'
      end
    end

    # Additional tests for other resources and includes can be added here
  end
end