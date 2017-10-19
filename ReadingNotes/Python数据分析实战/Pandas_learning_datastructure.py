# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 14:16:19 2017

@author: River
"""

#%%pandas 数据结构简介
#Series DataFrame
import numpy as np
import pandas as pd

#%%Series
s=pd.Series([12,-4,7,9])
s
s=pd.Series([12,-4,7,9],index=['a','b','c','d'])
s
s.values
s.index
s[2]
s[0:2]
s[['b','c']]
s[1]=0
s

arr=np.array([1,2,3,4])
s=pd.Series(arr)
s
s4=pd.Series(s)
s
arr[2]=-2
s
s4#注意这里的关系为引用关系。多个对象同时发生改变

s[s>8]
s
s/2
np.log(s)

#Seires对象的组成元素
serd=pd.Series([1,0,2,1,2,3],index=['white','white','blue','green','green','yellow'])
serd
serd.unique()
serd.value_counts()
serd.isin([0,3])
serd[serd.isin([0,3])]

#NaN
s2=pd.Series([5,-3,np.NaN,14])#嵌入NaN
s2
s2.isnull()
s2.notnull()

#Series作为字典
mydict={'red':2000,'blue':1000,'yellow':500,'orange':1000}
myseries=pd.Series(mydict)
myseries
colors=['red','yellow','orange','blue','green']
myseries=pd.Series(mydict,index=colors)
myseries

#Series对象之间的运算
mydict2={'red':400,'yellow':1000,'black':700}
myseries2=pd.Series(mydict2)
myseries
myseries2
myseries+myseries2

#%%DataFrame对象
data={'color':['blue','green','yellow','red','white'],
      'object':['ball','pen','pencil','paper','mug'],
        'price':[1.2,1.0,0.6,0.9,1.7]}

frame=pd.DataFrame(data)
frame
frame2=pd.DataFrame(data,columns=['object','price'])
frame2
frame2=pd.DataFrame(data,index=['one','two','three','four','five'])
frame2

frame3=pd.DataFrame(np.arange(16).reshape((4,4)),
                    index=['red','blue','yellow','white'],
                    columns=['ball','pen','pencil','paper'])
frame3

#选取元素
frame.columns
frame.index
frame.values
frame['price']
frame.price
frame.ix[2]#注意是第三行,索引为2的一行
frame.ix[[2,4]]
frame[0:2]
frame['object'][3]#object列的第4个元素，注意要先选择列再选择行

#赋值
frame.index.name='id';frame.columns.name='item'
frame

frame['new']=12
frame
frame['new']=[3.0,1.3,2.2,0.8,1.1]
frame
ser=pd.Series(np.arange(5))
frame['new']=ser
frame
frame['price'][2]=3.3
frame
data#注意data没有更改，而原data的视图进行了copy变成副本

#元素的所属关系
frame.isin([1.0,'pen'])
frame[frame.isin([1.0,'pen'])]
del frame['new']
frame

#利用嵌套字典生成DataFrame对象
nestdict={'red':{2012:22,2013:33},
          'white':{2011:13,2012:22,2013:16},
            'blue':{2011:17,2012:27,2013:18}}
frame2=pd.DataFrame(nestdict)
frame2
frame2.T

#index对象
ser=pd.Series([5,0,3,8,4],index=['red','blue','yellow','white','green'])
ser.index
ser.idxmin()
ser.idxmax()

serd=pd.Series(range(6),index=['white','white','blue','green','green','yellow'])
serd
serd['white']
serd.index.is_unique

#%%索引对象的其它功能

#更改索引
ser=pd.Series([2,5,7,4],index=['one','two','three','four'])
ser
ser.reindex(['three','two','one','five','four'])
ser3=pd.Series([1,5,6,3],index=[0,3,5,6])
ser3
ser3.reindex(range(6),method='ffill')
ser3
ser3.reindex(range(6),method='bfill')

#删除
ser=pd.Series(np.arange(4.),index=['red','blue','yellow','white'])
ser
ser.drop('blue')
ser.drop(['red','yellow'])

frame=pd.DataFrame(np.arange(16).reshape((4,4)),
                   index=['red','blue','yellow','white'],
                    columns=['ball','pen','pencil','paper'])
frame
frame.drop(['blue','yellow'])
frame.drop(['pen','pencil'],axis=1)

#算数和数据对齐
s1=pd.Series([3,2,5,1],['white','yellow','green','blue'])
s2=pd.Series([1,4,7,2,1],['white','yellow','black','blue','brown'])##索引对齐后相加
s1+s2

frame1=pd.DataFrame(np.arange(16).reshape((4,4)),
                    index=['red','blue','yellow','white'],
                    columns=['ball','pen','pencil','paper'])
frame2=pd.DataFrame(np.arange(12).reshape((4,3)),
                    index=['blue','green','white','yellow'],
                    columns=['mug','pen','ball'])
frame1+frame2#索引和列名都要对齐才相加

#%%数据结构之间的运算
frame=pd.DataFrame(np.arange(16).reshape((4,4)),
                   index=['red','blue','yellow','white'],
                    columns=['ball','pen','pencil','paper'])
frame

ser=pd.Series(np.arange(4),index=['ball','pen','pencil','paper'])
ser
frame-ser

ser['mug']=9
ser
frame-ser

#%%函数应用和映射
#通用函数
frame=pd.DataFrame(np.arange(16).reshape((4,4)),
                   index=['red','blue','yellow','white'],
                    columns=['ball','pen','pencil','paper'])
frame
np.sqrt(frame)

#按行或列执行的函数
f=lambda x:x.max()-x.min()
def f(x):
    return x.max()-x.min()

frame.apply(f)#按列操作
frame.apply(f,axis=1)#按行操作

def f(x):
    return pd.Series([x.min(),x.max()],index=['min','max'])

frame.apply(f)


#统计函数
frame.sum()
frame.mean()

frame.describe()

#%%排序和排位次
ser=pd.Series([5,0,3,8,4],index=['red','blue','yellow','white','green'])
ser
ser.sort_index()
ser.sort_index(ascending=False)


frame=pd.DataFrame(np.arange(16).reshape((4,4)),
                   index=['red','blue','yellow','white'],
                    columns=['ball','pen','pencil','paper'])

frame
frame.sort_index()
frame.sort_index(axis=1)
frame.sort_values =(['pen','pencil'])
frame


ser.rank()
ser.rank(method='first')
ser.rank(ascending=False)


#%%相关性和协方差

seq2=pd.Series([3,4,3,4,5,4,3,2],['2006','2007','2008','2009','2010','2011','2012','2013'])
seq=pd.Series([1,2,3,4,4,3,2,1],['2006','2007','2008','2009','2010','2011','2012','2013'])
seq.corr(seq2)
seq.cov(seq2)

frame2=pd.DataFrame([[1,4,3,6],[4,5,6,1],[3,3,1,5],[4,1,6,4]],
                    index=['red','blue','yellow','white'],
                    columns=['ball','pen','pencil','paper'])
frame2
frame2.corr()
frame2.cov()

ser
frame2.corrwith(ser)
frame2.corrwith(frame)

#%%NaN数据
ser=pd.Series([0,1,2,np.NaN,9],index=['red','blue','yellow','white','green'])
ser
ser['white']=None
ser

ser.dropna()
ser[ser.notnull()]

frame3=pd.DataFrame([[6,np.nan,6],[np.nan,np.nan,np.nan],[2,np.nan,5]],
                    index=['blue','green','red'],
                    columns=['ball,','mug','pen'])
frame3
frame3.dropna()
frame3.dropna(how="all")

#缺失值填充
frame3.fillna(0)
frame3.fillna({'ball':1,'mug':0,'pen':99})


#%%等级索引和分级

mser=pd.Series(np.random.rand(8),
               index=[['white','white','white','blue','blue','red','red','red'],
                      ['up','down','right','up','down','up','down','left']])
mser
mser.index

mser[:,'up']
mser['white','up']

mser.unstack()
frame3
frame3.stack()

mframe=pd.DataFrame(np.random.randn(16).reshape((4,4)),
                    index=[['white','white','red','red'],['up','down','up','down']],
                    columns=[['pen','pen','paper','paper'],[1,2,1,2]])
mframe

#重新调整顺序和为层级排序
mframe.columns.names=['bojects','id']
mframe.index.names=['colors','status']
mframe
mframe.swaplevel('colors','status')
mframe.sortlevel('colors')

#按层级进行统计
mframe.sum(level="colors")
mframe.sum(axis=1,level='id')
