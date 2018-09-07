print("\n", "=" * 10, "蚂蚁庄园动态", "+" * 10, "\n")
file = open('message.txt', 'a')
# 追加一条动态信息
file.write('追加一条信息\n')
print('\n追加了一条动态\n')
file.flush()
