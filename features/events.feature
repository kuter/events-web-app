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

    Scenario: User cannot create event in the past
        Given I'm logged in
        And I see index page
        And I click on "Create event" menu item
        When fill title input with test@foo.bar
        And fill date date field with 2020-01-01
        And fill description text field with "Lorem Ipsum"
        And click Create button
        Then I should see "You cannot create event in the past" error
