import requests

data = {'world': 'hello'}
response = requests.post('http://httpbin.org/post', data=data)
print(response.content)

r1 = requests.put('http://httpbin.org/post', data={'key': 'value'})
r2 = requests.delete('http://httpbin.org/delete')
r3 = requests.head('http://httpbin.org/get')
r4 = requests.options('http://httpbin.org/get')
print(r1.content)
print(r2.content)
print(r3.content)
print(r4.content)
