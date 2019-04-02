# 无用文件



import requests
from lxml import etree
from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
soup = BeautifulSoup(html, features="lxml")
print(soup.h1)
all_href = soup.find_all('a')
print('\n',all_href)
all_href = [l['href'] for l in all_href]
print('\n',all_href)

# r = requests.get('https://www.douban.com/search', params={'q':'python','cat':'1001'})
# print(r.status_code)
# print(r.text)

# import re
# ptn = r"r[au]n"
# print(re.search(ptn,"dog runs to cat"))
# print(re.search(r"ab+", "a"))
# print(re.search(r"ab+", "ababbbbbb"))