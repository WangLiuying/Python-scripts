# -*- coding: utf-8 -*-
"""
SVM

Created on Sun Mar 18 18:23:39 2018

@author: Liuying Wang
"""
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.setrecursionlimit(10000)
#%%testdata
def dataGene():
    #pdb.set_trace()
    X1 = np.random.multivariate_normal(mean = [0.,0.],
                                   cov = [[1.,0.],[0.,1.]],size = 10)
    X2 = np.random.multivariate_normal(mean = [2.,0.],
                                   cov = [[1.,.5],[.5,1.]],size = 10)
    #X3 = np.random.multivariate_normal(mean = [1.,2.],
    #                               cov = [[1.,0],[0.,1.]],size = 10)
    X = np.r_[X1,X2]
    Y = np.array([1]*10+[-1]*10)
    return X,Y

X,Y = dataGene()
plt.scatter(X[:,0],X[:,1],c = ['r']*10+['b']*10)

#%%class SVMclassifier
class SVMclassifier:
    X = None
    Y = None
    kernelProduct = None
    sampleScore = None
    alpha = None
    b = None
    C = None
    kernel = None
    __Escore = None
    sigma = 1
    N = None
    
    def __init__(self,C,kernel,sigma=None):
        self.C = C
        self.kernel = kernel
        self.sigma = sigma
    
    #线性核
    def __linearKernel(self,x1,x2):
        return (x1*x2).sum()
    #高斯核
    def __gaussianKernel(self,x1,x2,sigma):
        return np.exp(-((x1-x2)**2).sum()/(2*(sigma**2)))   
    #计算核内积
    def __computekernelProduct(self,kernelfunction,sigma = None):
        N = self.X.shape[0]
        self.kernelProduct = np.zeros(shape = [N,N])    
        if kernelfunction=='linear':
            for i in range(N):
                for j in range(N):
                    self.kernelProduct[i,j] = self.__linearKernel(self.X[i],self.X[j])
        elif kernelfunction=='gaussian':
            for i in range(N):
                for j in range(N):
                    self.kernelProduct[i,j] = self.__gaussianKernel(self.X[i],self.X[j],sigma)
        else:
            raise AttributeError('no this kernel imposed')
    
    #计算样本得分
    def __computeSampleScore(self):
        for i in range(Y.shape[0]):
            self.sampleScore[i] = (self.alpha*self.Y*self.kernelProduct[:,i]).sum()+self.b
    
    #更新阈值b
    def __update_b(self,i,j,alphaiNew,alphajNew):
        b1 = -self.__Escore[i]-self.Y[i]*self.kernelProduct[i,i]*(alphaiNew-self.alpha[i])-self.Y[j]*self.kernelProduct[i,j]*(alphajNew-self.alpha[j])+self.b
        b2 = -self.__Escore[j]-self.Y[j]*self.kernelProduct[j,j]*(alphajNew-self.alpha[j])-self.Y[i]*self.kernelProduct[i,j]*(alphaiNew-self.alpha[i])+self.b
        if alphaiNew>=0 and alphaiNew<=self.C:
            if alphajNew>=0 and alphajNew<=self.C:
                self.b = (b1+b2)/2
            else:
                self.b = b1
        elif alphajNew >=0 and alphajNew<=self.C:
            self.b = b2
        else:
            pass

    
        
    def inputData(self,x,y):
        self.X = x
        self.Y = y
        self.__computekernelProduct(self.kernel,self.sigma)
        self.N = self.X.shape[0]
        self.alpha = np.zeros(shape = self.N)
        self.b = 0
        self.sampleScore = np.zeros(shape = self.N)
        self.__Escore = self.sampleScore-self.Y
        
        
    def train(self):
        
        i,j = -1,-1
        #pdb.set_trace()
        #检查停止条件的违背情况
        violation = np.zeros(self.N)
        indexSearch = np.where(self.alpha==0)
        violation[indexSearch] = 1-self.Y[indexSearch]*self.sampleScore[indexSearch]
        indexSearch = np.where(self.alpha==self.C)
        violation[indexSearch] = self.Y[indexSearch]*self.sampleScore[indexSearch]-1
        indexSearch = np.where((self.alpha>0)&(self.alpha<self.C))
        violation[indexSearch] = np.abs(self.Y[indexSearch]*self.sampleScore[indexSearch]-1)
        #找出违背情况最严重的第一个alpha
        find = violation.argmax()
        if violation[find]>1e-4:
            i = find
            random = np.random.uniform()
            if random>0.8:
               i= np.random.randint(0,self.N)
            #根据第一个alpha的Escore选择第二个alpha
            if self.__Escore[i]>=0:
                j = self.__Escore.argmin()
            else:
                j = self.__Escore.argmax()
            
            random = np.random.uniform()
            if random>0.8:
               j = np.random.randint(0,self.N)
        else:
            return None#设置了递归的出口
        
        #找到了两个变量需要做更新
        eta = self.kernelProduct[i,i]+self.kernelProduct[j,j]-2*self.kernelProduct[i,j]
        alphajNew = self.alpha[j]+self.Y[j]*(self.__Escore[i]-self.__Escore[j])/(eta+1e-4)
        #计算约束边界
        if self.Y[i]!=self.Y[j]:
            H = np.min([self.C,self.C+self.alpha[j]-self.alpha[i]])
            L = np.max([0,self.alpha[j]-self.alpha[j]])
        else:
            H = np.min([self.C,self.alpha[j]+self.alpha[i]])
            L = np.max([0,self.alpha[j]+self.alpha[j]-self.C])
        #根据约束边界更新alpha
        if alphajNew>H:
            alphajNew = H
        elif alphajNew<L:
            alphajNew = L
        else:
            pass
        alphaiNew = self.alpha[i]+self.Y[i]*self.Y[j]*(self.alpha[j]-alphajNew)
        
        #先更新b再更新E
        self.__update_b(i,j,alphaiNew,alphajNew)
        self.__computeSampleScore()
        self.__Escore = self.sampleScore-self.Y
        
        #修改alpha列表
        self.alpha[i] = alphaiNew
        self.alpha[j] = alphajNew
        
        #更新一次完成。递归。

        self.train()
        return None

        
        
            
            
            
            
#%%
svm = SVMclassifier(1,kernel = 'gaussian',sigma = 1)
svm.inputData(X,Y)
svm.train()
