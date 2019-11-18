import unittest

from page_obj.PC.applicationDetails_page import ApplicationDetailsPage
from page_obj.PC.applicationList_page import ApplicationListPage
from page_obj.PC.form_page import FormPage
from page_obj.PC.login_page import LoginPage
from page_obj.PC.portal_page import PortalPage
from pubilc.driver import pcdriver


class JinXiaoCun(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = pcdriver()
        cls.driver.maximize_window()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_1_addPro_record(self):
        '''应用管理员录入商品信息'''
        loginpage = LoginPage (self.driver)
        loginpage.user_login ('https://qy.do1.com.cn/qiqiao/runtime', "liuyan@A", "qiqiao123")
        portalpage = PortalPage (self.driver)
        portalpage.click_header_menu ("应用")
        applicationPage = ApplicationListPage (self.driver)
        applicationPage.click_application ('默认分组', "进销存")
        applicationDetailPage = ApplicationDetailsPage (self.driver)
        applicationDetailPage.clickTreeItem('进销存','基础信息')
        applicationDetailPage.clickTreeItem ('进销存', '产品管理')
        applicationDetailPage.clickViewButton('添加')
        formPage = FormPage(self.driver)
        formPage.sendkeysToText('产品名称','')

        applicationDetailPage.get_viewList_CellValue()



    def test_2_addSupplier_record(self):
        '''应用管理员录入供应商信息'''


