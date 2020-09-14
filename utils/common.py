"""
获取文件路径
os.path.abspath(__file__)
os.path.dirname(pathname)
"""

import os


def get_rootpath():
    """
    返回当前项目的绝度路径
    :return:
    """
    return  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


if __name__ == '__main__':
    path=get_rootpath()
    print(path)