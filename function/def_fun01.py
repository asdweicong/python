#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# check##################################

# 如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）：
import math

from def_fun import firstFunction
from def_fun import twoFunction
from def_fun import move

print(isinstance(3, (int, float)))

print(firstFunction(5))
print(twoFunction(-20))
# print(twoFunction('fdfd'))


x, y = move(100, 100, 60, math.pi / 6);
z = move(100, 100, 60, math.pi / 6);
print(x, y);
print(z);


def quadratic(a, b, c):
    d = b * b - 4 * a * c
    x1 = 0;
    x2 = 0;
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
    if d == 0:
        return (-b + math.sqrt(d)) / (2 * a)
    if d < 0:
        return '方程无解'
    else:
        return x1, x2


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(2, 4, 2) =', quadratic(2, 4, 2))
print('quadratic(3, 4, 2) =', quadratic(3, 4, 2))
# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple
