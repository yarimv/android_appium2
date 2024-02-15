from appium.webdriver.webdriver import AppiumBy
from driver import driver_setup
import time
from basemethod.custom_method import CustomMethod

# Get the Appium driver
get_driver = driver_setup.get_appium_driver()

print("start")


# 케이스명 = script

# Find an element using AppiumBy
element = get_driver.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.TextView")

# Do something with the found element (e.g., click, send_keys, etc.)
element.click()
time.sleep(5)


# Close the session
get_driver.driver.quit()
