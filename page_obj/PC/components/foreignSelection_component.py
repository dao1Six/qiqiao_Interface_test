#外键
from page_obj.selenium_page import SeleniumPage


class ForeignSelection_component(SeleniumPage):


    def sendkeysToForeignSelection(self,fieldName,list,*args):
        '''外键选择组件输入值
        fieldName：字段标题
        list：下拉选项 list类型
        '''
        loc = self.ForeignSelectionBox_loc.replace('%title',fieldName)
        self.clickElemByCSS_Presence(loc)
        for i in list:
            self.clickElemByCSS_Presence(self.ForeignSelectOption_loc.replace('%option',i))