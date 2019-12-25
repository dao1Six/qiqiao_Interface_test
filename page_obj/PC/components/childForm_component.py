#子表
import time

from page_obj.selenium_page import SeleniumPage


class ChildForm_component(SeleniumPage):

    ChildForm_AddButton_loc ='[data-mark=%title] [data-mark=button_添加]'  #子表添加按钮

    ChildForm_Input_loc = "[data-mark='%title'] .row_%title_%row [data-mark='%text'] input"  #子表输入框

    ChildForm_div_loc = "[data-mark='%title'] .row_%title_%row [data-mark='%text']"  # 子表输入框div


    ChildForm_SelectOption_loc = "[data-mark='%option']"  #下拉选项

    ChildForm_label_loc = "[data-mark='%title']>label"  #字段标题

    ChildForm_userSelect_loc = "[data-mark=%title] .row_%title_%row [data-mark=%user] [data-mark='选择人员按钮']"  #子表人员选择



    def scroll_To_ChildForm_Div(self):
        self.scrollIntoView(self.ChildForm_div_loc)


    def click_ChildForm_AddButton(self,fieldName,*args):
        '''点击添加按钮
        fieldName：字段标题
        '''
        self.clickElemByCSS_Presence (self.ChildForm_AddButton_loc.replace ('%title', fieldName))



    def delete_ChildForm_Record(self):
        '''删除子表记录'''
        pass


    #给子表的单行文本组件字段添加数据
    def sendkeys_To_ChildFormText(self,childformTitle,row,TextTitle,key):
        '''给子表的单行文本组件输入值
        childformTitle :子表字段名
        row：行数
        TextTitle：文本字段标题
        key：文本值
        '''
        reallyRow = str(row-1)
        self.sendkeysElemByCSS_Presence(self.ChildForm_Input_loc.replace('%title',childformTitle).replace('%row',reallyRow).replace('%text',TextTitle),key)


    # 给子表的数字组件字段添加数据

    # 给子表的多行文本组件字段添加数据

    # 给子表的选择框组件字段添加数据
    def sendkeys_To_ChildFormSelect(self,childformTitle,row,SelectTitle,list,*args):
        '''
        childformTitle :子表字段名
        row：行数
        TextTitle：文本字段标题
        key：文本值
        '''
        reallyRow = str (row - 1)
        self.clickElemsByCSS_Presence (self.ChildForm_Input_loc.replace ('%title', childformTitle).replace ('%row', reallyRow).replace ('%text',SelectTitle))
        for i in list:
            self.clickElemsByCSS_Presence(self.ChildForm_SelectOption_loc.replace('%option',i),num=1)


    def sendkeys_To_ChildFormDate(self,childformTitle,DateTitle,row,key):
        '''给子表的日期组件字段添加数据
        childformTitle :子表字段名
        DateTitle：日期字段标题
        key：文本值
        '''
        reallyRow = str(row-1)
        self.sendkeysElemByCSS_Presence(self.ChildForm_Input_loc.replace('%title',childformTitle).replace('%row',reallyRow).replace('%text',DateTitle),key)
        self.clickElemByCSS_Presence(self.ChildForm_label_loc.replace('%title',childformTitle))


    def sendkeys_To_ChildFormDateTime(self, childformTitle,DateTimeTitle, row, dateKey,timeKey):
        '''给子表的日期时间组件字段添加数据
        childformTitle :子表字段名
        DateTimeTitle：日期时间字段标题
        key：文本值
        '''
        reallyRow = str(row-1)
        self.sendkeysElemsByCSS_Presence(self.ChildForm_Input_loc.replace('%title',childformTitle).replace('%row',reallyRow).replace('%text',DateTimeTitle),dateKey, num=0)
        self.clickElemByCSS_Presence (self.ChildForm_label_loc.replace ('%title', childformTitle))
        self.sendkeysElemsByCSS_Presence (
            self.ChildForm_Input_loc.replace ('%title', childformTitle).replace ('%row', reallyRow).replace ('%text',
                                                                                                             DateTimeTitle),
            dateKey, num=1)
        self.clickElemByCSS_Presence (self.ChildForm_label_loc.replace ('%title', childformTitle))




    def sendkeys_To_ChildFormTime(self,childformTitle,TimeTitle,row,key):
        '''给子表的时间组件字段添加数据
        childformTitle :子表字段名
        TimeTitle：时间字段标题
        key：文本值
        '''
        reallyRow = str(row-1)
        self.sendkeysElemByCSS_Presence(self.ChildForm_Input_loc.replace('%title',childformTitle).replace('%row',reallyRow).replace('%text',TimeTitle),key)
        self.clickElemByCSS_Presence (self.ChildForm_label_loc.replace ('%title', childformTitle))

    # 给子表的富文本组件字段添加数据

    #
    def sendkeys_To_ChildFormPicUpload(self,childformTitle,PicUploadTitle,row,picPath):
        '''给子表的图片上传组件输入值
        childformTitle :子表字段名
        row：行数
        PicUploadTitle：图片字段标题
        picPath：图片路径
        '''
        reallyRow = str(row-1)
        self.sendkeysElemsByCSS_Presence(self.ChildForm_Input_loc.replace('%title',childformTitle).replace('%row',reallyRow).replace('%text',PicUploadTitle),picPath)


    #
    def sendkeys_To_ChildFormUser(self,childformTitle,UserTitle,row,userNameList):
        '''给子表的人员选择组件字段添加数据
        childformTitle :子表字段名
        row：行数
        UserTitle：人员字段标题
        '''
        reallyRow = str(row-1)
        #点击人员选择
        self.clickElemsByCSS_Presence(self.ChildForm_userSelect_loc.replace('%title',childformTitle).replace('%row',reallyRow).replace('%user',UserTitle))

        for name in userNameList:
            self.clickElemByXpath_Presence (self.User_search_loc)
            self.sendkeysElemByXpath_Presence (self.User_search_loc, name)
            self.clickElemByXpath_Presence (self.User_searchOption_loc.replace ('%s', name))
        self.clickElemByXpath_Presence (self.User_querenButton_loc)


    # 给子表的部门选择组件字段添加数据

    # 给子表的地址选择组件字段添加数据

    # 给子表的级联选择组件字段添加数据


