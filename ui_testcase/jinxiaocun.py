import os
import time
import unittest

from page_obj.PC.applicationDetails_page import ApplicationDetailsPage
from page_obj.PC.applicationList_page import ApplicationListPage
from page_obj.PC.form_page import FormPage
from page_obj.PC.login_page import LoginPage
from page_obj.PC.portal_page import PortalPage
from pubilc.driver import pcdriver


class JinXiaoCun(unittest.TestCase):


    project_path = os.path.abspath(os.path.dirname(__file__)).split('qiqiao_Interface_test')[0]+'\\qiqiao_Interface_test'


    @classmethod
    def setUpClass(cls):
        cls.driver = pcdriver()
        cls.driver.maximize_window()



    def tearDown(cls):
        cls.driver.quit()


    def test_1_addPro_record(self):
        '''应用管理员录入商品信息'''
        loginpage = LoginPage (self.driver)
        loginpage.user_login ('https://tqy.do1.net.cn/dev-runtime/', "liuyan@A", "qiqiao123")
        portalpage = PortalPage (self.driver)
        portalpage.click_header_menu ("应用")
        applicationPage = ApplicationListPage (self.driver)
        applicationPage.click_application ('默认分组', "进销存")
        applicationDetailPage = ApplicationDetailsPage (self.driver)
        applicationDetailPage.clickTreeItem('基础信息')
        applicationDetailPage.clickTreeItem ('产品管理')
        applicationDetailPage.clickViewButton('添加')
        formPage = FormPage(self.driver)
        formPage.sendkeysToText('产品名称','榴莲')
        formPage.sendkeysToPicUpload('产品图片',self.project_path+'\\file_data\\pic.jpeg')
        formPage.sendkeysToTextarea('产品描述','的哈加达还是觉得哈师大库哈斯打赏')
        formPage.sendkeysToNumber('建议采购价',80)
        formPage.sendkeysToNumber ('建议销售价', 80)
        formPage.click_submit_button()
        applicationDetailPage.get_viewList_CellValue()



    def test_2_addSupplier_record(self):
        '''应用管理员录入供应商信息'''
        loginpage = LoginPage (self.driver)
        loginpage.user_login ('https://tqy.do1.net.cn/dev-runtime/', "liuyan@A", "qiqiao123")
        portalpage = PortalPage (self.driver)
        portalpage.click_header_menu ("应用")
        applicationPage = ApplicationListPage (self.driver)
        applicationPage.click_application ('默认分组', "进销存")
        applicationDetailPage = ApplicationDetailsPage (self.driver)
        applicationDetailPage.clickTreeItem('基础信息')
        applicationDetailPage.clickTreeItem ('供应商管理')
        applicationDetailPage.clickViewButton('添加')
        formPage = FormPage (self.driver)
        formPage.sendkeysToText ('供应商名称', '')
        #点击子表添加按钮
        formPage.click_ChildForm_AddButton('联系人')
        formPage.sendkeys_To_ChildFormText('联系人',1,'姓名','刘能')
        formPage.sendkeys_To_ChildSelect('联系人',1,'性别',['女'])
        #点击子表添加按钮
        formPage.click_ChildForm_AddButton('联系人')
        formPage.sendkeys_To_ChildFormText('联系人',2,'姓名','刘能')
        formPage.sendkeys_To_ChildSelect('联系人',2,'性别',['女'])
        time.sleep(10)



    def test_3_addCustomer_record(self):
        '''应用管理员录入客户信息'''
        loginpage = LoginPage (self.driver)
        loginpage.user_login ('https://tqy.do1.net.cn/dev-runtime/', "liuyan@A", "qiqiao123")
        portalpage = PortalPage (self.driver)
        portalpage.click_header_menu ("应用")
        applicationPage = ApplicationListPage (self.driver)
        applicationPage.click_application ('杨李杰的分组', "1.01")
        applicationDetailPage = ApplicationDetailsPage (self.driver)
        applicationDetailPage.clickTreeItem('关联组件')
        applicationDetailPage.clickTreeItem ('子表组件')
        applicationDetailPage.clickViewButton('添加')
        formPage = FormPage (self.driver)
        #点击子表添加按钮
        formPage.click_ChildForm_AddButton('子表单组件')
        #
        # formPage.sendkeys_To_ChildSelect('子表单组件',1,'单选',['java'])
        # formPage.sendkeys_To_ChildSelect ('子表单组件', 1, '下拉', ['足球'])
        # # formPage.sendkeys_To_ChildSelect ('子表单组件', 1, '多选', ['苹果','华为'])
        # formPage.sendkeys_To_ChildPicUpload('子表单组件', '图片上传',1, self.project_path+'\\file_data\\pic.jpeg')
        # formPage.sendkeys_To_ChildFormDate('子表单组件','日期',1,'2018-11-22')
        # formPage.sendkeys_To_ChildFormTime ('子表单组件', '时间', 1,'19:20')
        # formPage.sendkeys_To_ChildFormDateTime ('子表单组件', '日期时间', 1,'2018-11-22','19:20')
        formPage.sendkeys_To_ChildFormUser('子表单组件', '人员选择', 1)
        time.sleep(30)

    def test_4_addCustomer_record(self):
        '''多表关联'''
        loginpage = LoginPage (self.driver)
        loginpage.user_login ('https://tqy.do1.net.cn/dev-runtime/', "liuyan@A", "qiqiao123")
        portalpage = PortalPage (self.driver)
        portalpage.click_header_menu ("应用")
        applicationPage = ApplicationListPage (self.driver)
        applicationPage.click_application ('杨李杰的分组', "1.01")
        applicationDetailPage = ApplicationDetailsPage (self.driver)
        applicationDetailPage.clickTreeItem('关联组件')
        applicationDetailPage.clickTreeItem ('多表组件表单')
        applicationDetailPage.clickViewButton('添加')
        formPage = FormPage (self.driver)
        # 点击多表关联组件的批量管理按钮
        formPage.click_MultiFormAssociation_HandleManagerButton('多表关联组件')
        #勾选几条记录
        formPage.tick_MultiFormManagementDialog_Record('多表关联组件',[1,2])
        # formPage.click_MultiFormManagementDialog_ConfirmButton('多表关联组件')

        #点击添加按钮
        formPage.sendkeys_To_MultiFormText('多表关联组件',1,'中间表_单行文本','dadasdksadhashdjashjd')

        time.sleep (30)

