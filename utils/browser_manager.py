"""Browser manager."""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.config import CHROME_DRIVER_PATH


SERVICE = Service(executable_path=CHROME_DRIVER_PATH)


def get_driver(browser="chrome"):
    """Get different drivers from CHROME_DRIVER_PATH."""
    if browser == "chrome":
        driver = webdriver.Chrome(service=SERVICE)
    elif browser == "firefox":
        driver = webdriver.Firefox(service=SERVICE)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(10)  # Implicit wait.
    return driver
