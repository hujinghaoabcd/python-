#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# author:hao

# 简单的for循环
names = ['Tom', 'jim', 'hem']
for name in names:
    print(name)

# 求和
he = 0
a = [1, 2, 3, 4, 5, 6]
for x in a:
    he = he + x
print(he)

# range函数
lists = list(range(101))
sums = 0
for y in lists:
    sums = sums + y
print(sums)

# while 循环
sums = 0
n = 100
while n > 0:
    sums = sums + n
    n = n - 1
print(sums)

# break 跳出循环
n = 1
while n < 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print("end")

# continue语句会直接继续下一轮循环，后续的print()语句不会执行
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
