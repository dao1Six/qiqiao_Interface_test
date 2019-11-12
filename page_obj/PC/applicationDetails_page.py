#应用详情页面
from page_obj.selenium_page import SeleniumPage

class ApplicationDetailsPage(SeleniumPage):

    ApplicationDetailsPage_treeitem_loc = "//div[@role='treeitem']/*/span[@title='%name']"  #左侧分组或页面元素

    ApplicationDetailsPage_viewbutton_loc = "//button[@type='button']/span[text()='%buttonName']"  #列表按钮

    #点击分组或页面
    def clickTreeItem(self,name,*args):
        '''点击应用页面或菜单
        name：分组或页面名
        '''

        self.clickElemByXpath_Visibility(self.ApplicationDetailsPage_treeitem_loc.replace('%name',name))

    #
    def clickViewButton(self,buttonName,*args):
        '''点击列表头按钮
        buttonName：按钮名称
        '''
        self.clickElemByXpath_Visibility(self.ApplicationDetailsPage_viewbutton_loc.replace('%buttonName',buttonName))


    #查询