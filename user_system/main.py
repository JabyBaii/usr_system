# -*- coding:utf-8 -*-

# 用户管理系统
# 1.1 系统简介
# 需求：进⼊系统显示系统功能界⾯，功能如下：
# 添加用户
# 删除用户
# 修改用户信息
# 查询用户信息
# 显示所有用户信息
# 退出系统
# 系统共6个功能，⽤户根据⾃⼰需求选取。
# 1.2 步骤分析
# 1. 显示功能界⾯
# 2. ⽤户输⼊功能序号
# 3. 根据⽤户输⼊的功能序号，执⾏不同的功能(函数)
# 3.1 定义函数
# 3.2 调⽤函数

"""
开发思路：
1. 搭建整体框架，包括接口，可运行的完整框架，是否分文件、函数的接口
2. 各接口的具体实现
3. 异常的处理，尽量考虑全面
"""
# from sys_info import _init
from sys_info import *
from user_add import *
from user_change import *
from user_del import *
from user_query import *

# init()


def user_display():
    print('显示所有用户信息')


while True:
    print_info()
    input_num = input('请根据数字提示，输入操作的类型：')
    if input_num == '1':
        user_add()
    elif input_num == '2':
        user_del()
    elif input_num == '3':
        user_change()
    elif input_num == '4':
        user_query()
    elif input_num == '5':
        user_display()
    elif input_num == '6':
        print('退出管理系统\n')
        break
    else:
        print('输入有误，请重新输入...\n')
