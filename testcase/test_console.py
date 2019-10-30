import json
import unittest
import sys
from collections import OrderedDict
from urllib import parse

import params as params
import requests
from requests import request

from requests_toolbelt.multipart.encoder import MultipartEncoder

from ddt import ddt, data, unpack

from util.codeController import CodeController
from util.requestController import RequestController


@ddt
class ConsoleTestSuit (unittest.TestCase):
    '''七巧开发平台测试类'''

    applicationId = "c4cafae231b042949861bd73a10a65c4"  # 昂星demo应用

    domain = "https://qy.do1.com.cn/qiqiao/console/api/v1"

    def setUp(self):
        # 添加请求头，模拟浏览器访问
        self.headers = {"Accept": "application/json, text/plain, */*",
                        "Cookie": "corpAB=ww6b6c5c4fa6f34b16; _lastReqID=d66bcee5d1f64ce0bde68cfeadd715a1",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
                        "X-Auth0-Token": "1430343df6493be7800d578600952ff4",
                        "Content-Type": "application/json"}

    def test_query_application_01(self):
        '''用户搜索查找已存在应用'''
        name = "OKR"
        url = self.domain+"/workbench/applications?delete=false&name=" + name + "&applicationGroupId=&page=1"
        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        self.assertEqual (responseJson['data']['totalCount'], 1)
        self.assertEqual (responseJson['data']['list'][0]['name'], name)

    def test_appstore(self):
        '''用户进入应用市场页面'''
        url = self.domain+"/appstore/app_stores?name="
        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        self.assertEqual (responseJson['code'], 0)
        self.assertGreater (len (responseJson['data']['list']), 2)

    def test_appstoreoOerview(self):
        '''用户应用市场查看应用详情'''
        applicationId = "93aad8fe99174ed7bf8a76060ea87ccb"
        url = self.domain+"/appstore/app_stores/" + applicationId # OKR应用
        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['applicationName'], 'OKR管理')
        self.assertIn ('OKR是一套明确和跟踪目标及其完成情况的管理工具和方法', responseJson['data']['overview'])
        self.assertEqual (responseJson['data']['status'], "ONLINE")

    def test_locales_en_US(self):
        '''用户在选择语言处切换使用英文'''
        url = self.domain+"//workbench/i18n/locales/en_US"
        response = requests.put (url=url, headers=self.headers)
        responseJson = response.json ()
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['country'], 'US')
        self.assertEqual (responseJson['data']['displayName'], 'English (United States)')

    def test_locales_zh_TW(self):
        '''用户在选择语言处切换使用英文'''
        url = self.domain+"//workbench/i18n/locales/zh_TW"
        response = requests.put (url=url, headers=self.headers)
        responseJson = response.json ()
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['country'], 'TW')
        self.assertEqual (responseJson['data']['displayName'], 'Chinese (Taiwan)')

    def test_loginQiqiao(self):
        '''用户退出当前账号'''
        url = 'https://qy.do1.com.cn/qwy/sso/loginQiqiao'
        response = requests.put (url=url, headers=self.headers)
        self.assertEqual (response.status_code, 200)

    def test_create_application(self):
        '''用户创建应用'''

        headers = {"Accept": "application/json, text/plain, */*",
                   "Cookie": "corpAB=ww6b6c5c4fa6f34b16; _lastReqID=d66bcee5d1f64ce0bde68cfeadd715a1",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
                   "X-Auth0-Token": "1430343df6493be7800d578600952ff4",
                   "Content-Type": "application/json"}

        url = self.domain+"/workbench/applications/"

        data = {"createUserId": "05f35264ba3441c4be607c25f75cb492", "applicationGroupId": "",
                "logo": "icon-zhenggaileixing", "mainColor": "#96DECC", "name": "创建应用接口测试", "status": [],
                "terminalType": ["PC_WEB", "WX_MINI_PROGRAM", "MOBILE_WECHAT"], "delete": False}

        data_json = json.dumps (data)

        response = requests.post (url=url, headers=headers, data=data_json)
        responseJson = response.json ()
        print (responseJson)
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['name'], "创建应用接口测试")

        # 删除应用
        applicationId = responseJson['data']['id']
        applicationName = parse.quote (responseJson['data']['name'])
        delUrl = self.domain+"/workbench/applications/" +applicationId+ "?applicationName=" + applicationName
        delresponse = requests.delete (delUrl, headers=headers)
        delresponseJson = delresponse.json ()
        self.assertEqual (delresponseJson['code'], 0)

    def test_importApplication(self):
        '''用户导入应用'''
        url = self.domain+"/workbench/applications/import"

        file = '..\\file_data\\昂星demo.zip'

        a = open (file, 'rb')
        m = MultipartEncoder (
            fields={
                'applicationGroupId': '',
                'importType': 'ADD',
                'file': ('昂星demo.zip', a, 'application/x-zip-compressed')
            }
        )
        header = {"Content-Type": m.content_type,
                  "Cookie": "corpAB=ww6b6c5c4fa6f34b16; Hm_lvt_aed59972e7075b4acd495cf5b000c257=1568119947; _lastReqID=81cfe8ae522a42bdbcc961a35ec90bba; tgw_l7_route=2757773c8c583b0e1941ae61de7a309d",
                  "X-Auth0-Token": "99e741e5aecca5799cbe7b380a59351e"}
        response = requests.post (headers=header, url=url, data=m)
        responseJson = response.json ()
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['name'], "昂星demo")

        # 删除应用
        applicationId = responseJson['data']['id']
        applicationName = parse.quote (responseJson['data']['name'])
        delUrl = self.domain+"/workbench/applications/" +applicationId+ "?applicationName=" + applicationName
        delresponse = requests.delete (delUrl, headers=self.headers)
        delresponseJson = delresponse.json ()
        self.assertEqual (delresponseJson['code'], 0)

    def test_create_groups(self):
        '''用户添加分组'''

        url = self.domain+"/workbench/applications/groups"

        data = {"name": "A", "createUserId": None}
        data_json = json.dumps (data)

        response = requests.post (url=url, headers=self.headers, data=data_json)
        responseJson = response.json ()

        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['name'], "A")

        # 删除分组

        delUrl = self.domain+"/workbench/applications/groups/"+\
                 responseJson['data']['id']
        delresponse = requests.delete (delUrl, headers=self.headers)
        delresponseJson = delresponse.json ()
        self.assertEqual (delresponseJson['code'], 0)

    def test_applications_groups(self):
        '''用户切换应用分组'''
        applicationGroupId = "5dad537cd662f60001460fa6"
        url = self.domain+"/workbench/applications?delete=false&name=&applicationGroupId=" + applicationGroupId + "&page=1"

        data = {"name": "A", "createUserId": None}
        data_json = json.dumps (data)

        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()

        self.assertEqual (responseJson['code'], 0)
        self.assertGreater (len (responseJson['data']['list']), 1)



    def test_applications_release(self):
        '''用户发布应用'''

        applicationId = "5dad5206d662f60001460fa4"   #发布接口测试应用


        url = self.domain+"/workbench/applications/" +applicationId+ "/release"
        data = {"status": ["DEFAULT", "DEFAULT", "DEFAULT"]}  # 下架
        datajson = json.dumps (data)

        data2 = {"status": ["PC_WEB", "MOBILE_WECHAT", "WX_MINI_PROGRAM"]}  # 上架
        datajson2 = json.dumps (data2)

        response = requests.post (url=url, headers=self.headers, data=datajson)  # 先下架

        response2 = requests.post (url=url, headers=self.headers, data=datajson2)  # 再上架
        responseJson2 = response2.json ()

        self.assertEqual (responseJson2['code'], 0)
        self.assertEqual (responseJson2['data']['status'], ["PC_WEB", "MOBILE_WECHAT", "WX_MINI_PROGRAM"])

    def test_creat_roles(self):
        '''用户为应用添加角色'''

        url = self.domain+"/workbench/applications/" + self.applicationId + "/roles"

        data = {"name": "A", "applicationId": "a6aece61fa4248fc9a9d4721cb0775f7", "defaultRole": False, "orderNo": 1}

        dataJson = json.dumps (data)

        response = requests.post (url, data=dataJson, headers=self.headers)

        responseJson = response.json ()
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['name'], "A")

        # 删除角色

        delUrl = self.domain+"/workbench/applications/" + self.applicationId+ "/roles/" + \
                 responseJson['data']['id']
        delresponse = requests.delete (delUrl, headers=self.headers)
        delresponseJson = delresponse.json ()
        self.assertEqual (delresponseJson['code'], 0)

    def test_form_models(self):
        '''用户进入表单设计页面'''



        url = self.domain+"/workbench/applications/" + self.applicationId+ "/form_models/list?applicationId=" + self.applicationId+ "&formGroupId="
        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        self.assertEqual (responseJson['code'], 0)
        self.assertGreater (len (responseJson['data']), 1)

    def test_add_forms_groups(self):
        '''用户创建表单分组'''


        name = "aaa"

        url = self.domain+"/workbench/applications/" + self.applicationId+ "/forms/groups"
        data = json.dumps ({"applicationId": self.applicationId, "name": name})
        response = requests.post (url=url, headers=self.headers, data=data)
        responseJson = response.json ()
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['name'], name)

        # 删除分组
        delUrl = self.domain+"/workbench/applications/" + self.applicationId+ "/forms/groups/" + \
                 responseJson['data']['id']
        delresponse = requests.delete (delUrl, headers=self.headers)
        delresponseJson = delresponse.json ()
        self.assertEqual (delresponseJson['code'], 0)

    def test_creat_form_models(self):
        '''用户创建表单'''


        name = "aaa"

        url = self.domain+"/workbench/applications/" + self.applicationId+ "/form_models"
        data = json.dumps (
            {"name": name, "formTableId": "form_", "formGroupId": "", "erType": "1", "applicationId": self.applicationId})
        response = requests.post (url=url, headers=self.headers, data=data)
        responseJson = response.json ()
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['name'], name)

        # 删除表单
        delUrl = self.domain+"/workbench/applications/" + self.applicationId+ "/form_models/" + \
                 responseJson['data']['id'] + "?formName=" + name
        delresponse = requests.delete (delUrl, headers=self.headers)
        delresponseJson = delresponse.json ()
        self.assertEqual (delresponseJson['code'], 0)

    def test_switch_form(self):
        '''用户切换表单页面'''


        formId = "e436de232fec4a77849c6599ed4793ba"
        url = self.domain+"/workbench/applications/" + self.applicationId+ "/forms/" + formId

        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        self.assertEqual (responseJson['data']['formModelId'], formId)
        self.assertGreater (len (responseJson['data']['formFields']), 0)

    def test_process_models(self):
        '''用户进入流程设计页面'''

        url = self.domain+"/workbench/applications/" + self.applicationId+ "/process_models"

        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        self.assertEqual (responseJson['data'][0]['name'], '销售退货流程')

    def test_creat_process_models(self):
        '''用户在流程设计中新建流程'''


        name = "接口新建流程"

        url = self.domain+"/workbench/applications/" + self.applicationId+ "/process_models"
        data = json.dumps ({"name": name, "icon": "icon-renwu"})
        response = requests.post (url=url, headers=self.headers, data=data)
        responseJson = response.json ()
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['name'], name)

        # 删除流程
        delUrl = self.domain+"/workbench/applications/" + self.applicationId+ "/processData/" + \
                 responseJson['data']['id']
        delresponse = requests.delete (delUrl, headers=self.headers)
        delresponseJson = delresponse.json ()
        self.assertEqual (delresponseJson['code'], 0)



    def test_creat_pc_menus(self):
        '''用户创建PC业务建模页面'''


        name = "接口新建PC业务建模页面"

        url = self.domain+"/workbench/applications/" + self.applicationId+ "/menus"
        data = json.dumps (
            {"orderBy": 0, "name": name, "parentId": None, "applicationId": self.applicationId, "action": "PAGE",
             "device": "PC"})
        response = requests.post (url=url, headers=self.headers, data=data)
        responseJson = response.json ()
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['name'], name)

        # 删除页面
        delUrl = self.domain+"/workbench/applications/" + self.applicationId+ "/menus/" + \
                 responseJson['data']['id']
        delresponse = requests.delete (delUrl, headers=self.headers)
        delresponseJson = delresponse.json ()
        self.assertEqual (delresponseJson['code'], 0)

    def test_switch_business(self):
        '''用户切换PC端页面'''



        businessId = "c2a97bbd6c6f4712b5d04f67ea5cd319"

        url = self.domain+"/workbench/applications/" + self.applicationId+ "/business/" + businessId

        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        self.assertGreater (len (responseJson['data']['roleModel']), 3)




    @data (('PC', '退换货信息', 0, "用户点击PC业务建模设计"), ('MOBILE', '应用首页', 0, "用户点击移动业务建模设计"))
    @unpack
    def test_device(self, device, dataName, dataLen,casename):
        """{3}"""

        url = self.domain+"/workbench/applications/" + self.applicationId+ "/menus/tree?device=" + device

        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        self.assertEqual (responseJson['data'][0]['name'], dataName)
        self.assertGreater (len (responseJson['data']), dataLen)



    def test_creat_mobile_menus(self):
        '''用户创建移动业务建模页面'''

        name = "接口新建移动业务建模页面"

        url = self.domain+"/workbench/applications/" + self.applicationId+ "/menus"
        data = json.dumps (
            {"name": name, "parentId": "", "applicationId": "", "orderBy": 0, "action": "PAGE",
             "device": "MOBILE", "hasUseAuth": True,
             "extras": {"navigate": True, "navigateIcon": "icon-zhenggaileixing",
                        "roleIds": ["f16023cd89444ccfba1ceeb95d4225f7"], "index": False}})
        response = requests.post (url=url, headers=self.headers, data=data)
        responseJson = response.json ()
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['name'], name)

        # 删除页面
        delUrl = self.domain+"/workbench/applications/" + self.applicationId+ "/menus/" +responseJson['data']['id']
        delresponse = requests.delete (delUrl, headers=self.headers)
        delresponseJson = delresponse.json ()
        self.assertEqual (delresponseJson['code'], 0)

    @data(('用户进入系统管理的平台操作日志页面','','','','','',5),
          ('用户在平台操作日志页面填写操作人查询',CodeController.code_unquote('王浩'),'','','','',0),
          ('用户在平台操作日志页面填写模块查询','','APP_MANAGER','APP_MANAGER_INFO','','',5),
          ('用户在平台操作日志页面填写操作时间查询','','','','2019-10-28%2000%3A00%3A00','2019-10-29%2000%3A00%3A00',5),
          ('用户在平台操作日志页面组合查询',CodeController.code_unquote('王浩'),'APP_MANAGER','APP_MANAGER_INFO','2019-10-28%2000%3A00%3A00','2019-10-29%2000%3A00%3A00',0))
    @unpack
    def test_log_query(self,casename,personName,module,submodule,startTime,endTime,datalen):
        '''{0}'''

        personNameCode = CodeController.code_unquote(personName)
        url = self.domain+"/storage/log/operations/?limit=10&page=1&startTime="+startTime+"&endTime="+endTime+"&module="+module+"&submodule="+submodule+"&personName="+personNameCode

        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        self.assertGreaterEqual(responseJson['data']['totalCount'], datalen)


    def test_organization(self):
        '''用户进入系统管理的企业信息页面'''
        url = self.domain+"/authorize/admin/sessions/organization"
        responseJson = RequestController.getRequestJson (url=url, headers=self.headers)
        self.assertEqual(responseJson['data']['orgName'], "接口自动化七巧")
        self.assertEqual (responseJson['data']['purchaseVersionText'], "七巧专属VIP")


    def test_warningPage_application(self):
        '''用户在低代码监控选择所属应用'''

        url = self.domain+"/workbench/applications?page=1&pageSize=1000&delete=false"
        responseJson = RequestController.getRequestJson(url=url,headers=self.headers)
        self.assertGreaterEqual(len(responseJson['data']['list']), 4)

    @data(('用户在低代码监控查询','','',1),
          ('用户在低代码监控按应用模块查询',applicationId, 'USER_DEFINED',0))
    @unpack
    def test_warningPage_query(self,casename,appId,modelType,datalen):
        '''{0}'''

        url = self.domain+"/workbench/applications/scripts/warning?page=1&pageSize=10&applicationId="+appId+"&modelType="+modelType
        responseJson = RequestController.getRequestJson(url=url,headers=self.headers)
        self.assertGreaterEqual(len(responseJson['data']['list']),datalen)


    def test_role_tag_refs(self):
        '''用户在权限管理点击切换不同标签'''
        tagId = "fc25fa6b1a474d5ba8aaa0d0a35164ca"  #标签：测试
        url = self.domain+"/workbench/role_tag_refs?tagId="+tagId
        responseJson = RequestController.getRequestJson(url=url,headers=self.headers)
        self.assertEqual((responseJson['data'][5]['roles'][1]['check']),True)
        self.assertEqual ((responseJson['data'][5]['roles'][1]['name']), '测试')


    def test_application_permissions(self):
        '''用户在权限管理点击查看应用详细权限'''
        roleId = "d3376eb527934d47b5115ebc20f53d74"  #角色：应用管理员
        pageId = "c2a97bbd6c6f4712b5d04f67ea5cd319"  #退换货信息页面id
        url = self.domain+"/workbench/applications/"+self.applicationId+"/resources?parentId=0&roleId="+roleId+"&device=PC"
        responseJson = RequestController.getRequestJson(url=url,headers=self.headers)

        self.assertEqual ((responseJson['data']['rightResource'][pageId][1]['checked']), True)
        self.assertEqual (len(responseJson['data']['rightResource'][pageId]), 8)


    def test_authorizer_info(self):
        '''用户进入小程序设置页面'''
        url = self.domain+"/workbench/miniprogram/authorization/authorizer_info"
        responseJson = RequestController.getRequestJson(url=url,headers=self.headers)
        self.assertEqual((responseJson['data']['miniProgramInfo']['authorizerAppid']),'')
        self.assertEqual (len(responseJson['data']['miniProgramInfo']['categories']), 0)


    def test_release_processModelIds(self):
        '''用户发布流程'''
        url = self.domain+"/workbench/miniprogram/authorization/authorizer_info"
        responseJson = RequestController.getRequestJson(url=url,headers=self.headers)
        self.assertEqual((responseJson['data']['miniProgramInfo']['authorizerAppid']),'')
        self.assertEqual (len(responseJson['data']['miniProgramInfo']['categories']), 0)










if __name__ == '__main__':
    unittest.main ()
