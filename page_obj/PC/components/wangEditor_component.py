#富文本组件

from page_obj.selenium_page import SeleniumPage


class WangEditor(SeleniumPage):


    WangEditor_input_loc = "//div[@title='%s']//div[@class='wangEditor-txt']"  #富文本输入框

    #
    def sendkeysToWangEditor(self,fieldName,key,*args):
        '''给富文本组件输入值
        fieldName：字段标题
        key：文本值
        '''
        self.sendkeysElemByCSS_Visibility(self.WangEditor_input_loc.replace('%s',fieldName),key)


