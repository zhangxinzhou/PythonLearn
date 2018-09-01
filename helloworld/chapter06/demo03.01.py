import math


def ciclearea(r):
    result1 = math.pi * r * r
    return result1


r = 10
print("半径为", r, "的圆的面积为:", ciclearea(r))

# **************************lambda 匿名函数***************************** #

r = 10
result2 = lambda r: math.pi * r * r
print("半径为", r, "的圆的面积为:", result2)
