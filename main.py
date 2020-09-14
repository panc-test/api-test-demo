"""
程序主入口
"""

import unittest
from BeautifulReport import BeautifulReport


def suite():
    suite=unittest.TestSuite()
    tests=unittest.TestLoader().discover(start_dir='./testcases',pattern="test*.py")
    suite.addTests(tests)
    return suite


if __name__ == '__main__':
    suite = suite()
    result=BeautifulReport(suite)
    result.report(report_dir='./report',filename='cnode测试报告',description='test_20200914')


