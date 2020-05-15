Feature: Registration
    As a anonymous user
    I want to test if registration works

    Scenario: Registraton with email
        Given I see index page
        When I click on "Register" menu item
        And fill email input with test@foo.bar
        And fill password1 input with s3C4etPa$s!
        And fill password2 input with s3C4etPa$s!
        And click Register button
        Then inactive user test@foo.bar should be created
        And confirmation link should be sent
