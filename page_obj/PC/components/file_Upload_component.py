#文件组件
from page_obj.selenium_page import SeleniumPage


class FileUpload(SeleniumPage):

    #给文件组件输入值
    def sendkeysToFileUpload(self,fieldName,key):
        locator = "div[title='"+fieldName+"'] input[type='file']"
        self.sendkeysElemByCSS(locator,key)
        #等待上传成功
        success_loc = "div[title='"+fieldName+"'] ul.file_content"
        self.wait_elem_visible(success_loc)



    #获取文件组件的值