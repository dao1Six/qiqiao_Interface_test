#测试单行文本控件用例集
import os
import time

from page_obj.PC.applicationDetails_page import ApplicationDetailsPage
from page_obj.PC.applicationMenu_page import ApplicationMenuPage
from page_obj.PC.form_page import FormPage
from page_obj.PC.login_page import LoginPage
from page_obj.PC.portal_page import PortalPage
from page_obj.selenium_page import SeleniumPage
from ui_testcase import myunit


class Text(myunit.MyTest):

    project_path = os.path.abspath(os.path.dirname(__file__)).split('qiqiao_Interface_test')[0]+'\\qiqiao_Interface_test'
    picpath = project_path+'\\file_data\\pic.jpeg'


    def setUp(self):
        #先登录1
        seleniumPage = SeleniumPage(self.driver)
        loginpage = LoginPage(self.driver)
        loginpage.user_login("wujianlun@jiekou","qiqiao123")
        portalpage = PortalPage(self.driver)
        portalpage.goto_menu("应用")
        applicationPage = ApplicationMenuPage(self.driver)
        applicationPage.enter_application("接口测试")



    def test_01(self):
        applicationDetailPage = ApplicationDetailsPage (self.driver)
        applicationDetailPage.clickViewButton("添加")
        formPage = FormPage(self.driver)
        formPage.sendkeysToData("日期",'2018-11-22')
        formPage.sendkeysToTime("时间",'19:20')
        formPage.sendkeysToDataTime("日期时间",'2018-11-22','19:20')
        formPage.sendkeysToPicUpload("图片上传",self.picpath)
        formPage.submit_doc()

        time.sleep(5)
