str1 = "人生苦短,我用Python"
length = len(str1)
print(length)

# utf-8 字符串长度
length = len(str1.encode())
print(length)

# gbk 字符串长度
length = len(str1.encode("gbk"))
print(length)
