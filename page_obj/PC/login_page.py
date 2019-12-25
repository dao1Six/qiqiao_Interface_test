#登录页面

from page_obj.selenium_page import SeleniumPage


class LoginPage(SeleniumPage):
    '''登录界面'''

    denglu = "//a[text()='账号密码登录']"
    zhanghao = "//input[@title='请输入账号']"
    mima = "//input[@title='请输入密码']"
    anniu = "//button[text()='登录']"


    def user_login(self,login_url, username,password,*args):
        '''通过用户名密码登录
        username：账号
        password：密码
        '''
        self.open(login_url)
        self.clickElemByXpath_Presence(self.denglu)
        self.sendkeysElemByXpath_Presence(self.zhanghao,username)
        self.sendkeysElemByXpath_Presence(self.mima,password)
        self.clickElemByXpath_Presence(self.anniu)

