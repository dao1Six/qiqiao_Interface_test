#级联组件
from page_obj.selenium_page import SeleniumPage


class Cascade(SeleniumPage):

    cascade_label_Xpath_loc = "//div[@title='%s']//span[@class='el-cascader__label']"
    cascade_menus_Xpath_loc = "//div[@class='el-cascader-menus el-popper']//span[contains(text(),'%s')]"

    #输入级联组件的值
    def sendkeysToCascade(self,fieldName,keys):

        self.clickElemByXpath_Visibility(self.cascade_label_Xpath_loc.replace('%s', fieldName))
        for i in keys:
            self.clickElemByXpath_Visibility(self.cascade_menus_Xpath_loc.replace('%s', i))

    #给级联组件输入值