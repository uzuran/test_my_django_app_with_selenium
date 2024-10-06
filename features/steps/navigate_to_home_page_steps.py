from selenium.webdriver.common.by import By
from utils.browser_manager import get_driver
from behave import given, when, then
from utils.config import BASE_URL

@given('the user is on the homepage')
def step_given_user_on_homepage(context):
    """Navigate the user to the homepage."""
    context.browser = get_driver("chrome")
    context.browser.get(BASE_URL)

@when('the user clicks on the "Home" link')
def step_when_user_clicks_home_link(context):
    """Simulate clicking the 'Home' link."""
    home_link = context.browser.find_element(By.LINK_TEXT, "Home")
    home_link.click()

@then('the user should be on the homepage')
def step_then_user_on_home_page(context):
    """Verify that the user is on the homepage."""
    expected_url = 'https://uzuran.pythonanywhere.com/#home'
    assert context.browser.current_url == expected_url, f"Expected URL: {expected_url}, but got: {context.browser.current_url}"
    assert 'Černopaščenko' in context.browser.title, f"Expected title to contain 'Černopaščenko', but got: '{context.browser.title}'"

# environment.py

def after_scenario(context, scenario):
    if context.browser:
        context.browser.quit()
