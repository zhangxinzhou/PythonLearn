print("仅有一物,除3余2,除5余3,除7余2,")
number = int(input("请输入您认为符合条件的数"))
if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
    print(number, "符合条件")
else:
    print(number, "不符合条件")
