"""Base web drive class"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BaseWebDriver:
    """
    Base class to initialize and handle the WebDriver instance.

    Attributes:
        driver_path (str): The path to the WebDriver executable.
        driver (WebDriver): The WebDriver instance.
    """

    def __init__(self, driver_path):
        """
        Initializes the BaseWebDriver with the given driver path.

        Args:
            driver_path (str): The path to the WebDriver executable.
        """
        self._driver_path = driver_path  # Use a different name to avoid shadowing
        self.driver = None

    def start_driver(self):
        """
        Starts the WebDriver instance and sets implicit wait.
        """
        service = Service(self._driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(5)  # Waits up to 5 seconds for elements to appear

    def quit_driver(self):
        """
        Quits the WebDriver instance if it is running.
        """
        if self.driver:
            self.driver.quit()
