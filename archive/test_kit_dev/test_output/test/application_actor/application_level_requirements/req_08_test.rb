module Test
  class MustSupportDisplayGroup < Inferno::TestGroup
    id :must_support_display_group
    title 'Must Support Elements Display Tests'
    description %(
      Verify that the Application Actor properly handles Must Support data elements
      by displaying them for human use or storing them for other purposes.
    )

    test do
      id :must_support_elements_display
      title 'Must Support elements are properly handled'
      description %(
        Verify that the Application Actor can properly display or store Must Support
        data elements as defined in the profiles.
      )

      input :displayed_elements,
            title: 'Must Support Elements Displayed',
            description: 'List of Must Support elements that were displayed', 
            type: 'textarea'

      input :stored_elements,
            title: 'Must Support Elements Stored',
            description: 'List of Must Support elements that were stored',
            type: 'textarea',
            optional: true

      run do
        skip_if displayed_elements.blank? && stored_elements.blank?,
                'No Must Support elements were displayed or stored'

        displayed = displayed_elements.split(/\n+/).map(&:strip)
        stored = stored_elements.split(/\n+/).map(&:strip) if stored_elements.present?

        assert displayed.present? || stored&.present?,
               'Must Support elements must be either displayed or stored'

        if displayed.present?
          displayed.each do |element|
            info "Must Support element displayed: #{element}"
          end
        end

        if stored&.present?
          stored.each do |element|
            info "Must Support element stored: #{element}"
          end
        end

        pass "Application properly handled Must Support elements:\n"\
             "#{displayed.length} elements displayed\n"\
             "#{stored&.length || 0} elements stored"
      end
    end
  end
end