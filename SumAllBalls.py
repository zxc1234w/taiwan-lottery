import numpy as np
import matplotlib.pyplot as plt

def pick_n_max_value_index(array, n):
    return np.argsort(array)[-n:], np.sort(array)[-n:]

def sumallballs(data, nball, nchoice):
    sum = []
    for i in range(0, nchoice):
        singleBall = [0] * nball
        for j in range(len(data)):
            singleBall[data[int(j)][i] - 1] += 1
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
