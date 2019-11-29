#多表关联组件
from page_obj.selenium_page import SeleniumPage


class MultiFormAssociation(SeleniumPage):
    MultiFormAssociation_HandleManagerButton_loc = "[data-mark=%title] [data-mark=button_批量管理]" #批量管理按钮


    def click_MultiFormAssociation_HandleManagerButton(self,fileName,*args):
        '''点击批量管理按钮'''
        self.clickElemByCSS_Presence(self.MultiFormAssociation_HandleManagerButton_loc.replace('%title',fileName))


    def click_MultiFormAssociation_AddButton(self,*args):
        '''点击添加按钮'''
        pass


    def tick_MultiFormManagementDialog_Record(self,*args):
        '''勾选批量管理页面关联表记录'''
        pass


    def click_MultiFormManagementDialog_ConfirmButton(self,*args):
        '''点击批量管理页面确认按钮'''
        pass


    def click_MultiFormManagementDialog_CancelButton(self,*args):
        '''点击批量管理页面取消按钮'''
        pass

    def delete_MultiForm_Record(self):
        '''删除多表记录'''
        pass



    #给多表中间表的单行文本组件字段添加数据

    # 给多表中间表的数字组件字段添加数据

    # 给多表中间表的多行文本组件字段添加数据

    # 给多表中间表的选择框组件字段添加数据

    # 给多表中间表的日期组件字段添加数据

    # 给多表中间表的日期时间组件字段添加数据

    # 给多表中间表的时间组件字段添加数据

    # 给多表中间表的富文本组件字段添加数据

    # 给多表中间表的图片上传组件字段添加数据

    # 给多表中间表的文件上传组件字段添加数据

    # 给多表中间表的人员选择组件字段添加数据

    # 给多表中间表的部门选择组件字段添加数据

    # 给多表中间表的地址选择组件字段添加数据

    # 给多表中间表的级联选择组件字段添加数据
