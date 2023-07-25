import requests

# 模拟登陆
url = 'https://passport.17k.com/ck/user/login'
data = {
    "loginName": '13251953746',
    "password": 'a123456',
}

headers = {
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",

}
# res = requests.post(url, data=data, headers=headers)
# # print(dict(res.cookies))
# cookie = res.cookies
# # 登陆后才能访问的
login_url = 'https://user.17k.com/ck/user/myInfo/100711235?bindInfo=1&appKey=2406394919'
# response = requests.get(login_url, headers=headers, cookies=cookie)
# print(response.text)

session = requests.session()
session.post(url, data=data, headers=headers)
response = session.get(login_url, headers=headers)
print(response.text)
