class Swan:
    '''天鹅类'''
    __neck_swan = '天鹅的脖子很长'

    def __init__(self):
        print("__init__:", Swan.__neck_swan)


swan = Swan()
print("加入类名:", swan._Swan__neck_swan)  # 私有属性,可以通过"实例名._类名__xxx_"方式访问
print("直接访问:", swan.__neck_swan)  # 私有属性,不能通过实列名访问,出错
