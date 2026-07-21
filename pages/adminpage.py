from playwright.sync_api import Page,expect

from constants.appconstants import AppConstants
from pages.basepage import BasePage
from utils.date_and_time import DateAndTime


class AdminPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.event_title=page.locator("#event-title-input")
        self.event_description=page.get_by_placeholder("Describe the event…")
        self.category=page.locator("#category")
        self.city=page.locator("#city")
        self.venue=page.locator("#venue")
        self.event_date_and_time=page.locator("//input[@id='event-date-&-time']")
        self.price=page.locator("//input[@id='price-($)']")
        self.total_seat=page.locator("#total-seats")
        self.add_event_button=page.locator("//button[@type='submit']")
        #this will work only when the table contains this particular class and has tbody in it
        # self.result_table=page.locator("//table[@class='w-full text-sm']//tbody//tr")
        #this is a stable locator
        self.result_table = page.locator("table tbody tr")
        self.update_button=page.locator("//button[@type='submit']")


    def add_event(self, title, description, category, city, venue, price, seats):
        self.enter_text(self.event_title,title)
        self.enter_text(self.event_description,description)
        self.select_dropdown_value_by_value(self.category,category)
        self.enter_text(self.city,city)
        self.enter_text(self.venue,venue)
        future_date = DateAndTime.get_future_datetime(days=15)
        print("Expected:", future_date.strftime("%Y-%m-%dT%H:%M"))
        self.enter_datetime(self.event_date_and_time, future_date)
        print("Input value:", self.event_date_and_time.input_value())
        #self.enter_datetime(self.event_date_and_time, DateAndTime.get_future_datetime(days=15))
        self.enter_text(self.price,price)
        self.enter_text(self.total_seat,seats)
        self.click(self.add_event_button)
        # wait for newly created event
        expect(self.result_table.filter(has_text=title)).to_be_visible(timeout=10000)


    def get_event_row(self, event_title):
        row = self.result_table.filter(
            has_text=event_title
        )

        expect(row).to_be_visible(timeout=10000)

        return row


    # def get_event_row(self):
    #     return self.result_table.filter(has_text=AppConstants.TITLE)

    def get_event_title_locator(self, row):
        return row.locator("td").nth(0)

    def get_event_title_text(self, row):
        return self.get_event_title_locator(row).text_content().strip()

    def get_event_category(self, row):
        return row.locator("td").nth(1)

    def get_event_city(self, row):
        return row.locator("td").nth(2)

    def get_event_date_text(self, row):
        return row.locator("td").nth(3).text_content().strip()

    def get_event_price_text(self, row):
        price= row.locator("td").nth(4).text_content()
        price=price.replace("$", "").replace(",", "")
        print("price is", price)
        return price
    def get_event_price_locator(self, row):
        return row.locator("td").nth(4)

    def get_event_total_seats(self, row):
        seats= row.locator("td").nth(5).text_content().split("/")[1]
        return seats

    def edit_event(self,row,new_title,new_price):
        edit_event_button=row.get_by_test_id("edit-event-btn")
        self.click(edit_event_button)
        self.enter_text(self.event_title,new_title)
        self.enter_text(self.price,new_price)
        self.click(self.update_button)
       # print(self.result_table.all_text_contents())
        self.wait_for_element(self.result_table.filter(has_text=new_title))

