# coding=utf-8
# coding=utf-8
# coding=utf-8
import json
import unittest

import requests
from ddt import ddt, data, unpack
from sqlalchemy.sql.elements import Null


@ddt
class jichengWorkflowTestSuit (unittest.TestCase):
    '''七巧开发平台测试类'''

    applicationId = "dbd5119dfb46442aa2d14cf3dfe6ed4f"

    corpId = "wwf0d1682926a0822d"

    secret = "07430652a525c91c901b88b0b80bbcbc"

    UserId = "27958a5808ee3719bacd45ebe226ce45"  #吴健伦

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




    @data (("启动流程实例","e327cd8cf90344e99bb3370c3f7cbd8c"))
    @unpack
    def test_Workflow_1_002(self,casename,modelId,):
        """{0}"""

        url = self.http+"/v1/integration/open/applications/"+self.applicationId+"/workflow/process_definitions/"+modelId+"/start"
        data = json.dumps ({
     "nextNodesAndHandlers": [
           {
            "activityDefinitionId": "obj_03",
            "approvers": ["27958a5808ee3719bacd45ebe226ce45"]
           }
     ],
        "variables":{"关联基础数据":None,"关联外键联动筛选表":None,"单行文本":"道一2222","form_allzujian_number1":3232,"form_allzujian_select1":"1","form_allzujian_select2":"","form_allzujian_select3":[],"图片上传":[],"图片上传2":[],"文件上传1":[],"form_allzujian_date1":1577289600000,"form_allzujian_time1":"10:40","form_allzujian_datetime1":1577328000000,"人员选择":"5cb5ae8dafca4ffed4a9e2fc6d5e2808","用户所属部门":["7a9b11fa5e3d12a842dcb12d05d53f94"],"部门选择":[],"form_allzujian_address1":None,"生成编码":"","级联选择":None,"form_quanzujian_textarea1":"","form_quanzujian_editor1":"","子表关联外键":None,"子表外键选择":None,"数字1":3232}
},ensure_ascii=False)
        print(data)
        response = requests.post (url=url, headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json ()
        print(responseJson)
        self.assertEqual (responseJson['code'], 0)
        # self.assertEqual (responseJson['data']['name'], name)
        # self.assertEqual (responseJson['data']['parentId'], parentId)
        # self.assertEqual (responseJson['data']['parentName'], parentName)
        # self.assertEqual (responseJson['data']['fullName'], fullName)
        # self.assertEqual (responseJson['data']['id'], departmentsId)



    @data (("终止流程实例","65f6b32d141d4ba0919462c39e01b5c3","3980d823a9954b34b1b032c954782dd2"))
    @unpack
    def test_Workflow_1_003(self,casename,processInstanceId,taskId):
        """{0}"""

        url = self.http+"/v1/integration/open/applications/"+self.applicationId+"/workflow/process_instances/"+processInstanceId+"/task_instances/"+taskId+"/terminate"

        data = json.dumps ({
   "comment": "接口终止",
   "variables":{"关联基础数据": None, "关联外键联动筛选表": None, "单行文本": "道一2222", "form_allzujian_number1": 3232, "form_allzujian_select1": "1", "form_allzujian_select2": "", "form_allzujian_select3": [], "图片上传": [], "图片上传2": [], "文件上传1": [], "form_allzujian_date1": 1577289600000, "form_allzujian_time1": "10:40", "form_allzujian_datetime1": 1577328000000, "人员选择": "5cb5ae8dafca4ffed4a9e2fc6d5e2808", "用户所属部门": ["7a9b11fa5e3d12a842dcb12d05d53f94"], "部门选择": [], "form_allzujian_address1": None, "生成编码": "", "级联选择": None, "form_quanzujian_textarea1": "", "form_quanzujian_editor1": "", "子表关联外键": None, "子表外键选择": None, "数字1": 3232}
},ensure_ascii=False)
        print(data)
        response = requests.post (url=url, headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json ()
        print(responseJson)
        self.assertEqual (responseJson['code'], 0)


    @data (("删除流程实例","65f6b32d141d4ba0919462c39e01b5c3"))
    @unpack
    def test_Workflow_1_004(self,casename,processInstanceId):
        """{0}"""

        url = self.http+"/v1/integration/open/applications/"+self.applicationId+"/workflow/process_instances/"+processInstanceId
        response = requests.delete (url=url, headers=self.headers)
        responseJson = response.json ()
        print(responseJson)
        self.assertEqual (responseJson['code'], 0)


    @data (("查询指定用户的待办任务实例集合",0),("查询指定用户的待办任务实例集合",1))
    @unpack
    def test_Workflow_1_005_1(self,casename,page):
        """查询指定用户的待办任务实例集合"""
        parms = {"userId":"27958a5808ee3719bacd45ebe226ce45","page":page,"pageSize":10,"applicationId":"dbd5119dfb46442aa2d14cf3dfe6ed4f"}
        url = self.http+"/v1/integration/open/applications/"+self.applicationId+"/workflow/process_instances/task_instances/todos"
        response = requests.get (url=url, headers=self.headers,params=parms)
        responseJson = response.json ()
        print(responseJson)
        self.assertEqual (responseJson['code'], 0)
        self.assertGreater (len(responseJson['data']["list"]),0)


    @data (("查询指定用户的已办任务实例集合（分页）",0),("查询指定用户的已办任务实例集合（分页）",1))
    @unpack
    def test_Workflow_1_005_2(self,casename,page):
        """{0}"""
        parms = {"userId":"27958a5808ee3719bacd45ebe226ce45","page":page,"pageSize":10,"applicationId":"dbd5119dfb46442aa2d14cf3dfe6ed4f"}
        url = self.http+"/v1/integration/open/applications/"+self.applicationId+"/workflow/process_instances/task_instances/have_dones"
        response = requests.get (url=url, headers=self.headers,params=parms)
        responseJson = response.json ()
        print(responseJson)
        self.assertEqual (responseJson['code'], 0)
        self.assertGreater (len(responseJson['data']["list"]),0)


    @data (("查询指定用户的发起实例集合（分页）",0),("查询指定用户的发起实例集合（分页）",1))
    @unpack
    def test_Workflow_1_005_3(self,casename,page):
        """{0}"""
        parms = {"userId":"27958a5808ee3719bacd45ebe226ce45","page":page,"pageSize":10,"applicationId":"dbd5119dfb46442aa2d14cf3dfe6ed4f"}
        url = self.http+"/v1/integration/open/applications/"+self.applicationId+"/workflow/process_instances/initiates"
        response = requests.get (url=url, headers=self.headers,params=parms)
        responseJson = response.json ()
        print(responseJson)
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (len(responseJson['data']["list"]),1)



    @data (("根据流程实例id获取流程实例","d110f63e4dd44f839074055a408b52a7"))
    @unpack
    def test_Workflow_1_005_4(self,casename,processInstanceId):
        """{0}"""

        url = self.http+"/v1/integration/open/applications/"+self.applicationId+"/workflow/process_instances/"+processInstanceId+"/historys"
        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        print(responseJson)
        self.assertEqual (responseJson['code'], 0)


    @data (("根据流程实例id获取流程审批历史","d110f63e4dd44f839074055a408b52a7"))
    @unpack
    def test_Workflow_3_001(self,casename,processInstanceId):
        """{0}"""

        url = self.http+"/v1/integration/open/applications/"+self.applicationId+"/workflow/process_instances/"+processInstanceId
        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        print(responseJson)
        self.assertEqual (responseJson['code'], 0)


    @data (("查询任务实例(获取流程实例的当前任务集合)","d110f63e4dd44f839074055a408b52a7"))
    @unpack
    def test_Workflow_2_001(self,casename,processInstanceId):
        """{0}"""

        url = self.http+"/v1/integration/open/applications/"+self.applicationId+"/workflow/process_instances/"+processInstanceId+"/tasks"
        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        print(responseJson)
        self.assertEqual (responseJson['code'], 0)


    @data (("获取下一步人工任务参与人","54acb10daef5430f9778a60a543f54eb","6d93b786d3a14090b4f56ac75f9db857"))
    @unpack
    def test_Workflow_2_002(self,casename,processInstanceId,taskId):
        """{0}"""

        url = self.http+"/v1/integration/open/applications/"+self.applicationId+"/workflow/process_instances/"+code_quote(processInstanceId)+"/tasks/"+taskId+"/next_approvers"
        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        print(responseJson)
        self.assertEqual (responseJson['code'], 0)











