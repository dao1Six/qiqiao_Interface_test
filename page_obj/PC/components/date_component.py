#日期组件
from page_obj.selenium_page import SeleniumPage


class Date(SeleniumPage):

    Date_input_loc = "div[title='%s'] input[type='text']"  # 日期组件输入框

    Date_label_loc = "div[title='%s']>label>span[title='%title']"  # 日期组件字段标题


    #给日期组件输入值
    def sendkeysToDate(self,fieldName,key,*args):
        '''给日期组件输入值
        fieldName：字段标题
        key：日期值 格式：2018-11-22
        '''
        self.sendkeysElemByCSS_Visibility(self.Date_input_loc.replace('%s',fieldName),key)
        self.clickElemByCSS_Presence(self.Date_label_loc.replace('%s',fieldName).replace('%title',fieldName))


    #获取日期组件的值