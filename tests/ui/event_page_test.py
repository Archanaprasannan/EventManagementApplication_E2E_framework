# enable play button for test functions
import allure

from constants.appconstants import AppConstants
from playwright.sync_api import expect


class TestEventPage:
    @allure.feature("Event Page")
    @allure.story("Event Page verification")
    @allure.title("TC_019 - Verify event page title")
    def test_event_page_title(self,event_page):
        actual_event_page_title= event_page.get_event_page_title()
        assert actual_event_page_title == AppConstants.EXPECTED_EVENT_PAGE_TITLE

    @allure.feature("Event Page")
    @allure.story("Event Page verification")
    @allure.title("TC_020 - Verify event page url")
    def test_event_page_url(self,event_page):
        actual_event_page_url= event_page.get_event_page_url()
        assert actual_event_page_url == AppConstants.EXPECTED_EVENT_PAGE_URL
        
    @allure.feature("Event Page")
    @allure.story("Event Page verification")
    @allure.title("TC_021 - Verify event page search with valid event")
    def test_search_valid_event(self,event_page):
        event_page.do_event_search(AppConstants.FULL_EVENT_NAME)
        actual_event_page_search_result= event_page.get_event_search_result(AppConstants.FULL_EVENT_NAME)
        expect(actual_event_page_search_result).to_be_visible()

    @allure.feature("Event Page")
    @allure.story("Event Page verification")
    @allure.title("TC_022 - Verify event page search with partial event name")
    def test_search_partial_event_name(self,event_page):
        event_page.do_event_search(AppConstants.PARTIAL_EVENT_NAME)
        actual_event_page_search_result= event_page.get_event_search_result(AppConstants.FULL_EVENT_NAME)
        expect(actual_event_page_search_result).to_be_visible()

    @allure.feature("Event Page")
    @allure.story("Event Page verification")
    @allure.title("TC_023 - Verify event page search with invalid")
    def test_search_special_characters(self,event_page):
        event_page.do_event_search(AppConstants.INVALID_EVENT_NAME)
        actual_event_page_search_result= event_page.get_event_search_result(AppConstants.INVALID_EVENT_NAME)
        assert actual_event_page_search_result.count() == 0

    @allure.feature("Event Page")
    @allure.story("Event Page verification")
    @allure.title("TC_024 - Verify event page search by category dropdown")
    def test_search_event_by_category(self,event_page):
       event_page.select_category(AppConstants.DROPDOWN_CATEGORY_VALUE)
       actual_event_page_search_result= event_page.get_events_by_category(AppConstants.DROPDOWN_CATEGORY_VALUE)
       expect(actual_event_page_search_result.first).to_be_visible()
       