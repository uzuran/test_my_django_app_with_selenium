"""Class for get element from navbar web page"""
from selenium.common import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from base_web_driver import BaseWebDriver


class NavBar(BaseWebDriver):
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

    def get_logo_text(self):
        """
        Retrieves and returns the logo text from the current navbar.

        Returns:
            str: The logo text if found, otherwise an empty string.
        """
        try:
            logo_element = self.driver.find_element(By.CSS_SELECTOR, 'h1.logo-name')
            return logo_element.text  # Retrieve the text of the element
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
            return ""
        except WebDriverException as e:
            print(f"Webdriver error occurred: {e}")
            return ""

    def get_home_text(self):
        """
        Retrieves and returns the home text from the current navbar.

        Returns:
            str: The home text if found, otherwise an empty string.
        """
        try:
            menu_item_element = self.driver.find_element(By.XPATH,
                                                         "//a[text()='Home']")
            return menu_item_element.text
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
