# settings.py
import pytest
from utils.browser_manager import get_driver
from utils.config import BASE_URL
from pages.home_page import HomePage


class TestSettings:
    """Class for WebDriver setup and utilities."""

    @pytest.fixture(scope="class", autouse=True)
    def driver(self):
        """Fixture to initialize and clean up the WebDriver instance."""
        driver_instance = get_driver(browser="chrome")
        yield driver_instance
        driver_instance.quit()

    def navigate_to_home_page(self, driver):
        """Helper function to navigate to the base URL and create a HomePage instance."""
        driver.get(BASE_URL)
        return HomePage(driver)
