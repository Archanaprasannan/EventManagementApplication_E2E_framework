import allure
import pytest
from utils.config_reader_util import ConfigReader
from constants.appconstants import AppConstants


@pytest.mark.regression
class TestBookingFlow:
    @allure.feature("Booking")
    @allure.story("Booking Flow")
    @allure.title("TC_009 - Verify booking flow")
    def test_booking_flow(self,login_page,random_data):
        #login
        with allure.step("Login with valid credentials"):
            home_page= login_page.do_login(ConfigReader.get_email(), ConfigReader.get_password())
        #browse events
        with allure.step("Navigate to Events page"):
            event_page= home_page.do_browse_events()
        with allure.step(f"Search for event: {AppConstants.EVENT_NAME}"):
            booking_page=event_page.do_event_search(AppConstants.EVENT_NAME)
        with allure.step("Generate booking details"):
            name=random_data.generate_random_name()
            email=random_data.generate_random_email()
            phone=random_data.generate_random_phone_number()
        with allure.step("Book the selected event"):
            actual_confirm_message= booking_page.do_booking(name,email,phone)
        #booking_confirmation
        with allure.step("Verify booking confirmation"):
            assert AppConstants.BOOKING_CONFIRMATION_MESSAGE in actual_confirm_message
        
        