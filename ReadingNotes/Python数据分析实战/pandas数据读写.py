# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 18:56:53 2017

@author: River

python数据分析实战 第五章 pandas：数据读写
"""

"""
read_* to_*
其中*可以通配：
csv excel hdf sql json html stat clipboard pickle msgpack gbq
"""
import pandas as pd
import numpy as np
#%%csv and txt 读取
#read_csv read_table to_csv

csvframe=pd.read_csv('myCSV_01.csv')
csvframe
pd.read_table('myCSV_01.csv',sep=',')

pd.read_csv('myCSV_02.csv')#error
pd.read_csv('myCSV_02.csv',header=None)

pd.read_csv('myCSV_02.csv',names=['white','red','blue','green','animal'])#直接另赋列名

pd.read_csv('myCSV_03.csv',index_col=['color','status'])            

pd.read_table('ch05_04.txt',sep='\s*') #sep部分用了正则表达式

pd.read_table('ch05_05.txt',header=None,sep='\D+')

#跳过前五行使用参数 skiprows=5,跳过第五行使用 skiprows=[5]

pd.read_table('ch05_06.txt',sep=',',skiprows=[0,1,3,6])

#使用skiprows和nrows结合，仅读取一部分
pd.read_csv('myCSV_02.csv',skiprows=[2],nrows=3,header=None)


out=pd.Series()
pieces=pd.read_csv('myCSV_01.csv',chunksize=3)
i=0
for piece in pieces:
    out.set_value(i,piece['white'].sum())
    i += 1
out

#%% csv and txt 写入

frame2=pd.DataFrame(np.arange(16).reshape((4,4)),
                    columns=['ball','pen','pencil','paper'])
frame2
frame2.to_csv('ch05_07.csv')
frame2.to_csv('ch05_07.csv',index=False)


#%%读写HTML文件

#核心函数： read_html to_html

#写入
frame=pd.DataFrame(np.arange(4).reshape((2,2)))
frame
print(frame.to_html())

frame=pd.DataFrame(np.random.random((4,4)),
                   index=['white','black','red','blue'],
                    columns=['up','down','right','left'])
frame

s=['<HTML>']
s.append('<HEAD><TITLE>My DataFrame</TITLE></HEAD>')
s.append('<BODY>')
s.append(frame.to_html())
s.append('</BODY>')
s.append('</HTML>')
print(s)
html=''.join(s)
print(html)
html_file=open('myFrame.html','w')
html_file.write(html)
html_file.close()

#读取
web_frame=pd.read_html('myFrame.html')
web_frame[0]

#也可以直接读取网页
ranking=pd.read_html('http://www.meccanismocomplesso.org/en/meccanismo-complesso-sito-2/classifica-punteggio/')
ranking[0]

#%%处理xml格式
from lxml import objectify

xml=objectify.parse('books.xml')
xml
root=xml.getroot()
root.Book.Author
root.Book.PublishDate

root.getchildren()
[child.tag for child in root.Book.getchildren()]
[child.text for child in root.Book.getchildren()]
#%%
def etree2df(root):
    
    column_names=[]
    for i in range(0,len(root.getchildren()[0].getchildren())):
        column_names.append(root.getchildren()[0].getchildren()[i].tag)
    xml_frame=pd.DataFrame(columns=column_names)
    
    for j in range(0,len(root.getchildren())):
        obj=root.getchildren()[j].getchildren()
        texts=[]
        for k in range(0,len(column_names)):
            texts.append(obj[k].text)
        row=dict(zip(column_names,texts))
        
        row_s=pd.Series(row)
        row_s.name=j
        xml_frame=xml_frame.append(row_s)
    return xml_frame
        
#%%
etree2df(root)


#%%读写microsoft excel文件

pd.read_excel('data.xlsx')
pd.read_excel('data.xlsx','Sheet2')
pd.read_excel('data.xlsx',1)

frame=pd.DataFrame(np.random.random((4,4)),
                   index=['exp1','exp2','exp3','exp4'],
                    columns=['jan2015','feb2015','mar2015','apr2015'])

frame
frame.to_excel('data.xlsx',sheet_name='new')

#%%JSON数据处理
import pandas.io.json
frame
frame.to_json('frame.json')

pd.read_json('books.json')

file=open("books.json","r")
text=file.read()
text
text=json.loads(text)
pd.io.json.json_normalize(text,record_path="books")
pd.io.json.json_normalize(text,record_path="books",meta=['writer','nationality'])


#%%HDF5

from pandas.io.pytables import HDFStore

frame=pd.DataFrame(np.arange(16).reshape((4,4)),
                   index=['white','black','red','blue'],
                    columns=['up','down','right','left'])

store=HDFStore('mydata.h5')
store['obj1']=frame
frame2=pd.DataFrame(np.random.random((4,4)),
                   index=['white','black','red','blue'],
                    columns=['up','down','right','left'])
store['obj2']=frame2
store
store['obj2']


#%%cPickle

import pickle

data={'color':['white','black'],'value':[5,7]}
pickled_data=pickle.dumps(data)
print(pickled_data)
pickle.loads(pickled_data)


frame=pd.DataFrame(np.arange(16).reshape((4,4)),
                   index=['white','black','red','blue'],
                    columns=['up','down','right','left'])
frame.to_pickle('frame.pkl')
pd.read_pickle('frame.pkl')
