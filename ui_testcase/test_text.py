#测试单行文本控件用例集
import time


from page_obj.login_page import LoginPage
from pubilc.driver import pcdriver
from ui_testcase import myunit
from ui_testcase.myunit import MyTest


class Text(myunit.MyTest):

    # def setUp(self):
    #     #先登录1
    #     self.driver = pcdriver()
    #     self.driver.maximize_window()

    def test_01(self):
        loginpage = LoginPage(self.driver)
        loginpage.user_login("wujianlun@jiekou","qiqiao123")
        time.sleep(5)
