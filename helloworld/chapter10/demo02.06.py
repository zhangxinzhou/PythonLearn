import os

path = "C:\\Users\\zxz\\PycharmProjects\\helloworld"
print("[", path, "]目录下包括的文件和目录:")

for root, dirs, files in os.walk(path, topdown=True):  # 遍历指定目录
    for name in dirs:  # 循环输出遍历到的子目录
        print("■", os.path.join(root, name))
    for name in files:  # 循环输出遍历到的文件
        print("▣", os.path.join(root, name))
