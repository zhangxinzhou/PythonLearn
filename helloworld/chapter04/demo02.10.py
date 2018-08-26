str1 = "千山鸟飞绝"
str2 = "万锦人踪灭"
str3 = "孤舟蓑笠翁"
str4 = "独钓寒江雪"
varse = [list(str1), list(str2), list(str3), list(str4)]
print("\n-- 横板 --\n")
for i in range(4):
    for j in range(5):
        if j == 4:
            print(varse[i][j])
        else:
            print(varse[i][j], end="")

varse.reverse()
print("\n-- 竖版 --\n")
for i in range(5):
    for j in range(4):
        if j == 3:
            print(varse[j][i])
        else:
            print(varse[j][i], end="")
