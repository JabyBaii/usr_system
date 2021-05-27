# -*- coding:utf-8 -*-
"""
1.同样的问题，如果输入的id找不到，如何提示用户
"""

from sys_info import *


def user_query():
    print('查询用户信息--->：')
    # print(user_info)

    user_id = input('请输入要查询的用户ID:')
    for item in user_info:
        if user_id == item['id']:
            print(item)

