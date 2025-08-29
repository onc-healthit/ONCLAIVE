# frozen_string_literal: true

module Test5_gemini
  class Req12SupportForAllImplementationGuideProfilesTest < Inferno::TestGroup
    id :req_12_support_for_all_implementation_guide_profiles
    title 'REQ-12: Support for all Implementation Guide profiles'
    description %(
      Support all profiles defined in this Implementation Guide.
    )

    test do
      id :req_12_check_supported_profiles
      title 'Health Plan API SHALL support all profiles defined in this Implementation Guide'
      description %(
        This test checks if the Health Plan API supports all the profiles defined in this Implementation Guide.
      )
      run do
        skip 'TODO: Implement REQ-12 Support for all Implementation Guide profiles test'
        # 1. Retrieve the CapabilityStatement
        # 2. Extract the list of supported profiles from the CapabilityStatement
        # 3. Compare the list of supported profiles with the list of profiles defined in the IG
        # 4. Assert that all IG profiles are present in the list of supported profiles
      end
    end
  end
end
