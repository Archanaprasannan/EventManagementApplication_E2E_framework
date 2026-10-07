import allure
import pytest
from playwright.sync_api import expect

from constants.appconstants import AppConstants
from logs.logger_util import Logger

logger = Logger.get_logger(__name__)
pytest.mark.regression

class TestBookingPage:
    @allure.feature("Booking")
    @allure.story("Booking Page Title verification")
    @allure.title("TC_BOOKING_001 - Verify booking page title")
    def test_get_booking_page_title(self, booking_page):
        logger.info("Booking title test started")
        actual_title = booking_page.get_booking_page_title()
        assert actual_title == AppConstants.EXPECTED_BOOKING_PAGE_TITLE
        logger.info("Booking title test completed")

    @allure.feature("Booking")
    @allure.story("Booking Event Name verification")
    @allure.title("TC_BOOKING_002 - Verify event name on booking page")
    def test_event_name_in_booking_page(self, booking_page):
        logger.info("Booking event name test started")
        actual_event_name = booking_page.get_event_name()
        assert actual_event_name == AppConstants.BOOKING_EVENT_NAME
        logger.info("Booking event name test completed")

    @allure.feature("Booking")
    @allure.story("Booking Event verification")
    @allure.title("TC_BOOKING_003 - Verify booking an event")
    def test_book_event(self, booking_page,random_data):
        logger.info("Booking event test started")
        booking_page.do_booking(random_data.generate_random_name(), random_data.generate_random_email(),random_data.generate_random_phone_number())
        assert booking_page.get_confirm_booking_message()== AppConstants.CONFIRM_BOOKING_MESSAGE
        logger.info("Booking event test completed")
        logger.info("Booking details verification test started")
        booking_page.view_booking_details()

        expect(
            booking_page.cancel_booking_button
        ).to_be_visible(timeout=10000)
        logger.info("Booking page details test completed")

    def test_cancel_booking(self, booking_page,random_data):
        logger.info("Cancel booking test started")
        booking_page.do_booking(random_data.generate_random_name(), random_data.generate_random_email(),
                                random_data.generate_random_phone_number())
        assert booking_page.get_confirm_booking_message() == AppConstants.CONFIRM_BOOKING_MESSAGE
        logger.info("Booking event test completed")
        logger.info("Booking details verification test started")
        booking_page.view_booking_details()

        expect(
            booking_page.cancel_booking_button
        ).to_be_visible(timeout=10000)
        logger.info("Booking page details test completed")
        booking_page.cancel_booking()
        expect(booking_page.confirm_cancel_booking_message()).to_be_visible(timeout=30000)
        logger.info("Cancel booking test completed")