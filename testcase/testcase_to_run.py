import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver import Remote
from appium.webdriver.webdriver import AppiumBy
from appium.options.common import AppiumOptions



options = AppiumOptions().load_capabilities(
        {
                "appium:deviceName": "R5CRB2P3KDM",
                "appium:platformName": "Android",
                "appium:automationName": "uiautomator2"
        }
)


# driver = Remote("http://127.0.0.1:4723", options=options)
#

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        el = self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@content-desc='갤러리']")
        el.click()
        print("깃헙업로드를 위한 변경 줄")

if __name__ == '__main__':
    unittest.main()