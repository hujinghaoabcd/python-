#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# author:hao
import math


def equations(a, b, c):
    x1 = (-b+math.sqrt(c))/a*2
    x2 = (-b-math.sqrt(c))/a*2
    return x1, x2


print("************计算一元二次方程的解******************")
a1 = input("请输入一元二次方程的a参数")
b1 = input("请输入一元二次方程的b参数")
c1 = input("请输入一元二次方程的c参数")
a2 = int(a1)
b2 = int(b1)
c2 = int(c1)
d = equations(a2, b2, c2)
print("{0}x**2+{1}*x+{2}方程的解{3}".format(a1, b1, c1, d))

