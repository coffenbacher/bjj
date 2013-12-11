Feature: Creating and viewing techniques
    Scenario: Anonymous user views a technique
        Given I have the following techniques in my database:
            | name                  |
            | Armbar (from guard)   |
        When I go to the URL of technique indexed at 0
        Then I should see the header "Armbar (from guard)"
