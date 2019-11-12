#多行文本组件

from page_obj.selenium_page import SeleniumPage


class Textarea(SeleniumPage):

    Textarea_input_loc = "div[title='%s'] textarea.el-textarea__inner"  #多行文本组件字段输入框

    #
    def sendkeysToTextarea(self,fieldName,key,*args):
        '''给多行文本组件输入值
        fieldName：字段标题
        key：文本值
        '''
        self.sendkeysElemByCSS_Visibility(self.Textarea_input_loc.replace('%s',fieldName),key)


