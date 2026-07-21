from datetime import datetime
class BasePage:

    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, locator):
        locator.wait_for(state="visible")
        locator.click()

    def enter_text(self, locator, value):
        locator.fill(value)

    def enter_datetime(self, locator, dt: datetime):
        locator.fill(dt.strftime("%Y-%m-%dT%H:%M"))

    def get_text(self, locator):
        return  locator.text_content()

    def is_visible(self, locator):
        return locator.is_visible()

    def wait_for_element(self, locator):
        locator.wait_for(state="visible")
    def get_page_url(self):
        return self.page.url
    def get_page_title(self):
        return self.page.title()
    def get_element_count(self,locator):
        return locator.count()

    #dropdown methods
    #In Playwright Python, the first positional argument of select_option() maps to the value attribute of the HTML <option> tag (e.g. <option value="...">), not the visual label.
    #To select by the text label, it must be explicitly passed as a keyword argument: select_option(label=label).
    def select_dropdown_value_by_index(self,locator,index):
        locator.select_option(index=index)
    def select_dropdown_value_by_label(self,locator,label):
        locator.select_option(label=label)
    def select_dropdown_value_by_value(self,locator,value):
        locator.select_option(value=value)