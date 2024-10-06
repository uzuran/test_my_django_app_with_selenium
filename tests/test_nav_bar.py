import pytest
from utils.screenshot import take_screenshot
from tests.test_settings import TestSettings


class TestNavBar(TestSettings):
    """Test class containing test cases for the navbar."""
    def test_navbar_element_home(self, driver, db_queries):
        """Test to verify the H1 logo text on the home page."""
        navigate_to_home_page = self.navigate_to_home_page(driver)

        # Retrieve expected H1 text from the database
        expected_nav_element_home = db_queries.get_nav_element_home_from_database()

        if expected_nav_element_home is None:
            pytest.fail("Failed to retrieve expected H1 text from the database.")

        try:
            nav_element_home = navigate_to_home_page.get_nav_element_home()
            assert nav_element_home == expected_nav_element_home, \
                f"Expected H1 text: '{expected_nav_element_home}', but got: '{nav_element_home}'"
        except Exception as e:
            take_screenshot(driver, "nav_element_home_failed.png")
            raise e
