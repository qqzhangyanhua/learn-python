
import urllib.request
url = "https://www.axzo.cn/" #'https://www.haizol.com/'
headers = {
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}
# 伪装请求头
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
# 开始请求
with open('axzo.html', 'wb') as f:
    f.write(response.read())