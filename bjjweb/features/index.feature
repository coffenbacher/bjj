Feature: Welcome experience
    Scenario: Anonymous user opens the site
        When I go to the "/" URL
        Then I should see the header "Welcome anonymous"

    Scenario: Existing user opens the site
        Given I am logged in
        When I go to the "/" URL
        Then I should see the header "Welcome user"
        And I should see 4 img tags

