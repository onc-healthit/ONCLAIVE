module Test5_gemini
  class Req32GeneralSearchPharmacyTest < Inferno::TestGroup
    id :req_32_general_search_pharmacy
    title 'REQ-32: General Search for Pharmacy'
    description %(
      Verify that the server supports searching for Pharmacy resources using the following search parameters:
      - HealthcareService.category
      - HealthcareService.specialty
      - Location
      - network
    )

    test do
      id :req_32_pharmacy_search_by_category
      title 'Server supports searching Pharmacy by category'
      description 'Verify that the server supports searching Pharmacy resources by HealthcareService.category'
      input :search_category

      run do
        skip_if_not_supported(:HealthcareService, [:search, :read])
        skip_if search_category.blank?, 'No search category provided'

        fhir_search(:healthcareservice, params: { category: search_category })

        assert_response_status(200)
        assert_bundle_response
        assert_at_least_one_resource
      end
    end

    test do
      id :req_32_pharmacy_search_by_specialty
      title 'Server supports searching Pharmacy by specialty'
      description 'Verify that the server supports searching Pharmacy resources by HealthcareService.specialty'
      input :search_specialty

      run do
        skip_if_not_supported(:HealthcareService, [:search, :read])
        skip_if search_specialty.blank?, 'No search specialty provided'

        fhir_search(:healthcareservice, params: { specialty: search_specialty })

        assert_response_status(200)
        assert_bundle_response
        assert_at_least_one_resource
      end
    end

    test do
      id :req_32_pharmacy_search_by_location
      title 'Server supports searching Pharmacy by location'
      description 'Verify that the server supports searching Pharmacy resources by Location'
      input :search_location

      run do
        skip_if_not_supported(:HealthcareService, [:search, :read])
        skip_if search_location.blank?, 'No search location provided'

        fhir_search(:healthcareservice, params: { location: search_location })

        assert_response_status(200)
        assert_bundle_response
        assert_at_least_one_resource
      end
    end

    test do
      id :req_32_pharmacy_search_by_network
      title 'Server supports searching Pharmacy by network'
      description 'Verify that the server supports searching Pharmacy resources by network'
      input :search_network

      run do
        skip_if_not_supported(:HealthcareService, [:search, :read])
        skip_if search_network.blank?, 'No search network provided'

        fhir_search(:healthcareservice, params: { organization: search_network })

        assert_response_status(200)
        assert_bundle_response
        assert_at_least_one_resource
      end
    end
  end
end