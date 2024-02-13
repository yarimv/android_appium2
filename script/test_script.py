from appium.webdriver.common.mobileby import MobileBy
from driver_setup import get_appium_driver

# Get the Appium driver
driver = get_appium_driver()

try:
    # Find an element using AppiumBy
    element = driver.find_element(MobileBy.ID, "yourElementId")

    # Do something with the found element (e.g., click, send_keys, etc.)
    element.click()

finally:
    # Close the session
    driver.quit()
