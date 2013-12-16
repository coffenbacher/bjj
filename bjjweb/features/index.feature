Feature: Welcome experience
    Scenario: Anonymous user opens the site
        When I go to the "/" URL
        Then I should see the tag "login"

    Scenario: Existing user opens the site
        Given I am logged in
        And given I have the following techniques in my database:
            | name          | category  | start |
            | Armbar        | Submission|       |
            | Clarkoplata   | Submission|       |
        When I go to the "/" URL
        Then I should not see the tag "login"
        And I should see at least 1 img tags
        And I should see the text "Clarkoplata"
