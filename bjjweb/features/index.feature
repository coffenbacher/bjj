Feature: Welcome experience
    Scenario: Anonymous user opens the site
        When I go to the "/" URL
        Then I should see the header "Welcome anonymous"

    Scenario: Existing user opens the site
        Given I am logged in
        And given I have the following techniques in my database:
            | name          | category  | start |
            | Armbar        | Submission|       |
            | Clarkoplata   | Submission|       |
        When I go to the "/" URL
        Then I should see the header "Welcome user"
        And I should see at least 4 img tags
        And I should see the text "Clarkoplata"
