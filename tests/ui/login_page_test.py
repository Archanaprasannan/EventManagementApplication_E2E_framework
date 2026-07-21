import allure
import pytest
from playwright.sync_api import Page, expect

from constants.appconstants import AppConstants
from utils.config_reader_util import ConfigReader
pytest.mark.regression
class TestLoginPage:
    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_001 - Verify login page title")
    def test_get_login_page_title(self, login_page):
        actual_title= login_page.get_login_page_title()
        assert actual_title == AppConstants.EXPECTED_LOGIN_PAGE_TITLE

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_002 - Verify login page url")
    def test_get_login_page_url(self, login_page):
        actual_url=login_page.get_login_page_url()
        assert actual_url== AppConstants.EXPECTED_LOGIN_PAGE_URL

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_003 - Verify email field exist")
    def test_email_field_exist(self, login_page):
        assert login_page.get_email_field_exist() is True

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_004 - Verify password field exist")
    def test_password_field_exist(self, login_page):
        assert login_page.get_password_field_exist() is True

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_005 - Verify login button exist")
    def test_login_button_exist(self, login_page):
        assert login_page.get_login_button_exist() is True

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_006 - Verify register button exist")
    def test_register_button_exist(self, login_page):
        assert login_page.get_register_button_exist() is True

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_007 - Verify login with invalid credentials")
    def test_login_with_invalid_credentials(self,login_page,random_data):
        login_page.do_login(random_data.generate_random_email(),random_data.generate_random_password())
        actual_error_message= login_page.get_invalid_login_error_message()
        assert actual_error_message == AppConstants.INVALID_LOGIN_ERROR_MESSAGE

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_008 - Verify login with blank email")
    def test_login_with_blank_email(self, login_page, random_data):
        login_page.do_login("", random_data.generate_random_password())
        actual_error_message = login_page.get_blank_email_error_message()
        assert actual_error_message == AppConstants.INVALID_BLANK_EMAIL_ERROR_MESSAGE

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_009 - Verify login with blank password")
    def test_login_with_blank_password(self, login_page, random_data):
        login_page.do_login(random_data.generate_random_email(), "")
        actual_error_message = login_page.get_blank_password_error_message()
        assert actual_error_message == AppConstants.INVALID_BLANK_PASSWORD_ERROR_MESSAGE

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_010 - Verify login with valid credentials")
    def test_do_valid_login(self,login_page):
        home_page=login_page.do_login(ConfigReader.get_email(),ConfigReader.get_password())
        expect(home_page.page).to_have_url(AppConstants.EXPECTED_HOME_PAGE_URL)


