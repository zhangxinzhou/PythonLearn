def printcoffee(*coffeename):
    print("\n窝喜欢的咖啡有:")
    for item in coffeename:
        print(item)


printcoffee("蓝山", "卡布奇诺", "巴西")

parameter = [1, 2, 3, 4, 5, 6]
printcoffee(parameter)
