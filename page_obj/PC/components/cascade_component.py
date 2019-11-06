#级联组件
from page_obj.selenium_page import SeleniumPage


class Cascade(SeleniumPage):

    #输入级联组件的值
    def sendkeysToCascade(self,fieldName,key):
        elem  = self.find_elemByCSS("div[title='"+fieldName+"'] input")
        self.driver.execute_script ("arguments[0].removeAttribute('readonly');", elem)
        elem.send_keys(key)

    #给级联组件输入值