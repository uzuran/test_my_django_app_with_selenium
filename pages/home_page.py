from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    def get_h1_text(self):
        """
        Get the text of the first <h1> element on the page.
        """
        h1_locator = (By.TAG_NAME, "h1")
        return self.find_element(h1_locator).text
