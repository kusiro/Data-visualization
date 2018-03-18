import requests
import time
from bs4 import BeautifulSoup
import os
import re
import urllib.request
import json
weatherdata = {}
def get_data(link,datadic,time):
    datadic[time] = {}
    for i in range(13):
        datadic[time][i] = []
    r = requests.get(url = link)
    r.encoding = 'utf8'
    soup = BeautifulSoup(r.text,"html.parser")
    data = soup.find_all("tr")
    for i in range(3,34):
        counter = 0
        for d in data[i]:
            if (not d.string == "\n"):
                if (d.string == "-"):
                    datadic[time][counter].append(0)
                    counter += 1
                    continue
                if (d.string == "T"):
                    datadic[time][counter].append(0.1)
                    counter += 1
                    continue
                if (d.string == None):
                    counter +=1
                    continue
                datadic[time][counter].append(float(d.string))
                counter += 1
    return datadic


num = [2009,2010,2011,2012,2013,2014,2015,2016,2017]
for i in num:
    link = "https://www.cwb.gov.tw/V7/climate/dailyPrecipitation/Data/466920_"+str(i)+".htm"
    get_data(link,weatherdata,i)
with open("weatherdata.json", 'w', encoding='utf-8') as f:
    json.dump(weatherdata, f, indent=2, sort_keys=True, ensure_ascii=False)


#%%
a = {"g":[1],1:"f"}
a["g"].append(3)
print (a[1])
