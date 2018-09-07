print("\n", "=" * 10, "蚂蚁庄园动态", "+" * 10, "\n")
file = open('message.txt', 'w')
# 写入一条动态信息
file.write('你使用了一张加速卡,福建省看到了附件两款手机\n')
print('\n写入了一条动态\n')
file.flush()
