# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:33:27 2018

@author: Liuying Wang
"""

import pandas as pd
import numpy as np
import re
#%%
records = pd.read_pickle('2017年09-12月应聘数据之应聘记录_整理格式.pkl')
#position = pd.read_pickle('2017年09-12月应聘数据之职位信息_整理格式.pkl')

#%%先处理records表
#删除无用的字段
unuseful = ['人才编号','职位名称','公司编号','职位类型','意向职位名称']
records.drop(unuseful,axis=1,inplace=True)
records.head()
#%%
#转换时间和数字
timeType = {'申请时间':'datetime64[ns]',
            '企业查看简历时间':'datetime64[ns]',
            '企业通知简历时间':'datetime64[ns]',
            '应聘次数':'int','身高':'int',
            '居住地ID':'int'}
records.应聘次数.replace('',-1,inplace=True)
records.身高.replace('',-1,inplace=True)
records.居住地ID.replace('','0',inplace=True)

records = records.astype(timeType)
records.dtypes

#%%处理工作经验和月薪——提取出数字
expYear=[]
for s in records.工作经验.tolist():
    match = re.match(r'^(\d+)年工作经验',string=s)
    if match!=None:
        expYear.append(match.groups(0)[0])
    else:
        expYear.append('0')
        
records.工作经验=pd.Series(expYear).astype('int')
#%%处理目前月薪
nowWagelow=[]
nowWagehigh=[]
for w in records.目前月薪.tolist():
    match = re.match(r'(^(\d+)-(\d+)$)|(^(\d+))',string=w)
    if match!=None:
        if match.groups()[1]!=None:
            nowWagelow.append(match.groups()[1])
            nowWagehigh.append(match.groups()[2])
        elif match.groups()[3]!=None:
            nowWagelow.append(match.groups()[3])
            nowWagehigh.append(match.groups()[3])
        else:
            pass
    else:
        nowWagelow.append('0')
        nowWagehigh.append('0')
        
del records['目前月薪']
records['目前月薪下界']=pd.Series(nowWagelow).astype('int')
records['目前月薪上界']=pd.Series(nowWagehigh).astype('int')
#%%处理意向月薪
expWagelow=[]
expWagehigh=[]
for w in records.意向薪资.tolist():
    match = re.match(r'(^(\d+)-(\d+)$)|(^(\d+))',string=w)
    if match!=None:
        if match.groups()[1]!=None:
            expWagelow.append(match.groups()[1])
            expWagehigh.append(match.groups()[2])
        elif match.groups()[3]!=None:
            expWagelow.append(match.groups()[3])
            expWagehigh.append(match.groups()[3])
        else:
            pass
    else:
        expWagelow.append('0')
        expWagehigh.append('0')
        
del records['意向薪资']
records['意向薪资下界']=pd.Series(expWagelow).astype('int')
records['意向薪资上界']=pd.Series(expWagehigh).astype('int')

#%%提取教育背景->学校+专业
school=[]
major=[]
for s in records.教育背景.tolist():
    match = re.match(r'(^(\w*);@;.+;@;(\w*)$)',string=s)
    if match!=None:
        if match.groups()[1]!=None:
            school.append(match.groups()[1])
            major.append(match.groups()[2])
        else:
            pass
    else:
        school.append('无')
        major.append('无')

del records['教育背景']
records['学校']=pd.Series(school)
records['专业']=pd.Series(major)
#%%提取户籍地
def formCitiesList(alist,split,replace):
    cities = alist.split(split)
    cities = pd.Series(cities)
    cities = cities.str.replace(replace,'').tolist()
    cities = '|'.join(cities)
    return '('+cities+')'
prov = '北京市，天津市，上海市，重庆市，河北省，山西省，辽宁省，吉林省，黑龙江省，江苏省，浙江省，安徽省，福建省，江西省，山东省，河南省，湖北省，湖南省，广东省，海南省，四川省，贵州省，云南省，陕西省，甘肃省，青海省，台湾省，内蒙古自治区，广西壮族自治区，西藏自治区，宁夏回族自治区，新疆维吾尔自治区，香港特别行政区，澳门特别行政区'
replace='市|省|(自治区)|(壮族自治区)|(回族自治区)|(维吾尔自治区)|(特别行政区)'
prov = formCitiesList(prov,'，',replace)
hometown = records.户籍地
province = hometown.str.extract('^'+prov,expand=False)

cities = '厦门市、福州市、泉州市、莆田市、漳州市、宁德市、南平市、三明市、龙岩市'
replace = '市'
cities = formCitiesList(cities,'、',replace)
city = hometown.str.replace('^\w+省','').str.extract(cities,expand=False)

dist = '思明、湖里、集美、海沧、同安、翔安'
dist = formCitiesList(dist,'、','')
distinct = hometown.str.replace('^\w+省','').str.replace('(\w+市)','').str.extract(dist,expand=False)

del records['户籍地'],hometown
records['户籍地省份'] = province
records['户籍地市'] = city
records['户籍地区'] = distinct

#%%地点ID
file = open('应聘数据之地点字典.csv')
locationMapping = pd.read_csv(file).iloc[:,:2]
locationMapping.ID=locationMapping.ID.astype('str')
mappingdict = dict(locationMapping.set_index('ID').NAME_CN)
records.居住地ID=records.居住地ID.map(mappingdict)
#%%意向职位名称和意向工作地点(是否匹配)
# 需要连接职位信息后进行提取

#%%其它
records.学历 = records.学历.replace('','无',inplace=True)
#%%
#文本包括 IT技能 其它意向要求 培训经历 外语能力 自我评价
#%%再创建一个用户信息吧，不然好多重复呀
userscolumns = ['人才标识码','参加工作时间', '婚姻状况', '性别', '身高', '视力', '学历', 'IT技能', '工作经验', '居住地ID', '职称',
       '供职情况', '是否有照片', '培训经历', '外语能力', '意向工作地点ID', '意向行业ID', '意向职位名称',
       '其他意向要求', '中文简历是否完整', '英文简历是否完整', '工作经历是否完整', '教育背景是否完整', '自我评价',
       '目前月薪下界', '目前月薪上界', '意向薪资下界', '意向薪资上界', '学校', '专业', '户籍地省份', '户籍地市',
       '户籍地区']

users = records[userscolumns]
users.drop_duplicates(subset = '人才标识码',inplace=True)


#%%
users.columns
document=[]
for user in range(users.shape[0]):
    nowU = users.iloc[user][['IT技能','其他意向要求','培训经历','外语能力','自我评价']].tolist()
    document.append('  '.join(nowU))
    
document
users['文本信息']=document
users.drop(['IT技能','其他意向要求','培训经历','外语能力','自我评价'], axis=1,inplace = True)


users.to_pickle('userInfo.pkl')
users.to_csv('userInfo.csv',encoding='UTF-8')
#%%保存/读取

records.to_pickle('records.pkl')
records=pd.read_pickle('records.pkl')
