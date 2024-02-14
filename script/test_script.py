from appium.webdriver.common import appiumby
from driver import driver_setup
import time

# Get the Appium driver
driver = driver_setup.get_appium_driver()

print("start")
# Find an element using AppiumBy
element = driver.find_element(appiumby.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.TextView")

# Do something with the found element (e.g., click, send_keys, etc.)
element.click()
# time.sleep(5)
#
#
# # Close the session
# driver.quit()
