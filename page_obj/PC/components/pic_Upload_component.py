#图片组件
from page_obj.selenium_page import SeleniumPage


class PicUpload(SeleniumPage):


    PicUpload_Cssloc = "div[title='%s'] input[type='file']"  # 图片上传字段Css定位
    success_loc = "div[title='%s'] img"

    #给图片组件输入值
    def sendkeysToPicUpload(self,fieldName,key):
        locator = self.PicUpload_Cssloc.replace('%s',fieldName)
        self.sendkeysElemByCSS_Presence(locator,key)
        #等待上传成功
        self.wait_elem_visible(self.success_loc.replace('%s',fieldName))



    #获取图片组件的值