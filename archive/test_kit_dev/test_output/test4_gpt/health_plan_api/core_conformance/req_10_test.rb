module Test4Gpt
  class NetworkDocumentationTestGroup < Inferno::TestGroup
    id :req_10_network_documentation
    title 'Network Documentation for Practitioners'
    description %(
      Health Plan API SHALL document practitioner network participation using PractitionerRole instances linked to Networks.
      This test verifies that the Health Plan API provides PractitionerRole resources that are linked to Network resources.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :practitioner_role_network_linkage_test
      title 'PractitionerRole instances are linked to Networks'
      description %(
        Verify that PractitionerRole resources returned by the Health Plan API are linked to Network resources.
      )
      input :practitioner_role_id

      run do
        fhir_read(:practitioner_role, practitioner_role_id)
        assert_response_status(200)
        assert_resource_type(:practitioner_role)
        assert_valid_resource

        practitioner_role = resource
        assert practitioner_role.network.present?, 'PractitionerRole does not contain a network link'
        assert practitioner_role.network.all? { |network| network.reference.present? }, 'Network reference is missing in PractitionerRole'
      end
    end
  end
end