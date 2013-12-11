Feature: Creating and viewing techniques
    Scenario: Anonymous user views a technique
        Given I have the following techniques in my database:
            | name     |
            | Armbar   |
        And given I have the following videos in my database:
            | youtube_id    |
            | tM5XUVMhIsM   | 
        And given the following relationship in my database:
            | technique_name    | youtube_id    | start_time    |
            | Armbar            | tM5XUVMhIsM   | 10            |
        When I go to the URL of technique indexed at 0
        Then I should see the header "Armbar"
        And I should see the text "Instructionals"
        And I should see the video "tM5XUVMhIsM"
