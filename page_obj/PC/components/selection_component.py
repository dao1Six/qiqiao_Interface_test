#选择组件


from page_obj.selenium_page import SeleniumPage


class Selection(SeleniumPage):

    Selection_selectionBox_loc = "[data-mark=%title] input"  #下拉选择组件下拉框

    Selection_multiSelectOption_loc = "li[data-mark=%option]" #下拉多选选项

    Selection_monomialSelectOption_loc = "//span[text()='%s']"  #下拉单选选项

    Selection_Option_loc = "//div[@title='%s']//span[text()='%option']"  #单选多选选项

    #
    def sendkeysToMultiSelect(self,fieldName,list,*args):
        '''下拉多选组件输入值
        fieldName：字段标题
        list：下拉选项 list类型
        '''
        loc = self.Selection_selectionBox_loc.replace('%title',fieldName)
        self.clickElemByCSS_Presence(loc)
        for i in list:
            self.clickElemByCSS_Presence(self.Selection_multiSelectOption_loc.replace('%option',i))

    #
    def sendkeysToMonomialSelect(self,fieldName,option,*args):
        '''下拉单选组件输入值
        fieldName：字段标题
        option：下拉选项
        '''
        loc = self.Selection_selectionBox_loc.replace('%title',fieldName)
        self.clickElemByCSS_Presence (loc)
        self.clickElemByXpath_Presence(self.Selection_monomialSelectOption_loc.replace('%s',option))

    #
    def sendkeysToRadioSelect(self,fieldName,option,*args):
        '''给单项选择组件输入值
        fieldName：字段标题
        option：单项选项
        '''
        self.clickElemByXpath_Presence (self.Selection_Option_loc.replace('%s',fieldName).replace('%option',option))


    #
    def sendkeysToCheckboxSelect(self,fieldName,list,*args):
        '''给多项选择组件输入值
        fieldName：字段标题
        list：多项选项 list类型
        '''
        for i in list:
            self.clickElemByXpath_Presence(self.Selection_Option_loc.replace('%s',fieldName).replace('%option',i))