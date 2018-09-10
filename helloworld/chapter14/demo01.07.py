import requests

url = 'https://www.baidu.com'
# 创建头部信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
response = requests.get(url, headers=headers)
print(response.content)
