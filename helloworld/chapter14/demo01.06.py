import requests

payload = {'key1': 'value1', 'key2': 'value2'}
# 对需要爬取的网页发送请求
response = requests.get('http://httpbin.org/get', params=payload)
print(response.content)
