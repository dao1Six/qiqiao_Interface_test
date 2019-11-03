import json

import requests


class RequestController():

    #get请求返回json
    @staticmethod
    def getRequestJson(url,headers):
        response = requests.get (url=url, headers=headers)
        responseJson = response.json ()
        return responseJson



    #put请求返回json
    @staticmethod
    def putRequestJson(url,headers,data):
        response = requests.put (url=url, headers=headers,data=json.dumps (data))
        responseJson = response.json ()
        return responseJson

    #post请求返回json
    @staticmethod
    def postRequestJson(url,headers,data):
        response = requests.post (url=url, headers=headers,data=json.dumps (data))
        responseJson = response.json ()
        return responseJson


    #delete请求返回json
    @staticmethod
    def deleteRequestJson(url,headers,*args):
        response = requests.delete (url=url, headers=headers,data = args)
        responseJson = response.json ()
        return responseJson


