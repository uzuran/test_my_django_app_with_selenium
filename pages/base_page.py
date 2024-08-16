from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Base page class."""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Function for a find element."""
        return self.driver.find_element(*locator)

    def get_h1_text(self):
        """Get HTML <h1> in text form."""
        h1_locator = (By.TAG_NAME, "h1")
        return self.find_element(h1_locator).text
