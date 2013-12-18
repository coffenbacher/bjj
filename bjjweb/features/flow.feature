Feature: Creating and viewing flows
    Scenario: Anonymous user views a flow
        Given I have the following techniques in my database:
            | name     | category   | start | image             |
            | Guard    | Position   |       | clarkoplata.jpg   |
            | Armbar   | Submission | Guard | clarkoplata.jpg   |
        And given I have the following flows in my database:
            | name    |
            | BJJ     | 
        And given the following flow relationship in my database:
            | flow_name    | technique_name    |
            | BJJ          | Armbar            |
        When I go to the URL of flow with name "BJJ"
        Then I should see the text "Armbar"  

    Scenario: Anonymous user views the flow list
        Given I have the following flows in my database:
            | name      |
            | BJJ       |
            | Nogi      |
        When I go to the "/flow/" URL
        Then I should see the text "BJJ"
        And I should see the text "Nogi"
    Scenario: Logged in user creates a flow
        Given I have the following techniques in my database:
            | name     | category   | start | image             |
            | Guard    | Position   |       | clarkoplata.jpg   |
            | Armbar   | Submission | Guard | clarkoplata.jpg   |
        And given I have the following flows in my database:
            | name  |
        When I go to the "/flow/create/" URL
        And I fill in "name" with "BJJ"
        And I add "Armbar" to the flow
        And I submit the form "create"
        Then I should see the header "BJJ"
        And I should see the text "Armbar"
        
