import urllib.request

url = 'http://www.baidu.com'
# 开始请求
response = urllib.request.urlopen(url)
# 获取状态码，如果是200表示获取成功
print(response.getcode())
print(response.getheaders())
# 读取内容
# 获取请求头    
cont = response.read()

# 将内容写入文件
with open('baidu.html', 'wb') as f:
    f.write(cont)
