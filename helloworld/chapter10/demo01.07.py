print("\n", "=" * 10, "蚂蚁庄园动态", "=" * 10, "\n")
# file = open('message.txt', 'w')
print('\n即将显示\n')
print("\n", "=" * 35, "蚂蚁庄园动态", "=" * 35, "\n")
with open('message.txt', 'r') as file:
    number = 0
    while True:
        number += 1
        line = file.readline()
        if line == '':
            break
        print(number, line, end='\n')
print("\n", "=" * 35, "over", "=" * 35, "\n")
