import requests

url ='http://www.baidu.com?wd=python'
response = requests.get(url)
# 设置编码
response.encoding = 'utf-8'
# print(response.text)
# print(response.content.decode('utf-8'))
print(response.url)
# 获取状态码
print(response.status_code)
# 获取响应头
print(response.request.headers)

# 获取响应cookie
print(response.cookies)