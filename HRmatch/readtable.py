# -*- coding: utf-8 -*-
"""
阅读、整理。
重新整理职位信息数据，形成dataFrame格式

Created on Sat Mar 31 11:25:35 2018

@author: Liuying Wang
"""
import os
import pandas as pd
import re
#%%
def checkWhatVariable(filename):
    with open(filename,encoding = 'gb18030') as file:
        variables = file.readlines(1)
        print(variables)
#%%      
files = os.listdir()
for filename in files:
    print(filename+':')
    checkWhatVariable(filename)
#%%
file = open('2017年09-12月应聘数据之职位信息.csv',encoding = 'gb18030')
for i in range(10):
    print(file.readlines(1))
file.close()

#%%
files = ['2017年09-12月应聘数据之企业信息.csv',
 '2017年09-12月应聘数据之工作经历.csv',
 '2017年09-12月应聘数据之应聘记录.csv',
 '2017年09-12月应聘数据之职位信息.csv',
 '2017年09-12月应聘数据之证书信息.csv',
 '2017年09-12月应聘数据之附加信息.csv']

#%%断开句子

def collectTerms(filename):
    file = open(filename,encoding = 'gb18030')
    merge = "".join(file.readlines()) 
    collection = re.split('","|"\\n"',string = merge)
    file.close()
    return collection
    
#%%
#positionInfo = collectTerms('2017年09-12月应聘数据之职位信息.csv')
#len(positionInfo)
#for term in positionInfo[:50]:
#    print(term)
#%%去掉无用符号
def rmComma(termlist):
    for term in range(len(termlist)):
        termlist[term] = re.sub('^"',repl = "", string = termlist[term])
        termlist[term] = re.sub('"$',repl = "", string = termlist[term])
        termlist[term] = re.sub(r'\n',repl = "", string = termlist[term])
    
#rmComma(positionInfo)
#%%
#samples = [positionInfo[i:(i+19)] for i in range(0,len(positionInfo),19)]
#field = samples.pop(0)
#%%
df = pd.DataFrame(data = samples, columns = field)
df.head()
df.columns
df.职位编号
df.薪资类型
df.describe()
df.to_pickle('职位信息.pkl')

#%%批量处理
for filename in files:
    with open(filename) as nowfile:
        aline = nowfile.readline()
        aline = aline.split(r'","')
        s = len(aline)
    dataReadlines = collectTerms(filename)
    rmComma(dataReadlines)
    samples = [dataReadlines[i:(i+s)] for i in range(0,len(dataReadlines),s)]
    field = samples.pop(0)
    df = pd.DataFrame(data = samples,columns = field)
    print(df.head())
    print(df.columns)
    df.to_pickle(filename.split('.')[0]+'_整理格式.pkl')

#%%


#%%
indust = open('应聘数据之行业字典.csv')
indust = pd.read_csv(indust)
indust.to_pickle('应聘数据之行业字典.pkl')

location = open('应聘数据之地点字典.csv')
location = pd.read_csv(location)
location.to_pickle('应聘数据之地点字典.pkl')
    
