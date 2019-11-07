#人员组件
from page_obj.selenium_page import SeleniumPage


class User(SeleniumPage):

    UserquerenButton = "//div[@class='v-modal']//following-sibling::div/div[@aria-label='人员列表']//div[@class='dialog-footer ovf-hd']/button[2]/span"



    # 给人员单选组件输入值
    def sendkeysToMonomialUser(self,fieldName,userName):
        #点击选择框
        self.clickElemByXpath("//div[@title='"+fieldName+"']//span[text()='+选择人员']")
        self.sendkeysElemByXpath("//input[@placeholder='搜索用户']",userName)
        self.clickElemByXpath("//li/span[contains(text(),'"+userName+"')]")
        self.clickElemByXpath(self.UserquerenButton)


    # 给人员多选组件输入值
    def sendkeysToMultiUser(self,fieldName,userNameList):
        #点击选择框
        self.clickElemByXpath("//div[@title='"+fieldName+"']//span[text()='+选择人员']")
        for name in userNameList:
            self.remove_locator_Attr ("//input[@placeholder='搜索用户']", 'readonly')
            self.sendkeysElemByXpath("//input[@placeholder='搜索用户']",name)
            self.clickElemByXpath("//li/span[contains(text(),'"+name+"')]")
        self.clickElemByXpath(self.UserquerenButton)


    # 给部门单选组件输入值
    def sendkeysToMonomialDept(self,fieldName,DeptName):
        #点击选择框
        self.clickElemByXpath("//div[@title='"+fieldName+"']//span[text()='+选择部门']")
        self.sendkeysElemByXpath("//input[@placeholder='搜索部门']",DeptName)
        self.clickElemByXpath("//li/span[contains(text(),'"+DeptName+"')]")
        self.clickElemByXpath(self.UserquerenButton)


    # 给部门多选组件输入值
    def sendkeysToMultiDept(self,fieldName,DeptNameList):
        #点击选择框
        self.clickElemByXpath("//div[@title='"+fieldName+"']//span[text()='+选择部门']")

        for name in DeptNameList:
            self.remove_locator_Attr ("//input[@placeholder='搜索部门']",'readonly')
            self.sendkeysElemByXpath("//input[@placeholder='搜索部门']",name)
            self.clickElemByXpath("//li/span[contains(text(),'"+name+"')]")
        self.clickElemByXpath(self.UserquerenButton)

