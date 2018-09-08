import os

# 当前目录下操作
src = "demo"
dst = 'test'
if os.path.exists(src):
    os.rename(src, dst)
    print("文件已重命名")
else:
    print("文件不存在")
