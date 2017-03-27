# -*- coding:utf-8 -*-
# Code by cryosky, 2017-3-27, based on http://www.bilibili.com/video/av8834184

import re
import requests
import sys
from bs4 import BeautifulSoup

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
        'Cookie':'fts=1489280475; UM_distinctid=15ac008a05a298-0aec1b302bce4e-414a0229-1fa400-15ac008a05c285; \
        pgv_pvi=4094983168; sid=9v1px9pv; DedeUserID=952094; DedeUserID__ckMd5=2b91817d8de6238e; SESSDATA=863f5f2d%2C1491872501%2C5e16b813; \
        bili_jct=ebde4db8522358b10e58e3e68c6b7e6d; buvid3=CADFE85B-C3D9-4F0E-906D-2CA4ACEA248828062infoc; purl_token=bilibili_1490618879; \
        pgv_si=s8437248000; _cnt_pm=0; _cnt_notify=34; CNZZDATA2724999=cnzz_eid%3D962312883-1489277223-%26ntime%3D1490622506; \
        _dfcaptcha=19ea5f460ff3de88242028c7c3ec0f8d'
    }

    r = requests.get(url, headers = headers)
    bs = BeautifulSoup(r.text, 'html.parser')

    title = bs.title.text.split('_')[0]
    print(title)
    link = 'http:' + bs.body.img['src']

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


