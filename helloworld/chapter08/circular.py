import math

PI = math.pi


def girth(r):
    '''
    功能:计算周长
    :param r:
    :return:
    '''
    return round(2 * PI * r, 2)


def area(r):
    '''
    功能:计算面基
    :param r: 圆半径
    :return:
    '''
    return round(PI * r * r, 2)


if __name__ == '__main__':
    print(girth(10))
