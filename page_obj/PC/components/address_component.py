#地址组件
from page_obj.selenium_page import SeleniumPage


class Address(SeleniumPage):

    Address_selectionBox_loc = "//div[@title='%s']//span[@class='el-cascader__label']"  #地址组件字段选择下拉框
    Address_selecOption_loc = "//div[@class='el-cascader-menus el-popper']//span[contains(text(),'%s')]"  #地址组件字段选项
    Address_detilInput_loc = "//div[@title='%s']//input[@placeholder='详细地址']"  #地址组件字段地址详情输入框

    #给地址组件输入值
    def sendkeysToAddress(self,fieldName,addkeys,detilkey,*args):
        '''给地址组件字段输入值
        fieldName：字段标题
        addkeys：省市区地址  list类型
        detilkey：详情地址信息
        '''
        self.clickElemByXpath_Presence(self.Address_selectionBox_loc.replace('%s', fieldName))
        for i in addkeys:
            self.clickElemByXpath_Presence(self.Address_selecOption_loc.replace('%s', i))
        self.sendkeysElemByXpath_Presence(self.Address_detilInput_loc.replace('%s', fieldName),detilkey)

