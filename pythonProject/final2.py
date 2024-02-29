import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
page=[]
information = dict()
change = ""
addr = ""
for i in range(1,15):#抓14頁
    if i >= 2:
        change ="?page="+str(i)
    url = "https://www.harvest365.org/posts/sub/38"+change#根據頁數改變網頁碼
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')#Conver# ted into a special form to exist in soup
    table = soup.find_all('div', {"class": "btn"})#抓每頁每個區域出現連結的位置
    for line in table:
        pages = line.select_one('a').get("href")#抓取網頁連結址
        page.append(pages)
print(page)
for j in range(0,len(page)):#跑每個連結
    change = page[j]
    url = "https://www.harvest365.org" + change#根據連結址改網頁碼
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    contents1 = soup.find_all('div', {"class": "main-article xwg-fl"})#抓取標題位置
    contents2 = soup.find_all('div', {"class": "cont"})#抓取地點區域
    parser = re.compile(".*地[點址]：(.+)")#地點區域的標準限制
    for content in contents1:
        line = content.find("h3")
        for title in line:
            title = line.text
    for content in contents2:
        lines = content.text.replace("\xa0","").replace("\r","").split("\n")
        for line in lines:
            match = parser.fullmatch(line)#匹配標準
            if match != None:
                addr=match.group(1)#根據標準取符合群組的字串
    if addr != "":
        information[title]=addr#將標題與地點配對成字典


print(information)
