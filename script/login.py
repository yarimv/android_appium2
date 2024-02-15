from appium.webdriver.webdriver import AppiumBy
from driver import driver_setup
from appium.webdriver.webdriver import AppiumBy
import time
import subprocess
from basemethod.custom_method import CustomMethod
from basemethod.base import Basemethod
from basemethod.report import ResultJoin


class LoginPages:
    def __init__(self):
        # Get the Appium driver
        self.get_driver = driver_setup.get_appium_driver()
        self.bm = Basemethod()
        print("driver start")
        self.action = CustomMethod()
        self.report = ResultJoin()
        self.username = "이아림"
        self.rrn_birth = "880609"
        self.rrn_sex = "2"
        self.user_comm_company = "KT 알뜰폰"



    #test senario

    def 앱종료(self):
        subprocess.run(['adb', 'shell', 'am', 'force-stop', f'{"kr.co.finda.finda"}'])
        time.sleep(3)


    # 앱 실행
    def 앱실행(self):
        self.get_driver.driver.activate_app("kr.co.finda.finda", "kr.co.finda.finda.ui.splash.SplashActivity")
        # subprocess.run(['adb', 'shell', 'am', 'start', '-n', f'{"kr.co.finda.finda"}/{".ui.splash.SplashActivity"}'])
        # time.sleep(5)

    def 회원가입(self):
        self.action.find_and_click("시작하기")

    def 악성앱찾기(self):
        self.action.find_and_click("악성앱 찾기")
        time.sleep(10)

    def 문자인증안내(self):
        self.action.find_and_click("계속하기")
        time.sleep(2)
    def 문자앱(self):
        #전송버튼
        self.action.find_and_click_with_xpath('//android.widget.ImageButton[@content-desc="전송"]')
    def 이름입력(self):
        name_field_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText'
        time.sleep(5)
        result = self.get_driver.driver.find_element(AppiumBy.XPATH, name_field_xpath)
        result.send_keys(self.username)
        self.action.find_and_click("다음")

    def 주민등록번호_입력(self):
        rrn_birth = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[1]"
        rrn_sex = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[2]"
        result = self.get_driver.driver.find_element(AppiumBy.XPATH,rrn_birth)
        time.sleep(2)
        result.send_keys(self.rrn_birth)
        time.sleep(2)
        result = self.get_driver.driver.find_element(AppiumBy.XPATH,rrn_sex)
        time.sleep(2)
        result.send_keys(self.rrn_sex)
        self.action.find_and_click("다음")
        time.sleep(2)
        #통신사 바텀싯
        result = self.action.find_and_click(self.user_comm_company)
        time.sleep(2)
        self.action.find_and_click("다음")

    def 약관확인(self):
        #첫번째 약관 리스트 펼치기 선택
        target = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[1]/android.view.View"
        result = self.get_driver.driver.find_element(AppiumBy.XPATH, target)
        result.click()
        time.sleep(2)
        try:
            self.action.find_and_click("서비스 이용약관 동의")
            time.sleep(3)
            Result_ab = self.get_driver.driver.find_element(AppiumBy.XPATH,'//*[@text ="서비스 이용약관"]')
            self.assertIn("서비스 이용약관", Result_ab.text)
            print("서비스 이용약관 진입 : PASS")
            self.report.append("PASS")
        except AssertionError:
            self.report.append("FAIL")
            print("서비스 이용약관 진입 : FAIL")
            self.bm.save_screenshot('서비스 이용약관 진입 FAIL')
        except Exception as e:
            print("서비스 이용약관 진입 에러 발생 : {}".format(str(e)))
            self.report.append("Error")
            self.bm.save_screenshot('서비스 이용약관 진입 에러 발생')
        finally:
            time.sleep(3)
            self.bm.androidBackKey()
            time.sleep(3)




if __name__ == '__main__':
    login_pages = LoginPages()

    # login_pages.앱실행()
    # login_pages.회원가입()
    # login_pages.악성앱찾기()
    # login_pages.문자인증안내()
    # login_pages.문자앱()
    # login_pages.이름입력()
    # login_pages.주민등록번호_입력()
    login_pages.약관확인()

