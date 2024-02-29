import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
information = dict()
page=['124','122','792','123','619']#頁面址的差異
for i in range(0,len(page)):
    url = "https://www.c-are-us.org.tw/business/resturant/"+page[i]#改變網頁連結
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    soup = BeautifulSoup(html, 'html.parser')
    table1 = soup.find_all('p')#找到各庇護餐廳資訊
    if i <= 1:
        judge = "width: 100%; margin-top: 5px;"
    else:
        judge = "margin-top: 5px; width: 100%;"
    table2 = soup.find_all('table', {"style": judge })#找到地點區域
    parser = re.compile(".+地址 :(.+)》.+")#標準限制
    pos = []
    shop = []
    a = 0
    for titles in table1:
        title = titles.find_all('strong')
        if title != []:
            shop.append(title[0].text)#將餐廳名稱放到陣列中
    for contents in table2:
        lines = str(contents.text.replace("\n", ""))
        match = parser.fullmatch(lines)
        pos.append(str(match.group(1)).replace("\xa0", ""))#將符合標準限制的群組放入位置陣列

    for i in range(0, len(pos), 1):
        if shop[i] == "":
            a += 1
        elif i * 2 == 22:
            a += 1
        information[shop[a + i * 2]] = pos[i]#將店家名稱與位置配對成字典


print(information)