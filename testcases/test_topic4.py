'''
从excel文件中读取测试数据
'''

import unittest
from ddt import ddt,data
from utils.do_excel import DoExcel
from utils.do_request import DoRequests

# 从excel文件中读取测试数据，存放到列表中
doexcel = DoExcel(filepath='./data/topicdata.xlsx', sheetname='indextopic')
all_data = doexcel.read_excel()

@ddt    #数据驱动
class TestTopics(unittest.TestCase):

    def setUp(self) -> None:
        print('start')

    def tearDown(self) -> None:
        print('end')

    @data(*all_data)      #加载测试数据
    def test_index_page(self,value):
        print("value=",value)
        #调用封装的请求方法发送请求
        DR = DoRequests(method=value[1], url=value[2])
        r = DR.do_request(data=eval(value[3]))    # value[3] 是一个str类型,使用eval 函数将字符串转换成字典
        response = r.json()
        print('response=',response)

        #添加断言
        self.assertEqual(r.status_code,200,msg='响应状态码=200')


if __name__ == '__main__':
    unittest.main(verbosity=2)



