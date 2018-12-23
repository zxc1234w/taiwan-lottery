import numpy as np
import math
import copy

def calculate_probability_afterwards(data, nball, nchoice):
    all_probability = []
    for i in range(0, nchoice):
        #probability = list(range(1, 1+nball))
        probability = np.zeros((nball, nball))
        for j in range(1, len(data)):
            now_opend = data[j-1][i] - 1
            afterwards = data[j][i] - 1
            probability[now_opend][afterwards] += 1
        all_probability.append(probability)

    return

def calculate_probability_table(data, nball, nchoice):
    all_probability = np.zeros((nchoice,nball,nchoice,nball))
    
    for i in range(0, nchoice):
        for j in range(1, len(data)-1):
            now = data[j-1][i]
            for k in range(0, nchoice):
                next = data[j][k]
                all_probability[i][now][k][next] += 1

    return all_probability

def Get_probability(data, nball, nchoice, previousOpen):
    probabilityTable = calculate_probability_table(data, nball, nchoice)
    probability = []
    for i in range(0, nchoice):
        single_probability = np.zeros(nball).tolist()
        for j in range(0, nchoice):
            single_probability += probabilityTable[j][previousOpen[j]][i]
        probability.append(single_probability)
        sort = copy.copy(single_probability)
        sort.sort()
        median = int((len(sort)/2) - 1)
        print(single_probability.tolist().index(sort[median]))
    
    return


def calculate_probability_previous(data, nball, nchoice, previous):
    probability = []
    ndata = len(data) - 1
    for i in range(ndata, ndata-previous, -1):
        print(data[i])
    return
