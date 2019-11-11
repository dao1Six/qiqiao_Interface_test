#人员组件
import time

from page_obj.selenium_page import SeleniumPage


class User(SeleniumPage):

    UserquerenButton = "//div[@class='v-modal']//following-sibling::div/div[@aria-label='人员列表']//div[@class='dialog-footer ovf-hd']/button[2]/span" #人员选择确认按钮

    user_select_loc = "//div[@title='%s']//span[text()='+选择人员']"  #人员选择字段添加按钮

    user_search_loc = "//input[@placeholder='搜索用户']"  #人员选择组织架构搜索框

    user_option_loc = "//li/span[contains(text(),'%s')]"  #人员选择组织架构搜索项



    #
    def sendkeysToMonomialUser(self,fieldName,userName):
        '''给人员单选组件输入值
        fieldName：字段标题
        userName：人员名称
        '''
        #点击选择框
        self.clickElemByXpath_Visibility(self.user_select_loc.replace('%s',fieldName))
        self.sendkeysElemByXpath_Visibility(self.user_search_loc,userName)
        self.clickElemByXpath_Visibility(self.user_option_loc.replace('%s',userName))
        self.clickElemByXpath_Visibility(self.UserquerenButton)



    def sendkeysToMultiUser(self,fieldName,userNameList):
        ''' 给人员多选组件输入值
        fieldName：字段标题
        userNameList：人员名称集合  list类型
        '''
        #点击选择框
        self.clickElemByXpath_Visibility(self.user_select_loc.replace('%s',fieldName))
        for name in userNameList:
            self.clickElemByXpath_Visibility(self.user_search_loc)
            self.sendkeysElemByXpath_Visibility(self.user_search_loc,name)
            self.clickElemByXpath_Visibility(self.user_option_loc.replace('%s',name))
        self.clickElemByXpath_Visibility(self.UserquerenButton)




