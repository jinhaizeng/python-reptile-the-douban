# config=utf-8
# 本文档实现了豆瓣上海绵宝宝这个视频中类型的爬取，后面要开始做的就开始复杂起来了，要开始跑大量的视频然后找链接的工作
from bs4 import  BeautifulSoup
import requests

r = requests.get('https://movie.douban.com/subject/11808948/')
soup = BeautifulSoup(r.content, 'lxml')
spans = soup.find_all('span',attrs={'property':'v:genre'})
genre = ''
for span in spans:
    genre = genre +span.get_text()+ '、'
print(genre)