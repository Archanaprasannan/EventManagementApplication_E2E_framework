from pages.basepage import BasePage
from pages.homepage import HomePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_input = page.get_by_role("textbox", name="Email")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button",name="Sign In")
        self.register_button = page.get_by_role("link", name="Register")
        self.invalid_login_error_message=page.locator("p").filter(has_text="Invalid email or password")
        self.blank_email_error_message=page.get_by_text("Enter a valid email")
        self.blank_password_error_message=page.get_by_text("Password must be at least 6 characters")

    def get_login_page_url(self):
        return self.get_page_url()

    def get_login_page_title(self):
        return self.get_page_title()

    def get_register_button_exist(self):
        return self.is_visible(self.register_button)

    def get_login_button_exist(self):
        return self.is_visible(self.login_button)

    def get_email_field_exist(self):
        return self.is_visible(self.email_input)

    def get_password_field_exist(self):
        return self.is_visible(self.password_input)

    def get_invalid_login_error_message(self):
        return self.get_text(self.invalid_login_error_message)

    def get_blank_email_error_message(self):
        return self.get_text(self.blank_email_error_message)

    def get_blank_password_error_message(self):
        return self.get_text(self.blank_password_error_message)

    def do_login(self, email, password):
        self.enter_text(self.email_input, email)
        self.enter_text(self.password_input, password)
        self.click(self.login_button)
        #self.page.wait_for_url("https://eventhub.rahulshettyacademy.com/")

        return HomePage(self.page)