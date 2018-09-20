#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# author:hao

# if条件语句
age = 20
if age >= 10:
    print("age =", age)
else:
    print("未成年")

# elseif条件语句
age = 12
if age >= 50:
    print("old")
elif age <= 18:
    print("young")
else:
    print("auld")

# input + if结合
s = input("birth = ")
birth = int(s)
if birth == 100:
    print("hao")
else:
    print("huai")
