import requests
from lxml import etree
ur1 = 'https://movie.douban.com/subject/1292052/'
data = requests.get(ur1).text
s = etree.HTML(data)


