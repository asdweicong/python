#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 请始终牢记，代码越少，开发效率越高。

L = [x * x for x in range(10)];
print(L);

g = (x * x for x in range(10));
print (g);
print(next(g))


# for n in g:
#     print(n);
# 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了
def fib(max):
    n, a, b = 0, 0, 1;
    while n < max:
        yield (b)
        a, b = b, a + b
        n += 1;


print (fib(100))
g = fib(6)
while True:
    try:
        x = next(g);
        print("g:", x);
    except StopIteration as e:
        print("Generator return value:", e)
        break;


# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield (3)
#     print('step 3')
#     yield (5)






# for n in odd():
#     print(n);
# print (odd())
