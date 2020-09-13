"""
post /topics 新建主题,接收 post 参数
url:http://49.233.108.117:3000/api/v1/topics
accesstoken String 用户的 accessToken
title String 标题
tab String 目前有 ask share job dev。开发新客户端的同学，请务必将你们的测试帖发在 dev 专区，以免污染日常的版面，否则会进行封号一周处理。
content String 主体内容

"""
import unittest
import requests
from ddt import ddt,data,file_data

@ddt
class TestCreateTopics(unittest.TestCase):

    def setUp(self) -> None:
        print('start-------------------')

    def tearDown(self) -> None:
        print('end---------------------')

    @file_data('../data/create_topics.yaml')
    def test_create_topics(self,accesstoken,title,tab,content):
        body={
            "accesstoken":accesstoken,
            "title":title,
            "tab":tab,
            "content":content
        }
        print("body=",body)
        r=requests.post(url='http://49.233.108.117:3000/api/v1/topics',data=body)
        print(r.json())
        #添加断言
        self.assertEqual(r.status_code,200,'响应码=200')


if __name__ == '__main__':
    unittest.main(verbosity=2)