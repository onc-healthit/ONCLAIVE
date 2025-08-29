module Test5_claude
  class IndividualSearchParameterGroup < Inferno::TestGroup
    id :individual_search_parameter_support
    title 'Individual Search Parameter Support'
    description %(
      Verify that the server supports the searchParameters on each profile individually.
      Each defined search parameter must be tested independently to validate proper 
      server implementation.
    )

    test do
      id :patient_name_search
      title 'Patient name search parameter'
      description %(
        Verify that Patient resources can be searched by name parameter.
      )
      
      run do
        fhir_search(:patient, params: {name: 'Smith'})
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries(:patient)
      end
    end

    test do
      id :patient_identifier_search  
      title 'Patient identifier search parameter'
      description %(
        Verify that Patient resources can be searched by identifier parameter.
      )

      run do
        fhir_search(:patient, params: {identifier: 'urn:oid:1.2.36.146.595.217.0.1|12345'})
        assert_response_status(200) 
        assert_resource_type(:bundle)
        assert_valid_bundle_entries(:patient)
      end
    end

    test do
      id :practitioner_name_search
      title 'Practitioner name search parameter' 
      description %(
        Verify that Practitioner resources can be searched by name parameter.
      )

      run do
        fhir_search(:practitioner, params: {name: 'Smith'})
        assert_response_status(200)
        assert_resource_type(:bundle) 
        assert_valid_bundle_entries(:practitioner)
      end
    end

    test do 
      id :practitioner_identifier_search
      title 'Practitioner identifier search parameter'
      description %(
        Verify that Practitioner resources can be searched by identifier parameter.
      )

      run do
        fhir_search(:practitioner, params: {identifier: 'http://hl7.org/fhir/sid/us-npi|9941339108'})
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries(:practitioner)
      end
    end

    test do
      id :location_name_search
      title 'Location name search parameter'
      description %(
        Verify that Location resources can be searched by name parameter.
      )

      run do
        fhir_search(:location, params: {name: 'General Hospital'})
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries(:location)
      end
    end

    test do
      id :location_address_search
      title 'Location address search parameter'
      description %(
        Verify that Location resources can be searched by address parameter. 
      )

      run do
        fhir_search(:location, params: {address: '123 Main St'})
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries(:location)
      end
    end

    def assert_valid_bundle_entries(resource_type)
      bundle = resource
      assert bundle.entry.present?, 'Bundle must contain entries'
      bundle.entry.each do |entry|
        assert entry.resource.resourceType == resource_type.to_s.capitalize,
               "Expected resourceType #{resource_type} but found #{entry.resource.resourceType}"
        assert_valid_resource(entry.resource)
      end
    end

  end
end