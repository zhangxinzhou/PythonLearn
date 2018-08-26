print("\n手机店正在打折,活动进行中....")
strWeek = input("请输入中文星期(如星期一):")
intTime = int(input("请输入事件中的小时(范围:0~23)"))
# 判断是否满足活动参入条件(使用了if条件遇见)
if (strWeek == "星期二" and (intTime >= 10 and intTime <= 11)) or (strWeek == "星期五" and (14 <= intTime <= 15)):
    print("恭喜您,获得了折扣活动参与资格,快快选购吧")
else:
    print("对不起,您来晚一步,期待下次活动....")

