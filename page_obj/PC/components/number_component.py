#数字组件
from page_obj.selenium_page import SeleniumPage


class Number(SeleniumPage):

    number_Cssloc = "div[title='%s'] input[type='number']"  # 数字组件字段输入框

    #
    def sendkeysToNumber(self,fieldName,key,*args):
        '''给数字组件输入值
        fieldName：字段标题
        key：数值  数字类型
        '''
        a = self.number_Cssloc.replace('%s',fieldName)
        self.sendkeysElemByCSS_Visibility(a, key)

