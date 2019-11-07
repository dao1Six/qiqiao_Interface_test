#级联组件
from page_obj.selenium_page import SeleniumPage


class Cascade(SeleniumPage):

    #输入级联组件的值
    def sendkeysToCascade(self,fieldName,keys):
        self.clickElemByXpath_Visibility("//div[@title='"+fieldName+"']//span[@class='el-cascader__label']")
        for i in keys:
            self.clickElemByXpath_Visibility("//div[@class='el-cascader-menus el-popper']//span[contains(text(),'"+i+"')]")

    #给级联组件输入值