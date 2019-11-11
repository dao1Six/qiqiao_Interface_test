#应用管理页面

from page_obj.selenium_page import SeleniumPage


class ApplicationMenuPage(SeleniumPage):
    '''应用管理页面'''

    ApplicationMenuPage_application_card_loc = "div.precessCenter_card1 > div.el-collapse-item__wrap a[title='%name']"  #应用管理页面应用卡片

    #查询应用



    def click_application_card(self,name):
        '''点击固定分组的应用
        name:应用名称
        '''
        self.clickElemByCSS_Visibility(self.ApplicationMenuPage_application_card_loc.replace('%name',name))
