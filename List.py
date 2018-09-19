#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# author:hao

classmate = ['hujinghao', 'guanbaoyu']
print(classmate)
print(len(classmate))
print(classmate[0])
print(classmate[1])
print(classmate[-1])

# list中追加元素到末尾
classmate.append('caoshhuo')
print(classmate)

# 把元素插入到指定的位置
classmate.insert(1, 'shexin')
print(classmate)

# 删除list末尾的元素
# 删除指定位置的元素
a = classmate.pop()
b = classmate.pop(1)
print(a + b)

# 替换
classmate[1] = 'Sarah'
print(classmate)

# list里面的元素的数据类型也可以不同
# list元素也可以是另一个list
c = ['hujinghsp', 2]
s = [['a', 'c'], 12, 'jjj']
print(c)
print(s)