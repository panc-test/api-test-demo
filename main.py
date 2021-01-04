"""
程序主入口
"""

import unittest
from BeautifulReport import BeautifulReport


def suite():
    """
    定义测试套件，并加载测试用例
    :return:
    """
    suite=unittest.TestSuite()
    tests=unittest.TestLoader().discover(start_dir='./testcases',pattern="test*.py")
    suite.addTests(tests)
    return suite


if __name__ == '__main__':
    """
    执行测试套件，生成测试报告
    """
    suite = suite()
    result=BeautifulReport(suite)
    result.report(report_dir='./report',filename='cnode测试报告',description='test_conde')



