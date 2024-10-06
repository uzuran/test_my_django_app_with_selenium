from selenium.webdriver.common.by import By
from utils.browser_manager import get_driver
from behave import given, when, then
from utils.config import BASE_URL

@given('the user is on the homepage')
def step_given_user_on_homepage(context):
    """Navigate the user to the homepage."""
    context.browser = get_driver("chrome")
    context.browser.get(BASE_URL)

@when("the user clicks on the 'Home' link")
def step_when_user_clicks_home_link(context):
    """Simulate clicking the 'Home' link."""
    home_link = context.browser.find_element(By.LINK_TEXT, "Home")
    home_link.click()

@then('the user should be on the homepage')
def step_then_user_on_home_page(context):
    """Verify that the user is on the homepage."""
    expected_url = 'https://uzuran.pythonanywhere.com/#home'
    assert context.browser.current_url == expected_url,\
        f"Expected URL: {expected_url}, but got: {context.browser.current_url}"
    assert 'Černopaščenko' in context.browser.title,\
        f"Expected title to contain 'Černopaščenko', but got: '{context.browser.title}'"


@when("the user clicks on the 'About' link")
def step_when_user_clicks_about_link(context):
    """Simulate clicking the 'About' link."""
    about_link = context.browser.find_element(By.LINK_TEXT, "About")
    about_link.click()

@then("the user should see the about section")
def step_then_user_should_see_about_section(context):
    """Verify that the user see te about section."""
    expected_url = "https://uzuran.pythonanywhere.com/#about"
    assert context.browser.current_url == expected_url,\
        f"Expected URL: {expected_url}, but got: {context.browser.current_url}"

@when("the user clicks on the 'Skills' link")
def step_when_user_cliks_skills_link(context):
    """Simulate clicking the 'Skills' link. """
    skills_link = context.browser.find_element(By.LINK_TEXT, "Skills")
    skills_link.click()

@then("the user should see the skills section")
def step_then_user_should_see_about_section(context):
    """Verify that the user see the skills section."""
    expected_url = "https://uzuran.pythonanywhere.com/#skills"
    assert context.browser.current_url == expected_url,\
        f"Expected URL: {expected_url}, but got: {context.browser.current_url}"

@when("the user clicks on the 'Projects' link")
def step_when_user_clicks_projects_link(context):
    """Simulate clicking the 'Projects' link."""
    projects_link = context.browser.find_element(By.LINK_TEXT, "Projects")
    projects_link.click()


@then("the user should see the projects section")
def step_then_user_should_see_contacts_sections(context):
    expected_url = "https://uzuran.pythonanywhere.com/#projects"
    assert context.browser.current_url == expected_url, \
        f"Expected URL: {expected_url}, but got: {context.browser.current_url}"

@when("the user clicks on the 'Contacts' link")
def step_when_user_clicks_contacts_link(context):
    contacts_link = context.browser.find_element(By.LINK_TEXT, "Contacts")
    contacts_link.click()

@then("the user should see the contacts sections")
def step_then_user_should_see_contacts_sections(context):
    expected_url = "https://uzuran.pythonanywhere.com/#contacts"
    assert context.browser.current_url == expected_url, \
        f"Expected URL: {expected_url}, but got: {context.browser.current_url}"