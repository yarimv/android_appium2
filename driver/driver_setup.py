from appium.webdriver import Remote
from appium.options.common import AppiumOptions
from appium.webdriver.webdriver import AppiumBy
import time




options = AppiumOptions().load_capabilities(
        {
                "appium:deviceName": "R5CRB2P3KDM",
                "appium:platformName": "Android",
                "appium:automationName": "uiautomator2"
        }
)


driver = Remote("http://127.0.0.1:4723", options=options)

driver.quit()


if __name__ == "__main__":
        print("running")
        time.sleep(5)

        el = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@content-desc='갤러리']")
        print(el)






