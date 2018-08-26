import random

randomdict = {i: random.randint(10, 100) for i in range(1, 5)}
print('生成的字典是:', randomdict)

name = ['一梦', '白雪', '黑雾', '带蓝']
sign = ['水瓶', '射手', '双鱼', '双子']
dictionary = {i: j + '座' for i, j in zip(name, sign)}
print(dictionary)
