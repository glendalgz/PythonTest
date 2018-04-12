#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# s = (x * x for x in range(5))
# print(s)
# for x in s:
#     print(x)

#generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处（已经被赋新值）继续执行。
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
#所以函数fib是返回b值，最后成为一个生成器对象。可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

# 意义：集合具有迭代意义
# 可迭代：iterable isinstance([], Iterable)
# 迭代器：iterator isinstance([], Iterator)
# 转化法：iterable 通过iter() 变成 iterator

f = fib(5)
print('fib(5):', f)
for x in f:
    print(x)

# call generator manually:
# g = fib(5)
# while 1:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break