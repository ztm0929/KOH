import requests
from bs4 import BeautifulSoup

root_url = 'https://pvp.qq.com/web201605'

hero_url = f'{root_url}/herolist.shtml'

hero_list = requests.get(hero_url)
hero_list.encoding = 'gbk'

content = hero_list.text
soup = BeautifulSoup(content,'lxml')

links = [link['href'] for link in soup.find_all('a',href=True)]

for link in links:
    result = requests.get(f'{root_url}/{link}')
    content = result.text
    soup_all = BeautifulSoup(content,'lxml')
    print(link)