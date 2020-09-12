'''
主题详情  get
url=http://49.233.108.117:3000/api/v1/topic/:id
mdrender String 当为 false 时，不渲染。默认为 true，渲染出现的所有 markdown 格式文本。
accesstoken String 当需要知道一个主题是否被特定用户收藏以及对应评论是否被特定用户点赞时，才需要带此参数。
会影响返回值中的 is_collect 以及 replies 列表中的 is_uped 值

'''


import unittest
import requests


id='5f59e27e95933d295b621564'

data = {
    'mdrender':'false'
}


class TestCreateTopic(unittest.TestCase):

    def setUp(self) -> None:
        print('start----------------------')

    def tearDown(self) -> None:
        print('end-----------------------')

    def test_create_topic(self):
        r=requests.get(url='http://49.233.108.117:3000/api/v1/topic/'+id,params=data)
        print(r.json())
        #断言
        self.assertEqual(r.status_code,200,msg='断言响应码')


if __name__ == '__main__':
    unittest.main(verbosity=2)
