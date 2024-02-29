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
addr= input("輸入地址:")
translator= Translator(from_lang="chinese",to_lang="english")
translation = translator.translate(addr[:2])

YOUR_API_KEY = "AIzaSyCj439fsb887n94U1c3nEWI3duNiHLm4W0"
res1="https://maps.googleapis.com/maps/api/geocode/json?"+"address="+str(translation)+"&key="+YOUR_API_KEY
data1 = urllib.request.urlopen(res1).read().decode()
lines1 = json.loads(data1)#get id
for ids in lines1['results']:
    i = ids['geometry']['location']['lat']
    d = ids['geometry']['location']['lng']

print(str(i),str(d))
res ="https://maps.googleapis.com/maps/api/place/nearbysearch/json?"+"location="+str(i)+","+str(d)+"&radius=3000"+"&type=attraction"+"&key="+YOUR_API_KEY
data = urllib.request.urlopen(res).read().decode()
lines = json.loads(data)#get id
atr = dict()
for contents in lines['results']:
    print(contents['name'])
    atr[contents['name']]=contents['place_id']
print(atr)