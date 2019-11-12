#单行文本组件
from page_obj.selenium_page import SeleniumPage


class Text(SeleniumPage):


    text_Cssloc = "div[title='%s'] input[type='text']"  #单行文本组件字段Css定位

    #
    def sendkeysToText(self,fieldName,key,*args):
        '''给单行文本组件输入值
        fieldName：字段标题
        key：文本值
        '''
        self.sendkeysElemByCSS_Visibility(self.text_Cssloc.replace('%s',fieldName), key)


