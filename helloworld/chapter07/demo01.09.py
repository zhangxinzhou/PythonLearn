class Swan:
    '''天鹅类'''
    _neck_swan = '天鹅的脖子很长'

    def __init__(self):
        print("__init__():", Swan._neck_swan)


swan = Swan()
print("直接访问:", swan._neck_swan)
