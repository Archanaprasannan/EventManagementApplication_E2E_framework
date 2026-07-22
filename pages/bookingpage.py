from pages.basepage import BasePage
from playwright.sync_api import expect

class BookingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.customer_name=page.locator("#customerName")
        self.customer_email=page.locator("#customer-email")
        self.customer_phone=page.locator("#phone")
        self.confirm_booking_button=page.locator("#confirm-booking")
        self.confirm_booking_message=page.locator("//div[@class='text-center py-6']//h3")
        self.button=page.locator("#helllo")
        

    def do_booking(self,name,email,phone):
        self.enter_text(self.customer_name,name)
        self.enter_text(self.customer_email,email)
        self.enter_text(self.customer_phone,phone)
        self.click(self.confirm_booking_button)
        expect(self.confirm_booking_message).to_be_visible()
        return self.confirm_booking_message.text_content()