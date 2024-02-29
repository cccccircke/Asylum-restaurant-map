import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
url = "https://www.harvest365.org/posts/7648"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')#Converted into a special form to exist in soup
names = []
addrs = []
pro_shop = dict()
name_get = soup.find_all('span', {"style": "font-size:24px;"})[1::2]#抓取餐廳名稱
for name in name_get:
    names.append(name.text)#把餐廳名稱加到陣列中
table = soup.find_all('div', {"class": "cont"})
contents = str(table[0]).split("<br/>")
parser = re.compile("\r\n地址：(.+)")#限制抓取地點的格式
for content in contents:
    match = parser.fullmatch(content)
    if match != None:
        addrs.append(match.group(1))#取格式內符合群組的字串
for i in range (0,len(names)):
    pro_shop[names[i]] = addrs[i]#將名字跟地點配對成字典
print(pro_shop)



