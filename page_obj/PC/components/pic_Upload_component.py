#图片组件
from page_obj.selenium_page import SeleniumPage


class PicUpload(SeleniumPage):

    #给图片组件输入值
    def sendkeysToPicUpload(self,fieldName,key):
        locator = "div[title='"+fieldName+"'] input[type='file']"
        self.sendkeysElemByCSS_Presence(locator,key)
        #等待上传成功
        success_loc = "div[title='"+fieldName+"'] img"
        self.wait_elem_visible(success_loc)



    #获取图片组件的值