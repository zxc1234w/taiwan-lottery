#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree, html
from bs4 import BeautifulSoup
import requests, json
import re
import urllib
import numpy

def get_hiddenvalue(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "lxml")
    VIEWSTATE = soup.find(id = "__VIEWSTATE")['value']
    EVENTVALIDATION = soup.find(id = "__EVENTVALIDATION")['value']
    return VIEWSTATE,EVENTVALIDATION

def getkey(data):
    return data[0]

def checklotterytype(url):
    lotterytype = url[38] + url[39] + url[40] + url[41]
    if (lotterytype == '38M6'):
        return 'M638', 4
    if (lotterytype == '39M5'):
        return 'M539', 10
    if (lotterytype == '49M6'):
        return 'M649', 3

def transformyear(_url, _year):
    year = str(_year)
    url = list(_url)
    start = re.search("\d", _url).start()
    if url[start] == '5' and url[start+1] == '3' and url[start+2] == '9':
        start = 39
    for i in range(0,4):
        url[start+i] = year[i]

    return "".join(url)

def getlotterydata(url, name, nchoice):

    #startyear = url[36] + url[37] + url[38] +url[39]
    startyear = "".join(re.findall(r'\d+', url))
    if startyear[0]=='5' and startyear[1]=='3' and startyear[2]=='9':
        startyear = startyear[3] + startyear[4] + startyear[5] + startyear[6]
    data = []
    for year in range(int(startyear), 2018):
        url = transformyear(url, year)
        result = requests.post(url)
        result.encoding = 'utf8'
        soup = BeautifulSoup(result.text, "lxml")
        # Table = soup.select('li')
        # y = []
        # for i in range(0, len(Table)):
        #     y.append(int(Table[i].select('p').text))
        
        Table = soup.find_all("ul", class_="history_ball")
        Index = soup.find_all('span', style="font-size:18px; color:#fb4202; font-weight:bold;")
        print(len(Index))
        #print(Table[0].select('a')[0].text)
        
        for i in range(len(Table)):
            y = []
            y.append(int(Index[i].text))
            start = 0
            end = nchoice
            if name == 'daily539':
                start = nchoice
                end = start + nchoice
            for j in range(start, end):
                y.append(int(Table[i].select('a')[j].text))
            data.append(y)

        # for i in range(2,len(Table)):
        #     y = []
        #     y.append(int(Table[i].select('span')[0].text))
        #     for j in range(3,3+int(url[41])):
        #         y.append(int(Table[i].select('span')[j].text))
        #     data.append(y)


    sort = sorted(data, key=getkey)
    numpy.savetxt(name+".csv", sort, delimiter = ',')
    #print(sort)

