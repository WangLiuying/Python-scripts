# -*- coding: utf-8 -*-
"""
naive bayes classifier
Created on Wed Mar  7 19:40:40 2018
reference: 李航 统计学习方法
@author: Liuying Wang
"""
import numpy as np
import pandas as pd
#import pdb
#%% data
def dataGene():
    X1 = np.array([1,1,1,1,1,2,2,2,2,2,3,3,3,3,3])
    X2 = np.array([1,2,2,1,1,1,2,2,3,3,3,2,2,3,3])
    Y = np.array([-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1])
    data = pd.DataFrame({'X1':X1,'X2':X2,'Y':Y})
    return data

data = dataGene()

newX = np.array([2,1])
#%% 输出先验概率和条件概率，采用拉普拉斯平滑
def NBclassifier(x,y):
    #pdb.set_trace()
    N = len(y)
    P = x.shape[1]    
    prior = ((pd.value_counts(y)+1)/(N+len(y.unique()))).to_dict()
    cond = {}
    for k in y.unique().tolist():
        cond[k]={}
        for p in range(P):
            xpossible = pd.Series(x.iloc[:,p].unique())
            templist = x.loc[y==k,x.columns[p]].append(xpossible,ignore_index = True)
            numerator = pd.value_counts(templist)
            denominator = templist.shape[0]
            cond[k][p] = numerator/denominator
    return {"prior":prior,"condProb":cond}

#%%
NBmodel = NBclassifier(data.iloc[:,:2],data.iloc[:,2])

#%%
def predict_NB(model,newx):
    ypossible = list(model['prior'].keys())
    yhat = pd.Series([0.]*len(ypossible),index = ypossible)
    P = newx.shape[0]
    for c in ypossible:
        yhat[c] = model['prior'][c]
        cond = model['condProb'][c]
        for p in range(P):
            yhat[c] = yhat[c]*cond[p][newx[p]]
    return yhat
    
#%%
predict_NB(NBmodel,newX)
