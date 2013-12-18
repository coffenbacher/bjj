Feature: Creating and viewing techniques
    Scenario: Anonymous user views a technique
        Given I have the following techniques in my database:
            | name     | category   | start | image             |
            | Guard    | Position   |       | clarkoplata.jpg   |
            | Armbar   | Submission | Guard | clarkoplata.jpg   |
        And given I have the following videos in my database:
            | youtube_id    |
            | tM5XUVMhIsM   | 
        And given the following relationship in my database:
            | technique_name    | youtube_id    | start_time    |
            | Armbar            | tM5XUVMhIsM   | 10            |
        When I go to the URL of technique named "Armbar" 
        Then I should see the header "Armbar"
        And I should see the text "Instructionals"
        And I should see the video "tM5XUVMhIsM"
        And I should see the text "Guard"
        And I should see the text "Submission"

    Scenario: Logged in user creates a technique
        Given I have the following techniques in my database:
            | name      | category  | start |
            | Guard     | Position  |       |
        And given I am logged in
        When I go to the "/technique/create/" URL
        And I fill in "name" with "Armbar"
        And I select "start" as technique "Guard"
        And I fill in "category" with "Submission"
        And I submit the form "create"
        Then I should see the header "Armbar" 

        
    Scenario: Anonymous user views the technique list
        Given I have the following techniques in my database:
            | name      | category  | start |
            | Guard     | Position  |       |
            | Armbar    | Submission| Guard |
        When I go to the "/technique/" URL
        Then I should see the text "Guard"
        And I should see the text "Submission"
