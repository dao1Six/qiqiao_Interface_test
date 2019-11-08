#富文本组件

from page_obj.selenium_page import SeleniumPage


class WangEditor(SeleniumPage):

    #给富文本组件输入值
    def sendkeysToWangEditor(self,fieldName,key):
        self.sendkeysElemByCSS_Visibility("//div[@title='"+fieldName+"']//div[@class='wangEditor-txt']",key)


