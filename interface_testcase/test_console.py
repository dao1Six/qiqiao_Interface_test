import json
import os
import unittest
import sys
from collections import OrderedDict
from urllib import parse

import params as params
import requests
import xmlrunner as xmlrunner
from requests import request

from requests_toolbelt.multipart.encoder import MultipartEncoder

from ddt import ddt, data, unpack

from reportRunner import Report
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



    @data(('用户创建PC业务建模分组',{"orderBy":0,"name":"a","parentId":None,"applicationId":"c4cafae231b042949861bd73a10a65c4","action":"MENU","device":"PC"}),
          ('用户创建小程序业务建模分组',{"name":"ces","parentId":"","applicationId":"","orderBy":0,"action":"MENU","device":"MINI_PROGRAM","hasUseAuth":False,"extras":{"navigate":False,"navigateIcon":"","roleIds":[]}}),
          ('用户创建移动业务建模分组',{"name":"ds","parentId":"","applicationId":"","orderBy":0,"action":"MENU","device":"MOBILE","hasUseAuth":True,"extras":{"navigate":False,"navigateIcon":"","roleIds":[]}}),

          ('用户创建PC业务建模页面',
           {"orderBy": 0, "name": "dd", "parentId": None, "applicationId": "c4cafae231b042949861bd73a10a65c4",
            "action": "PAGE", "device": "PC"}),
          ('用户创建小程序业务建模页面', {"name":"dasd","parentId":"","applicationId":"","orderBy":0,"action":"PAGE","device":"MINI_PROGRAM","hasUseAuth":False,"extras":{"navigate":False,"navigateIcon":"icon-zhenggaileixing","roleIds":[],"index":False}}),
          ('用户创建移动业务建模页面',
           {"name": "da", "parentId": "", "applicationId": "", "orderBy": 0, "action": "PAGE", "device": "MOBILE",
            "hasUseAuth": True, "extras": {"navigate": False, "navigateIcon": "icon-zhenggaileixing",
                                           "roleIds": ["d3376eb527934d47b5115ebc20f53d74"], "index": False}}),
          )
    @unpack
    def test_creat_menus(self,casename,data):
        '''{0}'''

        url = self.domain+"/workbench/applications/" + self.applicationId+ "/menus"
        responseJson = RequestController.postRequestJson (url=url, headers=self.headers, data=data)
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['name'], data['name'])

        # 删除页面
        delUrl = self.domain+"/workbench/applications/" + self.applicationId+ "/menus/" + \
                 responseJson['data']['id']
        delresponseJson = RequestController.deleteRequestJson (delUrl, headers=self.headers)
        self.assertEqual (delresponseJson['code'], 0)

    def test_switch_business(self):
        '''用户切换PC端页面'''

        businessId = "c2a97bbd6c6f4712b5d04f67ea5cd319"

        url = self.domain+"/workbench/applications/" + self.applicationId+ "/business/" + businessId

        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        self.assertGreater (len (responseJson['data']['roleModel']), 3)




    @data (('PC', '退换货信息', 0, "用户点击PC业务建模设计"), ('MOBILE', '应用首页', 0, "用户点击移动业务建模设计"),('MINI_PROGRAM', '首页', 1, "用户进入小程序业务建模页面"))
    @unpack
    def test_device(self, device, dataName, dataLen,casename):
        """{3}"""

        url = self.domain+"/workbench/applications/" + self.applicationId+ "/menus/tree?device=" + device

        response = requests.get (url=url, headers=self.headers)
        responseJson = response.json ()
        self.assertEqual (responseJson['data'][0]['name'], dataName)
        self.assertGreaterEqual(len (responseJson['data']), dataLen)



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
        self.assertIsNotNone((responseJson['data']['miniProgramInfo']['authorizerAppid']))
        self.assertEqual (len(responseJson['data']['miniProgramInfo']['categories']), 0)


    def test_release_processModelIds(self):
        '''用户发布下架流程'''
        processModelIds = 'e60177c4b0f347f49ec15505def5184a'
        xiajia = 'DISRELEASE'  #下架
        fabu = 'RELEASE'  #上架

        #先上架
        url = self.domain+"/workbench/applications/0/process_models/release?processModelIds="+processModelIds+"&processStatusEnum="+fabu
        responseJson = RequestController.putRequestJson(url=url,headers=self.headers,data=None)
        self.assertEqual(responseJson['msg'],'执行成功')

        #下架
        xiajiaurl = self.domain+"/workbench/applications/0/process_models/release?processModelIds="+processModelIds+"&processStatusEnum="+xiajia
        xiajiaresponseJson = RequestController.putRequestJson(url=xiajiaurl,headers=self.headers,data=None)
        self.assertEqual(xiajiaresponseJson['msg'],'执行成功')



    def test_portal_settings(self):
        '''用户进入门户设置的基础设置页面'''
        url = self.domain+"/workbench//portal_settings"
        responseJson = RequestController.getRequestJson(url=url,headers=self.headers)
        self.assertEqual(responseJson['msg'],'执行成功')
        self.assertIsNotNone (responseJson['data']['name'])



    @data(('用户编辑门户名称',{"name":'接口测试',"logoPath":"","pcBackgrounPath":"","applicationNum":"SIX_COUNT","processNum":"SIX_COUNT"}),
          ('用户设置PC端常用应用数量',{"name":'接口测试',"logoPath":"","pcBackgrounPath":"","applicationNum":"EIGHT_COUNT","processNum":"SIX_COUNT"}),
          ('用户设置PC端常用流程数量', {"name": '接口测试', "logoPath": "", "pcBackgrounPath": "", "applicationNum": "SIX_COUNT",
                     "processNum": "EIGHT_COUNT"}) )
    @unpack
    def test_portal_settings_modify(self,casename,json):
        '''{0}'''
        url = self.domain+"/workbench//portal_settings"
        responseJson = RequestController.postRequestJson (url=url, headers=self.headers,data=json)
        self.assertEqual (responseJson['data']['name'],json['name'])
        self.assertEqual (responseJson['data']['applicationNum'], json['applicationNum'])
        self.assertEqual (responseJson['data']['processNum'], json['processNum'])


    def test_process_visible_permissions(self):
        '''用户配置流程可见权限'''
        url = self.domain+"/workbench/process_visible_permissions"
        json = {"applicationId":"c4cafae231b042949861bd73a10a65c4","applicationName":"昂星demo","applicationOrderBy":0,"createTime":1572317073000,"createUserId":"05f35264ba3441c4be607c25f75cb492","delete":False,"departIds":["9b5acd0ced7f4c4794fcd855083a02ce","44eb0451b8d7459488a1b4405c0b9766"],"id":"","processModelId":"e60177c4b0f347f49ec15505def5184a","processModelName":"销售退货流程","processModelOrderBy":0,"status":"DISRELEASE","tagIds":[],"tenantId":"2ade557c80d0430d9eee7589b30e4447","updateTime":1572317073000,"userIds":[],"tags":[{"id":"9b5acd0ced7f4c4794fcd855083a02ce","name":"质量委员会","type":"departments"},{"id":"44eb0451b8d7459488a1b4405c0b9766","name":"事业三部","type":"departments"}],"rowIndex":1}

        json2 = {"applicationId":"c4cafae231b042949861bd73a10a65c4","applicationName":"昂星demo","applicationOrderBy":0,"createTime":1572317073000,"createUserId":"05f35264ba3441c4be607c25f75cb492","delete":False,"departIds":[],"id":"","processModelId":"e60177c4b0f347f49ec15505def5184a","processModelName":"销售退货流程","processModelOrderBy":0,"status":"DISRELEASE","tagIds":[],"tenantId":"2ade557c80d0430d9eee7589b30e4447","updateTime":1572317073000,"userIds":[],"tags":[],"rowIndex":1}

        responseJson = RequestController.postRequestJson (url=url, headers=self.headers,data=json)  #授权
        self.assertEqual (len(responseJson['data']['departIds']),2)

        responseJson = RequestController.postRequestJson (url=url, headers=self.headers,data=json2)  #还原
        self.assertEqual (len(responseJson['data']['departIds']),0)



    def test_process(self):
        '''用户进入流程发布设置页面'''
        url = self.domain+"/workbench/process_visible_permissions?applicationName=&status="
        responseJson = RequestController.getRequestJson(url=url,headers=self.headers)
        self.assertEqual(responseJson['msg'],'执行成功')
        self.assertGreaterEqual (responseJson['data']['processVisiblePermissionRestPage']['totalCount'],7)


    @data(
        ('用户访问应用低代码中心','',1),
        ('用户在低代码查询已选择的脚本所属模型','USER_DEFINED',0)
    )
    @unpack
    def test_scriptsPage(self,casename,modelType,datalen):
        '''{0}'''
        url = self.domain+"/workbench/applications/5db92b05eadba6000150f3b9/scripts?pageSize=10&page=1&status=&modelType="+modelType
        responseJson = RequestController.getRequestJson(url=url,headers=self.headers)
        self.assertEqual(responseJson['msg'],'执行成功')
        self.assertGreaterEqual (responseJson['data']['totalCount'],datalen)


    @data(
        ('用户更改PC端业务角色权限','PC',["c2a97bbd6c6f4712b5d04f67ea5cd319","e24dfb7b215642d189a3e20a4fe960d9","ad90ead228f34e51b9ad0ab9bcc438df","f80561f7438543af94f344a8230a40d3","d34b6cedb49c45a4b7f2a8c46989a751","cb8c88bc6c7e47fc98e8b6577486fa85","c9fd1946386d4be1a8ca2ea94241f192","bb3ab08c01044a94830424c655782f1e","aac988e03e95427fa5d9324c5dce01e3"]),
        ('用户更改移动端门户角色权限','MOBILE',["a553d6a863a64d8ba1afbcde0554dd7d"])
    )
    @unpack
    def test_(self,casename,device,data):
        ''''''
        roleid = "5dba87241536b40001dbcb90"
        url = self.domain + "/workbench/applications/"+self.applicationId+"/resources/roles/"+roleid+"?device="+device
        responseJson = RequestController.putRequestJson (url=url, headers=self.headers,data=data)
        self.assertEqual (responseJson['msg'], '执行成功')

        #还原
        responseJson2 = RequestController.putRequestJson (url=url, headers=self.headers,data=[])
        self.assertEqual (responseJson2['msg'], '执行成功')


