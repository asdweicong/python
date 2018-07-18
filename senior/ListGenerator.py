#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 请始终牢记，代码越少，开发效率越高。

List = list(range(1, 11));
print(List);

L = [];
for x in range(1, 11):
    L.append(x * x);
print(L);

a = [x * x for x in range(1, 11)];
print(a);
b = [x * x for x in range(1, 11) if x % 2 == 0];
print(b);

# 还可以使用两层循环，可以生成全排列：
c = [m + n for m in "ABC" for n in "EFG"];
print(c);

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os  # 导入os 模块，

d = [d for d in os.listdir('.')];
print(d);
e = {'x': 'A', 'y': 'B', 'z': 'C'};
for k, v in e.items():
    print(k + "=" + v);

f = ['Hello', 'World', 'IBM', 'Apple'];
g = [s.lower() for s in f];
print (g);

from collections import Iterable

h = ['Hello', 'World', 18, 'Apple', None]
i = [j.lower() for j in h if (isinstance(j, str))];
print(i);
