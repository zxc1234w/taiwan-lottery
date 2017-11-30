#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum
from SumAllBalls import sumallballs
#from WebCrawler import getlotterydata
from WebCrawlerAuzo import getlotterydata
from Kmeans import Kmeans
import numpy as np

class Lottery(Enum):
    M6_38 = "http://www.taiwanlottery.com.tw/lotto/38M6/history.aspx"
    M5_39 = "http://www.taiwanlottery.com.tw/lotto/39M5/history.aspx"
    M6_49 = "http://www.taiwanlottery.com.tw/lotto/49M6/history.aspx"
class LotteryAuzo(Enum):
    power = "power", "http://lotto.auzonet.com/power/list_2008_all.html", 38, 6
    biglotto = "biglotto", "http://lotto.auzonet.com/biglotto/list_2007_all.html", 49, 6
    daily539 = "daily539", "http://lotto.auzonet.com/daily539/list_2007_all.html", 39, 5


#url = Lottery.M6_49.value
#url = Lottery.M6_49.value
Name, url, nBall, nChoice = LotteryAuzo.power.value

loadData = np.genfromtxt(Name + ".csv", delimiter=",", dtype = None)
loadData = loadData.astype(np.int64)

Index = loadData[:,0]
Data = loadData[:,range(1,nChoice + 1)]

Kmeans(Data)
#sumallballs(Data, nBall, nChoice)
#getlotterydata(url, Name, nChoice)