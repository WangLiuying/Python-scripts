# -*- coding: utf-8 -*-
"""
Decision Tree

Created on Thu Mar 15 12:17:50 2018

@author: Liuying Wang
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%%
def createDataset():
    dataset = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    return pd.DataFrame(dataset,columns = ['NoSurfacing','Flippers','Fish'])
dataset = createDataset()
X,Y = dataset.iloc[:,:2],dataset.iloc[:,2]
#%%计算经验熵
#in:结点所含样本idx
#out：该节点entropy
def Entropy(nodeList):
    data = Y[nodeList]
    prob = data.value_counts()/data.count()
    ent = (-prob*np.log(prob)).sum()
    return ent
#in: feature index, 结点所含样本idx
#out: 该结点上特征的entropy
def featEnt(feature,nodeList):
    data = X.loc[nodeList,feature]
    prob = data.value_counts()/data.count()
    ent = (-prob*np.log(prob)).sum()
    return ent



#%%定义结点
class Node:
    parent = -1
    children = 'Leaf'
    splitFeature = -1
    entropy = 0.
    dataList = []
    dataNum = 0
    prediction = None
    subTreeEntropy = 0.
    gt = 0.
    
    def __init__(self,nodeList, parentNode = -1,feature = -1):
        self.entropy = Entropy(list(nodeList))
        self.dataList = list(nodeList)
        self.dataNum = len(self.dataList)
        self.parent = parentNode
        self.splitFeature = feature
        self.prediction = Y[self.dataList].value_counts().argmax()
        
#test = Node(Y.index)

#%%根据特征划分数据
#in: 特征index，结点所含样本
#out:子结点
def splitData(node,feature):
    y = Y[node.dataList]
    x = X.loc[node.dataList,feature]
    children = {}
    group = y.groupby(x)
    for i in x.unique():
        childrenNode = Node(group.groups[i],node)
        children[i] = childrenNode
    return children

#test = splitData(root,features[0])

#%%选择最佳特征
#in：结点，特征候选列表
#out:最优分割特征 子结点
def bestSplit(node,features):
    x = X.loc[node.dataList,features]
    y = Y[node.dataList]
    bestFeat = 0
    entRatio = 0
    for feat in features:
        if len(x.loc[:,feat].unique())==1:
            features = features.drop(feat)
            continue
        ent1 = node.entropy
        children = splitData(node,feat)
        ent2 = np.array([child.entropy*child.dataNum 
                         for child in list(children.values())]).sum()
        ent2 = ent2/node.dataNum
        entRatioTemp = (ent1 - ent2)/featEnt(feat, node.dataList)
        if entRatioTemp>entRatio:
            bestFeat = feat
            entRatio = entRatioTemp
            bestChildren = children
    return bestFeat, bestChildren, entRatio

#%%树生成
#in：根结点,候选特征列表，阈值
#out：无。但结点之间应有指针互相联结
def treeGrow(self, node, features, epsilon):
    if node.entropy==0 or len(features)==0:
        
        return None
       
    bestfeat,bestChildren,entRatio = bestSplit(node,features)
    if entRatio>epsilon:
        node.splitFeature = bestfeat
        node.children = bestChildren
        for child in list(node.children.values()):
            treeGrow(child, features.drop(bestfeat), epsilon)
    else:
        return None
#%%
class C45Tree:
    X = None
    Y = None
    root = None
    epsilon = 0
    leafNumber = 0
    leaves = []
    
    def __init__(self,epsilon = 1e-4):
        self.epsilon = epsilon

    #in：根结点,候选特征列表，阈值
    #out：无。但结点之间应有指针互相联结
    def treeGrow(self, node, features, epsilon):
        if node.entropy==0 or len(features)==0:
            self.leaves.append(node)
            return None
        bestfeat,bestChildren,entRatio = bestSplit(node,features)
        if entRatio>epsilon:
            node.splitFeature = bestfeat
            node.children = bestChildren
            for child in list(node.children.values()):
                self.treeGrow(child, features.drop(bestfeat), epsilon)
        else:
            return None    
    #in：数据
    #out：树
    def fit(self,X,Y):
        self.X = X
        self.Y = Y
        self.root = Node(Y.index)
        self.treeGrow(self.root,X.columns,self.epsilon)
        self.leafNumber = 0
        self.__getNumberLeafs()
        
        
    def __getNumberLeafs(self,node = None):
        if node==None:
            node = self.root
        if type(node.children).__name__=='dict':
            for i in list(node.children.values()):
                self.__getNumberLeafs(node = i)
        else:
           self.leafNumber = self.leafNumber+1
           
    #预测
    def predict(self, newX, node = None):   
         if node==None:
             node = self.root
         if node.children=='Leaf':
             return node.prediction
         nextnode = newX.loc[node.splitFeature]
         nextnode = node.children[nextnode]
         return self.predict(newX, node = nextnode)
     
    
    #计算子树的cost
    def subTreeEnt(self, alpha = 0.1, node = None):
        if node==None:
            node = self.root
        if node.children=='Leaf':
            return node.entropy*node.dataNum/(self.root.dataNum)+alpha
        for child in list(node.children.values()):
            node.subTreeEntropy += self.subTreeEnt(alpha,child)
        return node.subTreeEntropy
# 实在不会写了    
#    def prune(self, alpha = 0.1, node = None):
#        if node==None:
#            parentNode = set([node.parent for node in self.leaves])
#        for cutnode in parentNode
            
        
        
#%%draft
testTree=C45Tree(1e-5)
testTree.fit(X,Y)        
testTree.predict(newX)
#%%test draft

import sys
sys.getsizeof(testTree.root)
