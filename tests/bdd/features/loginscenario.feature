Feature: Login Validation

  Scenario Outline: Login validation with different credentials

    Given the user is on the login page
    When the user logs in with "<email>" and "<password>"
    Then the "<expected_message>" should be displayed

    Examples:
      | email              | password      | expected_message |
      | invalid@test.com   | wrongPassword | Invalid login    |
      |                    | validPassword  | Blank email      |
      | valid@test.com     |               | Blank password   |