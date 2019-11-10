#工作台页面

from page_obj.selenium_page import SeleniumPage


class PortalPage(SeleniumPage):
    '''工作台页面'''

    #Action
    header_menu_title_loc = "//a[@class='header_menu_title' and text()='%menu']"



    #点击菜单进入相应菜单页面
    def goto_menuPage(self,menu):

        self.clickElemByXpath_Visibility(self.header_menu_title_loc.replace('%menu',menu))



    #进入应用页面


    #获取常用应用数


    #获取常用流程数


    #获取