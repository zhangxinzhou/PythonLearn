import requests

# 导入requests.exceptions模块中的三种异常类
from requests.exceptions import ReadTimeout, HTTPError, RequestException

# 循环发送请求50次
for a in range(1, 50):
    try:
        # 设置超时为0.5秒
        response = requests.get('https://www.baidu.com', timeout=0.1)
        print(response.status_code)
    except ReadTimeout:  # 超时异常
        print('timeout')
    except HTTPError:  # http异常
        print('http error')
    except RequestException:  # 请求
        print('req error')
