#图片组件
from page_obj.selenium_page import SeleniumPage


class PicUpload(SeleniumPage):


    PicUpload_input_loc = "div[title='%s'] input[type='file']"  # 图片上传字段输入框
    PicUpload_success_loc = "div[title='%s'] img"  #图片上传成功标识

    #给图片组件输入值
    def sendkeysToPicUpload(self,fieldName,picPath,*args):
        '''给文件组件输入值
        fieldName：字段标题
        picPath：图片路径
        '''
        locator = self.PicUpload_input_loc.replace('%s',fieldName)
        self.sendkeysElemByCSS_Presence(locator,picPath)
        #等待上传成功
        self.wait_elem_visible(self.PicUpload_success_loc.replace('%s',fieldName))



    #获取图片组件的值