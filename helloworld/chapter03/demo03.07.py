print("仅有一物,除3余2,除5余3,除7余2,")
for number in range(200):
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
        print("这个数是:", number)
        break

string = "不要再说我不能:"
print(string)
for ch in string:
    print(ch)
