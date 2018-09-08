import os
import shutil

path = "d:/mr/test/demo"
if os.path.exists(path):
    # os.rmdir(path) # 该函数只能删除空目录
    shutil.rmtree(path)  # 该函数能删除目录和该目录下的所有文件
    print("目录删除成功")
else:
    print("该目录不存在")
