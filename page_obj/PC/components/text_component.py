#单行文本组件
from page_obj.selenium_page import SeleniumPage


class Text(SeleniumPage):

    #获取单行文本组件的值
    def sendkeysToText(self,fieldName,key):
        self.sendkeysElemByCSS("div[title='"+fieldName+"'] input[type='text']",key)


    #给单行文本组件输入值