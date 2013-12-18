Feature: Creating and viewing videos
    Scenario: Anonymous user views a video
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
        When I go to the URL of video with id "tM5XUVMhIsM"
        Then I should see the video "tM5XUVMhIsM"  
        And I should see the text "Armbar"
