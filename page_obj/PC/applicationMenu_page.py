#应用管理页面

from page_obj.PC.selenium_page import SeleniumPage


class applicationMenuPage(SeleniumPage):
    '''应用管理页面'''



    #查询应用


    #进入应用
    def enter_application(self,name):
        #点击固定分组的应用
        self.find_elem_is_clickableByCSS("div.precessCenter_card1 > div.el-collapse-item__wrap a[title='"+name+"']").click()
