#应用详情页面
from page_obj.selenium_page import SeleniumPage

class ApplicationDetailsPage(SeleniumPage):


    #点击分组或页面
    def clickTreeItem(self,name):
        '''点击应用页面或菜单'''
        self.clickElemByXpath_Visibility("//div[@role='treeitem']/*/span[@title='"+name+"']")

    #点击按钮
    def clickViewButton(self,buttonName):
        self.clickElemByXpath_Visibility("//button[@type='button']/span[text()='"+buttonName+"']")


    #查询