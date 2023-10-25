import requests
import json

url = ' https://pvp.qq.com/web201605/js/herolist.json'

resp = requests.get(url)

with open ('herolist.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(resp.json(), ensure_ascii=False, indent=4))

print(resp.status_code)