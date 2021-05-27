# -*- coding:utf-8 -*-

from sys_info import *


def user_del():
    print('删除用户--->')
    del_id = int(input('请输入要删除的用户ID:'))  # input输入默认是字符串

    if (0 < del_id < len(user_info)) and (len(user_info) > 0):
        del_tag = input(f'确认要删除ID为{del_id}的用户吗？y or n:')
        if del_tag == 'y':
            del user_info[del_id]
            print(user_info)
        else:
            return
    else:
        return


def ut_user_del():
    demo_user_info = [{'id': '10', 'name': 'TOM', 'tel': '123'}, {'id': '20', 'name': 'July', 'tel': '456'}]
    print('删除用户--->')
    del_id = int(input('请输入要删除的用户ID:'))  # input输入默认是字符串
    if (0 < del_id < len(demo_user_info)) and (len(demo_user_info) > 0):
        del_tag = input(f'确认要删除ID为{del_id}的用户吗？y or n:')
        if del_tag == 'y':
            del demo_user_info[del_id]
            print(demo_user_info)
        else:
            return
    else:
        return


ut_user_del()
