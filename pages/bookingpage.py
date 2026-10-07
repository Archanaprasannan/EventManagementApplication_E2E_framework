from constants.appconstants import AppConstants
from logs.logger_util import Logger
from pages.basepage import BasePage
from playwright.sync_api import expect


from constants.appconstants import AppConstants
from logs.logger_util import Logger

logger = Logger.get_logger(__name__)

class BookingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logger = Logger.get_logger(self.__class__.__name__)
        self.customer_name=page.get_by_placeholder("Your full name")
        self.customer_email=page.locator("#customer-email")
        self.customer_phone=page.locator("#phone")
        self.confirm_booking_button=page.locator("#confirm-booking")
        self.confirm_booking_message=page.get_by_role("heading").filter(has_text="Booking Confirmed! 🎉")
        self.button=page.locator("#helllo")
        self.event_name=page.get_by_role("heading", name=AppConstants.BOOKING_EVENT_NAME)
        self.view_booking_button=page.get_by_role("button", name="View My Bookings")
        self.cancel_booking_button = page.get_by_role("button", name="Cancel Booking").first
        # self.customer_name=page.get_by_label("Full Name")
        #self.confirm_booking_button = page.get_by_role("button", name="Confirm Booking")
        self.confirm_cancel_booking_button = page.get_by_role("button",name="Yes, cancel it")
        self.cancel_message=page.get_by_text("Booking cancelled successfully!!")

    def wait_for_page_load(self):
        self.customer_name.wait_for(state="visible", timeout=30000)

    def get_booking_page_title(self):
        self.logger.info("Getting booking page title")
        return self.get_page_title()


    def get_booking_page_url(self):
        self.logger.info("Getting booking page url")
        return self.get_page_url()

    def get_event_name(self):
        self.logger.info("Getting event name")
        expect(self.event_name).to_be_visible(timeout=10000)
        return self.get_text(self.event_name)

    def do_booking(self,name,email,phone):
        try:
            self.logger.info("Doing booking with name: %s, email: %s, phone: %s", name, email, phone)
            self.enter_text(self.customer_name,name)
            self.enter_text(self.customer_email,email)
            self.enter_text(self.customer_phone,phone)
            self.click(self.confirm_booking_button)
            self.logger.info("Booking successful")
        except Exception as e:
            self.logger.error("Booking failed")
            raise e    
        

    def get_confirm_booking_message(self):
        self.logger.info("Getting confirm booking message")
        return self.get_text(self.confirm_booking_message)

    def view_booking_details(self):
        try:
            self.logger.info("Viewing booking details")
            self.click(self.view_booking_button)
            self.logger.info("Navigated to booking details")
        except Exception as e:
            self.logger.error("View booking details failed")
            raise e
    # def is_cancel_booking_button_visible(self):
    #     return self.cancel_booking_button

    def is_confirm_booking_message_visible(self):
        self.logger.info("Checking if confirm booking message is visible")
        return self.is_visible(self.confirm_booking_message)

    def cancel_booking(self):
        try:
            self.logger.info("Cancelling booking")
            self.click(self.cancel_booking_button)

            self.click(self.confirm_cancel_booking_button)
            self.logger.info("Booking cancelled")
        except Exception as e:
            self.logger.error("Cancel booking failed")
            raise e

    def confirm_cancel_booking_message(self):
        self.logger.info("Getting confirm cancel booking message")
        return self.get_text(self.cancel_message)