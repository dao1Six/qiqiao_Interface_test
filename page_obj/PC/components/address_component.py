#地址组件
from page_obj.selenium_page import SeleniumPage


class Address(SeleniumPage):

    #输入地址组件的值
    def sendkeysToAddress(self,fieldName,addkey,detilkey):
        elems  = self.find_elemsByCSS("div[title='"+fieldName+"'] input")
        self.driver.execute_script ("arguments[0].removeAttribute('readonly');", elems)
        elems[0].send_keys(addkey)
        elems[1].send_keys(detilkey)

    #给地址组件输入值