# -*- coding:utf-8 -*-


from sys_info import *


def user_add():
    print('添加用户--->')
    new_id = input('\t请输入用户ID：')
    new_name = input('\t请输入用户名：')
    new_tel = input('\t请输入用户电话号码：')

    '''检测输入的ID是否存在，存在则退出，用户ID（类似于学号）是全局唯一标识，不能重复'''
    for user in user_info:
        if new_id == user['id']:
            print(f'用户ID为{new_id}的用户已存在，不能添加相同的ID')
            return

    '''用户名不存在，则将用户信息添加到全局列表'''
    user_dict = {'id': new_id, 'name': new_name, 'tel': new_tel}
    user_info.append(user_dict)
    print(len(user_info))
    print(user_info)