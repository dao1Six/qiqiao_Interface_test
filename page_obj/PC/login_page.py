#登录页面

from page_obj.selenium_page import SeleniumPage


class LoginPage(SeleniumPage):
    '''登录界面'''

    login_url = 'https://tqy.do1.net.cn/dev-runtime/'
    denglu = "//a[text()='账号密码登录']"
    zhanghao = "//input[@title='请输入账号']"
    mima = "//input[@title='请输入密码']"
    anniu = "//button[text()='登录']"


    def user_login(self, username,password,*args):
        '''通过用户名密码登录
        username：账号
        password：密码
        '''
        self.open(self.login_url)
        self.clickElemByXpath_Visibility(self.denglu)
        self.sendkeysElemByXpath_Visibility(self.zhanghao,username)
        self.sendkeysElemByXpath_Visibility(self.mima,password)
        self.clickElemByXpath_Visibility(self.anniu)

