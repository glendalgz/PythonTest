# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if(isinstance(s, str))]
print(L2)

#for循环等同于一个
for s in [1, 2, 3, 4, 5]:
    print(s)

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break