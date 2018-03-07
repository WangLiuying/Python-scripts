# -*- coding: utf-8 -*-
"""
感知机 

Created on Mon Mar  5 22:49:19 2018
@author: Liuying Wang
"""
import numpy as np
import matplotlib.pyplot as plt
#%%generate data
def dataGene():
    X1 = np.random.multivariate_normal(mean=np.array([0,0]),
                                       cov = np.array([[1,0],[0,1]]), size = 20)
    X2 = np.random.multivariate_normal(mean=np.array([3,3]),
                                       cov = np.array([[1,0],[0,1]]), size = 20)
    X = np.vstack([X1,X2])
    np.random.shuffle(X)
    ##w = 3, b = 1
    w,b = np.array([3.,2.]),-10.
    Y = np.sign(X.dot(w.T)+b)
    return X,Y

X,Y = dataGene()
w,b = np.array([3.,2.]),-10.
plt.scatter(X[:,0],X[:,1],c = Y)
x1plot = np.linspace(X[:,0].min(),X[:,0].max())
x2plot = (-b-w[0]*x1plot)/w[1]
plt.plot(x1plot,x2plot)
plt.show()
#%%
def perception(x,y,learning_rate):
    w,b = np.zeros(x.shape[1]),0
    M = np.where((x.dot(w.T)+b)*y<=0)[0]
    while M.shape[0]!=0:
        index = np.random.choice(M)
        w = w + learning_rate*y[index]*x[index,:]
        b = b + learning_rate*y[index]
        M = np.where((x.dot(w.T)+b)*y<=0)[0]
    return w,b
        
#%%
what,bhat = perception(X,Y,learning_rate = 0.5)   

#%%
plt.scatter(X[:,0],X[:,1],c = Y)

x1plot = np.linspace(X[:,0].min(),X[:,0].max())
x2plot = (-b-w[0]*x1plot)/w[1]
plt.plot(x1plot,x2plot)


x1plot = np.linspace(X[:,0].min(),X[:,0].max())
x2plot = (-bhat-what[0]*x1plot)/what[1]
plt.plot(x1plot,x2plot,'r')

plt.show()