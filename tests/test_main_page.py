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
from utils.screenshot import take_screenshot
from utils.db_queries import get_h1_strings_from_db
from tests.test_settings import TestSettings


class TestMainPage(TestSettings):
    """Test class containing test cases for the home page."""

    def test_h1_logo_text(self, driver):
        """Test to verify the H1 logo text on the home page."""
        home_page = self.navigate_to_home_page(driver)

        # Retrieve expected H1 text from the database
        expected_h1_text = get_h1_strings_from_db()

        if expected_h1_text is None:
            pytest.fail("Failed to retrieve expected H1 text from the database.")

        try:
            h1_logo_text = home_page.get_h1_logo_text()
            assert h1_logo_text == expected_h1_text, \
                f"Expected H1 text: '{expected_h1_text}', but got: '{h1_logo_text}'"
        except Exception as e:
            take_screenshot(driver, "h1_check_failed.png")
            raise e

    def test_count_of_h1_elements(self, driver):
        """Test to verify the count of H1 elements on the home page."""
        home_page = self.navigate_to_home_page(driver)

        try:
            h1_count = home_page.count_of_h1_elements()
            # Assert that the count is less than 6
            assert h1_count < 6, \
                f"Expected fewer than 6 <h1> elements, but found {h1_count}"

        except Exception as e:
            take_screenshot(driver, "h1_count_check_failed.png")
            raise e
