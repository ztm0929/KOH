import requests
import json
import time

# 定义请求URL
url = "https://kohcamp.qq.com/honor/ranklist"

# 创建一个 session 对象
session = requests.Session()

# 设置通用的请求头
session.headers.update({
    "Host": "kohcamp.qq.com",
    "userId": "376304606",
    "Cookie": "accessToken=73_KVc3J8T1vTWlLp19Ui1KGo93tT9pMOxytGFx-BgWKQkln2DLKnwSwb0puBaMw-9nXyD2M93Kcvm-xn6DpUgFHP9nEoYAc3iL3a_x97jtURQ; appOpenId=oFhrws3KDvUB3ZzWB0xzlSt3c3mE; tgw_l7_route=bcf9e4f19953dbb1b953fe331856e985; pgv_pvid=943343360; eas_sid=H1W6k9K5W5q9j7q2k0c9U960e1",
    "cClientVersionCode": "68220107866308",
    "User-Agent": "SmobaHelper/7.91.0920 (iPhone; iOS 17.0.3; Scale/3.00)",
    "cCurrentGameId": "20001",
    "openId": "oFhrws3KDvUB3ZzWB0xzlSt3c3mE",
    "gameServerId": "4011",
    "encodeParam": "CWEV7iBp8BZ6mK4kn9N6SaIJyerg7tJX1nWg%2Fl4rXcJmEB2XOhO6d5T95e5fF8iLXPwYLI0P4d5uYylmxh0YS6u5ESB5RimcJAv1iRkBHTZQVGx20K2gqVkO939gi%2F%2FXNZgiXA%3D%3D",
    "cClientVersionName": "7.91.0920",
    "specialEncodeParam": "",
    "cGzip": "1",
    "gameUserSex": "1",
    "cSystem": "ios",
    "gameId": "20001",
    "cRand": "1698098073582",
    "isTestFlight": "0",
    "cChannelId": "0",
    "Content-Length": "799",
    "token": "cH4P3bW3",
    "Connection": "keep-alive",
    "gameRoleId": "916286154",
    "Accept-Language": "zh-Hans-CN;q=1, en-CN;q=0.9, zh-Hant-CN;q=0.8, yue-Hant-CN;q=0.7",
    "gameAreaId": "4",
    "gameOpenId": "owanlspsKGoxqCl4-w0-junm1eFs",
    "cSystemVersionCode": "17.0.3",
    "Accept": "*/*",
    "Content-Type": "application/json",
    "noencrypt": "1",
    "Accept-Encoding": "gzip, deflate, br",
    "cSystemVersionName": "iOS",
    "cGameId": "20001"
    # ...（其他请求头）
})

# 读取地区编码
with open('region_code.json', 'r') as f:
    region_codes = json.load(f)

for item in region_codes['data']['list'][0]['list']:
    try:
        # 定义请求体，更新 adcode
        data = {
            "cSystemVersionName": "iOS",
            "gameUserSex": 1,
            "cGzip": 1,
            "kWegIosNativeTrpcMarkKey": "1",
            "openId": "oFhrws3KDvUB3ZzWB0xzlSt3c3mE",
            "cRand": "1698098073582",
            "cClientVersionCode": "68220107866308",
            "gameServerId": 4011,
            "reportHashValue": "10779000576",
            "recommendPrivacy": 0,
            "cClientVersionName": "7.91.0920",
            "cCurrentGameId": 20001,
            "cSystem": "ios",
            "gameId": 20001,
            "cGameId": 20001,
            "encodeParam": "CWEV7iBp8BZ6mK4kn9N6SaIJyerg7tJX1nWg%2Fl4rXcJmEB2XOhO6d5T95e5fF8iLXPwYLI0P4d5uYylmxh0YS6u5ESB5RimcJAv1iRkBHTZQVGx20K2gqVkO939gi%2F%2FXNZgiXA%3D%3D",
            "specialEncodeParam": "",
            "roleId": "916286154",
            "heroId": 132,     # 英雄代码
            "areaId": "4",
            "token": "cH4P3bW3",
            "adcode": item['adcode'],  # 6位数字地区代码
            "gameRoleId": "916286154",
            "gameAreaId": 4,
            "gameOpenId": "owanlspsKGoxqCl4-w0-junm1eFs",
            "cSystemVersionCode": "17.0.3",
            "isTestFlight": 0,
            "cChannelId": 0,
            "userId": "376304606"
            # ...（其他字段）
        }
        

        # 使用 session 发送请求
        response = session.post(url, json=data, timeout=5)

        # 检查响应
        if response.status_code == 200:
            print("请求成功")
            with open("ranklist.json", "a", encoding='utf-8') as f:
                json.dump(response.json(), f, ensure_ascii=False, indent=4)
                f.write(",\n")

        else:
            print(f"请求失败，状态码：{response.status_code}")

        time.sleep(3)  # 或其他合适的间隔时间

    except requests.Timeout:
        print("请求超时，将在 10 秒后重试")
        time.sleep(10)
    except requests.RequestException as e:
        print(f"请求失败：{e}")
