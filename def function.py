#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# author:hao

import math as m


# 定义一个判断函数
def panduan(x):
    if x > 10:
        return 'true'
    else:
        return 'not true'


# 参数检查 利用内置函数isinstance()实现、
def my_abss(y):
    if not isinstance(y, (int, float)):
        raise TypeError('错误的数据类型')
    if y > 0:
        print("该数为正数")
    elif y == 0:
        print("该数为0")
    else:
        print("该数为负数")


# 空函数
def nop():
    pass


c = input("请输入一个数字：")
a = int(c)

print("*************该数字是否比十大**************")
d = panduan(a)
print(d)

print("******************该数字的类型*************")
e = my_abss(a)
print(e)

nop()


# 导入一个第三方包，并调用其函数
# 定义一个坐标计算函数


def move(x, y, step, angle=0):
    nx = x + step * m.cos(angle)
    ny = y + step * m.sin(angle)
    return nx, ny


print(move(1, 2, 3, 20))

