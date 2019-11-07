#地址组件
from page_obj.selenium_page import SeleniumPage


class Address(SeleniumPage):

    #输入地址组件的值
    def sendkeysToAddress(self,fieldName,addkeys,detilkey):
        self.clickElemByXpath_Visibility("//div[@title='"+fieldName+"']//span[@class='el-cascader__label']")
        for i in addkeys:
            self.clickElemByXpath_Visibility("//div[@class='el-cascader-menus el-popper']//span[text()='"+i+"']")
        self.sendkeysElemByXpath_Visibility("//div[@title='"+fieldName+"']//input[@placeholder='详细地址']",detilkey)
    #给地址组件输入值