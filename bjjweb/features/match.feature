Feature: Creating and viewing matches
    Scenario: Anonymous user views a match
        Given I have the following matches in my database:
            | name      |
            | Toquinho1 |
        When I go to the "/match/" URL
        Then I should see the text "Toquinho1"
