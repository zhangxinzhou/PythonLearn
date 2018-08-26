str1 = '@明日科技 @扎克伯格 @abc'
count = str1.count('@')
print("字符串:", str1, "包含", count, "个@符号")

print(str1.count('@'))
print(str1.find('@'))

print(str1.count('#'))
print(str1.find('#'))  # index与find类似,不过找不到时会抛异常
