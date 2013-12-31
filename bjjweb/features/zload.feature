Feature: Loading sample data
    Scenario: Loading for all models
        Given I have the following techniques in my database:
            | name                      | category   | start                    |   end                     |             image                         |
            | Guard (bottom)            | Position   |                          |                           |          metamoris.jpg                 |
            | Guard (top)               | Position   |                          |                           |          metamoris.jpg                 |
            | Half-guard (bottom)       | Position   |                          |                           |          metamoris.jpg                 |
            | Half-guard (top)          | Position   |                          |                           |          metamoris.jpg                 |
            | Side control (bottom)     | Position   |                          |                           |          metamoris.jpg                 |
            | Side control (top)        | Position   |                          |                           |          metamoris.jpg                 |
            | Mount (bottom)            | Position   |                          |                           |          metamoris.jpg                 |
            | Mount (top)               | Position   |                          |                           |          metamoris.jpg                 |
            | Back mount (top)          | Position   |                          |                           |          metamoris.jpg                 |
            | Back mount (bottom)       | Position   |                          |                           |          metamoris.jpg                 |
            | Armbar                    | Submission | Guard (bottom)           |                           |          flyingarmbar.jpg              |
            | Omoplata                  | Submission | Guard (bottom)           |                           |          flyingarmbar.jpg              |
            | Triangle                  | Submission | Guard (bottom)           |                           |          flyingarmbar.jpg              |
            | Loop choke                | Submission | Guard (bottom)           |                           |          flyingarmbar.jpg              |
            | Cross collar choke        | Submission | Guard (bottom)           |                           |          flyingarmbar.jpg              |
            | Kimura                    | Submission | Guard (bottom)           |                           |          flyingarmbar.jpg              |
            | Guillotine                | Submission | Guard (bottom)           |                           |          flyingarmbar.jpg              |
            | Clarkoplata               | Submission | Guard (bottom)           |                           |          clarkoplata.jpg               |
            | Footlock                  | Submission | Guard (bottom)           |                           |          footlock.jpg                  |
            | Ezekiel choke             | Submission | Mount (top)              |                           |          footlock.jpg                  |
            | Single-leg                | Transition | Guard (bottom)           |                           |          singleleg.jpg                 |
            | Scissor sweep             | Sweep      | Guard (bottom)           | Mount (top)               |          singleleg.jpg                 |
            | Hip bump sweep            | Sweep      | Guard (bottom)           | Mount (top)               |          singleleg.jpg                 |
        And given I have the following videos in my database:
            | youtube_id    |
            | tM5XUVMhIsM   | 
        And given the following relationship in my database:
            | technique_name    | youtube_id    | start_time    |
            | Armbar            | tM5XUVMhIsM   | 10            |
        And given I have the following flows in my database:
            | name    |
            | BJJ     | 
        And given the following flow relationship in my database:
            | flow_name    | technique_name         |
            | BJJ          | Guard (bottom)         |
            | BJJ          | Guard (top)            |
            | BJJ          | Half-guard (bottom)    |
            | BJJ          | Half-guard (top)       |
            | BJJ          | Side control (bottom)  |
            | BJJ          | Side control (top)     |
            | BJJ          | Mount (bottom)         |
            | BJJ          | Mount (top)            |
            | BJJ          | Back mount (bottom)    |
            | BJJ          | Back mount (top)       |
            | BJJ          | Armbar                 |
            | BJJ          | Omoplata               |
            | BJJ          | Kimura                 |
            | BJJ          | Triangle               |
            | BJJ          | Guillotine             |
            | BJJ          | Cross collar choke     |
            | BJJ          | Loop choke             |
            | BJJ          | Scissor sweep          |
            | BJJ          | Hip bump sweep         |
            | BJJ          | Ezekiel choke          |
        When I go to the "/" URL
        Then I should see the text "Armbar"
