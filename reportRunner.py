import os

import xmlrunner

class Report():
    def run_suite_output_xml_report(self,suite, **args):
        '''
        :param suite: 已组装好的测试套
        :param args: 可设置的参数及说明如下：
             TEST_OUTPUT_DESCRIPTIONS: 输出描述
             TEST_OUTPUT_DIR：测试报告输出路径，默认为根目录
             TEST_OUTPUT_FILE_NAME：测试报告输入文件名，默认为hsplatform_ut_testreport.xml
        :return:
        '''
        curpath = os.path.dirname (os.path.realpath (__file__))
        # 报告目录
        reportpath = os.path.join (curpath, "test_report")
        descriptions = args.get('TEST_OUTPUT_DESCRIPTIONS', True)
        output_dir = args.get('TEST_OUTPUT_DIR', reportpath)
        single_file = args.get('TEST_OUTPUT_FILE_NAME', 'qiqiao_testreport.xml')
        kwargs = dict(verbosity=1, descriptions=descriptions)
        if single_file is not None:
            file_path = os.path.join(output_dir, single_file)
            with open(file_path, 'wb') as xml:
                return xmlrunner.XMLTestRunner(output=xml, **kwargs).run(suite)
        else :
            return xmlrunner.XMLTestRunner(output=output_dir, **kwargs).run(suite)
