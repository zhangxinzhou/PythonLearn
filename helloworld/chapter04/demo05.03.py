mr = set(['1', '2', '3'])
mr.add('100')
print(mr)

str = '10000'
if str in mr:
    mr.remove(str)
print(mr)

# 删除一个元素
mr.pop()
print(mr)

mr.clear()
print(mr)
