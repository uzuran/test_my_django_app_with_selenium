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

    try:
        h1_text = home_page.get_h1_logo_text()
        assert h1_text == "Černopaščenko", f"Unexpected H1 text: {h1_text}"
    except AssertionError as e:
        take_screenshot(driver, "h1_check_failed.png")
        raise e
