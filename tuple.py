#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# author:hao

# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1, )

# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变
a = ('a', 'b', ['c', 'c'])
a[2][0] = 'x'
a[2][1] = 'y'
print(a)
