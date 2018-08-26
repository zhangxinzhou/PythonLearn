name = ['此梦', '香凝', '白雪', '黑雾']
sign = ['双子座', '射手座', '双鱼座', '双子座']
dictionary = dict(zip(name, sign))
print(dictionary)

dictionary = dict(k1='v1', k2='v2', k3='v3')
print(dictionary)
print(dictionary['k1'])
v = dictionary.get('k1', 'a')
print(v)
dictionary['key5'] = '5'
print(dictionary)

dictionary.clear()
print(dictionary)
