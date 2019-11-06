#表单页面
from page_obj.PC.components.datatime_component import DataTime
from page_obj.PC.components.pic_Upload_component import PicUpload
from page_obj.selenium_page import SeleniumPage
from page_obj.PC.components.number_component import Number
from page_obj.PC.components.text_component import Text
from page_obj.PC.components.textarea_components import Textarea
from page_obj.PC.components.data_component import Data
from page_obj.PC.components.time_component import Time
from page_obj.PC.components.file_Upload_component import FileUpload
from page_obj.PC.components.selection_component import Selection
from page_obj.PC.components.user_component import User
from page_obj.PC.components.address_component import Address


class FormPage(Number,Text,Textarea,Data,Time,DataTime,PicUpload,FileUpload,Selection,User,Address):
    '''PC表单页面'''
    submit_button_loc = "//button[@type='button']/span[contains(text(),'提交')]"

    #提交表单
    def submit_doc(self):
        self.clickElemByXpath(self.submit_button_loc)