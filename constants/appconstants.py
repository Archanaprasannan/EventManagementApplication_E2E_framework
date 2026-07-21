
class AppConstants:
    # Application constants

    #login page
    EXPECTED_LOGIN_PAGE_URL = "https://eventhub.rahulshettyacademy.com/login"
    EXPECTED_LOGIN_PAGE_TITLE = "EventHub — Discover & Book Events"

    #home page
    EXPECTED_HOME_PAGE_URL="https://eventhub.rahulshettyacademy.com/"
    EXPECTED_HOME_PAGE_TITLE="EventHub — Discover & Book Events"

    #error messages
    INVALID_LOGIN_ERROR_MESSAGE="Invalid email or password"
    INVALID_BLANK_EMAIL_ERROR_MESSAGE="Enter a valid email"
    INVALID_BLANK_PASSWORD_ERROR_MESSAGE="Password must be at least 6 characters"

    #event page
    EXPECTED_EVENT_PAGE_TITLE="EventHub — Discover & Book Events"
    EXPECTED_EVENT_PAGE_URL="https://eventhub.rahulshettyacademy.com/events"
    FULL_EVENT_NAME="World Tech Summit"
    PARTIAL_EVENT_NAME="World Tech"
    INVALID_EVENT_NAME="Invalid Event"
    DROPDOWN_CATEGORY_VALUE="Concert"

    #admin page: create event
    DESCRIPTION="Art workshop for students"
    CATEGORY="Festival"
    CITY="Toronto"
    VENUE="123 Square,Markham"
    PRICE = "1500"  # Used for entering into the form
    TOTAL_SEAT="8"
    EDITED_EVENT_TITLE="New Title"
    EDITED_PRICE="1200"


    #booking confirmation message
    BOOKING_CONFIRMATION_MESSAGE="Booking Confirmed!"


    #API constants
    LOGIN_ENDPOINT="/api/auth/login"
    EVENT_ENDPOINTS="api/events"
    BOOKING_ENDPOINT="/api/bookings"
    MY_BOOKING_ENDPOINT="/api/bookings?page=1&limit=10"


    #End_to_end_scenarios
    