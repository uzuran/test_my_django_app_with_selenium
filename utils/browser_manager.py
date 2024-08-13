"""Browser manager."""
from selenium import webdriver
from utils.config import CHROME_DRIVER_PATH


def get_driver(browser="chrome"):
    """Get different drivers from CHROME_DRIVER_PATH."""
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=CHROME_DRIVER_PATH)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(10)  # Implicit wait.
    return driver
