# -*- coding: utf-8 -*-
"""
KNN kd-tree implementation
Created on Tue Mar  6 20:53:11 2018

reference: https://leileiluoluo.com/posts/kdtree-algorithm-and-implementation.html
@author: Liuying Wang
"""
import numpy as np
import matplotlib.pyplot as plt
import collections
import pdb
#%% test data
def dataGene():
    #pdb.set_trace()
    X1 = np.random.multivariate_normal(mean = [0.,0.],
                                   cov = [[1.,0.],[0.,1.]],size = 10)
    X2 = np.random.multivariate_normal(mean = [2.,0.],
                                   cov = [[1.,.5],[.5,1.]],size = 10)
    X3 = np.random.multivariate_normal(mean = [1.,2.],
                                   cov = [[1.,0],[0.,1.]],size = 10)
    X = np.r_[X1,X2,X3]
    Y = np.array([0]*10+[1]*10+[2]*10)
    return X,Y

X,Y = dataGene()

plt.scatter(X[:,0],X[:,1],c = ['r']*10+['b']*10+['g']*10)
#%% normalization

def mean_std(x):
    mean = np.apply_along_axis(np.mean,axis = 0,arr = x)
    std = np.apply_along_axis(np.std,axis = 0,arr = x)
    return mean,std
        
        
def normalization(x,predict_x):
    mean,std = mean_std(np.r_[x,predict_x])
    x_scaled = (x-mean)/std
    pre_x_scaled = (predict_x-mean)/std
    return x_scaled, pre_x_scaled
    
#%%
def knn(x, y, predict_x, k = 5):
    if len(predict_x.shape)==1:
        predict_x = predict_x[np.newaxis,:]
    #x, predict_x = normalization(x,predict_x)
    dist = np.apply_along_axis(np.sum,axis = 1,arr = (x - predict_x)**2)
    predict_y = collections.Counter(y[dist.argsort()<k]).most_common(n = 1)[0][0]
    return predict_y

#%%test
X,Y = dataGene()
plt.scatter(X[:,0],X[:,1],c = ['r']*10+['b']*10+['g']*10)
xtest = np.array([0.,0.])
plt.scatter(xtest[0],xtest[1],c = 'k',marker = '^')

knn(X,Y,xtest,k = 5)
