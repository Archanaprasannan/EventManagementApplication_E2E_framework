
@smoke @regression
Feature: Event Booking

  Scenario: Successfully book an event with valid customer details
    Given the user is on the booking page for an event
    When the user enters valid customer details
    And confirms the booking
    Then the booking should be confirmed


  Scenario: Verify booked event details
    Given the user has successfully booked an event
    When the user views their booking details
    Then the booked event details should be displayed