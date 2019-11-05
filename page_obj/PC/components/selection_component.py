#选择组件
from page_obj.selenium_page import SeleniumPage


class Selection(SeleniumPage):

    #获取选择组件的值
    def sendkeysToSelection(self,fieldName,key):
        self.sendkeysElemByCSS("div[title='"+fieldName+"'] input[type='text']",key)

    #给选择组件输入值