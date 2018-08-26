import random

randomnumber = (random.randint(10, 100) for i in range(10))
randomnumber = tuple(randomnumber)
print("转换后:", randomnumber)
