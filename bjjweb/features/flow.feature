Feature: Creating and viewing flows
    Scenario: Anonymous user views a flow
        Given I have the following techniques in my database:
            | name     | category   | start |
            | Guard    | Position   |       |
            | Armbar   | Submission | Guard |
        And given I have the following flows in my database:
            | name    |
            | BJJ     | 
        And given the following flow relationship in my database:
            | flow_name    | technique_name    |
            | BJJ          | Armbar            |
        When I go to the URL of flow with name "BJJ"
        Then I should see the text "Armbar"  

    Scenario: Logged in user creates a flow
        Given I have the following techniques in my database:
            | name     | category   | start |
            | Guard    | Position   |       |
            | Armbar   | Submission | Guard |
        And given I have the following flows in my database:
            | name  |
        When I go to the "/flow/create/" URL
        And I fill in "name" with "BJJ"
        And I add "Armbar" to the flow
        And I submit the form "create"
        Then I should see the header "BJJ"
        And I should see the text "Armbar"
