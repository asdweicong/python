#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# check##################################
age = 1
if age >= 18:
    print('adult');
else:
    print('teenager');

#变量
#变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。
#变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头

a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)

x = 10
x = x + 2
print(x);

a = 'ABC'
b = a
a = 'XYZ'
print(b)
print(a + b)

#常量
#所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量：
PI = 3.14159265359
print(10 / 3);
print(10 // 3); #地板除
print(8 // 3); #地板除
print(10 % 3); #求余数



#inf（无限大）

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n);
print(f);
print(s1);
print(s2);
print(s3);
print(s4);