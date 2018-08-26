dictionary = dict((('绮梦', '水瓶座'), ('饼干', '双子座'), ('鱼丸', '大力做')))
print(dictionary)

dictionary['饼干'] = '你好'
print(dictionary)

del dictionary['饼干']
print(dictionary)

if dictionary.get('饼干') != None:
    del dictionary
else:
    print('不存在')

if '饼干' in dictionary:
    del dictionary
else:
    print('不存在')
