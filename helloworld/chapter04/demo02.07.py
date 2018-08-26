grade = [89, 94, 95, 96, 97, 98, 99, 100, 100, 100]
grade_as = sorted(grade)
print("升序:", grade_as)
grade_as = sorted(grade, reverse=True)
print("降序:", grade_as)
print("原序列:", grade)

import random

randomnumber = [random.randint(10, 100) for i in range(10)]
print(randomnumber)

for i in range(10):
    xxx = random.randint(10, 100)
    print(xxx)
