class Geese:
    '''雁类'''
    neck = "脖子较长"
    wing = "翅膀振动频率高"
    leg = "行走自如"

    def __init__(self):
        print("窝属于雁类!窝有以下特征")
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.neck)


geese = Geese()
