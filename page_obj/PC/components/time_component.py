#时间组件
from page_obj.selenium_page import SeleniumPage


class Time(SeleniumPage):

    #给时间组件输入值
    def sendkeysToTime(self,fieldName,key):
        locator = "div[title='" + fieldName + "'] input[type='text']"
        self.sendkeysElemByCSS_Visibility(locator, key)
        self.clickElemByCSS_Visibility("div[title='" + fieldName + "']>label>span[title='" + fieldName + "']")

    #获取时间组件的值