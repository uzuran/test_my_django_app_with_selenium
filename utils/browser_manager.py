"""Base settings for browsers"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(browser="chrome"):
    """Get different drivers from CHROME_DRIVER_PATH."""
    if browser == "chrome":
        option_for_chrome = Options()
        option_for_chrome.add_argument("--disable-search-engine-choice-screen")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option_for_chrome)
    elif browser == "firefox":
        # Similar initialization for Firefox
        pass
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(10)  # Implicit wait.
    return driver
