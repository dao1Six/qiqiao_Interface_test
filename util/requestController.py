import requests


class RequestController():

    #get请求返回json
    @staticmethod
    def getRequestJson(url,headers):
        response = requests.get (url=url, headers=headers)
        responseJson = response.json ()
        return responseJson