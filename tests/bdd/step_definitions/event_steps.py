import allure
from playwright.sync_api import expect
from pytest_bdd import given,when,then

from constants.appconstants import AppConstants

@allure.step("Verify the user is on the events page")
@given("the user is on the events page")
def user_is_on_events_page(event_page):
    assert event_page.get_event_page_title() == AppConstants.EXPECTED_EVENT_PAGE_TITLE

@allure.step("Search for a valid event")
@when("the user searches for a valid event")
def user_searches_for_valid_event(event_page):
    event_page.do_event_search(AppConstants.FULL_EVENT_NAME)

@allure.step("Verify the matching event is displayed")
@then("the matching event should be displayed")
def matching_event_is_displayed(event_page):
   result= event_page.get_event_search_result(AppConstants.FULL_EVENT_NAME)
   expect(result).to_be_visible()

@allure.step("Search using a partial event name")
@when("the user searches using a partial event name")
def user_searches_using_partial_event_name(event_page):
    event_page.do_event_search(AppConstants.PARTIAL_EVENT_NAME)

@allure.step("Search for an invalid event")
@when("the user searches for an invalid event")
def user_searches_for_invalid_event(event_page):
    event_page.do_event_search(AppConstants.INVALID_EVENT_NAME)

@allure.step("Verify no matching event is displayed")
@then("no matching event should be displayed")
def no_matching_event_should_be_displayed(event_page):
    result = event_page.get_event_search_result(
        AppConstants.INVALID_EVENT_NAME
    )
    assert result.count() == 0

@allure.step("Select an event category")
@when("the user selects an event category")
def user_selects_event_category(event_page):
    event_page.select_category(
        AppConstants.DROPDOWN_CATEGORY_VALUE
    )

@allure.step("Verify events belonging to the selected category are displayed")
@then("events belonging to that category should be displayed")
def events_belonging_to_category_should_be_displayed(event_page):
    result = event_page.get_events_by_category(
        AppConstants.DROPDOWN_CATEGORY_VALUE
    )
    expect(result.first).to_be_visible()