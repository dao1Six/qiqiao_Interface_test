#日期组件
from page_obj.selenium_page import SeleniumPage


class Data(SeleniumPage):

    data_Cssloc = "div[title='%s'] input[type='text']"  # 日期组件字段Css定位
    data_label_Cssloc = "div[title='%s']>label>span[title='%title']"

    #给日期组件输入值
    def sendkeysToData(self,fieldName,key):

        self.sendkeysElemByCSS_Visibility(self.data_Cssloc.replace('%s',fieldName),key)
        self.clickElemByCSS_Visibility(self.data_label_Cssloc.replace('%s',fieldName).replace('%title',fieldName))


        # elem = self.find_elemByCSS(locator)
        # elem.clear()
        # self.driver.execute_script("arguments[0].value='"+key+"';",elem)

    #获取日期组件的值