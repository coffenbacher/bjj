Feature: Static files
    Scenario: Anonymous user accesses static files
        When I go to the "/static/assets/js/bootstrap.js" URL
        Then I should see "bootstrap-transition.js" in the HTML
