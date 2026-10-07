import allure
from pytest_bdd import given,when,then

from constants.appconstants import AppConstants

@allure.step("Verify the user is logged in")
@given("the user is logged in")
def given_user_logged_in(home_page):
    pass

@allure.step("Click the logout button")
@when("the user clicks the logout button")
def when_user_clicks_logout_button(home_page):
    home_page.do_logout()

@allure.step("Verify the user is redirected to the login page")
@then("the user should be redirected to the login page")
def then_user_redirected_to_login_page(login_page):
    assert login_page.get_login_page_title() == AppConstants.EXPECTED_LOGIN_PAGE_TITLE

