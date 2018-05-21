# -*- coding: utf-8 -*-
"""
Created on Sun May 20 15:38:49 2018
构造人才-岗位矩阵
@author: Liuying Wang
"""
from scipy import sparse
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
