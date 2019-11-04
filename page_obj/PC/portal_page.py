#应用门户页面
from page_obj.PC.selenium_page import SeleniumPage


class PortalPage(SeleniumPage):
    '''应用门户页面'''

    #Action



    #传入menu名进入
    def goto_menu(self,menu):

        self.find_elem_visibleByXPATH("//a[@class='header_menu_title' and text()='"+menu+"']").click()



    #进入应用页面


    #获取常用应用数


    #获取常用流程数


    #获取