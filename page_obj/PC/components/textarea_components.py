#多行文本组件

from page_obj.selenium_page import SeleniumPage


class Textarea(SeleniumPage):
    textarea_input_loc = "div[title='%s'] textarea.el-textarea__inner"  #多行文本组件字段输入框

    #给多行文本组件输入值
    def sendkeysToTextarea(self,fieldName,key):
        self.sendkeysElemByCSS_Visibility(self.textarea_input_loc.replace('%s',fieldName),key)


