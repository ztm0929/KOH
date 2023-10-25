from bs4 import BeautifulSoup
import requests
import csv

url_hero = 'https://pvp.qq.com/web201605/herolist.shtml'
url_item = 'https://pvp.qq.com/web201605/item.shtml'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'PTTDate=1698115360892; ts_last=pvp.qq.com/web201605/herolist.shtml; ts_uid=5799659268; pgv_info=ssid=s9208225222; pgv_pvid=8375374770; pvpqqcomrouteLine=index_herolist_herodetail_herolist_herolist; ieg_ingame_userid=2iFGfQNUlqheYIrSmq355nlxjKY4r5fd; PTTosFirstTime=1698105600000; PTTosSysFirstTime=1698105600000; PTTuserFirstTime=1698105600000; isHostDate=19654; isOsDate=19654; isOsSysDate=19654; weekloop=0-0-0-43; LW_sid=c1U6e9Q8k1b1f302j4E3Z3M1R9; LW_uid=x1w6Q988O1G1n3y2j4w3f3e2J0; eas_sid=U1F6X9C8f1y1f3V2z49363N2n7; _clsk=1beo149|1698066385252|2|1|mp.weixin.qq.com/weheat-agent/payload/record; _clck=3283692246|1|fg3|0; ptcz=436df9e70c1499264b6b854d421c015842c1c1f67d57fbba0f4546927e6f4b49; RK=EL/NfXDJbA',  # 省略其他 Cookie 信息
    'Host': 'pvp.qq.com',
    'Referer': 'https://pvp.qq.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15'
}

hero_list = requests.get(url_hero, headers=headers)
item_list = requests.get(url_item)

hero_list.encoding = 'gbk'
item_list.encoding = 'gbk'

content1 = hero_list.text
content2 = item_list.text

soup1 = BeautifulSoup(content1,'lxml')
soup2 = BeautifulSoup(content2,'lxml')

print(soup1)

# box1 = soup1.find('ul',class_="herolist clearfix")
# herolist = str(box1)

# print(herolist)

# box2 = soup2.find('ul',class_="clearfix herolist")
# itemlist = str(box2)

# with open(f'hero.txt','w') as file:
#     file.write(herolist)

print("输出完成！")