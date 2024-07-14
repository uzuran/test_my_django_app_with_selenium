"""Base test class."""
import unittest
from selenium.webdriver.chrome.options import Options
from web_parts.nav_bar import NavBar  # Adjust this import according to your structure
from web_parts.my_base_page import MyBasePage


class BaseTest(unittest.TestCase):
    """Base test class for setting up and tearing down the WebDriver."""

    @classmethod
    def setUpClass(cls):
        """Set up the WebDriver for all tests."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        cls.driver_path = r'C:\drivers\chromedriver-win64\chromedriver.exe'
        cls.page_navbar = NavBar(cls.driver_path)
        cls.base_page = MyBasePage(cls.driver_path)

    @classmethod
    def tearDownClass(cls):
        """Tear down the WebDriver after all tests."""
        cls.page_navbar.close()
        cls.base_page.close()
