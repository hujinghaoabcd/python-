#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# author:hao


# 定义一个判断函数
def panduan(x):
    if x > 10:
        return 'true'
    else:
        return 'not true'


# 空函数
def nop():
    pass


c = input("请输入一个数字：")
a = int(c)
print("*************该数字是否比十大**************")
d = panduan(a)
print(d)

