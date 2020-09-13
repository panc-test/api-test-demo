"""
封装请求方法
"""

import requests

class DoRequests():

    def __init__(self,method,url):
        """
        构造器
        :param method:
        :param url:
        """
        self.method = method
        self.url = url

    def do_request(self,data=None):
        """
        封装请求方法
        :param data:
        :return:
        """
        if self.method == "get":
            return requests.get(url=self.url,params=data)
        elif self.method == "post":
            return requests.post(url=self.url,data=data)
