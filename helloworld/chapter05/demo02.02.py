template = '编号: {:0>9s}\t公司名称: {:s} \t官网: http://www.{:s}.com'

context1 = template.format('7', '百度', 'baidu')
context2 = template.format('8', '明日学院', 'mingrisoft')

print(context1)
print(context2)
