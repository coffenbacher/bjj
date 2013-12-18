Feature: Loading sample data
    Scenario: Loading for all models
        Given I have the following techniques in my database:
            | name     | category   | start | image                         |
            | Guard    | Position   |       | metamoris.jpg                 |
            | Armbar   | Submission | Guard | flyingarmbar.jpg              |
            | Clarkoplata | Submission  | Guard | clarkoplata.jpg           |
            | Footlock    | Submission  | Guard | footlock.jpg              |
            | Single-leg  | Transition  | Guard  |   singleleg.jpg       |
        And given I have the following videos in my database:
            | youtube_id    |
            | tM5XUVMhIsM   | 
        And given the following relationship in my database:
            | technique_name    | youtube_id    | start_time    |
            | Armbar            | tM5XUVMhIsM   | 10            |
        When I go to the "/" URL
        Then I should see the text "Armbar"
