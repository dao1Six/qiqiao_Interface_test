#日期组件
from page_obj.selenium_page import SeleniumPage


class Data(SeleniumPage):

    #获取日期组件的值
    def sendkeysToData(self,fieldName,key):

        self.sendkeysElemByCSS("div[title='"+fieldName+"'] input[type='text']",key)

    #给日期组件输入值