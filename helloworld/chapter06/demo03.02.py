bookinfo = [('不一样的卡梅拉(全套)', 22.50, 120), ('零基础学python', 65.10, 89.80), ('摆渡人', 23.20, 36.00)]
print("爬取到的商品信息为:\n", bookinfo, '\n')
#  按指定规则排序(普通做法,待补充)
bookinfo.sort(key=lambda x: (x[1], x[1] / x[2]))  # 按指定规则排序(lambda)
print("排序后的商品信息为:", bookinfo)
