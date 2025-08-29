module Test8_claude
  class MustSupportDisplayGroup < Inferno::TestGroup
    id :must_support_display_group
    title 'Must Support Elements Display Test'
    description %(
      Tests that the Application Actor can handle Must Support data elements
      by displaying them for human use or storing them for other purposes.
    )

    fhir_client do
      url :url
      oauth_credentials :credentials
    end

    test do
      id :must_support_elements_display
      title 'Application handles Must Support data elements'
      description %(
        Verify that Must Support data elements from resources can be:
        1. Displayed for human viewing, or
        2. Stored for other purposes
      )

      input :url,
            title: 'FHIR Server URL',
            description: 'Base URL for FHIR Server',
            type: 'text'

      input :credentials,
            title: 'OAuth Credentials',
            description: 'OAuth 2.0 credentials for server access',
            type: :oauth_credentials,
            optional: true

      input :resource_type,
            title: 'Resource Type',
            description: 'The FHIR resource type containing Must Support elements',
            type: 'text'
            
      input :must_support_elements,
            title: 'Must Support Elements',
            description: 'Comma-separated list of Must Support elements to verify',
            type: 'text'

      input :display_verification,
            title: 'Display Verification',
            description: 'Confirmation that Must Support elements are displayed/stored',
            type: 'radio',
            options: [
              {
                label: 'Elements are displayed to users',
                value: 'displayed'
              },
              {
                label: 'Elements are stored for other uses',
                value: 'stored'  
              }
            ]

      run do
        # Verify resource exists
        fhir_read(resource_type.to_sym, '123')
        assert_response_status(200)
        assert_resource_type(resource_type.to_sym)

        # Parse must support elements
        elements = must_support_elements.split(',').map(&:strip)

        # Verify each must support element exists in resource
        elements.each do |element|
          assert resource[element].present?,
                 "Must Support element #{element} is not present or has no value"
        end

        # Verify display/storage based on input
        case display_verification
        when 'displayed'
          pass 'Must Support elements are displayed for human use'
        when 'stored'  
          pass 'Must Support elements are stored for other purposes'
        else
          fail "Invalid display verification value: #{display_verification}" 
        end
      end
    end
  end
end