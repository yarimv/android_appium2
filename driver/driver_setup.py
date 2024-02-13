from appium import webdriver

def get_appium_driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "R5CRB2P3KDM",
        "appPackage": "your.app.package",
        "appActivity": "your.app.activity",
        "platformVersion": "Android_version",
        # Add other desired capabilities as needed
    }

    # Initialize the Appium driver
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    return driver
