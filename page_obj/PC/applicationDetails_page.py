#应用详情页面
from page_obj.selenium_page import SeleniumPage

class ApplicationDetailsPage(SeleniumPage):

    ApplicationDetailsPage_treeitem_loc = "//div[@role='treeitem']/*/span[@title='%name']"  #左侧分组或页面元素

    ApplicationDetailsPage_viewbutton_loc = "//button[@type='button']/span[text()='%buttonName']"  #列表按钮

    #点击分组或页面
    def clickTreeItem(self,name):
        '''点击应用页面或菜单'''
        self.clickElemByXpath_Visibility(self.ApplicationDetailsPage_treeitem_loc.replace('%name',name))

    #点击按钮
    def clickViewButton(self,buttonName):
        self.clickElemByXpath_Visibility(self.ApplicationDetailsPage_viewbutton_loc.replace('%buttonName',buttonName))


    #查询