#数字组件
from page_obj.selenium_page import SeleniumPage


class Number(SeleniumPage):

    number_Cssloc = "div[title='%s'] input[type='number']"  # 数字组件字段Css定位

    #获取数字组件的值
    def sendkeysToNumber(self,fieldName,key):
        # self.sendkeysElemByCSS_Visibility("div[title='"+fieldName+"'] input[type='number']",key)
        a = self.number_Cssloc.replace('%s',fieldName)
        self.sendkeysElemByCSS_Visibility(a, key)

    #给数字组件输入值