#测试单行文本控件用例集
import os
import time
import unittest

from page_obj.PC.applicationDetails_page import ApplicationDetailsPage
from page_obj.PC.applicationMenu_page import ApplicationMenuPage
from page_obj.PC.form_page import FormPage
from page_obj.PC.login_page import LoginPage
from page_obj.PC.portal_page import PortalPage
from page_obj.selenium_page import SeleniumPage
from reportRunner import Report
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
        # formPage.sendkeysToMultiSelect('多项下拉',['选项一','选项二'])
        # formPage.sendkeysToMonomialSelect('单项下拉','选项一')
        # formPage.sendkeysToRadioSelect('单项选择','苹果')
        # formPage.sendkeysToCheckboxSelect ('多项选择', ['中国','德国'])
        # formPage.sendkeysToData("日期",'2018-11-22')
        # formPage.sendkeysToTime("时间",'19:20')
        # formPage.sendkeysToDataTime("日期时间",'2018-11-22','19:20')
        # formPage.sendkeysToPicUpload("图片上传",self.picpath)
        # formPage.sendkeysToFileUpload("文件上传",self.picpath)
        # formPage.sendkeysToMonomialUser('人员单选','吴健伦')
        # formPage.sendkeysToMultiUser ('人员多选', ['吴健伦','王浩'])
        # formPage.sendkeysToMonomialDept ('部门单选', '创新')
        # formPage.sendkeysToMultiDept ('部门多选', ['创新','董办'])
        formPage.sendkeysToCascade('级联选择','A/a')
        # formPage.sendkeysToCascade('级联选择', ['A','a'])
        # formPage.sendkeysToAddress('地址选择器', ['四川省', '眉山市','彭山县'],'到ID阿段搜ID结案率扩大')
        formPage.submit_doc()


        time.sleep(5)


