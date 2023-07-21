import requests
import json
url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_web_fanyi&sign=2dea21062e29fa3a'
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

}
formData = {
    "from": "auto",
    "to": "auto",
    "q": "北京",
}
input_str = input('请输入要翻译的内容：')
formData['q'] = input_str

response = requests.post(url=url, headers=headers, params=formData)
val = json.loads(response.content.decode('utf-8'))
code = response.status_code
print(response.status_code)
if code == 200:
    print(val)
else:
    print('翻译失败')

# print(val['content']['out'])
