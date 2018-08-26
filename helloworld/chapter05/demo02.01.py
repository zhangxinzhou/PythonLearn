template = '编号: %07d\t公司名称: %s \t官网:  http://www.%s.com'
context1 = (7, '百度', 'baidu')
context2 = (8, '明日学院', 'mingrisoft')
print(template % context1)
print(template % context2)
