#!/usr/bin/env python3
# -*- coding: utf-8 -*-
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name);

sum = 0
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in list:
    sum = sum + x;
print(sum);
a = range(5)
print(range(5))
sum = 0;
for x in range(101):
    sum += x;
print(sum);

sum = 0;
num = 99;
while num > 0:
    sum += num;
    num -= 2;
print(sum);

L = ['Bart', 'Lisa', 'Adam'];
for x in L:
    print('Hello', x);

n = 1
while n <= 10:
    print(n)
    n = n + 1
print('END')

n = 1
while n <= 10:
    print(n)
    if n > 5:
        break;
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    print(n)
n = 0
while n < 10:
    n = n + 1
    if n == 8:
        continue;
    print(n)
