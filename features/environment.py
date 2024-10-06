from selenium import webdriver

def before_scenario(context, scenario):
    # Initialize the Chrome WebDriver before each scenario
    context.browser = webdriver.Chrome()

def after_scenario(context, scenario):
    # Quit the WebDriver after each scenario
    context.browser.quit()
