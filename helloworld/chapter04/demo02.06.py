grade = [99.98, 1, 4, 8, 88, 100, 22]
print("原列表:", grade)
grade.sort()
print("升序:", grade)
grade.sort(reverse=True)
print("降序:", grade)

char = ['cat', 'Tom', 'Angela', 'pet']
char.sort()
print("区分大小写", char)
char.sort(key=str.lower)
print("不区分大小写", char)
