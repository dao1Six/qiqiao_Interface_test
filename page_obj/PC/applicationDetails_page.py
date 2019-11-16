#应用详情页面
from page_obj.selenium_page import SeleniumPage

class ApplicationDetailsPage(SeleniumPage):

    # ApplicationDetailsPage_treeitem_loc = "//div[@role='treeitem']/*/span[@title='%name']"  #左侧分组或页面元素

    # ApplicationDetailsPage_viewbutton_loc = "//button[@type='button']/span[text()='%buttonName']"  #列表按钮


    ApplicationDetailsPage_treeitem_loc = "[data-mark=%applicationName] [data-mark=%menuName]" #左侧分组或页面元素

    ApplicationDetailsPage_viewbutton_loc = '[data-mark=%btnName] button'



    #点击分组或页面
    def clickTreeItem(self,applicationName,menuName,*args):
        '''点击应用页面或菜单
        name：分组或页面名
        '''

        self.clickElemByCSS_Visibility(self.ApplicationDetailsPage_treeitem_loc.replace('%applicationName',applicationName).replace('%menuName',menuName))

    #
    def clickViewButton(self,buttonName,*args):
        '''点击列表头按钮
        buttonName：按钮名称
        '''
        self.clickElemByCSS_Visibility(self.ApplicationDetailsPage_viewbutton_loc.replace('%btnName',buttonName))


    #查询