#选择组件


from page_obj.selenium_page import SeleniumPage


class Selection(SeleniumPage):

    #下拉多选组件输入值
    def sendkeysToMultiSelect(self,fieldName,list):
        loc = "div[title='"+fieldName+"'] input[type='text']"
        self.clickElemByCSS_Visibility(loc)
        for i in list:
            self.clickElemByXpath_Visibility("//div[text()='"+i+"']")

    #下拉单选组件输入值
    def sendkeysToMonomialSelect(self,fieldName,option):
        loc = "div[title='"+fieldName+"'] input[type='text']"
        self.clickElemByCSS_Visibility (loc)
        self.clickElemByXpath_Visibility("//span[text()='"+option+"']")

    #给单项选择组件输入值
    def sendkeysToRadioSelect(self,fieldName,option):
        self.clickElemByXpath_Visibility ("//div[@title='" + fieldName + "']//span[text()='" + option + "']")


    #给多项选择组件输入值
    def sendkeysToCheckboxSelect(self,fieldName,list):
        for i in list:
            self.clickElemByXpath_Visibility("//div[@title='"+fieldName+"']//span[text()='"+i+"']")