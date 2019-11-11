#部门组件
import time

from page_obj.selenium_page import SeleniumPage


class Dept(SeleniumPage):


    Dept_querenButton = "//div[@class='v-modal']//following-sibling::div/div[@aria-label='部门列表']//div[@class='dialog-footer ovf-hd']/button[2]/span"  #部门选择确认按钮

    dept_select_loc = "//div[@title='%s']//span[text()='+选择部门']"  #部门选择字段添加按钮


    dept_search_loc = "//input[@placeholder='搜索部门']"  #部门选择组织架构搜索框


    dept_option_loc = "//li/span[contains(text(),'%s')]" #部门选择组织架构搜索项


    # 给部门单选组件输入值
    def sendkeysToMonomialDept(self,fieldName,DeptName):
        ''' 给部门单选组件输入值
        fieldName：字段标题
        DeptName：部门名称
        '''
        #点击选择框
        self.clickElemByXpath_Visibility(self.dept_select_loc.replace('%s',fieldName))
        self.sendkeysElemByXpath_Visibility(self.dept_search_loc,DeptName)
        self.clickElemByXpath_Visibility(self.dept_option_loc.replace('%s',DeptName))
        self.clickElemByXpath_Visibility(self.Dept_querenButton)


    # 给部门多选组件输入值
    def sendkeysToMultiDept(self,fieldName,DeptNameList):
        ''' 给部门单选组件输入值
        fieldName：字段标题
        DeptNameList：部门名称集合  list类型
        '''
        #点击选择框
        self.clickElemByXpath_Visibility(self.dept_select_loc.replace('%s',fieldName))
        for name in DeptNameList:
            self.clickElemByXpath_Visibility (self.dept_search_loc)
            self.sendkeysElemByXpath_Visibility(self.dept_search_loc,name)
            e = self.find_elemByXPATH(self.dept_option_loc.replace('%s',name))
            e.click()
        self.clickElemByXpath_Visibility(self.Dept_querenButton)

