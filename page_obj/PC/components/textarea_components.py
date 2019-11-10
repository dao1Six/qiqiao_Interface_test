#多行文本组件

from page_obj.selenium_page import SeleniumPage


class Textarea(SeleniumPage):
    textarea_input_loc = "div[title='%s'] textarea.el-textarea__inner"
    #获取多行文本组件的值
    def sendkeysToTextarea(self,fieldName,key):
        self.sendkeysElemByCSS_Visibility(self.textarea_input_loc.replace('%s',fieldName),key)


    #给多行文本组件输入值