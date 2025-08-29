module Test6_claude
  class DirectoryUpdateTrackingGroup < Inferno::TestGroup
    id :directory_update_tracking
    title 'Client Tracking of Directory Content Updates'
    description %(
      Verify that clients can track additions or modifications to directory content 
      through queries using the _lastUpdated search parameter.
      
      This test validates that:
      * The server supports _lastUpdated search parameter
      * Results are properly filtered based on last update timestamp
      * Changes to resources are reflected in _lastUpdated results
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    input :url,
          title: 'FHIR Server URL',
          description: 'The base URL for the FHIR server'
          
    input :bearer_token,
          title: 'Bearer Token',
          description: 'Bearer token for server authentication'

    test do
      id :test_lastupdated_support
      title 'Server supports _lastUpdated search parameter'
      description %(
        Verify server supports searching by _lastUpdated parameter by performing
        a basic search and validating the response.
      )

      run do
        # Search with _lastUpdated parameter
        timestamp = DateTime.now.utc.iso8601
        search_params = { _lastUpdated: "le#{timestamp}" }
        
        fhir_search(:practitioner, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries
      end
    end

    test do
      id :test_lastupdated_filtering 
      title 'Server properly filters results by _lastUpdated'
      description %(
        Verify that _lastUpdated parameter correctly filters resources
        based on their last modification timestamp.
      )

      run do
        # First create a new resource
        practitioner = FHIR::Practitioner.new(
          active: true,
          name: [{ family: 'Test', given: ['Provider'] }]
        )
        
        fhir_create(practitioner)
        assert_response_status(201)
        created_id = resource.id
        
        created_time = DateTime.now.utc
        
        # Search after creation timestamp
        search_params = { _lastUpdated: "gt#{(created_time - 1).iso8601}" }
        fhir_search(:practitioner, params: search_params)
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        found = resource.entry&.any? do |entry|
          entry.resource.id == created_id
        end
        
        assert found, "Created resource not found in _lastUpdated results"

        # Search before creation timestamp 
        search_params = { _lastUpdated: "lt#{(created_time - 1).iso8601}" }
        fhir_search(:practitioner, params: search_params)
        
        found = resource.entry&.any? do |entry|
          entry.resource.id == created_id
        end
        
        assert !found, "Created resource found in results before its creation time"
      end
    end

    test do
      id :test_updates_reflected
      title 'Resource updates are reflected in _lastUpdated results'
      description %(
        Verify that when a resource is updated, the change is reflected
        in results filtered by _lastUpdated.
      )
      
      run do
        # Create initial resource
        practitioner = FHIR::Practitioner.new(
          active: true,
          name: [{ family: 'Initial', given: ['Name'] }]
        )
        
        fhir_create(practitioner)
        assert_response_status(201)
        practitioner_id = resource.id
        
        initial_time = DateTime.now.utc
        sleep(1) # Ensure timestamps will be different
        
        # Update the resource
        practitioner.id = practitioner_id
        practitioner.name.first.family = 'Updated'
        
        fhir_update(practitioner)
        assert_response_status(200)
        
        update_time = DateTime.now.utc
        
        # Search between initial creation and update
        search_params = {
          _lastUpdated: "gt#{initial_time.iso8601}&lt#{update_time.iso8601}"
        }
        
        fhir_search(:practitioner, params: search_params)
        
        found = resource.entry&.any? do |entry|
          entry.resource.id == practitioner_id &&
            entry.resource.name.first.family == 'Updated'
        end
        
        assert found, "Updated resource not found in _lastUpdated results"
      end
    end
  end
end