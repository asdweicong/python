#!/usr/bin/env python3
# -*- coding: utf-8 -*-
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print('Thomas' in d);  # 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print(d.get('Thomas', -1));  # 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
d.pop('Bob');  # 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
print(d);

b = [1, 2, 3, 5, 5, 2, 4, 4]
b = set(b);
b.add(8)
b.remove(5)
print(b);


s1 = set([1, 2, 3])
s2 = set([1, 5, 8])
print(s1 & s2);
print(s1 | s2);


