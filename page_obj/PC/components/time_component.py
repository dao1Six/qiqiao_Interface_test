#时间组件
from page_obj.selenium_page import SeleniumPage


class Time(SeleniumPage):

    Time_input_loc = "div[title='%s'] input[type='text']"  #时间组件字段输入框

    Time_label_loc = "div[title='%s']>label>span[title='%s']"  #时间组件字段名

    #
    def sendkeysToTime(self,fieldName,key,*args):
        '''给时间组件输入值
        fieldName：字段标题
        key：时间值  格式：19:20
        '''
        locator = self.Time_input_loc.replace('%s',fieldName)
        self.sendkeysElemByCSS_Visibility(locator, key)
        self.clickElemByCSS_Presence(self.Time_label_loc.replace('%s',fieldName))

    #获取时间组件的值