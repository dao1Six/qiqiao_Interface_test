# coding=utf-8
# coding=utf-8
import json
import unittest

import requests
from ddt import ddt, data, unpack

from util.codeController import CodeController


@ddt
class jichengFormTestSuit (unittest.TestCase):
    '''七巧开发平台测试类'''

    applicationId = "dbd5119dfb46442aa2d14cf3dfe6ed4f"

    corpId = "wwf0d1682926a0822d"

    secret = "07430652a525c91c901b88b0b80bbcbc"

    UserId = "5cb5ae8dafca4ffed4a9e2fc6d5e2808"

    http = "http://api.qiqiao.qa.do1.work"

    @classmethod
    def setUpClass(cls):
        #获取AccessToken
        url = "http://api.qiqiao.qa.do1.work/v1/integration/securities/access_token?corpId="+cls.corpId+"&secret="+cls.secret
        response = requests.get (url=url)
        responseJson = response.json ()
        AccessToken = responseJson['data']

        # 添加请求头，模拟浏览器访问
        cls.headers = {"Accept": "application/json, text/plain, */*",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
                        "X-Auth0-Token": AccessToken,
                       "X-Auth0-UserId":cls.UserId,
                        "Content-Type": "application/json"}

    @data (("获取指定表单的某一条表单实例数据","b67334e766154ee7bcd5cfe9b6fc315f","59b3763a92824084bda645d99b654e8b"))
    @unpack
    def test_Form_1_001(self,casename,formModelId,id):
        """{0}"""

        url = self.http+"/v1/integration/open/applications/"+self.applicationId+"/forms/"+formModelId+"/"+id

        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        print(responseJson)
        self.assertEqual (responseJson['code'], 0)


    @data (("获取指定主表数据实例下所有子表的表单实例数据","866f87d71d3b4420805e54e28635b849",CodeController.code_quote('子表外键选择'),"b67334e766154ee7bcd5cfe9b6fc315f"))
    @unpack
    def test_Form_1_002(self,casename,parentId,parentFieldName,subFormModelId):
        """{0}"""

        url = self.http+"/v1/integration/open/applications/"+self.applicationId+"/forms/"+parentId+"/"+parentFieldName+"/"+subFormModelId

        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        print (url)
        print(responseJson)
        self.assertEqual (responseJson['code'], 0)



    @data (("获取指定表单的分页数据","b67334e766154ee7bcd5cfe9b6fc315f",1,10))
    @unpack
    def test_Form_1_003(self,casename,formModelId,page,pageSize):
        """{0}"""

        url = self.http+"/v1/integration/open/applications/"+self.applicationId+"/forms/"+formModelId
        parms = {"page":page,"pageSize":pageSize}
        response = requests.get (url=url, headers=self.headers,data=parms)
        responseJson = response.json ()
        print(responseJson)
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (len(responseJson['data']['list']),responseJson['data']['total'])



    @data (("保存新增的表单实例数据","b67334e766154ee7bcd5cfe9b6fc315f"))
    @unpack
    def test_Form_1_004(self,casename,formModelId):
        """{0}"""

        url = self.http+"/v1/integration/open/applications/"+self.applicationId+"/forms/"+formModelId
        data = json.dumps ({
            "variables": {"关联基础数据": None, "关联外键联动筛选表": None, "单行文本": "444道一22222", "form_allzujian_number1": 3232,
                          "form_allzujian_select1": "1", "form_allzujian_select2": "", "form_allzujian_select3": [],
                          "图片上传": [], "图片上传2": [], "文件上传1": [], "form_allzujian_date1": 1577289600000,
                          "form_allzujian_time1": "10:40", "form_allzujian_datetime1": 1577328000000,
                          "人员选择": "5cb5ae8dafca4ffed4a9e2fc6d5e2808", "用户所属部门": ["7a9b11fa5e3d12a842dcb12d05d53f94"],
                          "部门选择": [], "form_allzujian_address1": None, "生成编码": "", "级联选择": None,
                          "form_quanzujian_textarea1": "", "form_quanzujian_editor1": "", "子表关联外键": None,
                          "子表外键选择": None, "数字1": 3232},
                          "id": formModelId,
                          "version": 0})
        response = requests.post (url=url, headers=self.headers,data=data)
        responseJson = response.json ()
        print(responseJson)
        self.assertEqual (responseJson['code'], 0)



    @data (("保存修改的表单实例数据","b67334e766154ee7bcd5cfe9b6fc315f","59b3763a92824084bda645d99b654e8b"))
    @unpack
    def test_Form_1_005(self,casename,formModelId,id):
        """{0}"""

        url = self.http+"/v1/integration/open/applications/"+self.applicationId+"/forms/"+formModelId
        data = json.dumps ({
            "variables": {"关联基础数据": None, "关联外键联动筛选表": None, "单行文本": "444道一22222", "form_allzujian_number1": 111111,
                          "form_allzujian_select1": "1", "form_allzujian_select2": "", "form_allzujian_select3": [],
                          "图片上传": [], "图片上传2": [], "文件上传1": [], "form_allzujian_date1": 1577289600000,
                          "form_allzujian_time1": "10:40", "form_allzujian_datetime1": 1577328000000,
                          "人员选择": "5cb5ae8dafca4ffed4a9e2fc6d5e2808", "用户所属部门": ["7a9b11fa5e3d12a842dcb12d05d53f94"],
                          "部门选择": [], "form_allzujian_address1": None, "生成编码": "", "级联选择": None,
                          "form_quanzujian_textarea1": "", "form_quanzujian_editor1": "", "子表关联外键": None,
                          "子表外键选择": None, "数字1": 3232},
                          "id": formModelId,
                          "version": 1})
        response = requests.put (url=url, headers=self.headers,data=data)
        responseJson = response.json ()
        print(responseJson)
        self.assertEqual (responseJson['code'], 0)





    @data (("删除指定表单的某条表单实例数据","b67334e766154ee7bcd5cfe9b6fc315f","86c374f0dd74417c8dd6ebe4e3ea36d3"))
    @unpack
    def test_Form_1_006(self,casename,formModelId,id):
        """{0}"""

        url = self.http+"/v1/integration/open/applications/"+self.applicationId+"/forms/"+formModelId+"/"+id
        response = requests.delete(url=url, headers=self.headers)
        responseJson = response.json ()
        print(responseJson)
        self.assertEqual (responseJson['code'], 0)



    @data (("删除子表实例数据","866f87d71d3b4420805e54e28635b849","子表外键选择","b67334e766154ee7bcd5cfe9b6fc315f"))
    @unpack
    def test_Form_1_007(self,casename,parentId,parentFieldName,subFormModelId):
        """{0}"""

        url = self.http+"/v1/integration/open/applications/"+self.applicationId+"/forms/"+parentId+"/"+CodeController.code_quote(parentFieldName)+"/"+subFormModelId
        response = requests.delete(url=url, headers=self.headers)
        responseJson = response.json ()
        print(responseJson)
        print(url)
        self.assertEqual (responseJson['code'], 0)


