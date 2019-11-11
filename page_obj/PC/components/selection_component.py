#选择组件


from page_obj.selenium_page import SeleniumPage


class Selection(SeleniumPage):

    selection_input_Cssloc = "div[title='%s'] input[type='text']"  #下拉单选和多选的输入框

    multiSelect_Xpathloc = "//div[text()='%s']" #下拉多选选项
    monomialSelect_loc = "//span[text()='%s']"  #下拉单选选项

    RadioSelect_loc = "//div[@title='%s']//span[text()='%option']"  #单选多选选项

    #下拉多选组件输入值
    def sendkeysToMultiSelect(self,fieldName,list):
        loc = self.selection_input_Cssloc.replace('%s',fieldName)
        self.clickElemByCSS_Visibility(loc)
        for i in list:
            self.clickElemByXpath_Visibility(self.multiSelect_Xpathloc.replace('%s',i))

    #下拉单选组件输入值
    def sendkeysToMonomialSelect(self,fieldName,option):
        loc = self.selection_input_Cssloc.replace('%s',fieldName)
        self.clickElemByCSS_Visibility (loc)
        self.clickElemByXpath_Visibility(self.monomialSelect_loc.replace('%s',option))

    #给单项选择组件输入值
    def sendkeysToRadioSelect(self,fieldName,option):
        self.clickElemByXpath_Visibility (self.RadioSelect_loc.replace('%s',fieldName).replace('%option',option))


    #给多项选择组件输入值
    def sendkeysToCheckboxSelect(self,fieldName,list):
        for i in list:
            self.clickElemByXpath_Visibility(self.RadioSelect_loc.replace('%s',fieldName).replace('%option',i))