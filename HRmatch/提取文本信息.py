# -*- coding: utf-8 -*-
"""
Created on Fri May 11 13:29:18 2018

@author: Liuying Wang
"""
import pandas as pd
import numpy as np
import re
import thulac
#%%
company = pd.read_pickle('pkl格式\\2017年09-12月应聘数据之企业信息_整理格式.pkl')
position = pd.read_pickle('pkl格式\\2017年09-12月应聘数据之职位信息_整理格式.pkl')
#%%
#posType = []
#for s in list(position.职位类别):
#    for term in s.split('、'):
#        if term not in posType:
#            posType.append(term)
#print(posType)

#%%
#互联网行业的公司编号
#检测
def matchForIndustry(s,industry):
    res = re.match(pattern = '(,|^)'+str(industry)+'\\d{3,3}(\\D|$)', string = s)
    if res!=None:
        return True
    else:
        return False
#取出所有互联网行业公司
ind_1 = company.loc[company.所属行业ID.apply(matchForIndustry, industry = 1)]
ind_1.公司编号.head()

#%%
#取出互联网行业公司的所有职位
csRelatedPosition = position.loc[position.公司编号.isin(ind_1.公司编号)]
segtext = csRelatedPosition.职位描述

#%%segment

segment = thulac.thulac(filt=True, rm_space=True)
seg = [segment.cut(s,text = True) for s in list(segtext)]


