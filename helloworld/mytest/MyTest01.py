import requests

s = requests.session()
url = 'https://www.baidu.com/'
res = s.get(url=url)
print(res.content)