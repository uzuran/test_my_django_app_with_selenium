"""Settings for tests."""
import pytest
from utils.browser_manager import get_driver
from utils.config import BASE_URL
from utils.db_queries import DbQueries  # Grouped with other imports from 'utils'
from pages.home_page import HomePage


class TestSettings:
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

    def navigate_to_home_page(self, driver):
        """Helper function to navigate to the base URL and create a HomePage instance."""
        driver.get(BASE_URL)
        return HomePage(driver)
