import pytest
from utils.browser_manager import get_driver
from pages.home_page import HomePage
from utils.config import BASE_URL
from utils.screenshot import take_screenshot


@pytest.fixture(scope="function")
def driver():
    driver = get_driver(browser="chrome")
    yield driver
    driver.quit()


def test_h1_check(driver):
    driver.get(BASE_URL)
    home_page = HomePage(driver)

    # Verify the h1 element's text
    try:
        h1_text = home_page.get_h1_text()
        assert h1_text == "Expected H1 Text", f"Unexpected H1 text: {h1_text}"
    except AssertionError as e:
        # Take a screenshot if the assertion fails
        take_screenshot(driver, "h1_check_failed")
        raise e
