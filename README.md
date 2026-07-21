
# Playwright Python End-to-End Test Automation Framework

This repository contains a comprehensive **hybrid test automation framework** for E2E testing of the **EventHub** web application. It is built using **Python**, **Playwright**, and **Pytest**, implementing clean Page Object Models (POM) for UI tests and structured API clients for API testing.

---

## 📁 Project Directory Structure

```text
PlaywrightE2EFramework/
├── api/                   # API Object Model (AOM) wrapper classes
│   ├── auth_api.py        # Authentication endpoint methods
│   ├── base_api.py        # Base HTTP methods (GET, POST, PUT, DELETE, etc.)
│   ├── bookings_api.py    # Bookings endpoints management
│   └── events_api.py      # Events endpoints management
├── configs/               # Environment-specific configuration files
│   └── config_qa.ini      # QA Environment configuration variables
├── constants/             # Application-wide constants & expected static values
│   └── appconstants.py    # URL endpoints, titles, labels, error messages
├── logs/                  # Log outputs from test executions
│   └── logfile.log        # File-based logger outputs
├── pages/                 # Page Object Model (POM) classes for UI layers
│   ├── basepage.py        # Base Page wrapping Playwright browser actions
│   ├── bookingpage.py     # Booking Page actions and elements (skeleton)
│   ├── eventpage.py       # Event search/booking flow Page actions and elements
│   ├── homepage.py        # Homepage actions, elements, and assertions
│   ├── loginpage.py       # Login Page actions, validations, and forms
│   ├── mybookingpage.py   # Bookings listing Page (skeleton)
│   └── paymentpage.py     # Checkout/Payment Page (skeleton)
├── reports/               # Test execution reports and artifacts
│   ├── allure-results/    # Raw Allure test result JSON files
│   └── report.html        # Auto-generated Pytest HTML execution report
├── screenshots/           # Failed-test screenshots automatically captured during teardown
├── testdata/              # Test inputs externalized by file format
│   ├── csv/               # CSV test data files
│   ├── excel/             # Excel sheets (e.g. data-driven inputs)
│   └── json/              # JSON request payloads
├── tests/                 # Automated Test Cases directory
│   ├── api/               # API endpoint test suites
│   │   ├── bookings_api_test.py
│   │   ├── events_api_test.py
│   │   └── login_api_test.py
│   └── ui/                # UI interface end-to-end test suites
│       ├── event_page_test.py
│       ├── home_page_test.py
│       └── login_page_test.py
├── utils/                 # General-purpose utility and helper modules
│   ├── config_reader_util.py # Config ini file parser
│   ├── excel_util.py      # Excel operations helper
│   ├── logger_util.py     # Logger initializer
│   └── randomdata_util.py # Faker-based dummy data generator
├── conftest.py            # Global fixtures, hooks, and execution setups
├── pytest.ini             # Framework-level runner settings and test configuration
└── requirements.txt       # List of Python dependencies
```

---

## 📂 File & Class Inventory

### 🖥️ Page Objects (`pages/`)

#### 📄 `basepage.py`
- **Class:** `BasePage`
- **Purpose:** Serves as the parent class for all pages. Wraps Playwright's `page` calls with generic wrapper methods (e.g., `click()`, `enter_text()`, `get_text()`, `is_visible()`, `wait_for_element()`, `get_page_url()`, and `get_page_title()`) to provide robust execution, cleaner syntax, and auto-waiting behaviors.

#### 📄 `loginpage.py`
- **Class:** `LoginPage(BasePage)`
- **Purpose:** Identifies page locators for email/password text boxes, register link, Sign In button, and various field-validation messages. Defines standard navigation checks and the core action `do_login(email, password)`.

#### 📄 `homepage.py`
- **Class:** `HomePage(BasePage)`
- **Purpose:** Holds locators and validation methods for the Post-Login homepage (user profile icon, log out button, navigation menus, upcoming event cards, and browse button). Contains flow redirection methods like `do_browse_events()`.

#### 📄 `eventpage.py`
- **Class:** `EventPage(BasePage)`
- **Purpose:** Models the Event searching and discovery layout. Manages the event search text field, result assertions, and booking redirects.

#### 📄 `bookingpage.py`, `mybookingpage.py`, `paymentpage.py`
- **Classes:** `BookingPage(BasePage)`, `MyBookingpage(BasePage)`, `Paymentpage(BasePage)`
- **Purpose:** Reusable skeletons configured to model booking registration, invoice payments, and listing/cancellation dashboard checks.

---

### 🔌 API Client Objects (`api/`)

#### 📄 `base_api.py`
- **Class:** `BaseAPI`
- **Purpose:** Wraps Playwright's HTTP client (`APIRequestContext`). Exposes simplified methods for performing asynchronous-compatible `GET`, `POST`, `PUT`, `DELETE`, `PATCH` requests against configured backends.

#### 📄 `auth_api.py`
- **Class:** `AuthAPI(BaseAPI)`
- **Purpose:** Models authentication operations. Offers the `api_login()` function which POSTs credentials to `/api/auth/login` to retrieve active Bearer authorization tokens.

#### 📄 `events_api.py`
- **Class:** `EventsAPI(BaseAPI)`
- **Purpose:** Focuses on query operations. Fetches all events or filters down to a single event by attaching authorization tokens to standard GET endpoint calls.

#### 📄 `bookings_api.py`
- **Class:** `BookingsAPI(BaseAPI)`
- **Purpose:** Facilitates user bookings workflows: booking creation, fetching user-specific bookings, retrieving individual booking items, and executing cancellations.

---

### 🛠️ Configuration & Utility Classes (`utils/`, `constants/`, `configs/`)

#### 📄 `config_reader_util.py`
- **Class:** `ConfigReader`
- **Purpose:** Utilizes `configparser` to load properties from `configs/config_qa.ini`. Supplies static methods to retrieve environment URLs, execution modes (headless/headed), credentials, and browser parameters.

#### 📄 `appconstants.py`
- **Class:** `AppConstants`
- **Purpose:** Standardized storage for static verification values (e.g. expected titles, validation labels, success strings, and API endpoint URIs) to prevent duplication across files.

#### 📄 `randomdata_util.py`
- **Class:** `Randomdata`
- **Purpose:** Uses `Faker` to generate real-time realistic usernames, emails, passwords, and addresses for dynamic UI form validation and API requests.

#### 📄 `logger_util.py`
- **Purpose:** Configures and provides a standardized `logging` helper that outputs timestamps, log-levels, and diagnostic information to `logs/logfile.log`.

---

## 🧪 Test Suites & Cases Inventory

### 🌐 UI Tests (`tests/ui/`)

#### 1. **Login Page Tests (`TestLoginPage` in `login_page_test.py`)**
| TC ID | Test Case Function | Description |
| :--- | :--- | :--- |
| **TC_001** | `test_get_login_page_title` | Verifies the login page displays the title `EventHub — Discover & Book Events`. |
| **TC_002** | `test_get_login_page_url` | Validates redirection / base path loads the correct EventHub Login URL. |
| **TC_003** | `test_email_field_exist` | Confirms the Email input text box is visible to the user. |
| **TC_004** | `test_password_field_exist` | Confirms the Password input text box is visible to the user. |
| **TC_005** | `test_login_button_exist` | Confirms the "Sign In" CTA button is visible. |
| **TC_006** | `test_register_button_exist` | Confirms the link to the "Register" form is present. |
| **TC_007** | `test_login_with_invalid_credentials` | Inputs fake credentials and asserts the warning message `Invalid email or password`. |
| **TC_008** | `test_login_with_blank_email` | Attempts sign-in with empty email and checks for validation feedback `Enter a valid email`. |
| **TC_009** | `test_login_with_blank_password` | Attempts sign-in with valid email but blank password, asserting validation: `Password must be at least 6 characters`. |
| **TC_010** | `test_do_valid_login` | Enters configuration credentials, clicks login, and asserts redirection to the homepage. |

#### 2. **Homepage Tests (`TestHomePage` in `home_page_test.py`)**
| TC ID | Test Case Function | Description |
| :--- | :--- | :--- |
| **TC_001** | `test_home_page_title` | Asserts title after successful login routing. |
| **TC_002** | `test_home_page_url` | Asserts the URL matches the application base URL post-authentication. |
| **TC_003** | `test_user_profile_icon_visible` | Validates that the active user's profile display element is visible on the top nav. |
| **TC_004** | `test_logout_button_visible` | Validates that the logout button element is present. |
| **TC_005** | `test_navigation_menu_visible` | Confirms the responsive top navigation menu bar is displayed. |
| **TC_006** | `test_browse_events_visible` | Validates that the user can locate the "Browse Events" button. |
| **TC_007** | `test_upcoming_events_section_visible` | Confirms that dynamic event cards are rendering correctly inside the upcoming events container. |
| **TC_008** | `test_my_bookings_link_visible` | Asserts visibility of the "My Bookings" button/link in the menu. |

#### 3. **Event Page Tests (`TestEventPage` in `event_page_test.py`)**
| TC ID | Test Case Function | Description |
| :--- | :--- | :--- |
| **TC_003** | `test_event_page_title` | Verifies the page title once navigated to the Events tab. |
| **TC_004** | `test_event_page_url` | Verifies the page URL matches expectations. |

---

### 🔌 API Tests (`tests/api/`)

#### 1. **Authentication API Tests (`TestLoginPageAPI` in `login_api_test.py`)**
| TC ID | Test Case Function | Description |
| :--- | :--- | :--- |
| **TC_API_001** | `test_login_api` | Sends credentials via POST to `/api/auth/login` and asserts response code `200`, `success=True`, presence of JWT token, and matching user email profile. |

#### 2. **Events API Tests (`TestAllEventsAPI` in `events_api_test.py`)**
| TC ID | Test Case Function | Description |
| :--- | :--- | :--- |
| **TC_API_002** | `test_all_events` | Performs dynamic GET query `/api/events` and verifies status code `200` and events count > `0`. |
| **TC_API_003** | `test_event_by_id` | Fetches a target event by ID, asserting response code `200` and matching ID parameters. |
| **TC_API_004** | `test_event_details_by_id` | Compares a single event's query details (`title`, `venue`, `price`) against full lists data object validation. |

#### 3. **Bookings API Tests (`TestBookingsAPI` in `bookings_api_test.py`)**
| TC ID | Test Case Function | Description |
| :--- | :--- | :--- |
| **TC_API_005** | `test_create_booking` | Submits a customer booking JSON payload. Validates response code `201` and confirms event booking parameters in response data. |
| **TC_API_006** | `test_get_my_bookings` | Queries the active bookings database by booking ID and asserts returned values map correctly to original properties. |
| **TC_API_007** | `test_cancel_booking` | Issues a cancellation request via DELETE. Asserts code `200` and validation message `Booking cancelled`. |

---

## 🚀 Running the Tests

To configure and run the automated execution suites:

### 1. Installation
Ensure PyCharm/Venv is active, then run:
```bash
pip install -r requirements.txt
playwright install
```

### 2. Execution Commands
```bash
# Run all tests (UI & API)
pytest

# Run only UI tests
pytest -m ui

# Run only API tests
pytest -m api

# Run regression suite
pytest -m regression
```

### 3. Reporting
Allure results are outputted to `reports/allure-results/`.
HTML reporting is outputted to `reports/report.html`.

### 3. Reporting
Allure results are outputted to `reports/allure-results/`.
HTML reporting is outputted to `reports/report.html`.

# EventManagementApplication_E2E_framework
Automation framework for handling an EventManagement application : UI automation, E2E automation, API automation

