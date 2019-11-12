#应用管理页面

from page_obj.selenium_page import SeleniumPage


class ApplicationMenuPage(SeleniumPage):
    '''应用管理页面'''

    ApplicationMenuPage_application_card_loc = "//span[contains(text(),'%groupName')]/ancestor::div[@class='el-collapse-item is-active precessCenter_card precessCenter_card1']//a[@title='%title']"  #应用管理页面应用卡片

    #查询应用



    def click_application_card(self,groupName,title,*args):
        '''点击分组里的应用
        groupName:分组名
        title:应用名称
        '''
        self.clickElemByXpath_Visibility(self.ApplicationMenuPage_application_card_loc.replace('%groupName',groupName).replace('%title',title))
