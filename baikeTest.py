# 学习测试文件，基本也是没用

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random   #在选取的网页中随机挑一个

base_url = "https://baike.baidu.com"
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

for i in range(20):
    url = base_url + his[-1]  # 从his中抽出最后一个
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    print(i,soup.find('h1').get_text(), '     url', his[-1])

    # find valid urls
    sub_urls = soup.find_all("a",
                             {
                                "target": "_blank",
                                 "href": re.compile("/item/(%.{2})+$")
                             })
    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]["href"])
    else:
        his.pop()