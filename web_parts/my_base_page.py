"""Class for get element from base web page"""
from selenium.common import NoSuchElementException, WebDriverException
from base_web_driver import BaseWebDriver


class MyBasePage(BaseWebDriver):
    """
    Class representing nav bar on my web page.

    Inherits from BaseWebDriver.

    Attributes:
        driver_path (str): The path to the WebDriver executable.
    """

    def __init__(self, driver_path):
        """
        Initializes the main web page with the given driver path and opens website.

        Args:
            driver_path (str): The path to the WebDriver executable.
        """
        super().__init__(driver_path)
        self.start_driver()
        self.driver.get("http://uzuran.pythonanywhere.com/")

    def get_home_url(self):
        """:return: actual url."""
        return self.driver.current_url

    def get_title_text(self):
        """
        :return: title from my webpage.
        """
        try:
            get_title = self.driver.title
            return get_title
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
            return ""
        except WebDriverException as e:
            print(f"Webdriver error occurred: {e}")
            return ""

    def close(self):
        """
        Closes the WebDriver instance.
        """
        self.quit_driver()
