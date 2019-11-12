#文件组件
from page_obj.selenium_page import SeleniumPage


class FileUpload(SeleniumPage):

    FileUpload_input_loc = "div[title='%s'] input[type='file']"  # 文件上传组件输入框
    FileUpload_success_loc ="div[title='%s'] ul.file_content"  #文件上传成功标识



    def sendkeysToFileUpload(self,fieldName,key,*args):
        '''给文件组件输入值
        fieldName：字段标题
        key：文件路径
        '''
        locator = self.FileUpload_input_loc.replace('%s',fieldName)
        self.sendkeysElemByCSS_Presence(locator,key)
        #等待上传成功
        self.wait_elem_visible(self.FileUpload_success_loc.replace('%s',fieldName))



    #获取文件组件的值