# config=utf-8
# 本文档实现了豆瓣上海绵宝宝这个视频中类型的爬取，后面要开始做的就开始复杂起来了，要开始跑大量的视频然后找链接的工作
# 接下来开始测试爬取任意视频
from bs4 import BeautifulSoup
import requests
import getDoubanID


def spider(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    spans = soup.find_all('span',attrs={'property':'v:genre'})
    genre = ''
    for span in spans:
        genre = genre +span.get_text()+ '、'
    print(genre)
    return


url1 = 'https://movie.douban.com/subject/'
url2 = '/'



name = '海绵宝宝'
# item_name, item_id = doubanTest.find_ID(name)  # 执行find_ID函数，返回该剧名的name-id对
# finallyUrl = url1 + item_id[0] + url2
# print(finallyUrl)

try:
    item_name, item_id = getDoubanID.find_ID(name)  # 执行find_ID函数，返回该剧名的name-id对
    finallyUrl = url1 + item_id[0] + url2
    print(finallyUrl)
except:  # 如果执行出现错误，则将失败的name储存在error_list中
    print("没有找到你想要的内容")

spider(finallyUrl)