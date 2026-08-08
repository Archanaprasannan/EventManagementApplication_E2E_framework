

import allure
import pytest
from playwright.sync_api import Page, expect

from constants.appconstants import AppConstants

from utils.config_reader_util import ConfigReader
from utils.logger_util import Logger

logger = Logger.get_logger(__name__)
pytest.mark.regression
class TestLoginPage:
    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_001 - Verify login page title")
    def test_get_login_page_title(self, login_page):
        logger.info("Test_001 started")
        actual_title= login_page.get_login_page_title()
        assert actual_title == AppConstants.EXPECTED_LOGIN_PAGE_TITLE
        logger.info("Test_001 completed")

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_002 - Verify login page url")
    def test_get_login_page_url(self, login_page):
        logger.info("Test_002 started")
        actual_url=login_page.get_login_page_url()
        assert actual_url== AppConstants.EXPECTED_LOGIN_PAGE_URL
        logger.info("Test_002 completed")

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_003 - Verify email field exist")
    def test_email_field_exist(self, login_page):
        logger.info("Test_003 started")
        assert login_page.get_email_field_exist() is True
        logger.info("Test_003 completed")

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_004 - Verify password field exist")
    def test_password_field_exist(self, login_page):
        logger.info("Test_004 started")
        assert login_page.get_password_field_exist() is True
        logger.info("Test_004 completed")

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_005 - Verify login button exist")
    def test_login_button_exist(self, login_page):
        logger.info("Test_005 started")
        assert login_page.get_login_button_exist() is True
        logger.info("Test_005 completed")

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_006 - Verify register button exist")
    def test_register_button_exist(self, login_page):
        logger.info("Test_006 started")
        assert login_page.get_register_button_exist() is True
        logger.info("Test_006 completed")

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_007 - Verify login with invalid credentials")
    def test_login_with_invalid_credentials(self,login_page,random_data):
        logger.info("Test_007 started")
        login_page.do_login(random_data.generate_random_email(),random_data.generate_random_password())
        actual_error_message= login_page.get_invalid_login_error_message()
        assert actual_error_message == AppConstants.INVALID_LOGIN_ERROR_MESSAGE
        logger.info("Test_007 completed")

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_008 - Verify login with blank email")
    def test_login_with_blank_email(self, login_page, random_data):
        logger.info("Test_008 started")
        login_page.do_login("", random_data.generate_random_password())
        actual_error_message = login_page.get_blank_email_error_message()
        assert actual_error_message == AppConstants.INVALID_BLANK_EMAIL_ERROR_MESSAGE
        logger.info("Test_008 completed")

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_009 - Verify login with blank password")
    def test_login_with_blank_password(self, login_page, random_data):
        logger.info("Test_009 started")
        login_page.do_login(random_data.generate_random_email(), "")
        actual_error_message = login_page.get_blank_password_error_message()
        assert actual_error_message == AppConstants.INVALID_BLANK_PASSWORD_ERROR_MESSAGE    
        logger.info("Test_009 completed")

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_010 - Verify login with valid credentials")
    def test_do_valid_login(self,login_page):
        logger.info("Test_010 started")
        home_page=login_page.do_login(ConfigReader.get_email(),ConfigReader.get_password())
        logger.info("Test_010 completed")
        expect(home_page.page).to_have_url(AppConstants.EXPECTED_HOME_PAGE_URL)

    @allure.feature("Login")
    @allure.story("Login Page verification")
    @allure.title("TC_010 - Verify login using different test data")
    @pytest.mark.parametrize(
        "username, password, expected",
        [
            ("test123today@gmail.com", "Test@123", "success"),
            ("test56@gmail.com", "Test@57", "Invalid email or password"),
            ("", "Test@567", "Enter a valid email"),
            ("test567@gmail.com", "", "Password must be at least 6 characters")
        ]
    )
    def test_do_valid_login_using_multiple_data(self, login_page,username, password,expected):
        logger.info("Test_010 started")
        home_page = login_page.do_login(username,password)
        logger.info("Test_010 completed")
        if expected == "success":
            expect(home_page.page).to_have_url(AppConstants.EXPECTED_HOME_PAGE_URL)
        else:
            assert login_page.get_error_message() == expected