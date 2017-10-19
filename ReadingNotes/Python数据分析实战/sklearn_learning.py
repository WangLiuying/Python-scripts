# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 20:37:37 2017

@author: 13656

学习sklearn
参考书：Python数据分析实战
"""

"""
监督学习例子：
分类： KNN分类器，SVC
回归：线性回归，SVR
"""

#%%调出数据集
from sklearn import datasets
iris=datasets.load_iris()
dir(iris)
iris.data
iris.feature_names
iris.target
iris.target_names

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn import datasets

x=iris.data[:,0]
y=iris.data[:,1]
species=iris.target

x_min,x_max=x.min()-0.5,x.max()+0.5
y_min,y_max=y.min()-0.5,y.max()+0.5

#scatterplot
plt.figure()
plt.title('Iris Dataset')
plt.scatter(x,y,c=species)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)
plt.xticks(())
plt.yticks(())
#%%

x=iris.data[:,2]
y=iris.data[:,3]
species=iris.target

x_min,x_max=x.min()-0.5,x.max()+0.5
y_min,y_max=y.min()-0.5,y.max()+0.5
plt.figure()
plt.title('Iris Dataset')
plt.scatter(x,y,c=species)
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)
plt.xticks(())
plt.yticks(())

#%%多维度的可视化：主成分分解降维
#使用 sklearn.decomposition fit_transform
from sklearn.decomposition import PCA
x_reduced=PCA(n_components=3).fit_transform(iris.data)
x_reduced


#%%
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

iris=datasets.load_iris()

species=iris.target
x_reduced=PCA(n_components=3).fit_transform(iris.data)
fig=plt.figure()
ax=Axes3D(fig)
ax.set_title('Iris Dataset by PCA',size=14)
ax.scatter(x_reduced[:,0],x_reduced[:,1],x_reduced[:,2],c=species)
ax.set_xlabel('First eigenvector')
ax.set_ylabel('Second eigenvector')
ax.set_zlabel('Third eigenvector')
ax.w_xaxis.set_ticklabels(())
ax.w_yaxis.set_ticklabels(())
ax.w_zaxis.set_ticklabels(())

#%%KNN
import numpy as np
import pandas as pd
from sklearn import datasets
np.random.seed(0)
iris=datasets.load_iris()
x=iris.data
y=iris.target
i=np.random.permutation(len(iris.data))
#切分训练集和测试集
x_train=x[i[:-10]]
y_train=y[i[:-10]]
x_test=x[i[-10:]]
y_test=y[i[-10:]]

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)

knn.predict(x_test)
knn.predict(x_test)==y_test

#%%KNN可视化
from matplotlib.colors import ListedColormap
"""
思路：先用数据训练knn，然后去预测图内的所有点则可以绘制底色，得到决策边界
然后再用散点图做出原来的点。
"""


iris=datasets.load_iris()
x=iris.data[:,:2]
y=iris.target

x_min,x_max=x[:,0].min()-0.5,x[:,0].max()+0.5
y_min,y_max=x[:,1].min()-0.5,x[:,1].max()+0.5

cmap_light=ListedColormap(['#AAAAFF','#AAFFAA','#FFAAAA'])
h=0.02
xx,yy=np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(x,y)

zz=knn.predict(np.c_[xx.ravel(),yy.ravel()])
plt.figure()
plt.pcolormesh(xx,yy,zz.reshape(xx.shape),cmap=cmap_light)

plt.scatter(x[:,0],x[:,1],c=y)
plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)

#%%调出数据集2
diabetes=datasets.load_diabetes()
dir(diabetes)
diabetes.data[0]#已经经过去均值处理
np.sum(diabetes.data[:,0]**2)
diabetes.feature_names
diabetes.target


#%%线性回归
from sklearn import linear_model
linreg=linear_model.LinearRegression()

np.random.seed(6646)
i=np.random.permutation(len(diabetes.data))
x_train=diabetes.data[i[:-20]]
y_train=diabetes.target[i[:-20]]
x_test=diabetes.data[i[-20:]]
y_test=diabetes.target[i[-20:]]


#fit model
linreg.fit(x_train,y_train)
linreg.predict(x_test)
y_test
linreg.coef_
linreg.intercept_
linreg.score(x_test,y_test)#预测集R**2
