Feature: Events
    As a user
    I want to create and edit events

    Scenario: Logged user can access create event view
        Given I'm logged in
        And I see index page
        When I click on "Create event" menu item
        Then I should see "Create new event" heading

    Scenario: Anonmous user should be redirected to login page
        Given I see index page
        When I click on "Create event" menu item
        Then I should see "Login Form" heading
