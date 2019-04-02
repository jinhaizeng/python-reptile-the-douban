# coding: utf-8
# 本部分代码用来获取对应剧名的ID，这样可以直接利用https://movie.douban.com/subject/ID/得到剧所在页面
# 假设只知道剧名列表 ['战火西北狼','武林外传']，想爬取其豆瓣信息。首先我要知道它的豆瓣ID，这样才能更好地连接到该剧的信息页。

import urllib.request
import pandas as pd
import urllib.parse
import requests
import re
import matplotlib.pyplot as plt
from imageio import imread
from wordcloud import WordCloud
import jieba, codecs
from lxml import html
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import random
import time
import os


def find_ID(name):  # name即剧名
    try:
        url1 = 'https://movie.douban.com/j/subject_suggest?q='
        url2 = urllib.parse.quote(name)  # URL只允许一部分ASCII字符，其他字符（如汉字）是不符合标准的，此时就要进行编码。
        url = url1 + url2  # 生成针对该剧的链接，上面链接红字部分即为编码的name
        html = requests.get(url)  # 访问链接，获取html页面的内容
        html = html.content.decode()  # 对html的内容解码为utf-8格式
        html_list = html.replace('\/', '/')  # 将html中的\/全部转换成/，只是为了看着方便（不换也行）
        html_list = html_list.split('},{')  # 将html页面中的每一个条目提取为列表的一个元素。

        # 定义正则，目的是从html中提取想要的信息（根据title提取id）
        str_title = '"title":"' + name + '"'  ##匹配剧名name
        pattern_title = re.compile(str_title)

        str_id = '"id":"' + '[0-9]*'  ##匹配该剧的id值
        pattern_id = re.compile(str_id)

        # 从html_list中的每个item中提取对应的ID值
        id_list = []  # ID存放列表
        for l in html_list:  # 遍历html_list
            find_results_title = re.findall(pattern_title, l, flags=0)  # 找到匹配该剧name的条目item
            if find_results_title != []:  # 如果有title=name的条目，即如果有匹配的结果
                find_results_id = re.findall(pattern_id, l, flags=0)  # 从该匹配的item中的寻找对应的id之
                id_list.append(find_results_id)  # 将寻找到的id值储存在id_list中

        # 可能匹配到了多个ID（可能是同名不同剧），根据产生的id的数量，使剧名name匹配产生的id，使两个list相匹配
        name_list = [name] * len(id_list)

        # 对id_list的格式进行修整，使之成为标准列表格式
        id_list = str(id_list).replace('[', '').replace(']', '').replace("'", '').replace('"id":"', '').replace(' ', '')
        id_list = id_list.split(',')

    except:  # 如果不能正常运行上述代码（不能访问网页等），输出未成功的剧名name。
        print('ERROR:', name)
    return name_list, id_list


def generate_ID(nondup_name_list):  # 给定剧单（剧名列表）
    name_list = []
    id_list = []
    error_list = []
    for name in nondup_name_list:  # 遍历剧单中每个剧名
        try:
            item_name, item_id = find_ID(name)  # 执行find_ID函数，返回该剧名的name-id对
            name_list.extend(item_name)  # 储存name
            id_list.extend(item_id)  # 储存id
        except:  # 如果执行出现错误，则将失败的name储存在error_list中
            error_list.extend(name)
        time.sleep(1 + float(random.randint(1, 100)) / 20)  # 防止账号被封，随机延迟

    if '' in id_list:  # 除去异常的id
        id_list.remove('')

    if '' in error_list:  # 除去异常的id
        error_list.remove('')

    print(id_list)
    print(name_list)

    if error_list != []:
        print('未成功生成ID的剧名：', error_list)
    else:
        print('------------------------------全部成功生成豆瓣ID------------------------------------')
    return id_list, name_list


# nondup_name_list = ['战火西北狼','武林外传']
# id_list,name_list = generate_ID(nondup_name_list)
