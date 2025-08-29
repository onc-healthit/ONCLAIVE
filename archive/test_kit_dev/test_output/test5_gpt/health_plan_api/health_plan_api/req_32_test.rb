module Test5Gpt
  class GeneralSearchForPharmacyTestGroup < Inferno::TestGroup
    id :req_32_general_search_for_pharmacy
    title 'REQ-32: General Search for Pharmacy'
    description %(
      This test group verifies that the Health Plan API supports general search 
      for pharmacies using the HealthcareService resource. The search should 
      be based on the category and specialty fields, with qualifications of 
      location and network.
    )

    test do
      id :pharmacy_general_search_test
      title 'General Search for Pharmacy'
      description %(
        Verify that the server supports searching for pharmacies using 
        HealthcareService.category and HealthcareService.specialty. 
        The search results should be filtered by location and network.
      )
      input :server_url, :access_token, :location, :network

      fhir_client do
        url :server_url
        bearer_token :access_token
      end

      run do
        search_params = {
          'category' => 'pharmacy',
          'specialty' => 'pharmacy-specialty',
          'location' => location,
          'network' => network
        }

        reply = fhir_search(:HealthcareService, params: search_params)

        assert_response_status(200)
        assert_resource_type(:Bundle)
        assert_valid_resource

        entries = reply.resource.entry
        assert entries.present?, 'No HealthcareService resources were returned'

        entries.each do |entry|
          resource = entry.resource
          assert resource.category.any? { |cat| cat.coding.any? { |coding| coding.code == 'pharmacy' } },
                 'HealthcareService does not have the expected category of pharmacy'
          assert resource.specialty.any? { |spec| spec.coding.any? { |coding| coding.code == 'pharmacy-specialty' } },
                 'HealthcareService does not have the expected specialty of pharmacy-specialty'
        end
      end
    end
  end
end