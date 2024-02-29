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
local = input("縣市：")
time = input("xxxx-xx-xx:")
api_key = "CWB-279198A6-BA27-4437-8498-824C630CB3FE"
find_tipe= "F-D0047-091"
res ="https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/"+find_tipe+"?Authorization="+api_key +"&format=JSON"
data = urllib.request.urlopen(res).read().decode()
lines = json.loads(data)#get id

for line in lines['cwbopendata']['dataset']['locations']['location']:
    if str(line['locationName'])==local:
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






