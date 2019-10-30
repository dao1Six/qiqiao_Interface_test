import smtplib
from email.mime.text import MIMEText


def send_mail(title):
    try:
        msg = MIMEText(title+'')  # 邮件内容
        msg['Subject'] = ''  # 邮件主题
        msg['From'] ='service@weioa365.com'  # 发送者账号
        # msg['To'] = maillist  # 接收者账号列表

        server = smtplib.SMTP('smtp.exmail.qq.com')
        server.login("service@weioa365.com", "weioa365teemlink")

        to1 = '' #接收人
        server.sendmail(msg['from'], to1, msg.as_string())
        # 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
        server.close
        print('测试报告邮件发送成功！')

    except Exception as msg:
        print('测试报告邮件发送失败！异常：%s' % msg)



# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get("https://www.baidu.com")
#     insert_img(driver, 'baidu.jpg')
#     driver.quit()
