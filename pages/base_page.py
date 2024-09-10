"""Base page settings."""
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Base page class."""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Function for a find element."""
        return self.driver.find_element(*locator)
