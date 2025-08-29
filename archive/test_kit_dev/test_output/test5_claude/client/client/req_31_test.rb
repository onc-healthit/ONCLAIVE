module Test5_claude
  class DirectoryContentTrackingGroup < Inferno::TestGroup
    id :directory_content_tracking
    title 'Client Tracking of Directory Content Updates'
    description %(
      Verify that clients can track additions or modifications to directory content 
      through queries using the _lastUpdated search parameter.
      
      This test validates that:
      * The server supports _lastUpdated search parameter
      * Results are filtered appropriately based on last update timestamp
      * Changes to resources are reflected in _lastUpdated queries
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :lastupdate_parameter_support
      title 'Server supports _lastUpdated search parameter'
      description 'Verify server supports _lastUpdated parameter on resource searches'
      
      run do
        # Search with _lastUpdated
        timestamp = Time.now.utc - 3600 # 1 hour ago
        search_params = {
          _lastUpdated: "gt#{timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')}"
        }

        fhir_search(:Practitioner, params: search_params)
        assert_response_status(200)
        assert_resource_type(:Bundle)
      end
    end

    test do
      id :content_tracking_validation 
      title 'Content changes are reflected in _lastUpdated results'
      description 'Verify that resource updates are reflected in _lastUpdated query results'
      
      run do
        # Create timestamp before update
        pre_update_time = Time.now.utc
        sleep(1) # Ensure timestamps differ

        # Update a resource
        practitioner = FHIR::Practitioner.new(
          active: true,
          name: [{ family: 'Test', given: ['Provider'] }]
        )
        fhir_create(practitioner)
        assert_response_status(201)
        practitioner_id = resource.id

        # Search after update
        search_params = {
          _lastUpdated: "gt#{pre_update_time.strftime('%Y-%m-%dT%H:%M:%SZ')}"
        }
        
        fhir_search(:Practitioner, params: search_params)
        assert_response_status(200)
        assert_resource_type(:Bundle)

        bundle = resource
        
        # Verify updated resource is included
        found = bundle.entry.any? do |entry|
          entry.resource.id == practitioner_id
        end
        
        assert found, "Updated resource with id #{practitioner_id} not found in _lastUpdated results"

        # Cleanup
        fhir_delete(:Practitioner, practitioner_id)
      end
    end

    test do
      id :lastupdate_filter_accuracy
      title '_lastUpdated filter excludes older content'
      description 'Verify _lastUpdated parameter correctly filters out older content'

      run do
        # Create resource
        practitioner = FHIR::Practitioner.new(
          active: true,
          name: [{ family: 'Test', given: ['Provider'] }]
        )
        fhir_create(practitioner)
        assert_response_status(201)
        practitioner_id = resource.id

        # Search with future timestamp
        future_time = Time.now.utc + 3600 # 1 hour in future
        search_params = {
          _lastUpdated: "gt#{future_time.strftime('%Y-%m-%dT%H:%M:%SZ')}"
        }

        fhir_search(:Practitioner, params: search_params)
        assert_response_status(200)
        assert_resource_type(:Bundle)
        
        bundle = resource

        # Verify resource not included
        found = bundle.entry&.any? do |entry|
          entry.resource.id == practitioner_id
        end

        assert !found, "Resource found in results when it should have been filtered out"

        # Cleanup
        fhir_delete(:Practitioner, practitioner_id)
      end
    end
  end
end