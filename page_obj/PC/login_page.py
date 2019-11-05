#登录界面

from page_obj.selenium_page import SeleniumPage


class LoginPage(SeleniumPage):
    '''登录界面'''

    login_url = 'https://qy.do1.com.cn/qiqiao/runtime'
    denglu = "//a[text()='账号密码登录']"
    zhanghao = "//input[@title='请输入账号']"
    mima = "//input[@title='请输入密码']"
    anniu = "//button[text()='登录']"

    alertsuccess = "//div[@role='alert' and @class='el-message el-message--success']"







    # 定义统一登录入口
    def user_login(self, username,password):
        '''通过用户名密码登录'''
        self.open(self.login_url)
        self.clickElemByXpath(self.denglu)
        self.sendkeysElemByXpath(self.zhanghao,username)
        self.sendkeysElemByXpath(self.mima,password)
        self.clickElemByXpath(self.anniu)

