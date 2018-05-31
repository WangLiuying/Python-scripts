# -*- coding: utf-8 -*-
"""
Created on Sun May 20 15:38:49 2018
构造人才-岗位矩阵
切分数据集
@author: Liuying Wang
"""
from scipy import sparseb
import pandas as pd
import numpy as np
#%%
records = pd.read_pickle('2017年09-12月应聘数据之应聘记录_整理格式.pkl')
position = pd.read_pickle('2017年09-12月应聘数据之职位信息_整理格式.pkl')
persons = pd.Series(records.人才标识码.unique())
UID = pd.Series(records.人才标识码.unique())
PID = pd.Series(position.职位编号.unique())

#%%toy test
#testRS = records.iloc[:500,1:3]
#testUID = pd.Series(testRS.人才标识码.unique())
#testPID = pd.Series(testRS.应聘职位编号.unique())
#UPmat = sparse.dok_matrix((26,472), dtype = np.int8)
#
#for row in range(testRS.shape[0]):
#    User = testRS.iloc[row,0]
#    Pos = testRS.iloc[row,1]
#    UserID = np.where(testUID==User)[0]
#    PosID = np.where(testPID==Pos)[0]
#    UPmat[UserID,PosID] = 1

#%%
def formUPmat(RecordSet):
    """
    参数：
    RecordSet=记录表由两列组成，第一列为UserID，第二列为职位ID
    返回值:
    一个用户-职位稀疏矩阵，
    一个UserID映射表
    一个职位ID映射表
    """
    UID = pd.Series(RecordSet.人才标识码.unique())
    PID = pd.Series(RecordSet.应聘职位编号.unique())
    UPmat = sparse.dok_matrix((len(UID),len(PID)), dtype = np.int8) 
    for row in range(RecordSet.shape[0]):
        User = RecordSet.iloc[row,0]
        Pos = RecordSet.iloc[row,1]
        UserID = np.where(UID==User)[0]
        PosID = np.where(PID==Pos)[0]
        UPmat[UserID,PosID] = 1   
        if row%1000==0:
           print('completed row'+str(row)+'\n')
    print(UPmat)
    return UPmat.tocoo(),UID,PID

#%%
UPmat,UID,PID = formUPmat(records.iloc[:,1:3])
sparse.save_npz(file = 'User-Position.npz',matrix=UPmat)
UID.to_pickle('UserID.pkl')
PID.to_pickle('PositionID.pkl')


#%%Split test and train
#切分10分之一的记录作为测试集
#总计共有1474340条记录因此抽取 147434条作为测试集
N = 1474340
np.random.seed(123)
testIndex = np.random.choice(range(int(N)),size=int(N/10),replace=False)
testIndex = (UPmat.nonzero()[0][testIndex],UPmat.nonzero()[1][testIndex])
trainset = UPmat.copy().todok()
trainset[testIndex[0],testIndex[1]]=0
sparse.save_npz(file='training.npz',matrix=trainset.tocoo())
pd.to_pickle(testIndex,path='testIndex.pkl')

#%%
UPmat = sparse.load_npz('User-Position.npz')
UPmat=UPmat.todok()
PosHist = UPmat.sum(0)
UserHist = UPmat.sum(1)
PosHist = np.squeeze(np.asarray(PosHist))
UserHist = np.squeeze(np.asarray(UserHist))
#%%
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rcParams#默认参数
plt.rcParams['axes.prop_cycle']

plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

_,ax = plt.subplots()
plt.hist(UserHist,bins=100)
ax.set_xlim(0,150)
plt.title('单人投递简历数直方图')
plt.show()
UPmat
