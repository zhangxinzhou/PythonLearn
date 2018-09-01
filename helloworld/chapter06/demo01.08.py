def printsign(**sign):
    print()
    for key, value in sign.items():
        print("[" + key + "]的星座是:" + value)


printsign(绮梦='水瓶座', 能令='双子座')

dict1 = {'绮梦': '水瓶座', '小白': '射手座'}
printsign(**dict1) # 通过字典指定函数的可变参数
