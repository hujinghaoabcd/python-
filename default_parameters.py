#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# author:hao


# 一年级小学生注册的函数
# 一个简单函数
def enroll(name, gender):
    print("name", name)
    print("gender", gender)


# 改进函数 加入默认参数
def enroll1(name, gender, year = 6, city = "beijing"):
    print("name", name)
    print("gender", gender)
    print("year", year)
    print("city", city)


print("***********学生信息注册*************")

name1 = input("请输入姓名")
gender1 = input("请输入性别")
year1 = input("请输入年龄")
city1 = input("请输入籍贯")
year2 = int(year1)
enroll1(name1, gender1, year2, city1)


#  定义默认参数要牢记一点：默认参数必须指向不变对象
def addend(L=None):
    if L is None:
        L = []
    L.append("End")
    return L


C =[1, 23]
addend(C)