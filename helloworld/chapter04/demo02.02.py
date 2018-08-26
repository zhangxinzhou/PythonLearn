import datetime

# 定义一个列表
mot = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
day = datetime.datetime.now().weekday()
print([mot[day]])
