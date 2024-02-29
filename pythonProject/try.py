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
import requests
from translate import Translator
YOUR_API_KEY= "AIzaSyCj439fsb887n94U1c3nEWI3duNiHLm4W0"
addr = '台灣台北市萬華區康定路190號'
#print(addr.encode('UTF-8'c))
res2="https://maps.googleapis.com/maps/api/geocode/json?address="+ addr +"&key="+YOUR_API_KEY
#data2 = urllib.request.urlopen(res2).read().decode()
data2=requests.get(res2)
#lines2 = json.loads(data2)
print(data2.text)