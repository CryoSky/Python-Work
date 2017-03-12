import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error"

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    neirong = soup.table.contents
    for form in neirong[3:504]:
        if isinstance(form, bs4.element.Tag):
            tds = form('td')   #将所有td标签存为一个列表类型tds
            ulist.append([tds[0].string, tds[1].string, tds[3].string])    #在ulist中增加相应字段

def printUnivList(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))


def main():
    uinfo = []   #放输出的列表，初始化为空
    url = 'http://www.shanghairanking.com/ARWU2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)  # 20 univs

main()


'''
r = requests.get("http://www.shanghairanking.com/ARWU2016.html")

WebText = r.text

soup = BeautifulSoup(WebText, 'html.parser')
for form in soup.find.contents[3:504]
print(type(soup.table.contents))

'''
