# -*- coding: utf-8 -*-
"""
Spyder Editor

matplotlib learning: Advanced plot.
From the book python数据分析实战
"""
#%% packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%等高线图
dx=0.01;dy=0.01
x=np.arange(-2,2,dx)
y=np.arange(-2,2,dy)
X,Y=np.meshgrid(x,y)

def myf(x,y):
    return (1-y**5+x**5)*np.exp(-x**2-y**2)

C=plt.contour(X,Y,myf(X,Y),8,colors='black')#轮廓
plt.contourf(X,Y,myf(X,Y),8)#着色
plt.clabel(C,inline=1,fontsize=10)#添加数字标记
plt.colorbar()#添加图例

#%%极区图
N=8
theta=np.arange(0,2*np.pi,2*np.pi/N)
radii=np.array([4,7,5,3,1,5,6,7])
plt.axes([0.025,0.025,0.95,0.95],polar=True)
colors=np.array(['#4bb2c5','#c5b47f','#EAA228','#579575','#839557','#958c12','#953579','#4b5de4'])
bars=plt.bar(theta,height=radii,width=2*np.pi/N,bottom=0.0,color=colors)


#%%mplot3d
from mpl_toolkits.mplot3d import Axes3D

#%%
fig=plt.figure()
ax=Axes3D(fig)
X=np.arange(-2,2,0.1)
Y=np.arange(-2,2,0.1)
X,Y=np.meshgrid(X,Y)

def f(x,y):
    return (1-y**5+X**5)*np.exp(-x**2-y**2)

ax.plot_surface(X,Y,f(X,Y),rstride=1,cstride=1)

#%%3D散点图
xs=np.random.randint(30,40,100)
ys=np.random.randint(20,30,100)
zs=np.random.randint(10,20,100)
xs2=np.random.randint(50,60,100)
ys2=np.random.randint(30,40,100)
zs2=np.random.randint(50,70,100)
xs3=np.random.randint(10,30,100)
ys3=np.random.randint(40,50,100)
zs3=np.random.randint(40,50,100)

fig=plt.figure()
ax=Axes3D(fig)
ax.scatter(xs,ys,zs)
ax.scatter(xs2,ys2,zs2,c='r',marker='^')
ax.scatter(xs3,ys3,zs3,c='g',marker='*')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')


#%%3D条状图
x=np.arange(8)
y=np.random.randint(0,10,8)
y2=y+np.random.randint(0,3,8)
y3=y2+np.random.randint(0,3,8)
y4=y3+np.random.randint(0,3,8)
y5=y4+np.random.randint(0,3,8)
clr=['#4bb2c5','#c5b47f','#EAA228','#579575','#839557','#958c12','#953579','#4b5de4']
fig=plt.figure()
ax=Axes3D(fig)
ax.bar(x,y,0,zdir='y',color=clr)
ax.bar(x,y2,10,zdir='y',color=clr)
ax.bar(x,y3,20,zdir='y',color=clr)
ax.bar(x,y4,30,zdir='y',color=clr)
ax.bar(x,y5,40,zdir='y',color=clr)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.view_init(elev=40,azim=220)#elev初始海拔，azim偏转角

#%%多面板图形
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
inner_ax=fig.add_axes([0.6,0.6,0.25,0.25])

x1=np.arange(10)
y1=np.array([1,2,7,1,5,2,4,2,3,1])
x2=np.arange(10)
y2=np.array([1,3,4,5,4,5,2,6,4,3])
ax.plot(x1,y1)
inner_ax.plot(x2,y2)

#%%子图网格

gs=plt.GridSpec(3,3)
fig=plt.figure(figsize=(6,6))
fig.add_subplot(gs[1,:2])
fig.add_subplot(gs[0,:2])
fig.add_subplot(gs[2,0])
fig.add_subplot(gs[:2,2])
fig.add_subplot(gs[2,1:])

#%%绘制图形
gs=plt.GridSpec(3,3)
fig=plt.figure(figsize=(6,6))

x1=np.array([1,3,2,5])
y1=np.array([4,3,7,2])
x2=np.arange(5)
y2=np.array([3,2,4,6,4])

s1=fig.add_subplot(gs[1,:2])
s1.plot(x,y,'r')

s2=fig.add_subplot(gs[0,:2])
s2.bar(x2,y2)

s3=fig.add_subplot(gs[2,0])
s3.barh(x2,y2,color='g')

s4=fig.add_subplot(gs[:2,2])
s4.plot(x2,y2,'k')

s5=fig.add_subplot(gs[2,1:])
s5.plot(x1,y1,'b^',x2,y2,'yo')