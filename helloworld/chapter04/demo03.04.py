number = (i for i in range(3))
print(number.__next__())
print(number.__next__())
print(number.__next__())
number = tuple(number)
print("转换后:", number)

number = (i for i in range(4))
for i in number:
    print(i, end=" ")
print("转换后:", tuple(number))
