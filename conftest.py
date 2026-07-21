# contain Python code,fixtures and hooks for pytest
from datetime import datetime

import allure
import pytest
from playwright.sync_api import Playwright

from api.auth_api import AuthAPI
from api.bookings_api import BookingsAPI
from api.events_api import  EventsAPI
from constants.appconstants import AppConstants
from pages.loginpage import LoginPage
from utils.config_reader_util import ConfigReader
from utils.randomdata_util import Randomdata


# create fixture for setup and tear down of the browser
@pytest.fixture(scope="function")
def setup_and_teardown(playwright: Playwright):
    browser = getattr(playwright, ConfigReader.get_browser()).launch(headless=ConfigReader.get_headless())
    # viewport={"width": 1920, "height": 1080
    context = browser.new_context()
    page = context.new_page()
    page.goto(ConfigReader.get_ui_url())
    yield page
    context.close()
    browser.close()


@pytest.fixture
def login_page(setup_and_teardown):
    return LoginPage(setup_and_teardown)


@pytest.fixture
def home_page(login_page):
    return login_page.do_login(ConfigReader.get_email(), ConfigReader.get_password())

@pytest.fixture
def event_page(home_page):
    return home_page.do_browse_events()

@pytest.fixture
def admin_page(event_page):
    return event_page.add_event()

@pytest.fixture()
def random_data():
    return Randomdata()

@pytest.fixture
def event_data(random_data):

    return {
        "title": random_data.generate_random_event_title(),
        "description": AppConstants.DESCRIPTION,
        "category": AppConstants.CATEGORY,
        "city": AppConstants.CITY,
        "venue": AppConstants.VENUE,
        "price": AppConstants.PRICE,
        "seats": AppConstants.TOTAL_SEAT,

    }

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.failed:

        page = item.funcargs.get("setup_and_teardown")

        if page:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            screenshot_path = (
                f"screenshots/{item.name}_{timestamp}.png"
            )

            page.screenshot(path=screenshot_path)

            allure.attach.file(
                screenshot_path,
                name=item.name,
                attachment_type=allure.attachment_type.PNG)
            # allure.attach.file(
            #     "logs/test.log",
            #     name="Execution Log",
            #     attachment_type=allure.attachment_type.TEXT
            # )
            allure.attach(
                page.url,
                name="Current URL",
                attachment_type=allure.attachment_type.TEXT
            )


# since the scope is function, it will create new context for each test case and close it after the test case execution
@pytest.fixture(scope="function")
def api_context(playwright: Playwright):
    context = playwright.request.new_context(base_url=ConfigReader.get_api_url())
    yield context
    context.dispose()
    #closes the APIRequestContext.

#Otherwise, if you run hundreds of tests, Playwright
#keeps those contexts alive longer than necessary, which can waste memory and resources.

@pytest.fixture(scope='function')
def auth_api(api_context):
    return AuthAPI(api_context)

@pytest.fixture()
def auth_token(auth_api):
    response= auth_api.api_login(AppConstants.LOGIN_ENDPOINT,ConfigReader.get_email(),ConfigReader.get_password())
    return response.json()["token"]

@pytest.fixture()
def events_api(api_context):
    return EventsAPI(api_context)
@pytest.fixture()
def bookings_api(api_context):
    return BookingsAPI(api_context)

@pytest.fixture()
def get_booking_details(bookings_api,auth_token):
    all_booking = bookings_api.get_all_bookings(auth_token)
    assert all_booking.status==200
    all_booking_data = all_booking.json()["data"]
    first_booking_data = all_booking_data[0]
    return first_booking_data
