str1 = "人生苦短,我用Python"
try:
    substr1 = str1[15]
except IndexError:
    print("指定的索引不存在")
