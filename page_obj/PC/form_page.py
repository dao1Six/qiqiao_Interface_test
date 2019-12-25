#表单页面
from page_obj.PC.components.cascade_component import Cascade
from page_obj.PC.components.datetime_component import DateTime
from page_obj.PC.components.pic_Upload_component import PicUpload
from page_obj.selenium_page import SeleniumPage
from page_obj.PC.components.number_component import Number
from page_obj.PC.components.text_component import Text
from page_obj.PC.components.textarea_components import Textarea
from page_obj.PC.components.date_component import Date
from page_obj.PC.components.time_component import Time
from page_obj.PC.components.file_Upload_component import FileUpload
from page_obj.PC.components.selection_component import Selection
from page_obj.PC.components.user_component import User
from page_obj.PC.components.address_component import Address
from page_obj.PC.components.childForm_component import ChildForm_component
from page_obj.PC.components.childFormAssociation_component import ChildFormAssociation_component
from page_obj.PC.components.foreignSelection_component import ForeignSelection_component
from page_obj.PC.components.multiFormAssociation_component import MultiFormAssociation


class FormPage(Number,Text,Textarea,Date,Time,DateTime,PicUpload,FileUpload,Selection,User,Address,Cascade,ChildForm_component,ChildFormAssociation_component,ForeignSelection_component,MultiFormAssociation):
    '''PC表单页面'''

    FormPage_submit_button_loc = "//button[@type='button']/span[contains(text(),'提交')]"  #表单提交按钮

    #提交表单
    def click_submit_button(self,*args):
        self.clickElemByXpath_Presence(self.FormPage_submit_button_loc)