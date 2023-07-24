import requests

# 如果非200 先加header 不行就Host或者Referer再就是cookie
url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=518826&size=15'
headers = {
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Cookie": 'acw_tc=276077b216902116098701977e072b574239dc4f864349f6c357de82ace481; xq_a_token=197a3a870824d1754f6edf083d719bd1a3aabe88; xqat=197a3a870824d1754f6edf083d719bd1a3aabe88; xq_r_token=f3676d47182482b690747de814788450c6d4fcf1; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY5MTYyNzcwNSwiY3RtIjoxNjkwMjExNjA0NzA5LCJjaWQiOiJkOWQwbjRBWnVwIn0.Hzuq9SoBg0UbRuVhO7kFJ8sWpzCDNFS-RKEhAqSB-jJFl-YvPxd4EuSxt2wjpMNDxvh874sc0z6jemzDdOJOlQABlmwG5HL7gEwsYXsS6ag8CM8bxyyPFIZAq-6Yiu4voWMeoYn6UgGTNR4JhOYVu2RN5WGX9BIXcagC9Tx8sTc-2nqX90Rj_T5Raw_YKtQdniBtR4hHDZyIm_cb6-8ycp8JPQBJoi0PRfHXeEgFpqvPT2EWyTsL8Ysa0R33L37eLo7xceKGrMTRvc71eQQaPIk5NyoL7H4Gmbt111PiwAeWKOBWP74nmyT3fuqGXdg51ZQvur68Hrz5a2zCeclodw; u=221690211609868; device_id=6be7ca1aa9d633b1e74b64976d472e92; Hm_lvt_1db88642e346389874251b5a1eded6e3=1690211611; acw_sc__v2=64be9527720bc24506dcdf240e3870b6959618df; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1690211624'


}

response = requests.get(url, headers=headers)
print(response)
