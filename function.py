#python3.6
#learning from Liaoxuefeng

# a = 255
# b = 1000
# print(hex(a))
# print(hex(b))

# 一元二次方程ax2+bx+c=0求解
import math
def quadratic(a, b, c):
    de = b*b-4*a*c
    if de < 0:
        print('No Fact X')
        return
    elif de == 0:
        x1 = x2 = -b/(2*a)
        return x1,x2
    else:
        x1 = -b/(2*a)+(math.sqrt(de))/(2*a)
        x2 = -b/(2*a)-(math.sqrt(de))/(2*a)
        return x1,x2

print(quadratic(1,4,1))
