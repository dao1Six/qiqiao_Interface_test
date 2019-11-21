#应用详情页面
from page_obj.selenium_page import SeleniumPage

class ApplicationDetailsPage(SeleniumPage):


    ApplicationDetailsPage_treeitem_loc = "[data-mark=left_bar_%menuName]" #左侧分组或页面元素

    ApplicationDetailsPage_viewbutton_loc = '[data-mark=%btnName] button'

    ApplicationDetailsPage_ViewListCell_loc = ''  #列表单元格





    #点击分组或页面
    def clickTreeItem(self,menuName,*args):
        '''点击应用页面或菜单
        name：分组或页面名
        '''

        self.clickElemByCSS_Presence(self.ApplicationDetailsPage_treeitem_loc.replace('%menuName',menuName))

    #
    def clickViewButton(self,buttonName,*args):
        '''点击列表头按钮
        buttonName：按钮名称
        '''
        self.clickElemByCSS_Visibility(self.ApplicationDetailsPage_viewbutton_loc.replace('%btnName',buttonName))

    def get_viewList_CellValue(self,*args):
        '''获取列表某个单元格的值'''
        pass


    #点击查询按钮

    #点击重置按钮

    #切换选项卡

    #