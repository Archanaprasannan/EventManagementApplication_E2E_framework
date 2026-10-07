
@smoke @regression
Feature: Event Search Functionality
Scenario: Search for an event by its full name
    Given the user is on the events page
    When the user searches for a valid event
    Then the matching event should be displayed

Scenario: Search for an event using a partial name
    Given the user is on the events page
    When the user searches using a partial event name
    Then the matching event should be displayed

Scenario: Search for an invalid event
    Given the user is on the events page
    When the user searches for an invalid event
    Then no matching event should be displayed


Scenario: Filter events by category
    Given the user is on the events page
    When the user selects an event category
    Then events belonging to that category should be displayed