import requests

url = 'https://gimg3.baidu.com/search/src=http%3A%2F%2Fpics5.baidu.com%2Ffeed%2Fd788d43f8794a4c2f71af915918a66d9ad6e3959.jpeg%40f_auto%3Ftoken%3D02bdf14a610894dd51395bd933b52389&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=f360,240&n=0&g=0n&q=75&fmt=auto?sec=1689786000&t=697f689882845244f438c70593f72a1d'


response = requests.get(url)
with open('img.jpg', 'wb') as f:
    f.write(response.content)

