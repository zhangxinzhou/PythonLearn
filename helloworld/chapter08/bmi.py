def fun_bmi(person, height, weight):
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


def fun_bmi_upgrade(*person):
    '''
    功能: 根据身高和体重计算BMI指数(共享升级版)
    :param person: 可变参数该参数需要传递三个元素的列表,分别为姓名,身高(米)和体重(千克)
    :return:
    '''

    for list_person in person:
        for item in list_person:
            person = item[0]  # 姓名
            height = item[1]  # 身高(单位:米)
            weight = item[2]  # 体重(单位:千克)

            print("\n" + "=" * 13, person, "=" * 13)
            print(str(height) + "米 \t 体重: " + str(weight) + "千克")
            bmi = weight / (height ** 2)
            print("BMI指数为:" + str(bmi))
            # 判断身材是否合理
            if bmi < 18.5:
                print("你的体重过轻\n")
            if bmi >= 18.5 and bmi < 24.9:
                print("正常范围,注意保持\n")
            if bmi >= 24.9 and bmi < 29.9:
                print("您的体重过重\n")
            if bmi >= 29.9:
                print("肥胖\n")
