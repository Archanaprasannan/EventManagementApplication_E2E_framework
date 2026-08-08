from logs.logger_util import Logger
from pages.basepage import BasePage
from playwright.sync_api import expect

class BookingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logger = Logger.get_logger(self.__class__.__name__)
        self.customer_name=page.locator("#customerName")
        self.customer_email=page.locator("#customer-email")
        self.customer_phone=page.locator("#phone")
        self.confirm_booking_button=page.locator("#confirm-booking")
        self.confirm_booking_message=page.locator("//div[@class='text-center py-6']//h3")
        self.button=page.locator("#helllo")
        

    def do_booking(self,name,email,phone):
        try:
            self.logger.info("Doing booking with name: %s, email: %s, phone: %s", name, email, phone)
            self.enter_text(self.customer_name,name)
            self.enter_text(self.customer_email,email)
            self.enter_text(self.customer_phone,phone)
            self.click(self.confirm_booking_button)
            self.logger.info("Booking successful")
            return HomePage(self.page)
        except Exception as e:
            self.logger.error("Booking failed")
            raise e    
        

    def get_confirm_booking_message(self):
        self.logger.info("Getting confirm booking message")
        return self.get_text(self.confirm_booking_message)

    def is_confirm_booking_message_visible(self):
        self.logger.info("Checking if confirm booking message is visible")
        return self.is_visible(self.confirm_booking_message)