#日期组件
from page_obj.selenium_page import SeleniumPage


class DataTime(SeleniumPage):

    data_Cssloc = "div[title='%s'] input[type='text']"  # 日期组件字段Css定位
    data_label_Cssloc = "div[title='%s']>label>span[title='%title']"

    #给日期组件输入值
    def sendkeysToDataTime(self,fieldName,datakey,timekey):
        locator = self.data_Cssloc.replace('%s',fieldName)
        dataElem = self.find_elemsByCSS(locator)[0]
        timeElem = self.find_elemsByCSS(locator)[1]
        dataElem.send_keys(datakey)
        timeElem.send_keys(timekey)
        self.clickElemByCSS_Visibility(self.data_label_Cssloc.replace('%s',fieldName).replace('%title',fieldName))


    #获取日期组件的值