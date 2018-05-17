# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:30:34 2018

@author: Liuying Wang
"""
from scipy import sparse
import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer, scale
from sklearn.cluster import MiniBatchKMeans
from sklearn.externals import joblib
from scipy import sparse, ma, stats
import scipy.sparse.linalg as slinalg
import scipy.spatial.distance as distance
#import pdb  
#%%
class RecommendMovie():
    remarks = None
    randomSeed = None
    kmeansClf = None
    numU = None #用户数
    numM = None #电影数
    userGroup = None #用于记录所有用户的类别
    userNeighSize = 100
    movieNeighSize = 10
    reductSize = 50
    zeroImputer = None
    movieTitle = None
    
    #一些公用参数的初始化
    def __init__(self, sparseMatrix_file, movieTitle, randomSeed = None):
        self.remarks = sparse.load_npz(sparseMatrix_file)
        self.remarks = self.remarks.tocsr()
        self.randomSeed = randomSeed
        self.numU,self.numM = self.remarks.shape
        self.movieTitle = movieTitle    
        
    #修改协同过滤参数
    def tunningCollParams(self, userNeighSize, movieNeighSize, reductSize):
        self.userNeighSize = userNeighSize
        self.movieNeighSize = movieNeighSize
        self.reductSize = reductSize
        
    #初始化kmeans模型
    def createKMeans(self, n_clusters,max_iter):
        self.kmeansClf = MiniBatchKMeans(n_clusters= n_clusters, max_iter = max_iter, random_state=self.randomSeed)
        
    #训练kmeans模型
    def fitKMeans(self, trainsetsize, modelSavePath=None):  
        #抽取训练kmeans所用的集合
        np.random.seed(self.randomSeed)
        trainset_dense = self.remarks[np.random.choice(np.arange(self.numU), size = trainsetsize)].toarray()
        #平均值填补missing和用户（按行）标准化
        self.zeroImputer = Imputer(missing_values=0, strategy='mean', axis=1, copy = False)
        trainset_dense = self.zeroImputer.fit_transform(trainset_dense)
        trainset_dense = scale(X=trainset_dense, axis=1)
        self.kmeansClf.fit(trainset_dense)
        if modelSavePath!=None:
            joblib.dump(self.kmeansClf, filename=modelSavePath)
    
   # def updateKMeans(self, updatesetsize, modelSavePath=None)
   
    #给定一个稀疏矩阵，预测所属类别
    def __predictGroup(self, sparseArr):
        denseArr = self.zeroImputer.fit_transform(sparseArr.toarray())
        denseArr = scale(denseArr, axis=1)
        return self.kmeansClf.predict(denseArr)
    
    #预测所有用户所属的类别
    def findUsersGroup(self):
        userGroup = np.array([])
        for i in range(int(self.numU/10000)):
            temp = self.__predictGroup(self.remarks[(i*10000):((i+1)*10000)])
            userGroup = np.hstack([userGroup, temp])
        temp = self.__predictGroup(self.remarks[((i+1)*10000):])
        self.userGroup = np.hstack([userGroup,temp])
        print(self.userGroup, len(self.userGroup))
        print(pd.Series(self.userGroup).value_counts())
    
    #标准化单个用户的评分
    def __userRemarkScaler(self, aUser):
        tempaUser = self.zeroImputer.fit_transform(aUser.toarray())
        return scale(tempaUser,axis = 1).flatten()
    
    #找出同类成员并抽取子样
    def __findNeigbor(self, aUser, neighborsize=1000):
        g = self.__predictGroup(aUser)[0]
        np.random.seed(self.randomSeed)
        gindex = np.random.choice(np.where(self.userGroup==g)[0],size=neighborsize)
        groupMember = self.remarks[gindex].toarray()
        groupMember = self.zeroImputer.fit_transform(groupMember)
        groupMember = scale(groupMember, axis=1)
        return groupMember,gindex
    
    #按照pearson correlation遴选用户近邻
    def __pearsonRNeigh(self, aUser):
        groupMember, gindex = self.__findNeigbor(aUser,neighborsize=self.userNeighSize*10)
        pearsonDis = np.zeros(shape=self.userNeighSize*10)
        tempaUser = self.__userRemarkScaler(aUser)
        for i in range(self.userNeighSize*10):
            pearsonDis[i] = stats.pearsonr(tempaUser.flatten(),groupMember[i])[0]
        cutpoint = np.percentile(pearsonDis,90)
        maxindex = np.where(pearsonDis>=cutpoint)
        return groupMember[maxindex], gindex[maxindex]

    #给定 用户近邻-子矩阵和目标电影ID，计算电影间距离
    def __getScoreAndDist(self, movieindex, subRemarkMat, ratedIndex):
        u,s,vt = slinalg.svds(subRemarkMat, k=self.reductSize, which='LM')
        movieScore = vt.transpose()[movieindex,:].reshape(1,-1)
        dist = np.array([distance.cosine(movieScore, vt.transpose()[i]) for i in list(ratedIndex)])
        return dist
    
    #给定 电影间距离 计算用户对某电影的评分
    def __scorePredict(self, aUser, dist, ratedIndex):
        distRated = dist
        distSort = np.argsort(distRated)[1:min(self.movieNeighSize+1,len(distRated))]
        userSort = ratedIndex[distSort]
        similarity = 1-(dist[distSort])
        similarity[similarity<0]=0
        userRemarkP = (aUser.toarray()[0][userSort].dot(similarity.reshape(-1,1)))/(np.sum(similarity)+0.001)
        return userRemarkP

    #给定用户ID&电影ID预测得分    
    def __user2Movie(self, userID, movieID,subRemarkMat, gindex, ratedIndex):
        #aUser = self.remarks[userID]
        #subRemarkMat,gindex = self.__pearsonRNeigh(aUser)
        dist = self.__getScoreAndDist(movieID, subRemarkMat, ratedIndex)
        #ratedIndex = np.where(aUser[0].toarray().flatten()!=0)[0]#等会写到外层去
        score = self.__scorePredict(self.remarks[userID], dist, ratedIndex)
        return score
    
    #给定用户ID预测对候选电影的评分
    def recommend2User(self, userID, toPredict):
        #toPredict=a list of movieID
        aUser = self.remarks[userID]
        subRemarkMat,gindex = self.__pearsonRNeigh(aUser)
        ratedIndex=np.where(self.remarks[userID].toarray().flatten()!=0)[0]
        movieScoreP = []
        for movieID in toPredict:
            movieScoreP.append(self.__user2Movie(userID, movieID,subRemarkMat,gindex,ratedIndex))
        movieRecommend = pd.DataFrame(index=toPredict, 
                                   data={'Movie Title':self.movieTitle[toPredict],
                                         'Estimate':movieScoreP})
        movieRecommend.sort_values(by='Estimate', ascending=False, inplace=True)
        return movieRecommend
    
        


#%%调试代码
        
#titles = pd.read_pickle('titles.pkl')
#test = RecommendMovie('remarks_nonzero.npz', movieTitle=titles, randomSeed=6646)
#test.createKMeans(10,10000)
#test.fitKMeans(20000)
#test.findUsersGroup()
#test.tunningCollParams(100,5,50)
#test.recommend2User(0,list(range(100)))

#testmatrix = sparse.load_npz('remarks_nonzero.npz')[:,1000:1100]
#nonzero = np.unique(testmatrix.nonzero()[0])
#testmatrix = testmatrix[nonzero]
#sparse.save_npz('testmatrix.npz',testmatrix)

#%%读title
#title = pd.read_csv('titile.csv', titles)
#titles1 = title.iloc[:,2]
#titles2 = title.iloc[:,3].dropna()
#for i in titles2.index:
#    titles1[i] = titles1[i]+titles2[i]
#print(titles1)
#titles1.to_pickle('titles.pkl')

