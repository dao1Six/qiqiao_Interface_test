#日期组件
from page_obj.selenium_page import SeleniumPage


class DataTime(SeleniumPage):

    #给日期组件输入值
    def sendkeysToDataTime(self,fieldName,datakey,timekey):
        locator = "div[title='"+fieldName+"'] input[type='text']"
        dataElem = self.find_elemsByCSS(locator)[0]
        timeElem = self.find_elemsByCSS(locator)[1]
        dataElem.send_keys(datakey)
        timeElem.send_keys(timekey)
        self.clickElemByCSS_Visibility("div[title='"+fieldName+"']>label>span[title='"+fieldName+"']")


    #获取日期组件的值