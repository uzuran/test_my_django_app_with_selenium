"""
test_main_page.py

This module contains tests for the main page of the application.

Imports:
- pytest: Testing framework
- get_driver: Function to get the Selenium WebDriver instance
- HomePage: Page object model for the home page
- BASE_URL: Base URL for the application
- take_screenshot: Function to capture screenshots during tests
"""

import pytest
from utils.browser_manager import get_driver
from pages.home_page import HomePage
from utils.config import BASE_URL
from utils.screenshot import take_screenshot
from utils.db_queries import get_h1_strings_from_db


@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize and clean up the WebDriver instance."""
    driver_instance = get_driver(browser="chrome")
    yield driver_instance
    driver_instance.quit()


@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize and clean up the WebDriver instance."""
    driver_instance = get_driver(browser="chrome")
    yield driver_instance
    driver_instance.quit()


def test_h1_logo_text(driver):
    """Test to verify the H1 logo text on the home page."""
    driver.get(BASE_URL)
    home_page = HomePage(driver)

    # Retrieve expected H1 text from the database
    expected_h1_text = get_h1_strings_from_db()

    if expected_h1_text is None:
        pytest.fail("Failed to retrieve expected H1 text from the database.")

    try:
        h1_text = home_page.get_h1_logo_text()
        assert h1_text == expected_h1_text, f"Expected H1 text: '{expected_h1_text}', but got: '{h1_text}'"
    except AssertionError as e:
        take_screenshot(driver, "h1_check_failed.png")
        raise e
