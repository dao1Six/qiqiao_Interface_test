#登录页面

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
        self.clickElemByXpath_Visibility(self.denglu)
        self.sendkeysElemByXpath_Visibility(self.zhanghao,username)
        self.sendkeysElemByXpath_Visibility(self.mima,password)
        self.clickElemByXpath_Visibility(self.anniu)

