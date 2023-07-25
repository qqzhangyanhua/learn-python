
import base64
import json
import requests
# 一、图片文字类型(默认 3 数英混合)：
# 1 : 纯数字
# 1001：纯数字2
# 2 : 纯英文
# 1002：纯英文2
# 3 : 数英混合
# 1003：数英混合2
#  4 : 闪动GIF
# 7 : 无感学习(独家)
# 11 : 计算题
# 1005:  快速计算题
# 16 : 汉字
# 32 : 通用文字识别(证件、单据)
# 66:  问答题
# 49 :recaptcha图片识别
# 二、图片旋转角度类型：
# 29 :  旋转类型
#
# 三、图片坐标点选类型：
# 19 :  1个坐标
# 20 :  3个坐标
# 21 :  3 ~ 5个坐标
# 22 :  5 ~ 8个坐标
# 27 :  1 ~ 4个坐标
# 48 : 轨迹类型
#
# 四、缺口识别
# 18 : 缺口识别（需要2张图 一张目标图一张缺口图）
# 33 : 单缺口识别（返回X轴坐标 只需要1张图）
# 五、拼图识别
# 53：拼图识别


def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post(
        "http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        # ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]
    return ""


if __name__ == "__main__":
    code_url = 'https://so.gushiwen.cn/RandCode.ashx'
    headers = {
        'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    }
    # session = requests.session()
    # res = session.get(code_url, headers=headers)
    # with open('file.jpg', 'wb') as f:
    #     f.write(res.content)
    # img_path = "./file.jpg"
    # result = base64_api(uname='13251953746', pwd='a123456',
    #                     img=img_path, typeid=3)


url = 'https://passport-api.haizol.com/user/user-login'
main_url = 'https://www.haizol.com/'
session = requests.session()
data = {
    'account': "15162606973",
    'data': "%7B%22a%22%3A%22FFFF0N0000000000924F%22%2C%22c%22%3A%221690293190784%3A0.12367899040199681%22%2C%22d%22%3A%22nvc_login%22%2C%22j%22%3A%7B%22test%22%3A1%7D%2C%22h%22%3A%7B%22umidToken%22%3A%22T2gAJk_Pz_9VGz-NtVz0b8bvqCdTNjrn1IP4LTaNTuUt_8ixisVYJTorWQrNT1F8wUE%3D%22%7D%2C%22b%22%3A%22140%234AsDqvC%2FzzF%2Bezo22xtuCpSd0uydOcbv7t2zs7q6Te3q8T%2FzkyFHNUKgwRt%2BgTVJSuWL3llVNKbFeMgCOoOm%2B6hqzznpYtkqFrrzzBD6bHVulFzx2DD3VtgqzXL02X0mlpYazDrbV2TzrFrd2jToZshYaSvZrI7Zb519UyvwnST9cdc0iNozNVCgG3ls7LOAmUMQiSV%2Fvy5WPiQNUj2O9ZRI%2Bf82E1N9dt3LB35S9ELJEeLeb568r6zP2dZBlIyV3VuQfnLz6r4rGvDdZMAmJtsZRms35UK0XWA%2BPzWpmZ%2Br4Kj4iBmn8cuYIoPv9JqgOjw3qCwhfbkCqgu%2BwhSfPxDfZICzI7M0ZCL20KNBHuS18Ag8taJVoLDOam2H8bl4Os%2FeHPI47PsezigddjMVBpxuxLsIGb0A2LaIVMURiLXSpijx1sYTjckbobgUx8a48fdub%2FG2sJHnK5WDWeMwJLxCVwrm%2FGesGpDmFuu1Tcz%2FVgamIj%2FGXTKnqrd8GY1JwGWcWQHZP4AlK9cuvCocd2rwH3V8Xp99A0siR7%2BkhGSFoPFYQdcSNGpjkWDVSOnokd0kI4KlRQiS5z7%2B%2FPMNzNH0XPZBeEDZ%2B%2FhKeR6sbWHyGjMB03yERQf5T2kwwmCnAhBe7bOGS83CMzLgimOEQKz5HcNeMtw1JQPTcQb8oEqwWN2vah15YAJpQGimC1qRhMIy885x%2FjTV1x%2F9JAfmKP236qS1fvwWLEd6xP7OA5tG9XnZVFzWLig4t99n8BIVQcadQ9dHBHwcgqI%2B1gl%2FZ1rgj1dqtqy7eSJ0lkfaMR%2FhhVlHSsIUX9vOXSFPcM1zkLoS4den%2FbzaTAJ0VDjWM7MBfgqKS8joa5P8%2BLfS0HX8kFgxbRfAzD%2FLv0K4Xe8RL%2B7pZiAb%2BCglAsxg7Eim8LTc6o%2BLwBY2rnXQTOtzcFsDwgdwNP72KlKbe1BAcTBjcDrjY7crP84u76t75OLnszDjulJbCPHfM9Qxit4aDst9Me5dJlJQh5LaRyK1i7GhuzLM%2Fl%2B%2F5yban1CkXGKNm4bnzix5ZvYTTTCsR9wr7e4Ek1gsK6QTQJs4qHHdFNW3qJ0QC3Dt2b%2BN7YigIpObt%2FQIuGFdEa%2B0XOQAmSOkyN3uqgqBtoYjlmS3UzVcGdhmMF%2FWfguV8e3yW0hfDT1yFxJhyPT8%2F0PpfXTB%22%2C%22e%22%3A%22gg6VWIG0VSjVsqM6V9bDnd3jSi_5e51qkVIUPxRokeLPbs73V5pIs2uCDz9klg-QaI-4VKxA2I59p2hiNXwz9qlR4NYbu64QmJ2-YZUqDfbpWS8emKQ2rGNjAlZMl8YrJLRNyDimjECWquFccEOvHPkuRLiry7YVXxd9S-Qym2juTW8srUlVMzm64vI7-8lEqqgvgQ7m3hg8VVeQtP6jnw%22%7D",
    'password': "ZPMuaZUSKPMcZsrT6iVPdnPfqQHu3TV9gF/A0R99dVSlXk7V3AzSEdAMUA7ZaGAARAAp5q/BsQ591JIm5gLiQBzaek+RPPJR4QWlkfYedZewv+qMn5O4ncJTS1wq3XNAZGuj0GpyPhWasI62/I6KCE5/95Fgci1zQI3kggQqn6IOnhWg/ljPzvzoIpB8Yu0kmI3BrdKWXya8cGRVKFJJCxix4v+iD6n3Jgfpmpektm87dxNpwYVa9xuAcHPttmQLv6aAnOFwYIOgxVu0OR/JYUJztH/txewP0EfFotZjoXbrFc3ZzcZ24DgChtZQe3yb3NnVXWP9rLBDDvd9/dd00w==",
    'rememberMe': "true",
    'sessionId': "",
    'sig': "",
    'source': 40,
    'timestamp': 1690293200281,
    'token': "",
    'validateCode': ""
}
session.options(url, headers=headers)
res = session.post(url, data=data, headers=headers)
with open('haizol.html', 'wb', ) as f:
    f.write(res.content)
