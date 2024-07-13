"""Tests for navbar."""
import unittest
from selenium.webdriver.chrome.options import Options
from web_parts.nav_bar import NavBar  # Adjust this import according to your structure


class TestNavBar(unittest.TestCase):
    """Main test class for testing my navbar."""

    @classmethod
    def setUpClass(cls):
        """Set up the WebDriver for all tests."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        cls.driver_path = r'C:\drivers\chromedriver-win64\chromedriver.exe'
        cls.page = NavBar(cls.driver_path)

    def test_get_title_text(self):
        """Test if the get_title_text function retrieves the correct text."""
        expected_title = "Černopaščenko"  # Adjust this to the expected text
        actual_text = self.page.get_title_text()
        self.assertEqual(actual_text, expected_title, f"Expected logo text '{expected_title}'"
                                                      f" but got '{actual_text}'.")

    def test_get_logo_text(self):
        """Test if the get_logo_text function retrieves the correct text."""
        expected_text = "Černopaščenko"  # Adjust this to the expected text
        actual_text = self.page.get_logo_text()
        self.assertEqual(actual_text, expected_text, f"Expected logo text '{expected_text}'"
                                                     f" but got '{actual_text}'.")

    def test_get_home_text(self):
        """Test if the get_home_text function retrieves the correct text."""
        expected_text = "Home"
        actual_text = self.page.get_home_text()
        self.assertEqual(actual_text, expected_text, f"Expected home text '{expected_text}'"
                                                     f" but got '{actual_text}'.")

    @classmethod
    def tearDownClass(cls):
        """Tear down the WebDriver after all tests."""
        cls.page.close()


if __name__ == "__main__":
    unittest.main()
