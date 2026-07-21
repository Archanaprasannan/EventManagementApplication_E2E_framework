from pages.adminpage import AdminPage
from pages.basepage import BasePage
from constants.appconstants import AppConstants
from playwright.sync_api import expect
from pages.bookingpage import BookingPage


class EventPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.search_event_text_area=page.get_by_placeholder("Search events, venues…")
        self.category_dropdown=page.get_by_role("combobox").first
        self.category_dropdown.wait_for(state="visible")
        self.search_element_by_category_result=page.get_by_text("Concert")
        self.add_event_button=page.locator("//button[@type='button']")
        
    def get_event_page_title(self):
        return self.get_page_title()

    def get_event_page_url(self):
        return self.get_page_url() 
        

    def do_event_search(self,event_name):
        self.enter_text(self.search_event_text_area,event_name)
        

    def get_event_search_result(self,event_name):
        self.event_result=self.page.locator("[data-testid='event-card']").filter(has_text=event_name)
        return self.event_result   

    def click_book_now(self):
        self.book_event_button = self.event_result.get_by_test_id("book-now-btn")
        self.click(self.book_event_button)
        self.page.wait_for_url("**/events/*")
        return BookingPage(self.page)

    def select_category(self,category):
        # options = self.category_dropdown.locator("option")
        #
        # count = options.count()
        #
        # for i in range(count):
        #     print(
        #         options.nth(i).text_content(),
        #         options.nth(i).get_attribute("value")
        #     )
        self.select_dropdown_value_by_value(self.category_dropdown,category)

    def get_events_by_category(self, category):
        #It returns a Locator.
        return self.page.locator("[data-testid='event-card']").filter(has_text=category)
        
    def add_event(self):
        self.click(self.add_event_button)
        return AdminPage(self.page)







    