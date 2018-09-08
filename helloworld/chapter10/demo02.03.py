import os


def mkdir(path):
    if not os.path.exists(path):
        mkdir(os.path.split(path)[0])
    else:
        return
    os.mkdir(path)


mkdir("d:/mr/test/demo")

# 等效
# os.makedirs("d:/mr/test/demo")
