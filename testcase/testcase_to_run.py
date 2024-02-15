import sys
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
        print("driver opened")
    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
            print("driver closed")

    def test_임시_find_battery(self) -> None:
        #메소드명은 Checklist 의 항목명으로 지정하기
        #메소드명 반환
        current_func_name = sys._getframe().f_code.co_name
        print("The current running function name : {}".format(current_func_name))
        el = self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@content-desc='갤러리']")
        el.click()

    def test_2_신규_설치_및_구동(self) -> None:
        # 메소드명은 Checklist 의 항목명으로 지정하기
        # 메소드명 반환
        current_func_name = sys._getframe().f_code.co_name
        print("The current running function name : {}".format(current_func_name))
        el = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@content-desc='갤러리']")
        el.click()


    def test_3_가입약관확인(self) -> None:
        # 메소드명은 Checklist 의 항목명으로 지정하기
        # 메소드명 반환
        current_func_name = sys._getframe().f_code.co_name
        print("The current running function name : {}".format(current_func_name))
        el = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@content-desc='갤러리']")
        el.click()


if __name__ == '__main__':
    unittest.main()