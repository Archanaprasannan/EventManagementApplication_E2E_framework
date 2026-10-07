Feature: User Login
@smoke @regression
Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user logs in with valid credentials
    Then the home page should be displayed
@smoke @regression
 Scenario: Login with invalid credentials
    Given the user is on the login page
    When the user logs in with invalid credentials
    Then the invalid login error message should be displayed

  Scenario: Login with blank email
    Given the user is on the login page
    When the user logs in with a blank email
    Then the blank email validation message should be displayed

  Scenario: Login with blank password
    Given the user is on the login page
    When the user logs in with a blank password
    Then the blank password validation message should be displayed