Feature: Login
    As a registered user
    I want to log in

    Scenario: Login with email and valid password
        Given registered user test@foo.bar with password T3$t1234!
        And I see index page
        When I click on "Login" menu item
        And fill username input with test@foo.bar
        And fill password input with T3$t1234!
        And click Login button
        Then I should see I'm logged in as test@foo.bar
