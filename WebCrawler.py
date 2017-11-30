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
    

def getlotterydata(url):
    VIEWSTATE, EVENTVALIDATION = get_hiddenvalue(url)
    lotterytype, dropdown = checklotterytype(url)
    post = {
        '__EVENTTARGET' : '',
        '__EVENTARGUMENT' : '',
        '__LASTFOCUS' : '' ,
        '__VIEWSTATE' : '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',
        '__VIEWSTATEGENERATOR' : 'F9BA1DB1',
        '__VIEWSTATEENCRYPTED' : '',
        '__EVENTVALIDATION' : '5o1NqKE+YKbVxM7MzxpQ/rMVDrGwhc9IM9RoMdPdLCubJzq/ww3xqtekVZQWPbg1xmcXBEcuaCsz6tSXWBJJ++xWo7BuXDEAjKi1iZhPGK4INWnpzjeHyKzlRwP2JTrN1f+qX/hLx6YNK5QUpTS2zw5gUOO8ITrb5W0tm67MEb7Si+r7U3uE6nnvjhM/jUpI4mEA/KYefhcrCq9GClXJBisVRleX0pqlIXihZibmDGRTMOeKY6r8C2KbjhL/Boay1/7LyROZDqpViHzz8T8/3syal0LhWHQCD9DvI5vvrMnrg8NXyaMPpOcjdt/HkDmjjyoS+FI4vEz4T2h4YtZh3g==',
        lotterytype + 'Control_history1$DropDownList1' : '4',
        lotterytype + 'Control_history1$chk' : 'radYM',
        lotterytype + 'Control_history1$dropYear' : '106',
        lotterytype + 'Control_history1$dropMonth' : '10',
        lotterytype + 'Control_history1$btnSubmit' : '查詢'
    }

    post['__VIEWSTATE'] = VIEWSTATE
    post['__EVENTVALIDATION'] = EVENTVALIDATION
    post[lotterytype + 'Control_history1$DropDownList1'] = dropdown

    data = []
    for year in range(103, 107):
        post[lotterytype + 'Control_history1$dropYear'] = year
        for month in range(1, 13):
            post[lotterytype + 'Control_history1$dropMonth'] = month
            result = requests.post(url, data = post)
            result.encoding = 'utf8'
            soup = BeautifulSoup(result.text, "lxml")
            Table = soup.select('table')
            for i in range(2,len(Table)):
                y = []
                y.append(int(Table[i].select('span')[0].text))
                for j in range(3,3+int(url[41])):
                    y.append(int(Table[i].select('span')[j].text))
                data.append(y)



    sort = sorted(data, key=getkey)
    name = url[38] + url[39] + url[40] + url[41] + ".csv"
    numpy.savetxt(name, sort, delimiter = ',')
    #print(sort)

