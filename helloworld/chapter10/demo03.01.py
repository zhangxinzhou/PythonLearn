import os

path = r"D:\mr\test\test.txt"
if os.path.exists(path):
    os.remove(path)
    print("文件以删除")
else:
    print("文件不存在")
