#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# check##################################
# 要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。可以直接从Python的官方网站查看文档：
# http://docs.python.org/3/library/functions.html#abs
print(abs(100));
print(abs(-105));
print(abs(12.34));
# print(abs(1, 2));调用函数的时候，如果传入的参数数量不对，会报TypeError的错误，并且Python会明确地告诉你：abs()有且仅有1个参数，但给出了两个
# print(abs('a'));如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误，并且给出错误信息：str是错误的参数类型：
#而max函数max()可以接收任意多个参数，并返回最大的那个
print(max(2, 3, 1, -5));

#Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数
print(int(1.12))
print(float(112))
print(str(112))
print(bool(1))
a= abs#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
print(a(-1))


n1 = 255
n2 = 1000
print(hex(n1));
print(hex(n2));