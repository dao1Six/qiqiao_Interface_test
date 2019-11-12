#日期组件
from page_obj.selenium_page import SeleniumPage


class Data(SeleniumPage):

    Data_input_loc = "div[title='%s'] input[type='text']"  # 日期组件输入框

    Data_label_loc = "div[title='%s']>label>span[title='%title']"  # 日期组件字段标题


    #给日期组件输入值
    def sendkeysToData(self,fieldName,key,*args):
        '''给日期组件输入值
        fieldName：字段标题
        key：日期值 格式：2018-11-22
        '''
        self.sendkeysElemByCSS_Visibility(self.Data_input_loc.replace('%s',fieldName),key)
        self.clickElemByCSS_Visibility(self.Data_label_loc.replace('%s',fieldName).replace('%title',fieldName))


        # elem = self.find_elemByCSS(locator)
        # elem.clear()
        # self.driver.execute_script("arguments[0].value='"+key+"';",elem)

    #获取日期组件的值