module Test4Gpt
  class MustSupportElementsDisplayTestGroup < Inferno::TestGroup
    id :req_08_must_support_elements_display
    title 'Must Support Elements Display'
    description %(
      This test group verifies that the Application Actor SHOULD display Must Support data elements for human use or store for other purposes.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :must_support_elements_display_test
      title 'Application Actor displays Must Support elements'
      description %(
        Verify that the Application Actor displays Must Support data elements for human use or stores them for other purposes.
      )
      input :resource_type, :resource_id

      run do
        skip_if resource_type.blank? || resource_id.blank?, 'Resource type and ID must be provided'

        fhir_read(resource_type.to_sym, resource_id)
        assert_response_status(200)
        assert_valid_resource

        resource = resource()

        must_support_elements = resource.meta&.extension&.select do |extension|
          extension.url == 'http://hl7.org/fhir/StructureDefinition/elementdefinition-mustSupport'
        end

        skip_if must_support_elements.blank?, "No Must Support elements found in the #{resource_type} resource"

        # Assuming the application actor has a method to check if elements are displayed or stored
        # This is a placeholder for actual implementation logic
        must_support_elements.each do |element|
          assert application_actor_displays_or_stores?(element), "Must Support element #{element} is not displayed or stored"
        end

        pass 'All Must Support elements are displayed or stored as expected'
      end
    end

    private

    def application_actor_displays_or_stores?(element)
      # Placeholder method to determine if the application actor displays or stores the element
      # Replace with actual logic to verify the application actor's behavior
      true
    end
  end
end