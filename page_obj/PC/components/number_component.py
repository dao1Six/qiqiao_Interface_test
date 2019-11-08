#数字组件
from page_obj.selenium_page import SeleniumPage


class Number(SeleniumPage):

    #获取数字组件的值
    def sendkeysToNumber(self,fieldName,key):
        self.sendkeysElemByCSS_Visibility("div[title='"+fieldName+"'] input[type='number']",key)

    #给数字组件输入值