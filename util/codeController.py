#字符编码，解码
from urllib import parse


class CodeController():


    #字符编码
    @classmethod
    def code_quote(cls,code):
        return parse.quote (code)



    #字符解码
    @classmethod
    def code_unquote(cls,code):
        return parse.unquote (code)