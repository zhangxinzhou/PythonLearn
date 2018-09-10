import urllib.request

# 打开指定需要爬去的网页
response = urllib.request.urlopen('http://www.baidu.com')
html = response.read()
print(html)
