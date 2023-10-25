import requests
import json

# 定义URL
url = "http://kohcamp.qq.com/honor/districts"

# 定义请求头
headers = {
    "Host": "kohcamp.qq.com",
    "userId": "376304606",
    "Cookie": "accessToken=73_KVc3J8T1vTWlLp19Ui1KGo93tT9pMOxytGFx-BgWKQkln2DLKnwSwb0puBaMw-9nXyD2M93Kcvm-xn6DpUgFHP9nEoYAc3iL3a_x97jtURQ; appOpenId=oFhrws3KDvUB3ZzWB0xzlSt3c3mE; tgw_l7_route=bcf9e4f19953dbb1b953fe331856e985; pgv_pvid=943343360; eas_sid=H1W6k9K5W5q9j7q2k0c9U960e1",
    "cClientVersionCode": "68220107866308",
    "User-Agent": "SmobaHelper/7.91.0920 (iPhone; iOS 17.0.3; Scale/3.00)",
    "cCurrentGameId": "20001",
    "openId": "oFhrws3KDvUB3ZzWB0xzlSt3c3mE",
    "gameServerId": "4011",
    "encodeParam": "UhslK3Vr6IiqH2D99Gi%2B%2F0iqxpgOKLRb05AtvCYLr1uYi7E1cy3T5yrA2VXuz3mZFvFl89IFDtaahBO7iKHEOSyqHxqig3XvVeJJM1qeDpO1Pk5lU4aFLH%2F6%2BtqrP0M1OZ7VnA%3D%3D",
    "cClientVersionName": "7.91.0920",
    "cGzip": "1",
    "gameUserSex": "1",
    "cSystem": "ios",
    "gameId": "20001",
    "cRand": "1698098073583",
    "isTestFlight": "0",
    "cChannelId": "0",
    "Content-Length": "738",
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
}

# 定义请求体
payload = {
    "cSystemVersionName": "iOS",
    "gameUserSex": 1,
    "cGzip": 1,
    "kWegIosNativeTrpcMarkKey": "1",
    "openId": "oFhrws3KDvUB3ZzWB0xzlSt3c3mE",
    "cRand": "1698098073583",
    "cClientVersionCode": "68220107866308",
    "gameServerId": 4011,
    "reportHashValue": "10778570368",
    "recommendPrivacy": 0,
    "cClientVersionName": "7.91.0920",
    "cCurrentGameId": 20001,
    "cSystem": "ios",
    "gameId": 20001,
    "cGameId": 20001,
    "encodeParam": "UhslK3Vr6IiqH2D99Gi%2B%2F0iqxpgOKLRb05AtvCYLr1uYi7E1cy3T5yrA2VXuz3mZFvFl89IFDtaahBO7iKHEOSyqHxqig3XvVeJJM1qeDpO1Pk5lU4aFLH%2F6%2BtqrP0M1OZ7VnA%3D%3D",
    "specialEncodeParam": "",
    "token": "cH4P3bW3",
    "gameRoleId": "916286154",
    "gameAreaId": 4,
    "gameOpenId": "owanlspsKGoxqCl4-w0-junm1eFs",
    "cSystemVersionCode": "17.0.3",
    "isTestFlight": 0,
    "cChannelId": 0,
    "userId": "376304606"
}

# 发起POST请求
response = requests.post(url, headers=headers, json=payload)

# 检查响应
if response.status_code == 200:
    print("请求成功")
    with open ('region_code.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(response.json(), indent=4, ensure_ascii=False))
else:
    print(f"请求失败，状态码：{response.status_code}")
