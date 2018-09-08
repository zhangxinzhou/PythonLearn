import os

path = "c:\\demo"
if not os.path.exists(path):
    os.mkdir(path)
    print("目录创建成功")
else:
    print("该目录已经存在")
