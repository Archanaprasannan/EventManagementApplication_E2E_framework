import allure
from pytest_bdd import given,when,then

from constants.appconstants import AppConstants
from utils.config_reader_util import ConfigReader

@allure.step("Verify the user is on the login page")
@given("the user is on the login page")
def user_on_login_page(login_page):
    assert login_page.get_login_page_url() == AppConstants.EXPECTED_LOGIN_PAGE_URL

@allure.step("Log in with valid credentials")
@when("the user logs in with valid credentials",target_fixture="home_page")
def user_logs_in_with_valid_credentials(login_page):
    return login_page.do_login(ConfigReader.get_email(),ConfigReader.get_password())

@allure.step("Verify the home page is displayed")
@then("the home page should be displayed")
def home_page_should_be_displayed(home_page):
    assert home_page.get_home_page_title()==AppConstants.EXPECTED_HOME_PAGE_TITLE

@allure.step("Log in with invalid credentials")
@when("the user logs in with invalid credentials")
def user_logs_in_with_invalid_credentials(login_page,random_data):
     login_page.do_login(random_data.generate_random_email(),random_data.generate_random_password())

@allure.step("Verify the invalid login error message is displayed")
@then("the invalid login error message should be displayed")
def invalid_login_error_message(login_page):
    assert login_page.get_invalid_login_error_message() == AppConstants.INVALID_LOGIN_ERROR_MESSAGE

@allure.step("Log in with a blank email")
@when("the user logs in with a blank email")
def user_logs_in_with_blank_email(login_page):
    login_page.do_login("", ConfigReader.get_password())

@allure.step("Verify the blank email validation message is displayed")
@then("the blank email validation message should be displayed")
def blank_email_validation_message(login_page):
    assert login_page.get_blank_email_error_message() == AppConstants.INVALID_BLANK_EMAIL_ERROR_MESSAGE

@allure.step("Log in with a blank password")
@when("the user logs in with a blank password")
def user_logs_in_with_blank_password(login_page):
    login_page.do_login(ConfigReader.get_email(), "")

@allure.step("Verify the blank password validation message is displayed")
@then("the blank password validation message should be displayed")
def blank_password_validation_message(login_page):
    assert login_page.get_blank_password_error_message()==AppConstants.INVALID_BLANK_PASSWORD_ERROR_MESSAGE