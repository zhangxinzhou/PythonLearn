import keyword

kw = keyword.kwlist
print(kw)

# 内存地址是一样的
no = number = 2048
print(id(no))
print(id(number))