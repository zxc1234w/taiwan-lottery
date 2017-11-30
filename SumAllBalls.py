import numpy
import pandas as pd
import matplotlib.pyplot as plt

def checklotterytype(url):
    lotterytype = url[38] + url[39] + url[40] + url[41]
    if (lotterytype == '38M6'):
        return '38M6.csv', 38, 6
    if (lotterytype == '39M5'):
        return '39M5.csv', 39, 5
    if (lotterytype == '49M6'):
        return '49M6.csv', 49, 6

def pick_n_max_value_index(array, n):
    # sortedarray = sorted(range(len(array)), key = lambda x: array[x])
    # result = []
    # for i in range(len(array), len(array)-n):
    #     result.append(array[i])
    return numpy.argsort(array)[-n:], numpy.sort(array)[-n:]

def sumallballs(data, nball, nchoice):
    #filename, nball, nchoice = checklotterytype(url)
    # loadData = numpy.genfromtxt(filename, delimiter=",", dtype = None)
    # type(loadData)
    # iloadData = loadData.astype(numpy.int64)
    #print(len(iloadData[0]))

    # idx = []
    # one = []
    # count = [0] * 38#list(range(38))
    # for i in range(len(iloadData)):
    #     #print(iloadData[i][1])
    #     count[iloadData[int(i)][2] - 1]+=1
    #     idx.append(i)
    #     one.append(iloadData[int(i)][2])
    # print(len(idx), len(one))

    sum = []
    for i in range(1,1+nchoice):
        singleBall = [0] * nball
        for j in range(len(data)):
            #print(iloadData[i][1])
            singleBall[data[int(j)][i] - 1]+=1
        for j in range(len(singleBall)):
            singleBall[j]/=float(len(data))
        n = 0
        for j in range(len(singleBall)):
            n += singleBall[j]
        sum.append(singleBall)

    y = list(range(1,1+nball))
    maxIndex = []
    maxValue = []
    for i in range(0,nchoice):
        sortIndex, sortValue = pick_n_max_value_index(sum[i], 5)
        maxIndex.append(sortIndex)
        maxValue.append(sortValue)
        plt.scatter(maxIndex[i], maxValue[i], label=str(i+1))
        #plt.scatter(y, sum[i], label=str(i+1))
        #plt.plot(y, sum[i], label=str(i+1))
        for j in range(0, len(maxIndex[i])):
            plt.text( maxIndex[i][j], maxValue[i][j], str(maxIndex[i][j] + 1))

    plt.legend(loc="upper right")
    #plt.xlim([1,nball])
    plt.show();
    return
