import requests

url = 'http://www.baidu.com/s?wd=python'

headers = {
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 "
}
response = requests.get(url, headers=headers)
# 设置编码
print(response.content.decode('utf-8'))

with open('baidu.html', 'w', encoding='utf-8') as f:
    f.write(response.content.decode('utf-8'))