#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 请始终牢记，代码越少，开发效率越高。

list = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
for key in list:
    print(key, list[key]);

for ch in "ABC":
    print(ch);

# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
from collections import Iterable

print(isinstance("abc", Iterable))
print(isinstance(123456, Iterable))

# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(["A", "B", "C"]):
    print(i, value);
for x, y in [(1, 1), (2, 4), (3, 8)]:
    print(x, y);

nums = [100, -25.0, 36, '422', 12, 0.1, 34, 15, '123'];
num = [];


def findMaxAndMin(LNum):
    max = LNum[0];
    min = LNum[0]
    # if not isinstance(LNum, (list)):
    #     raise TypeError(TYPE_ERROR)
    if len(LNum) == 0:
        return (None, None)
    for num in LNum:
        if not isinstance(num, (int, float)):
            print(num, '數據類型錯誤，已被忽略……')
            continue
            # raise TypeError(TYPE_ERROR)
        if num > max:
            max = num
        if num < min:
            min = num
    return (min, max)


nums = [100, -25.0, 36, '422', 12, 0.1, 34, 15, '123']
num = []
print(findMaxAndMin(nums))
