from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def get_h1_logo_text(self):
        """
        Get the text of logo h1 text inside div navbar.
        """
        h1_locator = (By.CSS_SELECTOR, "div.navbar h1")
        return self.find_element(h1_locator).text
