# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 21:44:04 2017

@author: River

Python数据分析实战 深入pandas：数据处理
"""

#数据准备截断包括一下步骤
#加载 组装（合并 拼接 组合） 变形（轴向旋转） 删除

#本章核心：
#合并：pandas.merge 实现了不同的join操作
#拼接:pandas.concat 按照轴把多个对象拼接起来
#结合:pandas.DataFrame.combine_first 从拎一个数据结构获取数据，连接重合的数据，以填充缺失值


#%%合并
import numpy as np
import pandas as pd
frame1=pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],
                    'price':[12.33,11.44,33.21,13.23,33.62]})
frame2=pd.DataFrame({'id':['pencil','pencil','ball','pen'],
                     'color':['white','red','red','black']})
frame1
frame2
pd.merge(frame1,frame2,how='inner')


#%%
frame1=pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],
                    'color':['white','red','red','black','green'],
                    'brand':['OMG','ABC','ABC','POD','POD']})
frame2=pd.DataFrame({'id':['pencil','pencil','ball','pen'],
                     'brand':['OMG','POD','ABC','POD']})
pd.merge(frame1,frame2,on='id')
pd.merge(frame1,frame2,on='brand')

frame2.columns=['brand','sid']
pd.merge(frame1,frame2,left_on='id',right_on='sid')

frame2.columns=['brand','id']
pd.merge(frame1,frame2,on='id',how='inner')
pd.merge(frame1,frame2,on='id',how='outer')
pd.merge(frame1,frame2,on='id',how='left')

pd.merge(frame1,frame2,on=['id','brand'],how='outer')

#以索引为基准进行合并
pd.merge(frame1,frame2,right_index=True,left_index=True)
frame1.join(frame2)#error:同名列。重命名列后可以进行合并。

#%%拼接

#numpy中的拼接
array1=np.array([[0,1,2],[2,3,4],[3,4,5]])
array2=np.array([[9,8,7],[8,7,6],[7,6,5]])
np.concatenate((array1,array2),axis=1)
np.concatenate((array1,array2),axis=0)


#pandas中的拼接
ser1=pd.Series(np.random.rand(4),index=[1,2,3,4])
ser2=pd.Series(np.random.rand(4),index=[5,6,7,8])
pd.concat((ser1,ser2))
pd.concat((ser1,ser2),axis=1)
pd.concat((ser1,ser2),axis=1,join='inner')

#想要识别被拼接部分的来源，需要用keys参数
pd.concat((ser1,ser2),keys=[1,2])

#dataframe也可以一样拼接

frame1=pd.DataFrame(np.random.rand(9).reshape(3,3),index=[1,2,3])
frame2=pd.DataFrame(np.random.rand(9).reshape(3,3),index=[4,5,6])

pd.concat((frame1,frame2))
pd.concat((frame1,frame2),axis=1)

#%%组合
ser1=pd.Series(np.random.rand(5),index=[1,2,3,4,5])
ser2=pd.Series(np.random.rand(4),index=[2,4,5,6])
ser1.combine_first(ser2)#ser1中没有的用ser2中有的来补，ser1中有的不改变
ser2.combine_first(ser1)

#%%轴向旋转
frame1=pd.DataFrame(np.arange(9).reshape(3,3),
                    index=['white','black','red'],
                    columns=['ball','pen','pencil'])
frame1
frame1.stack()
frame1.stack(0)
ser5=frame1.stack()
ser5=ser5.swaplevel().sortlevel()
ser5.unstack()
ser5.unstack(level=0)

#%%长格式与宽格式

longframe=pd.DataFrame({'color':['white','white','white','red','red','red','black','black','black'],
                       'item':['ball','pen','mug','ball','pen','mug','ball','pen','mug'],
                        'value':np.random.rand(9)})

longframe
wideframe=longframe.pivot(index='color',columns='item',values='value')
wideframe

#%%删除
frame1=pd.DataFrame(np.arange(9).reshape(3,3),
                    index=['white','black','red'],
                    columns=['ball','pen','pencil'])
#删除一列
del frame1['ball']
frame1
#删除一行
frame1.drop('white')

#%%数据转换

dframe=pd.DataFrame({'color':['white','white','red','red','white'],
                     'value':[2,1,3,3,2]})
dframe

#检查重复项
dframe.duplicated()
dframe[dframe.duplicated()]
dframe.drop_duplicates()


#%%映射
map={'label1':'value1',
     'label2':'value2'}
     
#用映射替换元素

frame=pd.DataFrame({'item':['ball','mug','pen','pencil','ashtray'],
                    'color':['white','rosso','verde','black','yellow'],
                    'price':[5.56,4.20,1.30,0.56,2.75]})
frame
newcolors={'rosso':'red',
           'verde':'green'}
frame.replace(newcolors)

ser=pd.Series([1,3,np.nan,4,6,np.nan,3])
ser
ser.replace(np.nan,0)

#用映射添加元素
frame=pd.DataFrame({'item':['ball','mug','pen','pencil','ashtray'],
                    'color':['white','red','green','black','yellow']})
frame
price={'ball':5.56,'mug':4.20,'bottle':1.30,'scissors':3.41,
       'pen':1.30,'pencil':0.56,'ashtray':2.75}
frame['price']=frame['item'].map(price)
frame

#重命名轴索引
reindex={0:'first',
         1:'secone',
         2:'third',
         3:'fourth',
         4:'fifth'}
frame.rename(reindex)

recolumn={'item':'object',
          'price':'value'}
          
frame.rename(index=reindex,columns=recolumn)

frame.rename(index={1:'first'},columns={'item':'object'})

#%%离散化和面元划分
frame.rename(columns={'item':'object'},inplace=True)
frame
bins=[0,25,50,75,100]
results=np.random.rand(100)*100
cat=pd.cut(results,bins)
cat

cat.categories
cat.labels

pd.value_counts(cat)

bin_names=['unlikely','less likely','likely','highly likely']
pd.cut(results,bins,labels=bin_names)
pd.cut(results,5) #传入单个数则会分为切分5次

quintiles=pd.cut(results,5)
quintiles
pd.value_counts(quintiles)


#%%异常值检测和过滤
randframe=pd.DataFrame(np.random.randn(1000,3))
randframe.describe()

randframe.std()
randframe[(np.abs(randframe)>3*randframe.std()).any(1)]
          
nframe=pd.DataFrame(np.arange(25).reshape(5,5))
new_order=np.random.permutation(5)
new_order
nframe.take(new_order)


#随机取样
sample=np.random.randint(0,len(nframe),size=3)
sample
nframe.take(sample)



#%%字符窜处理
text='16 Bolton Avenue, Boston'
text.split('.')
[s.strip() for s in text.split(',')]
address, city = [s.strip() for s in text.split(',')]
address
city
address + ', '+city
#join拼接
strings=['A+','A','A-','B','BB','BBB','C+']
';'.join(strings)
#查找子串
'Boston' in text
text.index('Boston')
text.find('Boston')
text.index('New York')
text.find('New York')

text.count('e')
text.count('Avenue')

text.replace('Avenue','Street')
text.replace('e','E',1)


#%%正则表达式
import re

text='This is      an\t odd \n text!'
print(text)
re.split('\s+',text)

#其内部机制
regex=re.compile('\s+')
regex.split(text)

text='This is my address: 16 Bolton Avenue, Boston'
re.findall('A\w+',text)
re.findall('[A,a]\w+',text)

search=re.search('[A,a]\w+',text)
search.start()
search.end()

text[search.start():search.end()]

re.match('[A,a]\w+',text)
re.match('T\w+',text)

#%%数据聚合
"""Group by 的内部机制
split-apply-combine
分组：通常通过索引或某一列元素（键）来实现
用函数处理：对每一组运用函数
合并：将处理结果汇集到一起
"""
frame=pd.DataFrame({'color':['white','red','green','red','green'],
                    'object':['pen','pencil','pencil','ashtray','pen'],
                    'price1':[5.56,4.10,1.30,0.56,2.75],
                    'price2':[4.75,4.12,1.60,0.75,3.15]})
frame
#分组
group=frame['price1'].groupby(frame['color'])
group
group.groups
#处理、合并
group.mean()
group.sum()

#%%等级分组
group=frame['price1'].groupby([frame['color'],frame['object']])
group.groups
group.mean()
frame[['price1','price2']].groupby([frame['color']]).mean()
frame.groupby(frame['color']).mean()

#%%组迭代
for name,group in frame.groupby('color'):
    print(name)
    print(group)

#%%高级数据聚合
#链式转换
result1=frame['price1'].groupby(frame['color']).mean()
type(result1)
result2=frame.groupby(frame['color']).mean()
type(result2)

frame['price1'].groupby(frame['color']).mean()
frame.groupby(frame['color'])['price1'].mean()

frame.groupby(frame['color']).mean()['price1']

means=frame.groupby('color').mean().add_prefix('mean.')
means

#分组函数
group=frame.groupby('color')
group['price1'].quantile(0.6)
def range(series):
    return series.max()-series.min()
    
group['price1'].agg(range)#将自定义函数传给agg
group.agg(range)
group['price1'].agg(['mean','std',range])

#%%高级聚合函数
#transform和apply

frame=pd.DataFrame({'color':['white','red','green','red','green'],
                    'price1':[5.56,4.10,1.30,0.56,2.75],
                    'price2':[4.75,4.12,1.60,0.75,3.15]})
frame
sums=frame.groupby('color').sum().add_prefix('tot.')
sums
pd.merge(frame,sums,left_on='color',right_index=True)
frame.groupby('color').transform(np.sum).add_prefix('tot.')


frame=pd.DataFrame({'color':['white','black','white','white','black','black'],
                    'status':['up','up','down','down','down','up'],
                    'value1':[12.33,14.44,22.34,27.84,23.40,18.33],
                    'value2':[34.11,23.44,24.13,24.52,34.11,23.13]})
frame
frame.groupby(['color','status']).apply( lambda x: x.max())


#%%时间序列

temp=pd.date_range('1/1/2015',periods=10,freq='H')
temp
timeseries=pd.Series(np.random.rand(10),index=temp)
timeseries

timetable=pd.DataFrame({'date':temp,'value1':np.random.rand(10),
                     'value2':np.random.rand(10)})
timetable
timetable['cat']=['up','down','left','left','up','up','down','right','right','up']
timetable
