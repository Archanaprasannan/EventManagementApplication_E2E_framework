from logs.logger_util import Logger

from pages.basepage import BasePage
from constants.appconstants import AppConstants
from playwright.sync_api import expect



class EventPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.logger = Logger.get_logger(self.__class__.__name__)
        self.search_event_text_area=page.get_by_placeholder("Search events, venues…")
        self.category_dropdown=page.get_by_role("combobox").first
        self.category_dropdown.wait_for(state="visible")
        self.search_element_by_category_result=page.get_by_text("Concert")
        self.add_event_button=page.locator("//button[@type='button']")
        self.event_result=None
        self.book_event_button=None

        
    def get_event_page_title(self):
        self.logger.info("Getting event page title")
        return self.get_page_title()

    def get_event_page_url(self):
        self.logger.info("Getting event page url")
        return self.get_page_url() 
        

    def do_event_search(self,event_name):
        self.logger.info("Doing event search with event name: %s", event_name)
        self.enter_text(self.search_event_text_area,event_name)
        

    def get_event_search_result(self,event_name):
        self.logger.info("Getting event search result with event name: %s", event_name)
        self.event_result=self.page.locator("[data-testid='event-card']").filter(has_text=event_name)
        return self.event_result   

    def click_book_now(self, event_name):
        self.logger.info("Clicking book now button")
        if event_name:
            self.do_event_search(event_name)
            event_card = self.get_event_search_result(event_name)
        else:
            event_card = self.page.locator("[data-testid='event-card']").first
        self.book_event_button = event_card.get_by_test_id("book-now-btn")
        self.click(self.book_event_button)
        #self.customer_name.wait_for(state="visible", timeout=30000)

        #self.page.wait_for_url("**/events/*",timeout=10000)
        self.logger.info("Navigated to booking page")
        from pages.bookingpage import BookingPage
        booking_page = BookingPage(self.page)
        booking_page.wait_for_page_load()
        return booking_page

    def select_category(self,category):
        self.logger.info("Selecting category: %s", category)
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
        self.logger.info("Getting events by category: %s", category)
        return self.page.locator("[data-testid='event-card']").filter(has_text=category)
        
    def add_event(self):
        try:
            self.logger.info("Adding event")
            self.click(self.add_event_button)
            self.logger.info("Navigated to admin page")
            from pages.adminpage import AdminPage
            return AdminPage(self.page)
        except Exception as e:
            self.logger.error("Add event failed")
            raise e







    