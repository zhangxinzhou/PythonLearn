price = [1200, 5330, 2980, 6200, 1998, 8888]
sale = [int(x * 0.5) for x in price]
print("原价格:", price)
print("折后价:", sale)

print("---------------------------------------")
sale = [int(x * 0.5) for x in price if x > 5000]
print("原价格:", price)
print("折后价:", sale)
