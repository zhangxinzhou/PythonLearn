str1 = "明 日 学 院 官 网 >>> www.mingrisoft.com"
print("原字符串:", str1)

list1 = str1.split()
list2 = str1.split(">>>")
list3 = str1.split(".")
list4 = str1.split(" ", 4)
print(list1)
print(list2)
print(list3)
print(list4)

str2 = "@你好 @你不好 @小白"
list1 = str2.split(" ")
print("您@的好友有:")
for item in list1:
    print(item[1:])
