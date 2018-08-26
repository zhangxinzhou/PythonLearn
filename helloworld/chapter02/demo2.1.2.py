# coding=utf-8

'''
    @ 功能:根据身高,体重计算BMI指数
    @ author:无语
    @ create:2018-07-29
'''

height = float(input("请输入您的身高(米):"))  # 输入身高
weight = float(input("请输入您的体重(千克):"))  # 输入体重
bmi = weight / (height * height)  # 计算BMI指数

# 判断身材是否合理
if bmi < 18.5:
    print("您的BMI指数为:" + str(bmi))
    print("您的体重过轻")
if bmi >= 18.5 and bmi < 24.9:
    print("您的BMI指数为:" + str(bmi))
    print("正常范围,注意保持")
if bmi >= 24.9 and bmi < 29.9:
    print("您的BMI指数为:" + str(bmi))
    print("体重过重")
if bmi >= 29.9:
    print("您的BMI指数为:" + str(bmi))
    print("肥胖")
