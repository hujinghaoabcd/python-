#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# author:hao

# 一个简单的字典
d = {'tom': 88, 'jim': 90}
print(d['tom'])
d['jim'] = 99
print(d['jim'])

# 判断key是否存在
print('tom' in d)
print(d.get('jim'))

# 删除一个key
d.pop('tom')
print(d)

# set 实例
s1 = set([7, 1, 4, 5, 5, 6])
print(s1)
s1.add(0)
s1.remove(4)
print(s1)















