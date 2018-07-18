#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# check##################################

def firstFunction(a):
    if (a > 5):
        return "大于五";
    else:
        return "小于等于五";


a = firstFunction(5);


# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
# if(a >2):
#   pass;

def twoFunction(b):
    if not isinstance(b, (int, float)):
        raise TypeError("bad operand type");
    if b >= 0:
        return b;
    else:
        return -b;


import math;


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.cos(angle)
    return nx, ny
