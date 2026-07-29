import time
import pytest
from playwright.sync_api import expect
from conftest import admin_page
from constants.appconstants import AppConstants
from pages.adminpage import AdminPage
from utils.date_and_time import DateAndTime


class TestAdminPage:
    @allure.feature("Admin Page")
    @allure.story("Admin Page verification")
    @allure.title("TC_025 - Verify admin page title")
    def test_admin_page_title(self, admin_page):
        actual_title = admin_page.get_admin_page_title()
        assert actual_title == AppConstants.EXPECTED_ADMIN_PAGE_TITLE

    @allure.feature("Admin Page")
    @allure.story("Admin Page verification")
    @allure.title("TC_026 - Verify admin page url")
    def test_admin_page_url(self, admin_page):
        actual_url = admin_page.get_admin_page_url()
        assert actual_url == AppConstants.EXPECTED_ADMIN_PAGE_URL

    @allure.feature("Admin Page")
    @allure.story("Admin Page verification")
    @allure.title("TC_027 - Verify admin logout button visible")
    def test_admin_logout_button_visible(self, admin_page):
        actual_logout_button_visibility = admin_page.is_admin_logout_button_visible()
        assert actual_logout_button_visibility == True

    @allure.feature("Admin Page")
    @allure.story("Admin Page verification")
    @allure.title("TC_028 - Verify admin add event button visible")
    def test_admin_add_event_button_visible(self, admin_page):
        actual_add_event_button_visibility = admin_page.is_admin_add_event_button_visible()
        assert actual_add_event_button_visibility == True

    @allure.feature("Admin Page")
    @allure.story("Admin Page verification")
    @allure.title("TC_029 - Verify admin edit event button visible")
    def test_admin_edit_event_button_visible(self, admin_page):
        actual_edit_event_button_visibility = admin_page.is_admin_edit_event_button_visible()
        assert actual_edit_event_button_visibility == True

    @allure.feature("Admin Page")
    @allure.story("Admin Page verification")
    @allure.title("TC_030 - Verify admin delete event button visible")
    def test_admin_delete_event_button_visible(self, admin_page):
        actual_delete_event_button_visibility = admin_page.is_admin_delete_event_button_visible()
        assert actual_delete_event_button_visibility == True

    @allure.feature("Admin Page")
    @allure.story("Admin Page verification")
    @allure.title("TC_031 - Verify add event")
    def test_add_event(self, admin_page, event_data):
        admin_page.add_event(
            title=event_data["title"],
            description=event_data["description"],
            category=event_data["category"],
            city=event_data["city"],
            venue=event_data["venue"],
            price=event_data["price"],
            seats=event_data["seats"]
        )
        event_row= admin_page.get_event_row(event_data["title"])
        expect(event_row).to_be_visible()
        expect(admin_page.get_event_title_locator(event_row)).to_have_text(event_data["title"])
        expect(admin_page.get_event_category(event_row)).to_have_text(event_data["category"])
        expect(admin_page.get_event_city(event_row)).to_have_text(event_data["city"])

        future = DateAndTime.get_future_datetime(days=15)
        expected_date = f"{future.day} {future.strftime('%b %Y')}"
        assert admin_page.get_event_date_text(event_row) == expected_date

        actual_price = admin_page.get_event_price_text(event_row)
        assert actual_price == event_data["price"]

        actual_seats = admin_page.get_event_total_seats(event_row)
        assert actual_seats== event_data["seats"]

    @allure.feature("Admin Page")
    @allure.story("Admin Page verification")
    @allure.title("TC_032 - Verify edit event")
    def test_edit_event(self, admin_page, event_data):
        # Create event first
        admin_page.add_event(title=event_data["title"], description=event_data["description"],
                             category=event_data["category"],
                             city=event_data["city"], venue=event_data["venue"], price=event_data["price"],
                             seats=event_data["seats"])

        # Find created event
        original_row = admin_page.get_event_row(event_data["title"])
        expect(original_row).to_be_visible()
        # Edit
        new_title = f"Edited {event_data['title']}"
        admin_page.edit_event(original_row,new_title ,
                              new_price=AppConstants.EDITED_PRICE)

        # Verify
        edited_row = admin_page.get_event_row(new_title)
        expect(edited_row).to_be_visible()
        # Use expect() for elements(buttons, labels, messages, table cells before processing).
        # Use assert for data(parsed text, numbers, dates, API responses, calculated values).
        actual_title= admin_page.get_event_title_text(edited_row)
        assert actual_title==new_title
        assert admin_page.get_event_price_text(edited_row)==AppConstants.EDITED_PRICE

    @allure.feature("Admin Page")
    @allure.story("Admin Page verification")
    @allure.title("TC_033 - Verify delete event")
    def test_delete_event(self, admin_page, event_data):
        # Create event first
        admin_page.add_event(title=event_data["title"], description=event_data["description"],
                             category=event_data["category"],
                             city=event_data["city"], venue=event_data["venue"], price=event_data["price"],
                             seats=event_data["seats"])

        # Find created event
        original_row = admin_page.get_event_row(event_data["title"])
        expect(original_row).to_be_visible()
        # Delete
        admin_page.delete_event(original_row)

        # Verify
        event_row=admin_page.get_event_row(event_data["title"])
        expect(event_row).not_to_be_visible()


