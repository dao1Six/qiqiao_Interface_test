# coding=utf-8
# coding=utf-8
import unittest

import requests
from ddt import ddt, data, unpack


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

    @data (("获取指定表单的某一条表单实例数据","4a55fec5361d47cb8f472e4e8e0abb20","b67334e766154ee7bcd5cfe9b6fc315f"))
    @unpack
    def test_Form_1_001(self,casename,formModelId,id):
        """{0}"""

        url = self.http+"/v1/integration/open/applications/"+self.applicationId+"/forms/"+formModelId+"/"+id

        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        print(responseJson)
        # self.assertEqual (responseJson['data']['name'], name)
        # self.assertEqual (responseJson['data']['parentId'], parentId)
        # self.assertEqual (responseJson['data']['parentName'], parentName)
        # self.assertEqual (responseJson['data']['fullName'], fullName)
        # self.assertEqual (responseJson['data']['id'], departmentsId)

