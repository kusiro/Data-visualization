import requests
import time
from bs4 import BeautifulSoup
import os
import re
import urllib.request
import json

def get_data(link):
    weatherdata = {}
    for i in range(13):
        weatherdata[i] = {}
    r = requests.get(url = link)
    r.encoding = 'utf8'
    soup = BeautifulSoup(r.text,"html.parser")
    data = soup.find_all("tr")
    for i in range(3,34):
        counter = 0
        for d in data[i]:
            if (not d.string == "\n"):
                if (d.string == "-"):
                    weatherdata[counter][i-2] = 0
                    counter += 1
                    continue
                if (d.string == "T"):
                    weatherdata[counter][i-2] = "< 0.1"
                    counter += 1
                    continue
                weatherdata[counter][i-2] = d.string
                counter += 1
    return weatherdata

link = "https://www.cwb.gov.tw/V7/climate/dailyPrecipitation/Data/466920_2017.htm"
weatherdata = get_data(link)
with open('weatherdata.json', 'w', encoding='utf-8') as f:
    json.dump(weatherdata, f, indent=2, sort_keys=True, ensure_ascii=False)


#%%
a = {"g":[1],1:"f"}
a["g"].append(3)
print (a[1])
