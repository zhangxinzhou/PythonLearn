coffeename = ('蓝山', '卡布奇诺', '慢的宁')
for name in coffeename:
    print(name, end=" ")

print()
tuple1 = coffeename
print("原元组:", tuple1)
tuple1 = tuple1 + ("哥伦比亚", "麝香猫")
print("新元组:", tuple1)
