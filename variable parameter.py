#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# author:hao


# 计算a2 + b2 + c2 + ……。
def calc(number):
    sums = 0
    for n in number:
        sums = sums + n*n
    return sums


c = [1, 2, 3, 4]
d = calc(c)
print(d)


# 通过可变参数编写该函数
def calc1(*numbers):
    sums = 0
    for n in numbers:
        sums = sums + n**2
    return sums


print(calc1(1))
print(calc1(1, 2, 3, 4))
nums = [1, 2, 3]
print(calc1(*nums))


# 关键字参数
def person(name, age, **kw):
    print('name:', name , 'age:', age, 'other:', kw)


print(person('liu', 4,))
print(person('wang', 11, city='beijing'))


# 命名关键字参数
def persons(name, age, *, city, job):
    print(name, age, city, job)


print(persons('Jack', 24, city='Beijing', job='Engineer'))


# 多种参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
print(f1(*args, **kw))

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
print(f2(*args, **kw))
