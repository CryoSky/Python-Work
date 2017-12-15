# -*- coding:utf-8 -*-
# Written by cryosky, 2017-3-27, based on http://www.bilibili.com/video/av8834184 Last Homework for 中国大学MOOC-Python网络爬虫与信息提取
# 首先通过源代码中Network查找到需要的请求，记住方法是get。

import re
import requests
import sys
from bs4 import BeautifulSoup
from config import cookie

def main(video):
    url = 'http://www.bilibili.com/video/av' + video

    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'Referer':'http://www.bilibili.com',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Host':'www.bilibili.com',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Cache-Control':'max-age=0',
        'Cookie':COOKIE
    }

    r = requests.get(url, headers = headers)   #requests的get方法
    bs = BeautifulSoup(r.text, 'html.parser')  #使用BeautifulSoup解析网页

    title = bs.title.text.split('_')[0]  #视频标题
    print(title)
    link = 'http:' + bs.body.img['src']  #封面链接

    tail = re.findall('.*(\.\w+)', link)[0]
    pic = 'cover'+ tail

    r = requests.get(link)
    if r.status_code == 200:
        open(pic, 'wb').write(r.content)

if __name__ == '__main__':
    '''
    print('请输入视频av编号（仅限数字）')
    video = input()
    main(re.findall('\d+', video)[0])
    '''
    if len(sys.argv) != 2:
        print('请输入视频av编号（仅限数字）')
    else:
        video = sys.argv[1]
        main(re.findall('\d+', video)[0])


