#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'));
print(ord('好'));
print(chr(22909));
print('\u4e2d\u6587');
# x = b'ABC'
# print(x);

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
print('ABC'.encode('ascii'));
print('中文'.encode('utf-8'));
# print('中文'.encode('ascii'));
# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。
# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
print(b'ABC'.decode('ascii'));
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'));

# 如果bytes中包含无法解码的字节，decode()方法会报错：
# print(b'\xe4\xb8\xad\xff'.decode('utf-8'))

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'));

# 要计算str包含多少个字符，可以用len()函数：
print(len("qianqian"));

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len(b'ABC'));
print(len('中文'.encode('utf-8')));
print('中文'.encode('utf-8'));

print('%2d-%02d' % (3, 1));
print('%.2f' % 3.1415926);
print('Hello, {0}, 成绩提升了 {1:.2f}%'.format('小明', 17.125));


s1 = 72;
s2 = 85;
r = (85-72)/72
print('%.2f' % r)


