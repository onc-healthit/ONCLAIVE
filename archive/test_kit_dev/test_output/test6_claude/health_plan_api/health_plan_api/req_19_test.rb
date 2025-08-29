module Test6_claude
  class SearchParameterSupportTestGroup < Inferno::TestGroup
    id :individual_search_parameter_support
    title 'Individual Search Parameter Support'
    description %(
      This test group verifies that the Health Plan API supports the search parameters 
      defined on each profile individually as required by REQ-19.
      
      The server SHALL support querying resources using each defined search parameter
      independently.
    )

    PROFILES = [
      {
        resource_type: 'Patient',
        search_params: ['name', 'birthdate', 'gender']
      },
      {
        resource_type: 'Coverage', 
        search_params: ['subscriber', 'beneficiary', 'payor']
      },
      {
        resource_type: 'ExplanationOfBenefit',
        search_params: ['patient', 'created', 'type']
      }
    ]

    PROFILES.each do |profile|
      group do
        title "#{profile[:resource_type]} Search Parameter Tests"
        description "Verify support for #{profile[:resource_type]} search parameters"

        profile[:search_params].each do |param|
          test do
            id :"#{profile[:resource_type].downcase}_#{param}_search"
            title "#{profile[:resource_type]} #{param} search test"
            description "Verify server supports searching #{profile[:resource_type]} by #{param}"

            run do
              # Construct test search value based on parameter
              search_value = case param
                           when 'birthdate'
                             '1990-01-01'
                           when 'created' 
                             '2023-01-01'
                           else
                             'test'
                           end

              fhir_search(profile[:resource_type].to_sym, params: { param => search_value })
              
              assert_response_status(200)
              assert_resource_type(:bundle)
              
              bundle = resource

              assert bundle.type == 'searchset', 
                     "Expected Bundle type to be 'searchset', but found '#{bundle.type}'"

              assert_valid_bundle_entries(bundle)

              # Verify search parameter was processed
              assert bundle.total.present? || bundle.entry.present?,
                     "Search returned no results or total - server may not support #{param} parameter"
            end
          end
        end
      end
    end

    def assert_valid_bundle_entries(bundle)
      return unless bundle.entry&.any?

      bundle.entry.each do |entry|
        assert entry.resource.present?, 'Bundle entry missing resource'
        assert_valid_resource(resource: entry.resource)
      end
    end

  end
end