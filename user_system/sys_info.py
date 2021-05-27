# -*- coding:utf-8 -*-


user_info = []  # 全局用户信息列表


def init():  # 初始化
    global user_info


def print_info():
    print('-' * 20)
    print('欢迎登录用户管理系统')
    print('1: 添加用户')
    print('2: 删除用户')
    print('3: 修改用户信息')
    print('4: 查询用户信息')
    print('5: 显示用户信息')
    print('6: 退出系统')
    print('-' * 20)



    # global _global_dict
    # _global_dict = {}


# def set_value(key, value):
#     """ 定义一个全局变量 """
#     _global_dict[key] = value
#
#
# def get_value(key, defValue=None):
#     """ 获得一个全局变量,不存在则返回默认值 """
#     try:
#         return _global_dict[key]
#     except KeyError:
#         return defValue
