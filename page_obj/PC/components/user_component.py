#人员组件
import time

from page_obj.selenium_page import SeleniumPage


class User(SeleniumPage):

    UserquerenButton = "//div[@class='v-modal']//following-sibling::div/div[@aria-label='人员列表']//div[@class='dialog-footer ovf-hd']/button[2]/span"


    DeptquerenButton = "//div[@class='v-modal']//following-sibling::div/div[@aria-label='部门列表']//div[@class='dialog-footer ovf-hd']/button[2]/span"

    user_select_loc = "//div[@title='%s']//span[text()='+选择人员']"

    dept_select_loc = "//div[@title='%s']//span[text()='+选择部门']"

    user_search_loc = "//input[@placeholder='搜索用户']"
    dept_search_loc = "//input[@placeholder='搜索部门']"

    user_option_loc = "//li/span[contains(text(),'%s')]"

    dept_option_loc = "//li/span[contains(text(),'%s')]"


    # 给人员单选组件输入值
    def sendkeysToMonomialUser(self,fieldName,userName):
        #点击选择框
        self.clickElemByXpath_Visibility(self.user_select_loc.replace('%s',fieldName))
        self.sendkeysElemByXpath_Visibility(self.user_search_loc,userName)
        self.clickElemByXpath_Visibility(self.user_option_loc.replace('%s',userName))
        self.clickElemByXpath_Visibility(self.UserquerenButton)


    # 给人员多选组件输入值
    def sendkeysToMultiUser(self,fieldName,userNameList):
        #点击选择框
        self.clickElemByXpath_Visibility(self.user_select_loc.replace('%s',fieldName))
        for name in userNameList:
            self.clickElemByXpath_Visibility(self.user_search_loc)
            self.sendkeysElemByXpath_Visibility(self.user_search_loc,name)
            self.clickElemByXpath_Visibility(self.user_option_loc.replace('%s',name))
        self.clickElemByXpath_Visibility(self.UserquerenButton)


    # 给部门单选组件输入值
    def sendkeysToMonomialDept(self,fieldName,DeptName):
        #点击选择框
        self.clickElemByXpath_Visibility(self.dept_select_loc.replace('%s',fieldName))
        self.sendkeysElemByXpath_Visibility(self.dept_search_loc,DeptName)
        self.clickElemByXpath_Visibility(self.dept_option_loc.replace('%s',DeptName))
        self.clickElemByXpath_Visibility(self.DeptquerenButton)


    # 给部门多选组件输入值
    def sendkeysToMultiDept(self,fieldName,DeptNameList):
        #点击选择框
        self.clickElemByXpath_Visibility(self.dept_select_loc.replace('%s',fieldName))
        for name in DeptNameList:
            self.clickElemByXpath_Visibility (self.dept_search_loc)
            self.sendkeysElemByXpath_Visibility(self.dept_search_loc,name)
            e = self.find_elemByXPATH(self.dept_option_loc.replace('%s',name))
            e.click()
        self.clickElemByXpath_Visibility(self.DeptquerenButton)

