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
