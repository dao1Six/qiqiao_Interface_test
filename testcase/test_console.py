import json
import unittest
import sys
from collections import OrderedDict
from urllib import parse

import params as params
import requests

from requests_toolbelt.multipart.encoder import MultipartEncoder
from pubilc import function
import os
import time




class ConsoleTestSuit(unittest.TestCase):
    '''七巧开发平台测试类'''



    def setUp(self):
        #添加请求头，模拟浏览器访问
        self.headers = {"Accept": "application/json, text/plain, */*",
                   "Cookie": "corpAB=ww6b6c5c4fa6f34b16; _lastReqID=d66bcee5d1f64ce0bde68cfeadd715a1",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
                   "X-Auth0-Token": "1430343df6493be7800d578600952ff4",
                        "Content-Type": "application/json"}

    def test_query_application_01(self):
        '''用户搜索查找已存在应用'''
        name = "OKR"
        url = "https://qy.do1.com.cn/qiqiao/console/api/v1/workbench/applications?delete=false&name="+name+"&applicationGroupId=&page=1"
        response = requests.get(url=url,headers = self.headers)
        responseJson = response.json()
        self.assertEqual(responseJson['data']['totalCount'],1)
        self.assertEqual(responseJson['data']['list'][0]['name'],name)

    def test_appstore(self):
        '''用户进入应用市场页面'''
        url = "https://qy.do1.com.cn/qiqiao/console/api/v1/appstore/app_stores?name="
        response = requests.get(url=url,headers = self.headers)
        responseJson = response.json()
        self.assertEqual(responseJson['code'],0)
        self.assertGreater(len(responseJson['data']['list']),2)

    def test_appstoreoOerview(self):
        '''用户应用市场查看应用详情'''
        applicationId = "93aad8fe99174ed7bf8a76060ea87ccb"
        url = "https://qy.do1.com.cn/qiqiao/console/api/v1/appstore/app_stores/"+applicationId  #OKR应用
        response = requests.get(url=url,headers = self.headers)
        responseJson = response.json()
        self.assertEqual(responseJson['code'],0)
        self.assertEqual(responseJson['data']['applicationName'],'OKR管理')
        self.assertIn( 'OKR是一套明确和跟踪目标及其完成情况的管理工具和方法',responseJson['data']['overview'])
        self.assertEqual(responseJson['data']['status'],"ONLINE")

    def test_locales_en_US(self):
        '''用户在选择语言处切换使用英文'''
        url = "https://qy.do1.com.cn/qiqiao/console/api/v1//workbench/i18n/locales/en_US"
        response = requests.put (url=url, headers=self.headers)
        responseJson = response.json ()
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['country'], 'US')
        self.assertEqual (responseJson['data']['displayName'], 'English (United States)')

    def test_locales_zh_TW(self):
        '''用户在选择语言处切换使用英文'''
        url = "https://qy.do1.com.cn/qiqiao/console/api/v1//workbench/i18n/locales/zh_TW"
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
                   "Content-Type":"application/json"}

        url = "https://qy.do1.com.cn/qiqiao/console/api/v1/workbench/applications/"

        data = {"createUserId":"05f35264ba3441c4be607c25f75cb492","applicationGroupId":"","logo":"icon-zhenggaileixing","mainColor":"#96DECC","name":"创建应用接口测试","status":[],
             "terminalType":["PC_WEB","WX_MINI_PROGRAM","MOBILE_WECHAT"],"delete":False}

        data_json = json.dumps (data)

        response = requests.post(url=url,headers = headers,data=data_json)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson['code'],0)
        self.assertEqual (responseJson['data']['name'], "创建应用接口测试")

        #删除应用
        applicationId = responseJson['data']['id']
        applicationName = parse.quote(responseJson['data']['name'])
        delUrl = "https://qy.do1.com.cn/qiqiao/console/api/v1/workbench/applications/"+applicationId+"?applicationName="+applicationName
        delresponse = requests.delete(delUrl,headers = headers)
        self.assertEqual (responseJson['code'], 0)



    def test_importApplication(self):
        '''用户导入应用'''
        url = "https://qy.do1.com.cn/qiqiao/console/api/v1/workbench/applications/import"

        file = '..\\file_data\\昂星demo.zip'

        a = open(file,'rb')
        m = MultipartEncoder(
            fields={
                'applicationGroupId':'',
                'importType':'ADD',
            'file':('昂星demo.zip',a,'application/x-zip-compressed')
            }
        )
        header = {"Content-Type":m.content_type,
                  "Cookie": "corpAB=ww6b6c5c4fa6f34b16; Hm_lvt_aed59972e7075b4acd495cf5b000c257=1568119947; _lastReqID=81cfe8ae522a42bdbcc961a35ec90bba; tgw_l7_route=2757773c8c583b0e1941ae61de7a309d",
                  "X-Auth0-Token": "99e741e5aecca5799cbe7b380a59351e"}
        response = requests.post(headers = header,url =url,data=m)
        responseJson = response.json ()
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['name'],"昂星demo")

    def test_create_groups(self):
        '''用户添加分组'''

        url = "https://qy.do1.com.cn/qiqiao/console/api/v1/workbench/applications/groups"

        data = {"name":"A","createUserId":None}
        data_json = json.dumps(data)

        response = requests.post (url=url, headers=self.headers, data=data_json)
        responseJson = response.json ()

        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['name'], "A")


    def test_applications_groups(self):
        '''用户切换应用分组'''
        applicationGroupId = "5dad537cd662f60001460fa6"
        url = "https://qy.do1.com.cn/qiqiao/console/api/v1/workbench/applications?delete=false&name=&applicationGroupId="+applicationGroupId+"&page=1"

        data = {"name":"A","createUserId":None}
        data_json = json.dumps(data)

        response = requests.get(url=url, headers=self.headers)
        responseJson = response.json ()

        self.assertEqual (responseJson['code'], 0)
        self.assertGreater(len(responseJson['data']['list']),1)


    def test_applications_release(self):
        '''用户发布应用'''

        applicationId = "5dad5206d662f60001460fa4"

        url = "https://qy.do1.com.cn/qiqiao/console/api/v1/workbench/applications/"+applicationId+"/release"
        data = {"status":["DEFAULT","DEFAULT","DEFAULT"]}  #下架
        datajson = json.dumps(data)

        data2 = {"status":["PC_WEB","MOBILE_WECHAT","WX_MINI_PROGRAM"]}  #上架
        datajson2 = json.dumps (data2)

        response = requests.post (url=url, headers=self.headers, data=datajson)  #先下架

        response2 = requests.post (url=url, headers=self.headers, data=datajson2)  # 再上架
        responseJson2 = response2.json ()


        self.assertEqual (responseJson2['code'], 0)
        self.assertEqual(responseJson2['data']['status'],["PC_WEB", "MOBILE_WECHAT", "WX_MINI_PROGRAM"])


    def test_creat_roles(self):
        '''用户为应用添加角色'''
        applicationId = "a6aece61fa4248fc9a9d4721cb0775f7"
        url = "https://qy.do1.com.cn/qiqiao/console/api/v1/workbench/applications/"+applicationId+"/roles"

        data = {"name":"A","applicationId":"a6aece61fa4248fc9a9d4721cb0775f7","defaultRole":False,"orderNo":1}

        dataJson = json.dumps(data)

        response = requests.post(url,data=dataJson,headers =self.headers)

        responseJson = response.json ()
        self.assertEqual(responseJson['code'], 0)
        self.assertEqual (responseJson['data']['name'], "A")

        #删除角色

        delUrl = "https://qy.do1.com.cn/qiqiao/console/api/v1/workbench/applications/"+applicationId+"/roles/"+responseJson['data']['id']
        delresponse = requests.delete(delUrl,headers =self.headers)
        delresponseJson = delresponse.json ()
        self.assertEqual (delresponseJson['code'], 0)


    def test_form_models(self):
        '''用户进入表单设计页面'''

        applicationId = "a6aece61fa4248fc9a9d4721cb0775f7"

        url = "https://qy.do1.com.cn/qiqiao/console/api/v1/workbench/applications/"+applicationId+"/form_models/list?applicationId="+applicationId+"&formGroupId="
        response = requests.get(url=url,headers = self.headers)
        responseJson = response.json ()
        self.assertEqual (responseJson['code'], 0)
        self.assertGreater (len(responseJson['data']), 2)

    def test_add_forms_groups(self):
        '''用户创建表单分组'''

        applicationId = "a6aece61fa4248fc9a9d4721cb0775f7"
        name = "aaa"

        url = "https://qy.do1.com.cn/qiqiao/console/api/v1/workbench/applications/"+applicationId+"/forms/groups"
        data = json.dumps({"applicationId":applicationId,"name":name})
        response = requests.post(url=url,headers = self.headers,data=data)
        responseJson = response.json ()
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['name'], name)

        #删除分组
        delUrl = "https://qy.do1.com.cn/qiqiao/console/api/v1/workbench/applications/"+applicationId+"/forms/groups/"+responseJson['data']['id']
        delresponse = requests.delete(delUrl,headers =self.headers)
        delresponseJson = delresponse.json ()
        self.assertEqual (delresponseJson['code'], 0)

    def test_creat_form_models(self):
        '''用户创建表单'''

        applicationId = "a6aece61fa4248fc9a9d4721cb0775f7"
        name = "aaa"

        url = "https://qy.do1.com.cn/qiqiao/console/api/v1/workbench/applications/"+applicationId+"/form_models"
        data = json.dumps({"name":name,"formTableId":"form_","formGroupId":"","erType":"1","applicationId":applicationId})
        response = requests.post(url=url,headers = self.headers,data=data)
        responseJson = response.json ()
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['name'], name)

        #删除表单
        delUrl = "https://qy.do1.com.cn/qiqiao/console/api/v1/workbench/applications/"+applicationId+"/form_models/"+responseJson['data']['id']+"?formName="+name
        delresponse = requests.delete(delUrl,headers =self.headers)
        delresponseJson = delresponse.json ()
        self.assertEqual (delresponseJson['code'], 0)


    def test_switch_form(self):
        '''用户切换表单页面'''

        applicationId = "a6aece61fa4248fc9a9d4721cb0775f7"
        formId = "b567fef0a75f49fc8e345943f2ed3c09"
        url = "https://qy.do1.com.cn/qiqiao/console/api/v1/workbench/applications/"+applicationId+"/forms/"+formId

        response = requests.get(url=url,headers = self.headers)
        responseJson = response.json ()
        self.assertEqual (responseJson['data']['formModelId'], 'b567fef0a75f49fc8e345943f2ed3c09')
        self.assertGreater (len(responseJson['data']['formFields']), 0)


    def test_process_models(self):
        '''用户进入流程设计页面'''

        applicationId = "a6aece61fa4248fc9a9d4721cb0775f7"

        url = "https://qy.do1.com.cn/qiqiao/console/api/v1/workbench/applications/"+applicationId+"/process_models"

        response = requests.get(url=url,headers = self.headers)
        responseJson = response.json ()
        self.assertEqual (responseJson['data'][0]['name'], '销售退货流程')

    def test_creat_process_models(self):
        '''用户在流程设计中新建流程'''

        applicationId = "a6aece61fa4248fc9a9d4721cb0775f7"
        name = "接口新建流程"

        url = "https://qy.do1.com.cn/qiqiao/console/api/v1/workbench/applications/"+applicationId+"/process_models"
        data = json.dumps({"name":name,"icon":"icon-renwu"})
        response = requests.post(url=url,headers = self.headers,data=data)
        responseJson = response.json ()
        self.assertEqual (responseJson['code'], 0)
        self.assertEqual (responseJson['data']['name'], name)

        #删除流程
        delUrl = "https://qy.do1.com.cn/qiqiao/console/api/v1/workbench/applications/"+applicationId+"/processData/"+responseJson['data']['id']
        delresponse = requests.delete(delUrl,headers =self.headers)
        delresponseJson = delresponse.json ()
        self.assertEqual (delresponseJson['code'], 0)






























if __name__ == '__main__':
    unittest.main()