# coding=utf-8
import unittest

import requests
from ddt import ddt, data, unpack


@ddt
class jichengAddressBookTestSuit (unittest.TestCase):
    '''七巧开发平台测试类'''

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

    @data (("根据部门唯一标识获取指定部门","7a9b11fa5e3d12a842dcb12d05d53f94","创新技术中心->产品研发二部->产品规划组","产品研发二部",
            "0fd570074e5a47989d6e61dacd695a57","产品规划组"))
    @unpack
    def test_addressBook_1_001(self,casename,departmentsId,fullName,parentName,parentId,name):
        """{0}"""

        url = self.http+"/v1/integration/open/departments/"+departmentsId

        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        self.assertEqual (responseJson['data']['name'], name)
        self.assertEqual (responseJson['data']['parentId'], parentId)
        self.assertEqual (responseJson['data']['parentName'], parentName)
        self.assertEqual (responseJson['data']['fullName'], fullName)
        self.assertEqual (responseJson['data']['id'], departmentsId)

#0fd570074e5a47989d6e61dacd695a57 = 创新技术中心->产品研发二部
    @data (("获取指定部门的子级部门列表","0fd570074e5a47989d6e61dacd695a57","产品规划组","0fd570074e5a47989d6e61dacd695a57","创新技术中心->产品研发二部","创新技术中心->产品研发二部->产品规划组",
            "7a9b11fa5e3d12a842dcb12d05d53f94"))
    @unpack
    def test_addressBook_1_002(self,casename,departmentId,name,parentId,parentName,fullName,departmentsId):
        """{0}"""

        url = self.http+"/v1/integration/open/departments/"+departmentId+"/children"

        response = requests.get (url=url,params={'departmentId':'0fd570074e5a47989d6e61dacd695a57','recursion':True}, headers=self.headers)
        responseJson = response.json ()
        print(responseJson)
        self.assertEqual(len(responseJson['data']),3)
        self.assertEqual (responseJson['data'][2]['name'], name)
        self.assertEqual (responseJson['data'][2]['parentId'], parentId)
        self.assertEqual (responseJson['data'][2]['parentName'], parentName)
        self.assertEqual (responseJson['data'][2]['fullName'], fullName)
        self.assertEqual (responseJson['data'][2]['id'], departmentsId)

    # 0fd570074e5a47989d6e61dacd695a57 = 创新技术中心->产品研发二部
    # 7a9b11fa5e3d12a842dcb12d05d53f94  创新技术中心->产品研发二部->产品规划组
    #85ec2d9eb561416d97ef7e09921e4114  创新技术中心
    @data (("获取直属上级部门", "7a9b11fa5e3d12a842dcb12d05d53f94", "产品研发二部", "85ec2d9eb561416d97ef7e09921e4114",
            "创新技术中心", "创新技术中心->产品研发二部"))
    @unpack
    def test_addressBook_1_003(self, casename, departmentId, name, parentId, parentName, fullName):
        """{0}"""

        url = self.http + "/v1/integration/open/departments/" + departmentId + "/parent"

        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        print (responseJson)
        # self.assertEqual (len (responseJson['data']), 3)
        self.assertEqual (responseJson['data']['name'], name,msg="name参数值校验错误")
        self.assertEqual (responseJson['data']['parentId'], parentId,msg="parentId参数值校验错误")
        self.assertEqual (responseJson['data']['parentName'], parentName,msg="parentName参数值校验错误")
        self.assertEqual (responseJson['data']['fullName'], fullName,msg="fullName参数值校验错误")


    @data (("获取根部门信息", "总办", "f9f76710a21f4373bd81a6489cf339ca", "总办",
            "", ""))
    @unpack
    def test_addressBook_1_004(self, casename, fullName,id, name, parentId, parentName):
        """{0}"""

        url = self.http + "/v1/integration/open/departments/root"

        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        print (responseJson)
        self.assertEqual (len (responseJson['data']), 15)
        self.assertEqual (responseJson['data'][0]['name'], name,msg="name参数值校验错误")
        self.assertEqual (responseJson['data'][0]['parentId'], parentId,msg="parentId参数值校验错误")
        self.assertEqual (responseJson['data'][0]['parentName'], parentName,msg="parentName参数值校验错误")
        self.assertEqual (responseJson['data'][0]['fullName'], fullName,msg="fullName参数值校验错误")

    #5cb5ae8dafca4ffed4a9e2fc6d5e2808  王栋一
    @data (("根据账号名获取用户", "5cb5ae8dafca4ffed4a9e2fc6d5e2808", "WangDongYi@A", "王栋一",
            1, "15036109302","7a9b11fa5e3d12a842dcb12d05d53f94",
            "",["7a9b11fa5e3d12a842dcb12d05d53f94"]))
    @unpack
    def test_addressBook_2_001(self, casename,userid,account,name,gender,telephone,defaultDepartmentId,defaultDepartmentName,departmentIds):
        """{0}"""

        url = self.http + "/v1/integration/open/users/account"

        response = requests.get (url=url, headers=self.headers,params={"account":account})
        responseJson = response.json ()
        print (responseJson)
        self.assertEqual (responseJson['data']['id'], userid, msg="id参数值校验错误")
        self.assertEqual (responseJson['data']['account'], account,msg="account参数值校验错误")
        self.assertEqual (responseJson['data']['name'], name,msg="name参数值校验错误")
        self.assertEqual (responseJson['data']['gender'], gender,msg="gender参数值校验错误")
        self.assertEqual (responseJson['data']['telephone'], telephone,msg="telephone参数值校验错误")
        self.assertEqual (responseJson['data']['defaultDepartmentId'], defaultDepartmentId,msg="defaultDepartmentId参数值校验错误")
        self.assertEqual (responseJson['data']['defaultDepartmentName'], defaultDepartmentName,msg="defaultDepartmentName参数值校验错误")
        self.assertEqual (responseJson['data']['departmentIds'], departmentIds,msg="departmentIds参数值校验错误")



    #5cb5ae8dafca4ffed4a9e2fc6d5e2808  王栋一
    @data (("根据用户ID获取用户", "5cb5ae8dafca4ffed4a9e2fc6d5e2808", "WangDongYi@A", "王栋一",
            1, "15036109302","7a9b11fa5e3d12a842dcb12d05d53f94",
            "",["7a9b11fa5e3d12a842dcb12d05d53f94"]))
    @unpack
    def test_addressBook_2_002(self, casename,userid,account,name,gender,telephone,defaultDepartmentId,defaultDepartmentName,departmentIds):
        """{0}"""

        url = self.http + "/v1/integration/open/users/"+userid

        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        print (responseJson)
        self.assertEqual (responseJson['data']['account'], account,msg="account参数值校验错误")
        self.assertEqual (responseJson['data']['name'], name,msg="name参数值校验错误")
        self.assertEqual (responseJson['data']['gender'], gender,msg="gender参数值校验错误")
        self.assertEqual (responseJson['data']['telephone'], telephone,msg="telephone参数值校验错误")
        self.assertEqual (responseJson['data']['defaultDepartmentId'], defaultDepartmentId,msg="defaultDepartmentId参数值校验错误")
        self.assertEqual (responseJson['data']['defaultDepartmentName'], defaultDepartmentName,msg="defaultDepartmentName参数值校验错误")
        self.assertEqual (responseJson['data']['departmentIds'], departmentIds,msg="departmentIds参数值校验错误")

    # 5cb5ae8dafca4ffed4a9e2fc6d5e2808  王栋一
    # b4ec3d07d6cbaaa4e292184ffd56312d  朱浪锋
    @data (("根据用户ID批量获取用户", "5cb5ae8dafca4ffed4a9e2fc6d5e2808", "WangDongYi@A", "王栋一", 1, "15036109302",
            "7a9b11fa5e3d12a842dcb12d05d53f94", "", ["7a9b11fa5e3d12a842dcb12d05d53f94"]))
    @unpack
    def test_addressBook_2_003(self, casename, userid, account, name, gender, telephone, defaultDepartmentId,
                               defaultDepartmentName, departmentIds):
        """{0}"""

        url = self.http + "/v1/integration/open/users/list"

        response = requests.get (url=url, headers=self.headers,params={"userIds":["5cb5ae8dafca4ffed4a9e2fc6d5e2808","b4ec3d07d6cbaaa4e292184ffd56312d"]})
        responseJson = response.json ()
        print (responseJson)
        self.assertEqual (len(responseJson['data']),2)
        self.assertEqual (responseJson['data'][0]['account'], account, msg="account参数值校验错误")
        self.assertEqual (responseJson['data'][0]['name'], name, msg="name参数值校验错误")
        self.assertEqual (responseJson['data'][0]['gender'], gender, msg="gender参数值校验错误")
        self.assertEqual (responseJson['data'][0]['telephone'], telephone, msg="telephone参数值校验错误")
        self.assertEqual (responseJson['data'][0]['defaultDepartmentId'], defaultDepartmentId,
                          msg="defaultDepartmentId参数值校验错误")
        self.assertEqual (responseJson['data'][0]['defaultDepartmentName'], defaultDepartmentName,
                          msg="defaultDepartmentName参数值校验错误")
        self.assertEqual (responseJson['data'][0]['departmentIds'], departmentIds, msg="departmentIds参数值校验错误")




    # 5cb5ae8dafca4ffed4a9e2fc6d5e2808  王栋一
    # b4ec3d07d6cbaaa4e292184ffd56312d  朱浪锋
    #7a9b11fa5e3d12a842dcb12d05d53f94
    @data (("根据部门id获取用户集合(分页)", "7a9b11fa5e3d12a842dcb12d05d53f94","5cb5ae8dafca4ffed4a9e2fc6d5e2808", "WangDongYi@A", "王栋一", 1, "15036109302",
            "7a9b11fa5e3d12a842dcb12d05d53f94", "", ["7a9b11fa5e3d12a842dcb12d05d53f94"]))
    @unpack
    def test_addressBook_2_004(self, casename,departmentId, userid, account, name, gender, telephone, defaultDepartmentId,
                               defaultDepartmentName, departmentIds):
        """{0}"""

        url = self.http + "/v1/integration/open/users"

        response = requests.get (url=url, headers=self.headers,params={"departmentId":departmentId,"page":2,"pageSize":10})
        responseJson = response.json ()
        print (responseJson)
        self.assertEqual (len(responseJson['data']['list']),10)
        # self.assertEqual (responseJson['list'][0]['account'], account, msg="account参数值校验错误")
        # self.assertEqual (responseJson['list'][0]['name'], name, msg="name参数值校验错误")
        # self.assertEqual (responseJson['list'][0]['gender'], gender, msg="gender参数值校验错误")
        # self.assertEqual (responseJson['list'][0]['telephone'], telephone, msg="telephone参数值校验错误")
        # self.assertEqual (responseJson['list'][0]['defaultDepartmentId'], defaultDepartmentId,
        #                   msg="defaultDepartmentId参数值校验错误")
        # self.assertEqual (responseJson['list'][0]['defaultDepartmentName'], defaultDepartmentName,
        #                   msg="defaultDepartmentName参数值校验错误")
        # self.assertEqual (responseJson['list'][0]['departmentIds'], departmentIds, msg="departmentIds参数值校验错误")
