from appium import webdriver
from driver.driver_setup import get_appium_driver
import os
class Basemethod():
    def __init__(self):
        self.driver = get_appium_driver.driver

    def androidBackKey(self):
        self.driver.press_keycode(4)

    def saveScreenshot(self, name):
        directory = 'screenshots'
        if not os.path.exists(directory):
            os.mkdir(directory)
        else:
            screenshot_path = os.path.join(directory, f'{name}.png')
            self.driver.save_screenshot(screenshot_path)
            print(f'screenshat saverd. the file name: {screenshot_path}')

if __name__ == '__main__':
    basemethod = Basemethod()
    basemethod.androidBackKey()