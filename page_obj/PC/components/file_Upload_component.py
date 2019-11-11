#文件组件
from page_obj.selenium_page import SeleniumPage


class FileUpload(SeleniumPage):

    FileUpload_Cssloc = "div[title='%s'] input[type='file']"  # 文件上传字段Css定位
    filesuccess_loc ="div[title='%s'] ul.file_content"


    #给文件组件输入值
    def sendkeysToFileUpload(self,fieldName,key):
        locator = self.FileUpload_Cssloc.replace('%s',fieldName)
        self.sendkeysElemByCSS_Presence(locator,key)
        #等待上传成功
        self.wait_elem_visible(self.filesuccess_loc.replace('%s',fieldName))



    #获取文件组件的值