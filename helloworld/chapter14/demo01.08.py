import requests

# 循环发送请求50次
for a in range(1, 50):
    try:
        # 设置超时为0.5秒
        response = requests.get('https://www.baidu.com', timeout=0.1)
        print(response.status_code)
    except Exception as e:
        print(e)
