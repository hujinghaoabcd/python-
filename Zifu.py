#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# author:hao

print(ord('s'))
print(chr(66))
print(chr(25993))

# 把bytes变为str
print(b'abc'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# 格式化输出
print('%2d-%d' % (3, 3))
print('Age:%s.Gender: %s' % (25, True))

# format格式化输出
print('{0}是大坏蛋'.format('你'))
