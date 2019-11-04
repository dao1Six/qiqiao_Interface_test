#测试单行文本控件用例集
import time

from page_obj.PC.applicationMenu_page import applicationMenuPage
from page_obj.PC.login_page import LoginPage
from page_obj.PC.portal_page import PortalPage
from page_obj.PC.selenium_page import SeleniumPage
from ui_testcase import myunit


class Text(myunit.MyTest):

    def setUp(self):
        #先登录1
        seleniumPage = SeleniumPage(self.driver)
        loginpage = LoginPage(self.driver)
        loginpage.user_login("wujianlun@jiekou","qiqiao123")
        # h = self.driver.title
        # time.sleep(2)
        # self.assertEqual(h,"接口自动化七巧广泛广泛")
        portalpage = PortalPage(self.driver)
        portalpage.goto_menu("应用")
        applicationPage = applicationMenuPage(self.driver)
        applicationMenuPage.enter_application('接口测试')



    def test_01(self):


        time.sleep(5)
