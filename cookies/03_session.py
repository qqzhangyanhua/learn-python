import requests
headers = {
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",

}
main_url = 'https://xueqiu.com/'
session = requests.session()
## 为了获取cookie
res =session.get(main_url, headers=headers)
# print(response)

url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=518826&size=15'
response = session.get(url, headers=headers)
print(response.json())
