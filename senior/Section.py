#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 请始终牢记，代码越少，开发效率越高。
# L = [];
# n = 1;
# while n <= 99:
#     L.append(n);
#     n += 2;
# print(L);
#
# l = [1, 2, 3, 4, 5, 6];
# r = [];
# n = 3;
# for i in range(n):
#     r.append(l[i])
# # print(r)
# print(l[1:3]);  # 从索引1开始，取出2个元素出来：
# print(l[1:]);  # 从索引1开始，取出后面的数据
# print(l[-2:]);  # 从索引倒数第二个开始获取
# print(l[::2]);  # 每两个取一个：
# print(l[:]);  # 复制一份l
#
#
# # tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
# a = (0, 1, 2, 3, 4, 5);
# print(a[:3]);
# # 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
# b= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(b[:4])
# print(b[::5])

c = ' abcd e f  ';


# 去除左右两边空格函数
def trim(s):
    i = 0;
    j = len(s);
    while s[i] == " ":
        i += 1;
    while s[j - 1] == " ":
        j -= 1;
    s = s[i:j];
    return s


print('trims: = ', trim(c));


def trim2(s):
    if s[0] == " ":
        return trim2(s[1:])
    elif s[-1] == " ":
        return trim2(s[:-2])
    else:
        return s


print(trim2(c))


L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])

R = list(range(100))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])
