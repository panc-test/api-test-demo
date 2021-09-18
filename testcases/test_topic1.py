'''
主题首页：get
url:http://49.233.108.117:3000/api/v1/topics
page Number 页数
tab String 主题分类。目前有 ask share job good
limit Number 每一页的主题数量
mdrender String 当为 false 时，不渲染。默认为 true，渲染出现的所有 markdown 格式文本

'''

import unittest
import requests
from ddt import ddt, data

params_data1 = {
    "page": 1,
    "tab": "share",
    "limit": 1,
    "mdrender": "false"
}

params_data2 = {
    "page": 1,
    "tab": "ask",
    "limit": 1,
    "mdrender": "false"
}


@ddt  # 数据驱动
class TestTopicOne(unittest.TestCase):

    def setUp(self) -> None:
        print('start')

    def tearDown(self) -> None:
        print('end')

    @data(params_data1, params_data2)  # 加载测试数据
    def test_index_page(self, value):
        r = requests.get(url='http://49.233.108.117:3000/api/v1/topics', params=value)
        response = r.json()
        print('response=', response)

        # 添加断言
        self.assertEqual(r.status_code, 200, msg='响应状态码=200')

    @unittest.skip('跳过该条测试用例')
    def test_topics(self):
        pass
