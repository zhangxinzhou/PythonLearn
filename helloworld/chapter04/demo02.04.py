phone = ["摩托", "诺基亚", "三星", "OPPO"]
len(phone)
phone.append("iphone")
len(phone)
print(phone)

list1 = [1, 2, 3, 4]
list2 = [10, 11, 12, 13]
list1.extend(list2)
print(list1)

del list1[0]
print(list1)

list1.remove(2)
# list1.remove(1000) 删除不存在的元素会报错
value = 10000
if list1.count(value) > 0:
    list1.remove(value)
print(list1)
