#多行文本组件

from page_obj.selenium_page import SeleniumPage


class Textarea(SeleniumPage):

    #获取多行文本组件的值
    def sendkeysToText(self,fieldName,key):
        self.sendkeysElemByCSS_Visibility("div[title='"+fieldName+"'] textarea.el-textarea__inner",key)


    #给多行文本组件输入值