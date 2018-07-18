#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = 20
if age >= 18:
    print('your age is', age);
    print('adult');

birth = input('birth: ')
birth = int(birth)
if birth <= 2000:
    print('00前')
else:
    print('00后')

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
height = 1.75
weight = 80.5
bmi = weight / (height * height)
print(bmi);
# 条件判断可以让计算机自己做选择，Python的if...elif...else很灵活。
# 条件判断从上向下匹配，当满足条件时执行对应的块内语句，后续的elif和else都不再执行。
if bmi < 18.5:
    print("过轻");
elif bmi <= 25:
    print("正常");
elif bmi <= 27:
    print("过重");
elif bmi <= 32:
    print("肥胖");
else:
    print("严重肥胖");

