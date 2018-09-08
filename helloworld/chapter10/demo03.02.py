import os

src = r"D:\mr\test\test.txt"
dst = r"D:\mr\test\test1111.txt"
if os.path.exists(src):
    os.rename(src, dst)
    print("文件已重命名")
else:
    print("文件不存在")
