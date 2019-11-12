#选择组件


from page_obj.selenium_page import SeleniumPage


class Selection(SeleniumPage):

    selection_input_Cssloc = "div[title='%s'] input[type='text']"  #下拉单选和多选的输入框

    multiSelect_Xpathloc = "//div[text()='%s']" #下拉多选选项
    monomialSelect_loc = "//span[text()='%s']"  #下拉单选选项

    RadioSelect_loc = "//div[@title='%s']//span[text()='%option']"  #单选多选选项

    #
    def sendkeysToMultiSelect(self,fieldName,list,*args):
        '''下拉多选组件输入值
        fieldName：字段标题
        list：下拉选项 list类型
        '''
        loc = self.selection_input_Cssloc.replace('%s',fieldName)
        self.clickElemByCSS_Visibility(loc)
        for i in list:
            self.clickElemByXpath_Visibility(self.multiSelect_Xpathloc.replace('%s',i))

    #
    def sendkeysToMonomialSelect(self,fieldName,option,*args):
        '''下拉单选组件输入值
        fieldName：字段标题
        option：下拉选项
        '''
        loc = self.selection_input_Cssloc.replace('%s',fieldName)
        self.clickElemByCSS_Visibility (loc)
        self.clickElemByXpath_Visibility(self.monomialSelect_loc.replace('%s',option))

    #
    def sendkeysToRadioSelect(self,fieldName,option,*args):
        '''给单项选择组件输入值
        fieldName：字段标题
        option：单项选项
        '''
        self.clickElemByXpath_Visibility (self.RadioSelect_loc.replace('%s',fieldName).replace('%option',option))


    #
    def sendkeysToCheckboxSelect(self,fieldName,list,*args):
        '''给多项选择组件输入值
        fieldName：字段标题
        list：多项选项 list类型
        '''
        for i in list:
            self.clickElemByXpath_Visibility(self.RadioSelect_loc.replace('%s',fieldName).replace('%option',i))