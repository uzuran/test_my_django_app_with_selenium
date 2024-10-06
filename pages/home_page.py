from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    """
    A class representing the home page of the website.

    Inherits from BasePage and provides methods to interact with and retrieve information from the home page.
    """
    def count_of_h1_elements(self):
        """
        Count the number of H1 elements on the home page.

        Uses the Selenium WebDriver to find all <h1> elements and returns the count.

        Returns:
            int: The number of <h1> elements found on the page.
        """
        h1_elements = self.driver.find_elements(By.TAG_NAME, "h1")
        return len(h1_elements)

    def get_h1_logo_text(self):
        """
        Retrieve the text of the H1 logo element within the navbar.

        Finds the H1 element inside a div with the class 'navbar' and returns its text.

        Returns:
            str: The text content of the H1 element located inside the navbar div.
        """
        h1_locator = (By.CSS_SELECTOR, "div.navbar h1")
        return self.find_element(h1_locator).text

    def get_nav_element_home(self):
        """
        Retrieve the text of the H1 logo element within the navbar.

        Finds the H1 element inside a div with the class 'navbar' and returns its text.

        Returns:
            str: The text content of the H1 element located inside the navbar div.
        """
        nav_element_home = (By.XPATH, "//a[@class='menu__item' and text()='Home']")
        return self.find_element(nav_element_home).text

    def click_on_home_link(self):
        home_link = self.find_element(By.LINK_TEXT, "Home")
        return home_link.click()