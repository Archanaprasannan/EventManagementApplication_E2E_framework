@smoke @regression
Feature: Homepage Logout  Functionality
Scenario: Logout from the homepage
    Given the user is logged in
    When the user clicks the logout button
    Then the user should be redirected to the login page