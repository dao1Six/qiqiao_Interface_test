#地址组件
from page_obj.selenium_page import SeleniumPage


class Address(SeleniumPage):

    cascade_label_Xpath_loc = "//div[@title='%s']//span[@class='el-cascader__label']"  #地址组件字段名
    cascade_menus_Xpath_loc = "//div[@class='el-cascader-menus el-popper']//span[contains(text(),'%s')]"  #地址组件选项
    address_detil_Xpath_loc = "//div[@title='%s']//input[@placeholder='详细地址']"  #地址组件详情输入框

    #给地址组件输入值
    def sendkeysToAddress(self,fieldName,addkeys,detilkey):
        self.clickElemByXpath_Visibility(self.cascade_label_Xpath_loc.replace('%s', fieldName))
        for i in addkeys:
            self.clickElemByXpath_Visibility(self.cascade_menus_Xpath_loc.replace('%s', i))
        self.sendkeysElemByXpath_Visibility(self.address_detil_Xpath_loc.replace('%s', fieldName),detilkey)

