'''
测试用例
'''

import unittest
import requests
from ddt import ddt,data

param1 = {
    'page': 1,
    'tab': 'share',
    'limit': 1,
    'mdrender': 'false'
}
param2 = {
    'page': 1,
    'tab': 'ask',
    'limit': 1,
    'mdrender': 'false'
}

@ddt
class TestTopics(unittest.TestCase):
    #主题首页
    @data(param1, param2)
    def test_index_page(self,values):
        r=requests.get(url='http://49.233.108.117:3000/api/v1/topics',params=values)
        print(r.json())
        self.assertEqual(r.status_code,200,msg='响应状态码=200')


if __name__ == '__main__':
    unittest.main(verbosity=2)

