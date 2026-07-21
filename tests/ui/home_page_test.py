import allure
import pytest
from playwright.sync_api import expect
from constants.appconstants import AppConstants

pytest.mark.regression
class TestHomePage:
    @allure.feature("Home")
    @allure.story("Home Page verification")
    @allure.title("TC_011 - Verify login with valid credentials")
    def test_home_page_title(self,home_page):
        actual_home_page_title= home_page.get_home_page_title()
        assert actual_home_page_title == AppConstants.EXPECTED_HOME_PAGE_TITLE

    @allure.feature("Home")
    @allure.story("Home Page verification")
    @allure.title("TC_012 - Verify home page url")
    def test_home_page_url(self,home_page):
        actual_home_page_url= home_page.get_home_page_url()
        assert actual_home_page_url == AppConstants.EXPECTED_HOME_PAGE_URL

    @allure.feature("Home")
    @allure.story("Home Page verification")
    @allure.title("TC_013 - Verify user profile icon visible")
    def test_user_profile_icon_visible(self,home_page):
        actual_user_profile_icon_visibility= home_page.is_user_profile_icon_visible()
        assert actual_user_profile_icon_visibility == True

    @allure.feature("Home")
    @allure.story("Home Page verification")
    @allure.title("TC_014 - Verify logout button visible")
    def test_logout_button_visible(self,home_page):
        actual_logout_button_visibility= home_page.is_logout_button_visible()
        assert actual_logout_button_visibility == True

    @allure.feature("Home")
    @allure.story("Home Page verification")
    @allure.title("TC_015 - Verify navigation menu visible")
    def test_navigation_menu_visible(self,home_page):
        actual_navigation_menu_visibility= home_page.is_navigation_menu_visible()
        assert actual_navigation_menu_visibility == True

    @allure.feature("Home")
    @allure.story("Home Page verification")
    @allure.title("TC_016 - Verify browse events button visible")
    def test_browse_events_visible(self,home_page):
        actual_browse_events_visibility= home_page.is_browse_events_button_visible()
        assert actual_browse_events_visibility == True

    @allure.feature("Home")
    @allure.story("Home Page verification")
    @allure.title("TC_017 - Verify upcoming events section visible")
    def test_upcoming_events_section_visible(self,home_page):
        actual_upcoming_events_section_visibility= home_page.is_upcoming_events_section_visible()
        assert actual_upcoming_events_section_visibility ==True

    @allure.feature("Home")
    @allure.story("Home Page verification")
    @allure.title("TC_018 - Verify 'My Bookings' navigation link visible")
    def test_my_bookings_link_visible(self,home_page):
        actual_my_bookings_link_visibility = home_page.is_my_bookings_link_visible()
        assert actual_my_bookings_link_visibility == True


