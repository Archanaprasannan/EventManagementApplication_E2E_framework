import allure

from pytest_bdd import given, when, then, parsers

from constants.appconstants import AppConstants
from utils.config_reader_util import ConfigReader


@given("the user is on the login page")
@allure.step("Verify the user is on the login page")
def user_on_login_page(login_page):
    assert login_page.get_login_page_url() == AppConstants.EXPECTED_LOGIN_PAGE_URL


@when(
    parsers.parse('the user logs in with "{email}" and "{password}"')
)
@allure.step("Log in with the provided credentials")
def user_logs_in_with_credentials(login_page, email, password):
    login_page.do_login(email, password)


@then(
    parsers.parse(
        'the "{validation_type}" validation message should be displayed'
    )
)
@allure.step("Verify the expected validation message")
def validation_message_should_be_displayed(login_page, validation_type):

    if validation_type == "invalid login":
        assert (
            login_page.get_invalid_login_error_message()
            == AppConstants.INVALID_LOGIN_ERROR_MESSAGE
        )

    elif validation_type == "blank email":
        assert (
            login_page.get_blank_email_error_message()
            == AppConstants.INVALID_BLANK_EMAIL_ERROR_MESSAGE
        )

    elif validation_type == "blank password":
        assert (
            login_page.get_blank_password_error_message()
            == AppConstants.INVALID_BLANK_PASSWORD_ERROR_MESSAGE
        )