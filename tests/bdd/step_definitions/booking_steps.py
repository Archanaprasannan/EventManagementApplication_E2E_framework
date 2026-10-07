import allure
from playwright.sync_api import expect
from pytest_bdd import given, when, then

from constants.appconstants import AppConstants

@allure.step("Verify the user is on the booking page")
@given("the user is on the booking page for an event")
def user_is_on_booking_page(booking_page):
    assert booking_page.get_booking_page_title() == AppConstants.EXPECTED_BOOKING_PAGE_TITLE

@allure.step("Enter valid customer details")
@when("the user enters valid customer details")
def user_enters_valid_customer_details(booking_page, random_data):
    booking_page.enter_text(
        booking_page.customer_name, random_data.generate_random_name()
    )
    booking_page.enter_text(
        booking_page.customer_email, random_data.generate_random_email()
    )
    booking_page.enter_text(
        booking_page.customer_phone, random_data.generate_random_phone_number()
    )


@when("confirms the booking")
@allure.step("Confirm the booking")
def user_confirms_booking(booking_page):
    booking_page.click(booking_page.confirm_booking_button)

@allure.step("Verify booking confirmation")
@then("the booking should be confirmed")
def booking_is_confirmed(booking_page):
    assert booking_page.get_confirm_booking_message() == AppConstants.CONFIRM_BOOKING_MESSAGE

@allure.step("Create a successful event booking")
@given("the user has successfully booked an event")
def user_has_successfully_booked_event(booking_page, random_data):
    booking_page.do_booking(
        random_data.generate_random_name(),
        random_data.generate_random_email(),
        random_data.generate_random_phone_number(),
    )
    assert booking_page.get_confirm_booking_message() == AppConstants.CONFIRM_BOOKING_MESSAGE

@allure.step("View booking details")
@when("the user views their booking details")
def user_views_booking_details(booking_page):
    booking_page.view_booking_details()

@allure.step("Verify booked event details are displayed")
@then("the booked event details should be displayed")
def booked_event_details_are_displayed(booking_page):
    expect(booking_page.cancel_booking_button).to_be_visible(timeout=10000)