# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 12:59:38 2017

@author: River

matplotlib

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.show()
plt.plot([1,2,3,4,],[1,4,9,16],'ro')


#设置轴limit
#%%
plt.axis([0,5,0,20])
plt.title('My first plot')
plt.plot([1,2,3,4],[1,4,9,16],'ro')

#%%matplotlib和numpy的结合使用
import math
import numpy as np
t=np.arange(0,2.5,0.1)
y1=list(map(math.sin,math.pi*t))
y2=list(map(math.sin,math.pi*t+math.pi/2))
y3=list(map(math.sin,math.pi*t-math.pi/2))
plt.plot(t,y1,'b*',t,y2,'g^',t,y3,'ys')

plt.plot(t,y1,'b--',t,y2,'g',t,y3,'r-.')

#%%使用kwargs
plt.plot([1,2,4,2,1,0,1,2,1,4],linewidth=2.0)

#%%处理多个figure和axes对象
t=np.arange(0,5,0.1)
y1=np.sin(2*np.pi*t)
y2=np.sin(2*np.pi*t)
plt.subplot(211)#参数依次为：竖直划分、横向划分、激活区域
plt.plot(t,y1,'b-.')
plt.subplot(212)
plt.plot(t,y2,'r--')

#%%
t=np.arange(0.,1.,0.05)
y1=np.sin(2*np.pi*t)
y2=np.cos(2*np.pi*t)
plt.subplot(121)
plt.plot(t,y1,'b-')
plt.subplot(122)
plt.plot(t,y2,'r--')

#%%为图标添加更多元素

#%%文本
plt.axis([0,5,0,20])
plt.title('My plot')
plt.xlabel('Counting')
plt.ylabel('Square values')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
#%%修改文本属性
plt.axis([0,5,0,20])
plt.title('My plot')
plt.xlabel('Counting',color='gray')
plt.ylabel('Square values',color='gray')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
#%%任何位置添加文本
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Times New Roman')
plt.xlabel('Counting',color='gray')
plt.ylabel('Square values',color='gray')
plt.text(1,1.5,'First',color='blue')
plt.text(2,4.5,'Second',color='pink')
plt.plot([1,2,3,4],[1,4,9,16],'ro')

#%%添加latex表达式
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Times New Roman')
plt.xlabel('Counting',color='gray')
plt.ylabel('Square values',color='gray')
plt.text(1,1.5,'First',color='blue')
plt.text(2,4.5,'Second',color='pink')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.text(1.1,12,r'$y=x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})

#%%添加网格
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Times New Roman')
plt.xlabel('Counting',color='gray')
plt.ylabel('Square values',color='gray')
plt.text(1,1.5,'First',color='blue')
plt.text(2,4.5,'Second',color='pink')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.text(1.1,12,r'$y=x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})
plt.grid(True,color='gray',linestyle='-.')

#%%添加图例
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Times New Roman')
plt.xlabel('Counting',color='gray')
plt.ylabel('Values',color='gray')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.plot([1,2,3,4],[0.8,3.5,8,15],'g^')
plt.plot([1,2,3,4],[.5,2.5,4,12],'b*')
plt.legend(['First Series','Second series','Third series'],loc=2)

#%%保存图表
# %save my_first_chart 25
# %save my_first_chart 24-25

# %load my_first_chart.py
# %run my_first_chart.py

#%%保存图像
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Times New Roman')
plt.xlabel('Counting',color='gray')
plt.ylabel('Values',color='gray')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.plot([1,2,3,4],[0.8,3.5,8,15],'g^')
plt.plot([1,2,3,4],[.5,2.5,4,12],'b*')
plt.legend(['First Series','Second series','Third series'],loc=2)
plt.savefig('my_chart.png')



#%%处理日期值
import datetime
import numpy as np
events=[datetime.date(2015,1,23),datetime.date(2015,1,28),datetime.date(2015,2,3),
        datetime.date(2015,2,21),datetime.date(2015,3,15),datetime.date(2015,3,24),
        datetime.date(2015,4,8),datetime.date(2015,4,24)]
readings=[12,22,25,20,18,15,17,14]
plt.plot(events,readings)
#刻度管理很糟糕

#%%
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

months=mdates.MonthLocator()
days=mdates.DayLocator()
timeFmt=mdates.DateFormatter('%Y-%M')
events=[datetime.date(2015,1,23),datetime.date(2015,1,28),datetime.date(2015,2,3),
        datetime.date(2015,2,21),datetime.date(2015,3,15),datetime.date(2015,3,24),
        datetime.date(2015,4,8),datetime.date(2015,4,24)]
readings=[12,22,25,20,18,15,17,14]
fig,ax=plt.subplots()#可查看改函数的返回值
plt.plot(events,readings)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(days)
ax.xaxis.set_major_formatter(timeFmt)


#%%线性图
x=np.arange(-2*np.pi,2*np.pi+0.01,0.01)
y1=np.sin(3*x)/x
y2=np.sin(2*x)/x
y3=np.sin(3*x)/x
plt.plot(x,y1,'r-',linewidth=3)
plt.plot(x,y2,'m-.')
plt.plot(x,y3,'#87a3cc',linestyle='--')#调整线粗细和颜色

plt.xticks(np.arange(-2*np.pi,2*np.pi+1,np.pi)
           [r'$-2\pi$',r'$-1\pi$',r'$0$',r'$1\pi$',r'$2\pi$'])      #调整刻度和定义显示


#%%绘制笛卡尔坐标轴
x=np.arange(-2*np.pi,2*np.pi+0.01,0.01)
y1=np.sin(3*x)/x
y2=np.sin(2*x)/x
y3=np.sin(3*x)/x
plt.plot(x,y1,'r-',linewidth=3)
plt.plot(x,y2,'m-.')
plt.plot(x,y3,'#87a3cc',linestyle='--')#调整线粗细和颜色

plt.xticks(np.arange(-2*np.pi,2*np.pi+1,np.pi),
           [r'$-2\pi$',r'$-1\pi$',r'$0$',r'$1\pi$',r'$2\pi$'])      #调整刻度和定义显示
ax=plt.gca()#get current axis
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')#这一句设定x轴跟随底部边线
ax.spines['bottom'].set_position(('data',0))#这一句设定底部边线的位置
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

#%%添加注释(使用函数annotate)
x=np.arange(-2*np.pi,2*np.pi+0.01,0.01)
y1=np.sin(x)/x
y2=np.sin(2*x)/x
y3=np.sin(3*x)/x
plt.plot(x,y1,'r-',linewidth=3)
plt.plot(x,y2,'m-.')
plt.plot(x,y3,'#87a3cc',linestyle='--')#调整线粗细和颜色

plt.xticks(np.arange(-2*np.pi,2*np.pi+1,np.pi),
           [r'$-2\pi$',r'$-1\pi$',r'$0$',r'$1\pi$',r'$2\pi$'])      #调整刻度和定义显示
ax=plt.gca()#get current axis
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')#这一句设定x轴跟随底部边线
ax.spines['bottom'].set_position(('data',0))#这一句设定底部边线的位置
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.annotate(r'$\lim_{x\to 0}\frac{\sin(x)}{x}=1$',xy=[0,1],xycoords='data',
             xytext=[30,30],fontsize=16,textcoords='offset points',
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))


#%%绘制pandas数据结构中的数据
data={'series1':[1,3,2,4,5],'series2':[2,3,1,4,5],'series3':[3,2,1,2,3]}
df=pd.DataFrame(data)
x=np.arange(5)
plt.axis([0,4,0,7])
plt.plot(x,df)
plt.legend(data,loc=2)

#%%绘制直方图
pop=np.random.randint(0,100,100)
pop
n,bins,patches=plt.hist(pop,bins=20)

#%%条状图
index=[0,1,2,3,4]
values=[5,7,3,4,6]
plt.bar(index,values)
plt.xticks(index,['A','B','C','D','E'])
#%%高级版条状图

index=[0,1,2,3,4]
values=[5,7,3,4,6]
std1=[.8,1,.4,.9,1.3]
plt.title('A Bar Plot')
plt.bar(index,values,yerr=std1,error_kw={'ecolor':'0.1','capsize':6},alpha=.6,label="Series' name")
plt.legend(loc=2)
plt.xticks(index,['A','B','C','D','E'])

#%%水平条状图

index=[0,1,2,3,4]
values=[5,7,3,4,6]
std1=[.8,1,.4,.9,1.3]
plt.title('A Bar Plot')
plt.barh(index,values,xerr=std1,error_kw={'ecolor':'0.1','capsize':6},alpha=.6,label="Series' name")
plt.legend(loc=5)
plt.xticks(index,['A','B','C','D','E'])

#%%多序列条状图
index=np.arange(5)
value1=[5,7,3,4,6]
value2=[6,6,4,5,7]
value3=[5,6,5,4,6]
bw=0.3
plt.title('A Multiseries Bar Chart',fontsize=20)
plt.bar(index,value1,bw,color='b')
plt.bar(index+bw,value2,bw,color='g')
plt.bar(index+2*bw,value3,bw,color='r')
plt.xticks(index+1*bw,['A','B','C','D','E'])

#%%横板
index=np.arange(5)
value1=[5,7,3,4,6]
value2=[6,6,4,5,7]
value3=[5,6,5,4,6]
bw=0.3
plt.title('A Multiseries Bar Chart',fontsize=20)
plt.barh(index,value1,bw,color='b')
plt.barh(index+bw,value2,bw,color='g')
plt.barh(index+2*bw,value3,bw,color='r')
plt.yticks(index+1*bw,['A','B','C','D','E'])

#%%为pandas DataFrame 生成多序列条状图
data={'Series1':[1,2,4,3,2],'Series2':[1,3,2,5,6],'Series3':[2,5,6,3,4]}
df=pd.DataFrame(data)
df.plot(kind='bar')
df.plot(kind='barh')

#%%多序列堆积条状图
series1=data['Series1']
series2=data['Series2']
series3=data['Series3']
index=np.arange(5)
plt.bar(index,series1,color='r')
plt.bar(index,series2,color='b',bottom=series1)
plt.bar(index,series3,color='g',bottom=(np.array(series1)+np.array(series2)))
plt.xticks(index,['jan','feb','mar','apr','jun'])

#%%
series1=data['Series1']
series2=data['Series2']
series3=data['Series3']
index=np.arange(5)
plt.barh(index,series1,color='r')
plt.barh(index,series2,color='b',left=series1)
plt.barh(index,series3,color='g',left=(np.array(series1)+np.array(series2)))
plt.yticks(index,['jan','feb','mar','apr','jun'])

#%%
series1=data['Series1']
series2=data['Series2']
series3=data['Series3']
index=np.arange(5)
plt.barh(index,series1,color='w',hatch='xx')
plt.barh(index,series2,color='w',hatch='//',left=series1)
plt.barh(index,series3,color='w',hatch='\\\\\\\\',left=(np.array(series1)+np.array(series2)))
plt.yticks(index,['jan','feb','mar','apr','jun'])

#%%用pandas Dataframe直接作图
df.plot(kind='bar',stacked=True)
df.plot(kind='barh',stacked=True)

#%%其他条状图
import matplotlib.pyplot as plt
x0=np.arange(8)
y1=np.array([1,3,4,6,4,3,2,1])
y2=np.array([1,2,5,4,3,3,2,1])
plt.ylim(-7,7)
plt.bar(x0,y1,width=0.9,facecolor='r',edgecolor='w')
plt.bar(x0,-y2,width=0.9,facecolor='b',edgecolor='w')
plt.xticks(())
plt.grid(True)
for x, y in zip(x0,y1):
    plt.text(x,y+0.5,"%d"%y,ha='center',va='bottom')
for x, y in zip(x0,-y2):
    plt.text(x,y-0.5,'%d'%y,ha='center',va='top')
    
#%%饼图
labels=['Nokia','Samsung','Apple','Lumia']
values=[10,30,45,15]
colors=['yellow','green','red','blue']
plt.pie(values,labels=labels,colors=colors)
plt.axis('equal')
#%%使得某一块剥离出来explode，并进行旋转startangle
explode=[0.2,0,0,0]
plt.pie(values,labels=labels,colors=colors,explode=explode,startangle=90)

#%%添加百分比
plt.pie(values,labels=labels,colors=colors,explode=explode,autopct='%1.1f%%',shadow=True)
plt.axis('equal')

#%%直接使用pandas DataFrame作出饼图
data={'Series1':[1,2,4,3,2],'Series2':[1,3,2,5,6],'Series3':[2,5,6,3,4]}
df=pd.DataFrame(data)

df['Series1'].plot(kind='pie',figsize=(6,6))

