def fun_bmi(height, weight, person='路人甲'):
    '''功能: 根据身高和体重计算BMI指数
    person:姓名
    height:身高,单位:米
    weight:体重,单位:千克
    '''

    print(person + '的身高:' + str(height) + "米 \t 体重: " + str(weight) + "千克")
    bmi = weight / (height ** 2)
    print(person + "的BMI指数为:" + str(bmi))
    # 判断身材是否合理
    if bmi < 18.5:
        print("你的体重过轻\n")
    if bmi >= 18.5 and bmi < 24.9:
        print("正常范围,注意保持\n")
    if bmi >= 24.9 and bmi < 29.9:
        print("您的体重过重\n")
    if bmi >= 29.9:
        print("肥胖\n")


# *******************************调用函数************************************* #
fun_bmi(1.83, 60)

# *******************************查看默认值参数************************************* #
temp = fun_bmi.__defaults__
print(temp)
