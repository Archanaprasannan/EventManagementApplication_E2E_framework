# Playwright Python End-to-End Test Automation Framework

## Overview

This repository contains a **hybrid test automation framework** for the **EventHub** web application.

The framework is built using **Python, Playwright, and Pytest** and supports both:

* 🌐 UI End-to-End testing
* 🔌 REST API testing   

The UI automation follows the **Page Object Model (POM)** design pattern, while API automation uses structured API client classes.

The framework also includes reusable utilities for configuration management, test data generation, logging, screenshots, and test reporting.

**Application:** EventHub
**URL:** https://eventhub.rahulshettyacademy.com/login

**Browsers:** Chromium, Edge, Firefox
**Execution:** Headed / Headless

---

## 🛠️ Technologies & Tools

| Technology        | Purpose                      |
| ----------------- | ---------------------------- |
| Python            | Programming language         |
| Playwright        | UI and API automation        |
| Pytest            | Test execution and framework |
| APIRequestContext | REST API automation          |
| Allure            | Test reporting               |
| Pytest HTML       | HTML test reporting          |
| Faker             | Dynamic test data generation |
| Git / GitHub      | Source code management       |
| Jenkins           | CI execution                 |

---

## 📁 Project Structure

```text
PlaywrightE2EFramework/
│
├── api/
│   ├── auth_api.py
│   ├── base_api.py
│   ├── bookings_api.py
│   └── events_api.py
│
├── configs/
│   └── config_qa.ini
│
├── constants/
│   └── appconstants.py
│
├── pages/
│   ├── basepage.py
│   ├── bookingpage.py
│   ├── eventpage.py
│   ├── homepage.py
│   ├── loginpage.py
│   └── mybookingpage.py
│
├── reports/
│   ├── allure-results/
│   └── report.html
│
├── screenshots/
│
├── testdata/
│   ├── csv/
│   ├── excel/
│   └── json/
│
├── tests/
│   ├── api/
│   │   ├── bookings_api_test.py
│   │   ├── events_api_test.py
│   │   └── login_api_test.py
│   │
│   └── ui/
│       ├── event_page_test.py
│       ├── home_page_test.py
│       └── login_page_test.py
│
├── utils/
│   ├── config_reader_util.py
│   ├── excel_util.py
│   ├── logger_util.py
│   └── randomdata_util.py
│
├── conftest.py
├── pytest.ini
└── requirements.txt
```

---

# 🖥️ UI Automation

The UI automation layer follows the **Page Object Model (POM)** approach.

### `BasePage`

Provides reusable Playwright actions such as:

* Click
* Enter text
* Get text
* Check element visibility
* Wait for elements
* Get page URL
* Get page title

This keeps common browser interactions in one place and reduces duplication across page classes.

### `LoginPage`

Handles:

* Email and password fields
* Login button
* Register navigation
* Login validation messages
* Valid and invalid login scenarios

### `HomePage`

Handles:

* User profile
* Logout
* Navigation menu
* Upcoming events
* Browse Events navigation
* My Bookings navigation

### `EventPage`

Handles:

* Event search
* Event results
* Event details
* Booking navigation

### `BookingPage`

Contains the page objects and actions related to event booking.

### `MyBookingPage`

Handles the My Bookings page and booking-related validations.

---

# 🔌 API Automation

The API layer uses Playwright's **APIRequestContext** for REST API testing.

### `BaseAPI`

Provides reusable HTTP methods for:

* GET
* POST
* PUT
* PATCH
* DELETE

### `AuthAPI`

Handles authentication APIs, including:

* Login
* Bearer token generation
* Authentication-related API operations

### `EventsAPI`

Handles Event APIs such as:

* Get all events
* Get individual event
* Create event
* Update event
* Delete event

### `BookingsAPI`

Handles booking-related APIs such as:

* Create booking
* Get bookings
* Get individual booking
* Cancel booking

---

# 🛠️ Utilities & Configuration

### Configuration

`config_reader_util.py` reads environment-specific configuration from `.ini` files.

Configuration includes:

* Application URL
* API URL
* Username
* Password
* Browser
* Headless / headed execution

### Test Data

`randomdata_util.py` uses **Faker** to generate dynamic test data such as:

* Names
* Email addresses
* Passwords
* Addresses

### Logging

`logger_util.py` provides centralized logging for test execution and troubleshooting.

Logs are stored under:

```text
logs/logfile.log
```

### Constants

`appconstants.py` stores reusable application constants such as:

* URLs
* API endpoints
* Expected titles
* Validation messages
* Other static values

---

# 🧪 Test Coverage

## 🌐 UI Tests

The UI test suite covers:

### Login

* Login page title
* Login page URL
* Email field visibility
* Password field visibility
* Login button visibility
* Register button visibility
* Invalid credentials
* Blank email
* Blank password
* Valid login

### Home Page

* Page title
* Page URL
* User profile visibility
* Logout button
* Navigation menu
* Browse Events
* Upcoming Events
* My Bookings navigation

### Events

* Events page title
* Events page URL
* Event search
* Event results

### Bookings

* My Bookings page navigation
* My Bookings page title
* My Bookings page URL

---

## ⚙️ API Tests

The API test suite covers:

### Authentication

* Login with valid credentials
* Login with invalid credentials
* Authentication token validation

### Events

* Get all events
* Get event with valid token
* Get event with invalid token

### Bookings

* Booking API workflows
* Booking retrieval
* Booking-related validations

---

# 🔄 End-to-End Workflow

The framework supports testing complete application workflows across UI and API layers.

Example workflow:

```text
Login
  ↓
Home Page
  ↓
Browse Events
  ↓
Search Event
  ↓
Select Event
  ↓
Book Event
  ↓
My Bookings
```

---

# 🌎 Environment Configuration

The framework supports environment-based configuration.

Example:

```text
configs/
└── config_qa.ini
```

Configuration values are externalized rather than hardcoded inside test cases.(from command line)

This allows the same tests to be executed against different environments with minimal changes.

---

# Installation

Clone the repository and install the required dependencies.

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

# ▶️ Running the Tests

### Run all tests

```bash
pytest
```

### Run UI tests

```bash
pytest -m ui
```

### Run API tests

```bash
pytest -m api
```

### Run regression tests

```bash
pytest -m regression
```

### Run tests in headed mode

```bash
pytest --headed
```

---

# 📊 Reporting

The framework supports multiple reporting options.

### Pytest HTML Report

The HTML report is generated under:

```text
reports/report.html
```

### Allure Report

Raw Allure results are stored under:

```text
reports/allure-results/
```

Generate and open the Allure report using:

```bash
allure serve reports/allure-results
```

---

# 📸 Failure Screenshots

Screenshots are automatically captured for failed UI tests and stored under:

```text
screenshots/
```

These screenshots help with debugging failed test executions.

---

---

# 📈 Future Enhancements

Potential improvements include:

* Expanded API/UI test coverage
* Additional negative API/UI scenarios
* Data-driven testing
* CI/CD pipeline integration
* Enhanced Allure reporting

---

# 👩‍💻 Author

**Archana Prasannan**

QA Automation Engineer

**Focus:** UI Automation | API Automation | Python | Playwright | Pytest | Allure reporting | Parallel execution | cross browser Testing
