# coding=utf-8
import sys
import time
import unittest

import os

# # 获取路径

from BeautifulReport import BeautifulReport

curpath = os.path.dirname (os.path.realpath (__file__))
# 报告目录
reportpath = os.path.join (curpath, "test_report")
if not os.path.exists (reportpath): os.mkdir (reportpath)
# 用例目录
case_path = os.path.join (curpath, "testcase")
report_path = os.path.join(curpath, "test_report")  # 报告存放路径


discover = unittest.defaultTestLoader.discover (case_path, pattern="test_*.py")
# discover相当于在指定的case所在的路径里寻找所有名称模式匹配pattern的文件并加载其内容
result = BeautifulReport(discover)
result.report(filename='test_report', description='七巧接口自动化测试报告', log_path=report_path)





