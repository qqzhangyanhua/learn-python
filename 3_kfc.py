
import urllib.request
import json
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
formaData = {
    "cname": '',
    "pid": '',
    "keyword": '上海',
    "pageIndex": 1,
    "pageSize": 10
}
headers = {
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

# 发送post 请求

response = urllib.request.Request(url=url, headers=headers, data=urllib.parse.urlencode(formaData).encode('utf-8'), method='POST')
# 开始请求
with open('kfc.json', 'wb') as f:
    f.write(urllib.request.urlopen(response).read())

data_json = json.loads(urllib.request.urlopen(response).read().decode('utf-8'))
# print(data_json['Table1'])

for l in data_json['Table1']:
    print(l['storeName'], l['addressDetail'])