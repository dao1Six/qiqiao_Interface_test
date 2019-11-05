#时间组件
from page_obj.selenium_page import SeleniumPage


class Time(SeleniumPage):

    #获取时间组件的值
    def sendkeysToTime(self,fieldName,key):
        self.sendkeysElemByCSS("div[title='"+fieldName+"'] input[type='text']",key)

    #给时间组件输入值