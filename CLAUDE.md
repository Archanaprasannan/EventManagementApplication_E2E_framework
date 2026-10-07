# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project
Hybrid Playwright + Pytest E2E framework for EventHub (https://eventhub.rahulshettyacademy.com/login). Uses Page Object Model (`pages/`) for UI and API Object Model (`api/`) for API tests, with BDD (`tests/bdd/features/`) and data-driven inputs (`testdata/`).

## Common commands

- Run all tests: `pytest`
- Run single test: `pytest -v tests/ui/login_page_test.py::TestLoginPage::test_get_login_page_title`
- Run by marker: `pytest -m smoke`, `pytest -m ui`, `pytest -m api`
- Environment: `pytest --env=qa` (default), `--env=dev`, `--env=uat`; config loads `configs/config_{env}.ini`
- Cross-browser: `pytest --browser=chromium` / `--browser=firefox` / `--browser=edge` (fixture uses `browser` from pytest-playwright)
- BDD: `behave tests/bdd/features/` or `pytest tests/bdd/`
- Headless/headed controlled by `ConfigReader.get_headless()` via config
- Reports auto-generated: `reports/report.html` (pytest-html) and `reports/allure-results/` (allure); screenshots on failure go to `screenshots/`

## Architecture notes (multi-file)

- **Fixture dependency chain in `conftest.py`**: `setup_and_teardown` (function-scoped, new context/page per test, navigates to `ConfigReader.get_ui_url()`) → `login_page` → `home_page` (calls `do_login`) → `event_page` (`do_browse_events`) → `booking_page` (`click_book_now`). Tests typically inject `home_page`, `event_page`, etc. rather than raw `page`.
- **Cross-browser setup**: `request.config.getoption("--browser")` feeds `getattr(playwright, browser_name).launch(headless=...)`. The `browser` fixture is provided by `pytest-playwright`; `setup_and_teardown` depends on it.
- **API fixtures**: `api_context` (function-scoped `APIRequestContext` with `base_url=ConfigReader.get_api_url()`) → `auth_api` (`AuthAPI`) → `auth_token` (calls `api_login()` to get Bearer token for `EventsAPI`/`BookingsAPI`).
- **Config loading**: `pytest_configure` calls `ConfigReader.load_config(env)` so all fixtures and pages can read URLs/credentials at import/test time without manual setup.
- **Failure hook**: `pytest_runtest_makereport` captures screenshots (`screenshots/{name}_{timestamp}.png`) and attaches URL + screenshot to Allure on any failure; also logs via `logger_util.py`.
- **Page inheritance**: All pages inherit `BasePage` (`pages/basepage.py`) which wraps `click`, `enter_text`, `get_text`, `is_visible`, `wait_for_element`. `loginpage.py`, `homepage.py`, `eventpage.py`, `bookingpage.py`, `adminpage.py` extend it.
- **BDD structure**: `tests/bdd/features/*.feature` + `tests/bdd/step_definitions/*.py`; `event_bdd_test.py`/`login_bdd_test.py` bind them.

## Key files not to miss

- `conftest.py`: fixtures, `pytest_addoption` (`--env`, `--browser`), `pytest_configure` (config load), failure hook.
- `pytest.ini`: `-v --html=reports/report.html --alluredir=reports/allure-results -n 2`; `testpaths=tests`.
- `pages/basepage.py`: wrapper methods used by all POM classes.
- `constants/appconstants.py`: static URLs, titles, categories, prices, seats.
- `configs/config_qa.ini`: base URL, credentials, browser, headless settings.
- `pages/adminpage.py`: admin page POM.
- `pages/basepage.py`: wrapper methods used by all POM classes.
- `pages/bookingpage.py`: booking page POM (create booking flows).
- `pages/eventpage.py`: event page POM.
- `pages/homepage.py`: home page POM.
- `pages/loginpage.py`: login page POM.
- `pages/mybookingpage.py`: my bookings POM.
- `tests/ui/admin_page_test.py`: admin page tests.
- `tests/ui/booking_page_test.py`: booking page tests (separate methods for title, URL, create booking).
- `tests/ui/event_page_test.py`: event page tests.
- `tests/ui/home_page_test.py`: home page tests.
- `tests/ui/login_page_test.py`: login page tests.
- `tests/e2e/booking_flow_test.py`: end-to-end booking flow test.
- `tests/bdd/features/*.feature` + `tests/bdd/step_definitions/*.py`: BDD tests.

## Pattern when creating tests (check existing test files first)
Based on `tests/ui/booking_page_test.py`, `tests/ui/login_page_test.py`, etc.:
- Write separate methods for each verification (e.g., `test_create_booking`, `test_page_title_verification`, `test_page_url_verification`).
- Use fixtures from `conftest.py` (`home_page`, `event_page`, `booking_page`, etc.).
- For page-level assertions, use `expect(page).to_have_title()` / `expect(page).to_have_url()` when using Playwright fixtures; for POM-based tests call page methods (e.g., `booking_page.get_title()`) and assert results.
- Always update this `CLAUDE.md` (key files section) when adding new page or test files.
