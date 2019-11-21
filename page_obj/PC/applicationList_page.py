#应用列表页面

from page_obj.selenium_page import SeleniumPage


class ApplicationListPage(SeleniumPage):
    '''应用列表页面'''

    ApplicationListPage_application_loc = "[data-mark='%groupName'] [data-mark='%applicationName']"  #应用管理页面应用卡片

    ApplicationListPage_searchInput_loc = "[data-mark=应用名称搜索框]"



    def click_application(self,groupName,title,*args):
        '''点击分组里的应用
        groupName:分组名
        title:应用名称
        '''
        self.clickElemByCSS_Presence (
            self.ApplicationListPage_application_loc.replace ('%groupName', groupName).replace ('%applicationName', title))
