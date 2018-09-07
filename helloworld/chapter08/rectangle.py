def girth(width, height):
    '''
    功能:计算周长
    :param width:宽度
    :param height: 高度
    :return:
    '''
    return (width + height) * 2


def area(width, height):
    '''
    计算面积
    :param width:宽度
    :param height: 高度
    :return:
    '''
    return width * height


if __name__ == '__main__':
    print(area(10, 20))
