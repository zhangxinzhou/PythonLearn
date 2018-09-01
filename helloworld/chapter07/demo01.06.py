class Geese:
    '''雁类'''
    neck = "脖子较长"
    wing = "翅膀振动频率高"
    leg = "行走自如"
    number = 0

    def __init__(self):
        Geese.number += 1
        print("\n窝是第" + str(Geese.number) + "个大雁,窝属于雁类!窝有以下特征")
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.neck)


# 创建四个雁类的对象,相当于有四只大雁
list1 = []
for i in range(4):
    list1.append(Geese())
print("一共有", Geese.number, "只大雁")

Geese.beak = '鸟喙怎么怎么样'
print("第二只大雁的喙", list1[1].beak)
