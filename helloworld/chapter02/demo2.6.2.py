a = 10
b = 6
print(6)
print(a * b)
print(a if a > b else b)
print("成功的唯一秘诀---坚持到最后一分钟")

print(a, b)
print("a", "b")

# 文件输出
fp = open(r"D:\pytest.txt", "a+")  # 打开文件
print("文件输出测试", file=fp)  # 输出到文件中
fp.close()  # 关闭文件
