#时间组件
from page_obj.selenium_page import SeleniumPage


class Time(SeleniumPage):

    time_input_loc = "div[title='%s'] input[type='text']"
    time_label_loc = "div[title='%s']>label>span[title='%s']"
    #给时间组件输入值
    def sendkeysToTime(self,fieldName,key):
        locator = self.time_input_loc.replace('%s',fieldName)
        self.sendkeysElemByCSS_Visibility(locator, key)
        self.clickElemByCSS_Visibility(self.time_label_loc.replace('%s',fieldName))

    #获取时间组件的值