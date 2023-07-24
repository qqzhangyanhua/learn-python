
import requests

# 1.设置代理
proxies = {
    'http': 'http://113.124.220.137'
}
# 2.设置请求头
headers = {
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}
# 3.发送请求
url = 'https://www.baidu.com/s'
data = {
    'wd': 'ip查询'
}
response = requests.get(url, params=data, proxies=proxies, headers=headers)
response.encoding = 'utf-8'
with open('ip.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
