# -*- coding:utf-8 -*-

from sys_info import *


def user_change():
    print('修改用户信息--->')
    print(user_info)
    modify_id = int(input('请输入要修改的用户ID:'))

    for item in user_info:
        if modify_id == int(item['id']):
            print(f'ID为{modify_id}的用户原始信息为：{item}')
            user_info[user_info.index(item)]['id'] = input('请输入新的用户ID：')
            user_info[user_info.index(item)]['name'] = input('请输入新的用户名：')
            user_info[user_info.index(item)]['tel'] = input('请输入新的用户电话：')
            print(f'ID为{modify_id}的用户修改后的信息为：{item}')
    print(f'当前系统用户：{user_info}')



