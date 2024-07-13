import unittest
from selenium.webdriver.chrome.options import Options
from web_parts.nav_bar import NavBar  # Adjust this import according to your structure


class TestNavBar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the WebDriver for all tests."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Optional: run Chrome in headless mode
        cls.driver_path = r'C:\drivers\chromedriver-win64\chromedriver.exe'  # Update this path as needed
        cls.page = NavBar(cls.driver_path)

    def test_get_logo_text(self):
        """Test if the get_logo_text function retrieves the correct text."""
        expected_text = "Černopaščenko"  # Adjust this to the expected text
        actual_text = self.page.get_logo_text()
        self.assertEqual(actual_text, expected_text, f"Expected logo text '{expected_text}' but got '{actual_text}'.")

    @classmethod
    def tearDownClass(cls):
        """Tear down the WebDriver after all tests."""
        cls.page.close()


if __name__ == "__main__":
    unittest.main()
