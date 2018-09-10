from bs4 import BeautifulSoup

# 创建beautiful对象打开需要解析的html文件
soup = BeautifulSoup(open('index.html',encoding='utf-8'), 'html5lib')
print(soup.prettify())
