Feature: Welcome experience
    Scenario: Anonymous user opens the site
        When I go to the "/" URL
        Then I should see 4 img tags
        Then the header "Welcome anonymous"

    Scenario: Existing user opens the site
        When I go to the "/" URL
        Then I should see 8 img tags
        Then I should see the header "Yo dawg"

