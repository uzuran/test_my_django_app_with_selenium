"""Settings for tests."""
import pytest
from utils.browser_manager import get_driver
from utils.config import BASE_URL
from utils.db_queries import DbQueries  # Grouped with other imports from 'utils'
from pages.home_page import HomePage
import os


class SeleniumHelper:
    """Class for WebDriver setup and utilities."""

    @pytest.fixture(scope="module", autouse=True)
    def driver(self):
        """Fixture to initialize and clean up the WebDriver instance."""
        driver_instance = get_driver(browser="chrome")
        yield driver_instance
        driver_instance.quit()

    @pytest.fixture(scope="module")
    def db_queries(self):
        """Fixture to provide a DatabaseQueries instance."""
        queries = DbQueries()
        yield queries
        # Optionally close connections or perform cleanup
        queries.db_connection.close_connection()

    @staticmethod
    def navigate_to_home_page(driver):
        """Helper function to navigate to the base URL and create a HomePage instance."""
        driver.get(BASE_URL)
        return HomePage(driver)

    @staticmethod
    def take_screenshot(driver, screenshot_name, screenshot_dir="screenshots"):
        """Utility function to take a screenshot.

        Args:
            driver: WebDriver instance.
            screenshot_name: Name of the screenshot file to be saved.
            screenshot_dir: Directory where the screenshot will be saved (default is 'screenshots').
        """
        # Ensure the directory exists, create it if it doesn't
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        # Define the full screenshot path
        screenshot_path = os.path.join(screenshot_dir, f"{screenshot_name}.png")

        # Take a screenshot
        driver.save_screenshot(screenshot_path)

