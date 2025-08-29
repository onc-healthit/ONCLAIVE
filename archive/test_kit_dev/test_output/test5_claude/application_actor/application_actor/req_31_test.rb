module Test5_claude
  class DirectoryContentUpdateTest < Inferno::TestGroup
    id :directory_content_update_tracking
    title 'Client Tracking of Directory Content Updates'
    description %(
      Verify that clients can track additions or modifications to directory content 
      through queries using the _lastUpdated search parameter.
      
      This test validates that:
      * The server supports _lastUpdated search parameter
      * Results can be filtered by last update timestamp
      * Modified resources are returned when querying with timestamp criteria
    )

    test do
      id :last_updated_parameter_support
      title 'Server supports _lastUpdated search parameter'
      description 'Verify server accepts _lastUpdated parameter in searches'
      
      run do
        # Search with _lastUpdated parameter
        time = DateTime.now.iso8601
        search_params = {_lastUpdated: "le#{time}"}
        
        fhir_search(:practitioner, params: search_params)
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource
        assert bundle.total.positive?, 'Expected search to return matching resources'
      end
    end

    test do
      id :track_content_updates
      title 'Track content modifications using _lastUpdated'
      description 'Verify modified resources can be found via _lastUpdated searches'
      
      run do
        # Get initial timestamp
        start_time = DateTime.now.iso8601
        
        # Create a new practitioner resource
        practitioner = FHIR::Practitioner.new(
          active: true,
          name: [
            {
              family: 'Test',
              given: ['Provider']
            }
          ]
        )
        
        begin
          fhir_create(practitioner)
          assert_response_status([200, 201])
          created_id = resource.id
          
          # Search for updates since start time
          search_params = {_lastUpdated: "gt#{start_time}"}
          fhir_search(:practitioner, params: search_params)
          
          assert_response_status(200)
          assert_resource_type(:bundle)
          
          bundle = resource
          
          assert bundle.total.positive?, 'Expected to find newly created resource'
          assert bundle.entry.any? { |e| e.resource.id == created_id }, 
                 'Created resource not found in _lastUpdated results'
        
        # Cleanup
        ensure
          fhir_delete(:practitioner, created_id) if created_id
        end
      end
    end

    test do 
      id :last_updated_filtering
      title 'Filter results by last update time range'
      description 'Verify _lastUpdated parameter correctly filters by time range'
      
      run do
        # Search with time range
        end_time = DateTime.now
        start_time = end_time - 1 # 1 day ago
        
        search_params = {
          _lastUpdated: "gt#{start_time.iso8601}&le#{end_time.iso8601}"
        }
        
        fhir_search(:practitioner, params: search_params)
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource
        
        bundle.entry&.each do |entry|
          resource_time = DateTime.parse(entry.resource.meta.lastUpdated)
          assert resource_time >= start_time && resource_time <= end_time,
                 "Resource lastUpdated #{resource_time} outside requested range"
        end
      end
    end
  end
end