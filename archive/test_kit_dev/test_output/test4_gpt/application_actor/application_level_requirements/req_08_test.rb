module Test4Gpt
  class MustSupportElementsDisplayTestGroup < Inferno::TestGroup
    id :req_08_must_support_elements_display
    title 'Must Support Elements Display'
    description %(
      Application Actor SHOULD display Must Support data elements for human use or store for other purposes.
      This test verifies that the application actor can handle Must Support elements appropriately.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :must_support_elements_display_test
      title 'Application Actor displays or stores Must Support elements'
      description %(
        This test checks if the Application Actor displays Must Support data elements for human use or stores them for other purposes.
        It verifies that the elements marked as Must Support in the profile are present in the resources retrieved.
      )
      input :resource_type, :resource_id, :must_support_elements

      run do
        skip_if must_support_elements.blank?, 'No Must Support elements provided for testing.'

        response = fhir_read(resource_type.to_sym, resource_id)
        assert_response_status(200)
        assert_valid_resource

        must_support_elements.each do |element|
          assert resource[element].present?, "Must Support element '#{element}' is not present in the resource."
        end

        pass 'All Must Support elements are present in the resource.'
      end
    end
  end
end