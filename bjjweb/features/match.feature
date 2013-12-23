Feature: Creating and viewing matches
    Scenario: Anonymous user views the match list
        Given I have the following matches in my database:
            | name          | youtube_id  |
            | Toquinho1     | qsblWuiwMGY |
            | ToquinhoADCC  | FohRibjEbgI |
        When I go to the "/match/" URL
        Then I should see the text "Toquinho1"
        And I should see the text "ToquinhoADCC"

    Scenario: Anonymous user views a match
        Given I have the following matches in my database:
            | name          | youtube_id  |
            | Toquinho1     | qsblWuiwMGY |
            | ToquinhoADCC  | FohRibjEbgI |
        When I go to the URL of match named "Toquinho1"
        Then I should see the header "Toquinho1"
