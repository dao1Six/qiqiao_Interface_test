#日期组件
from page_obj.selenium_page import SeleniumPage


class Data(SeleniumPage):

    #给日期组件输入值
    def sendkeysToData(self,fieldName,key):
        locator = "div[title='"+fieldName+"'] input[type='text']"
        self.sendkeysElemByCSS_Visibility(locator,key)
        self.clickElemByCSS_Visibility("div[title='"+fieldName+"']>label>span[title='"+fieldName+"']")


        # elem = self.find_elemByCSS(locator)
        # elem.clear()
        # self.driver.execute_script("arguments[0].value='"+key+"';",elem)

    #获取日期组件的值