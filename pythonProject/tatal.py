import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import datetime
import os
import pyodbc
import urllib.request
import zipfile
import json
import re
from translate import Translator
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

Flag = 1
while Flag:
    place = []
    PLACE= []
    local = input("輸入地址:")
    time = input("xxxx-xx-xx:")
    api_key = "CWB-279198A6-BA27-4437-8498-824C630CB3FE"
    find_tipe= "F-D0047-091"
    res ="https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/"+find_tipe+"?Authorization="+api_key +"&format=JSON"
    data = urllib.request.urlopen(res).read().decode()
    lines = json.loads(data)#get id

    for line in lines['cwbopendata']['dataset']['locations']['location']:
        if str(line['locationName'])[:3]==local:
            for contents in line['weatherElement']:
                if contents['description']=='平均溫度':
                    sum = 0
                    for tps in contents['time']:
                        if str(tps['startTime'][:10])==str(time):
                            sum += float(tps['elementValue']['value'])
                    avg = str(sum/2)
                    print('溫度:',avg,'攝氏度')
                TF = 1
                if contents['description']=='12小時降雨機率':
                    sum = 0
                    for precent in contents['time']:
                        if str(precent['startTime'][:10])==str(time):
                            if str(precent['elementValue']['value']) == 'None':
                                print("無法預測降雨率")
                                TF = 0
                                break
                            sum += float(precent['elementValue']['value'])
                    if TF == 1:
                        avg = str(sum/2)
                        print('降雨概率',avg,'百分比')
                if contents['description']=='天氣現象':
                    for detail in contents['time']:
                        if str(detail['startTime'][:10])==str(time):
                            print(detail['elementValue'][0]['value'])
                            break
                if contents['description']=='紫外線指數':
                    for uva in contents['time']:
                        if str(uva['startTime'][:10])==str(time):
                            print('紫外線強度:',uva['elementValue'][1]['value'])
                            break

    translator = Translator(from_lang="chinese", to_lang="english")
    translation = translator.translate(local[:2])
    YOUR_API_KEY = "AIzaSyCj439fsb887n94U1c3nEWI3duNiHLm4W0"
    res1 = "https://maps.googleapis.com/maps/api/geocode/json?" + "address=" + str(translation) + "&key=" + YOUR_API_KEY
    data1 = urllib.request.urlopen(res1).read().decode()
    lines1 = json.loads(data1)  # get id
    for ids in lines1['results']:
        i = ids['geometry']['location']['lat']
        d = ids['geometry']['location']['lng']

    res = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?" + "location=" + str(i) + "," + str(d) + "&radius=3000" + "&type=attraction" + "&key=" + YOUR_API_KEY
    data = urllib.request.urlopen(res).read().decode()
    lines = json.loads(data)  # get id
    atr = dict()
    for contents in lines['results']:
        print(contents['name'])
        atr[contents['name']]=contents['place_id']
    print("輸入選取，結束按Q")
    while 1:
        choices = input("")
        if choices=='Q':
            break
        else:
            PLACE.append(choices)
            place.append(atr[choices])
    for name, grade in pro_shop.items():
        print(name, grade)
    while 1:
        choices = input("")
        if choices=='Q':
            break
        else:
            PLACE.append(choices)
            place.append(pro_shop[choices])
    for name, grade in information.items():
        print(name, grade)
    while 1:
        choices = input("")
        if choices=='Q':
            break
        else:
            PLACE.append(choices)
            place.append(information[choices])
    print(place)
    i=0
    TIMMMM=[]
    try:
        for i in range(0,len(place),1):
            YOUR_API_KEY = "AIzaSyCj439fsb887n94U1c3nEWI3duNiHLm4W0"
            res2 = "https://maps.googleapis.com/maps/api/directions/json?origin=place_id:" + place[i] + "&destination=place_id:" + place[i+1] + "&key=" + YOUR_API_KEY
            data2 = urllib.request.urlopen(res2).read().decode()
            lines2 = json.loads(data2)
            for road in lines2['routes']:
                for time in road['legs']:
                    TIMMMM.append(time['duration']['text'])
    except:
        pass
    a=0
    for a in range(0,len(place),1):
        print(PLACE[a])
        try:
            print ("→→→"+TIMMMM[a]+"→→→")
        except:
            pass
    CB = input('繼續按任一鍵，退出按B：')

    if CB=='B':
        Flag = 0
        break
    else:
        continue


