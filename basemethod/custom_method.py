from driver.driver_setup import get_appium_driver
from appium.webdriver.webdriver import AppiumBy
import time


get_driver = get_appium_driver()
class CustomMethod():


    def find(self, button_name_text):
        button_name = button_name_text
        if type(button_name) == str:
            result = f'//*[@text = "{button_name}"]'
            try:
                button_locator = get_driver.driver.find_element(AppiumBy.XPATH, result)
                print(f"결과요소 찾음 :  {button_locator}")
                return button_locator
            except:
                print("버튼 찾지 못함")
        else:
            print("The element is not a string.")

    #return 이 없음

    def find_with_xpath(self, absulte_xpath):
        xpath = absulte_xpath
        if type(xpath) == str:
            try:
                button_locator = get_driver.driver.find_element(AppiumBy.XPATH, xpath)
                print(f"결과요소 찾음 :  {button_locator}")
                return button_locator
            except:
                print("버튼 찾지 못함")
        else:
            print("The element is not a string.")

    def find_include(self, text):
        word = text
        if type(word) == str:
            result = f'//*[contains(@text, "{word}")]'
            try:
                button_locator = get_driver.driver.find_element(AppiumBy.XPATH, result)
                print(f"결과요소 찾음 :  {result}")
                return button_locator
            except:
                print("버튼 찾지 못함")
        else:
            print("The element is not a string.")


    def find_and_click(self, button_name_text):
        button_name = button_name_text
        if type(button_name) == str:
            result = f'//*[@text = "{button_name}"]'
            print(result)
            try:
                button_locator = get_driver.driver.find_element(AppiumBy.XPATH, result)
                print("버튼 찾음")
                time.sleep(2)
                button_locator.click()
                print("버튼 클릭 완료")
                return button_locator
            except:
                print("버튼 찾지 못하거나 클릭 못함")
        else:
            print("The element is not a string.")



    def find_and_click_with_xpath(self, absulte_xpath):
        xpath = absulte_xpath
        if type(xpath) == str:
            try:
                button_locator = get_driver.driver.find_element(AppiumBy.XPATH, xpath)
                print(f"버튼 찾음 :  {button_locator}")
                button_locator.click()
                print("버튼 클릭 완료")
                return button_locator
            except:
                print("버튼 찾지 못하거나 클릭 못함")
        else:
            print("The element is not a string.")



if __name__ == "__main__":
    custom_method = CustomMethod()
    custom_method.find_and_click('내 대출 한도 한번에 조회하기')