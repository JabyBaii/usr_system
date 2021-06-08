# -*- coding:utf-8 -*-
"""
1：想想怎么写ut函数，变量传参好还是用全局变量好；
2：有个bug，就是输入的ID如果是用户信息系统里没有的，则不会有任何提示，想想这个问题怎么解决
"""

from sys_info import *


def user_del():
    print('删除用户--->')
    del_id = int(input('请输入要删除的用户ID（ID格式应为整数）:'))  # input输入默认是字符串
    if (isinstance(del_id, int)) and (len(user_info) > 0):
        '''确定要删除这个ID的用户，需要先进行查找是否存在这个ID'''
        for item in user_info:  # 取出所有字典元素
            # print(item['id'])   # 取出每个字典元素key对应的value
            # print(type(item['id']))   # 取出每个字典元素key对应的value
            # print(user_info.index(item))    # 取出每个字典元素在列表中的下标，用于删除这个用户的所有信息
            if int(item['id']) == del_id:
                while True:  # 这个循环，防止用户y or n 输入失误
                    del_tag = input(f'确认要删除ID为{del_id}的用户吗？y or n:')
                    if del_tag == 'y':
                        del user_info[user_info.index(item)]  # 删除列表中的字典元素
                        print(f'当前系统用户：{user_info}')
                        break
                    elif del_tag == 'n':
                        break
                    else:
                        print('输入有误...')
    else:
        print('输入的ID有误,格式应为整数')


# def ut_user_del():
#     user_info = [{'id': '10', 'name': 'TOM', 'tel': '123'}, {'id': '20', 'name': 'July', 'tel': '456'}]
#
#     print('删除用户--->')
#     del_id = int(input('请输入要删除的用户ID（ID格式应为整数）:'))  # input输入默认是字符串
#     if (isinstance(del_id, int)) and (len(user_info) > 0):
#         '''确定要删除这个ID的用户，需要先进行查找是否存在这个ID'''
#         for item in user_info:  # 取出所有字典元素
#             # print(item['id'])   # 取出每个字典元素key对应的value
#             # print(type(item['id']))   # 取出每个字典元素key对应的value
#             # print(user_info.index(item))    # 取出每个字典元素在列表中的下标，用于删除这个用户的所有信息
#             if int(item['id']) == del_id:
#                 while True:  # 这个循环，防止用户y or n 输入失误
#                     del_tag = input(f'确认要删除ID为{del_id}的用户吗？y or n:')
#                     if del_tag == 'y':
#                         del user_info[user_info.index(item)]  # 删除列表中的字典元素
#                         print(f'剩余用户：{user_info}')
#                         break
#                     elif del_tag == 'n':
#                         break
#                     else:
#                         print('输入有误...')
#     else:
#         print('输入的ID有误,格式应为整数')

# 优化 下面这段代码可用于做UT测试
if __name__ == '__main__':
    user_info = [{'id': '10', 'name': 'TOM', 'tel': '123'}, {'id': '20', 'name': 'July', 'tel': '456'}]
    print(f'{user_info}')
    user_del()
    print(f'{user_info}')
