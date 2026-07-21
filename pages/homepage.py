from pages.basepage import BasePage
from playwright.sync_api import expect
from pages.eventpage import EventPage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.user_profile=page.locator("#user-email-display")
        self.user_profile.wait_for(state='visible',timeout=10000)
        self.logout_button=page.locator("#logout-btn")
        self.navigation_menu=page.locator("//div[@class='hidden md:flex items-center gap-1']")
        self.browse_events_button=page.locator("//a[text()='Browse Events']")
        self.upcoming_events_section=page.locator("#event-card")
        self.my_bookings_link=page.get_by_role("button", name="My Bookings")

    def get_home_page_url(self):
        return self.get_page_url()

    def get_home_page_title(self):
        return self.get_page_title()

    def is_user_profile_icon_visible(self):
        return self.is_visible(self.user_profile)

    def is_logout_button_visible(self):
        return self.is_visible(self.logout_button)

    def is_navigation_menu_visible(self):
        return self.is_visible(self.navigation_menu)

    def is_browse_events_button_visible(self):
        return self.is_visible(self.browse_events_button)

    def is_upcoming_events_section_visible(self):
        expect(self.upcoming_events_section.first).to_be_visible(timeout=5000)
        return self.upcoming_events_section.first.is_visible()

    def is_my_bookings_link_visible(self):
        return self.is_visible(self.my_bookings_link)

    def do_browse_events(self):
        self.click(self.browse_events_button)
        return EventPage(self.page)
    
    


    
    



    