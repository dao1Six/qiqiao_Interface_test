#字符编码，解码
from urllib import parse


class CodeController():


    #字符编码
    @classmethod
    def code_quote(cls,str):
        return parse.quote (str)



    #字符解码
    @classmethod
    def code_unquote(cls,code):
        return parse.unquote (code)