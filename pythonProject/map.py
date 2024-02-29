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
YOUR_API_KEY= "AIzaSyCj439fsb887n94U1c3nEWI3duNiHLm4W0"
res2="https://maps.googleapis.com/maps/api/directions/json?origin=place_id:"+"ChIJ685WIFYViEgRHlHvBbiD5nE"+"&destination=place_id:"+"ChIJA01I-8YVhkgRGJb0fW4UX7Y"+"&key="+YOUR_API_KEY
data2 = urllib.request.urlopen(res2).read().decode()
lines2 = json.loads(data2)
for road in lines2['routes']:
    for time in road['legs']:
        print(time['duration']['text'])

