#!/usr/bin/env python3
# -*- coding: utf-8 -*-
classmates = ['Michael', 'Bob', 'Tracy'];
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
#list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Adam');
print(classmates[-1]);
#也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'Jack')
print(classmates);
#要删除list末尾的元素，用pop()方法
classmates.pop();#最后一个
print(classmates);
classmates.pop(2);#指定第几个
print(classmates)

l = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(l[0][0])
print(l[1][1])
print(l[2][2])