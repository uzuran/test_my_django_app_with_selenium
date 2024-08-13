import os
from datetime import datetime


def take_screenshot(driver, name="screenshot"):
    # Create screenshots directory if it doesn't exist
    screenshots_dir = os.path.join(os.getcwd(), "screenshots")
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    # Generate a timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{name}_{timestamp}.png"
    filepath = os.path.join(screenshots_dir, filename)

    # Take the screenshot
    driver.save_screenshot(filepath)
    print(f"Screenshot saved: {filepath}")
    