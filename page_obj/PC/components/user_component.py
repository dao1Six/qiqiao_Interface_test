#人员组件
import time

from page_obj.selenium_page import SeleniumPage


class User(SeleniumPage):

    User_querenButton_loc = "//div[@class='v-modal']//following-sibling::div/div[@aria-label='人员列表']//div[@class='dialog-footer ovf-hd']/button[2]/span" #人员选择确认按钮

    User_selectBox_loc = "//div[@title='%s']//span[text()='+选择人员']"  #人员选择字段添加按钮

    User_search_loc = "//input[@placeholder='搜索用户']"  #人员选择组织架构搜索框

    User_searchOption_loc = "//li/span[contains(text(),'%s')]"  #人员选择组织架构搜索项



    #
    def sendkeysToMonomialUser(self,fieldName,userName):
        '''给人员单选组件输入值
        fieldName：字段标题
        userName：人员名称
        '''
        #点击选择框
        self.clickElemByXpath_Presence(self.User_selectBox_loc.replace('%s',fieldName))
        self.sendkeysElemByXpath_Presence(self.User_search_loc,userName)
        self.clickElemByXpath_Presence(self.User_searchOption_loc.replace('%s',userName))
        self.clickElemByXpath_Presence(self.User_querenButton_loc)



    def sendkeysToMultiUser(self,fieldName,userNameList,*args):
        ''' 给人员多选组件输入值
        fieldName：字段标题
        userNameList：人员名称集合  list类型
        '''
        #点击选择框
        self.clickElemByXpath_Presence(self.User_selectBox_loc.replace('%s',fieldName))
        for name in userNameList:
            self.clickElemByXpath_Presence(self.User_search_loc)
            self.sendkeysElemByXpath_Presence(self.User_search_loc,name)
            self.clickElemByXpath_Presence(self.User_searchOption_loc.replace('%s',name))
        self.clickElemByXpath_Presence(self.User_querenButton_loc)




