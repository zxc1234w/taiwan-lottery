from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def Kmeans(data):
    X = np.array(data)

    k = KMeans(6, random_state=None).fit(X)
    labels = k.labels_
    print(k.labels_)

    return