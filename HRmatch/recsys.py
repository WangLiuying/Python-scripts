# -*- coding: utf-8 -*-
"""
Created on Thu May 24 15:20:19 2018

@author: Liuying Wang
"""

import surprise
import pandas as pd
import numpy as np
from surprise import SVDpp, KNNWithZScore
from surprise import Dataset
from surprise import accuracy,dump
from surprise.model_selection import train_test_split
#%%整理适合surprise读取的数据
remark = pd.read_pickle('2017年09-12月应聘数据之应聘记录_整理格式.pkl')
remark = remark.iloc[:,1:3]
remark['rate']=1
remark.rename(columns={'人才标识码':'User','应聘职位编号':'Item'},inplace=True)
remark.to_pickle('recordsForSurprise.pkl')
#%%隐式推荐系统需要进行负采样
def NegativeSampling(df):
    """
    给出评分记录，进行负采样
    df由三列构成，分别是：用户编号；项目编号；评分（1）
    """
    userSize = pd.value_counts(df.iloc[:,0])
    itemSize = pd.value_counts(df.iloc[:,1])
    samplingDF = pd.DataFrame(columns = ['Item','User','rate'])
    for itertime,user in enumerate(userSize.keys()):
        tchoice = df.loc[df.iloc[:,0]==user].iloc[:,1]
        titem = itemSize.drop(tchoice)
        t = np.random.choice(titem.keys(),size=max(userSize[user],10),
                             replace=False,p=titem/titem.sum())
        tDf = pd.DataFrame({'Item':t,'User':user,'rate':0})
        samplingDF = pd.concat([samplingDF,tDf])
        if itertime%100==0:
            print('sampling for' + str(itertime) +'\n')
    return samplingDF

samplingDF = NegativeSampling(remark)
#%%
remark = pd.read_pickle('recordsForSurprise.pkl')
samplingDF = pd.read_pickle('negativeSampling.pkl')
merge = pd.concat([remark,samplingDF])
merge.reset_index(inplace = True)
del merge['index'],remark,samplingDF
merge = merge[['User','Item','rate']]

#%%

reader = surprise.Reader(rating_scale=(0,1))
data = Dataset.load_from_df(merge, reader)
del merge

train,test =  train_test_split(data,random_state=123,test_size=0.1)
#%%训练模型（未调参）
algo = SVDpp() #声明模型
algo.biased = False

algo.fit(train)

predictions = algo.test(test)
accuracy.mae(predictions)
a = algo.predict('15cbc496d67626ad90514b4243e7c045','2204590')
print(a)
dump.dump(file_name='SVDmodel.pkl',algo=algo)
#%%
algo = dump.load('best_model.pkl')[1]
#%%瞎猜模型（供对比）
algocompare = surprise.NormalPredictor()
algocompare.fit(train)
preCompare = algocompare.test(test)
accuracy.mae(preCompare)

#%%计算precision and recall
## code from scikit-surprise documentation FAQs
from collections import defaultdict

def precision_recall_at_k(predictions, k=10, threshold=3.5):
    '''Return precision and recall at k metrics for each user.'''

    # First map the predictions to each user.
    user_est_true = defaultdict(list)
    for uid, _, true_r, est, _ in predictions:
        user_est_true[uid].append((est, true_r))

    precisions = dict()
    recalls = dict()
    for uid, user_ratings in user_est_true.items():

        # Sort user ratings by estimated value
        user_ratings.sort(key=lambda x: x[0], reverse=True)

        # Number of relevant items
        n_rel = sum((true_r >= threshold) for (_, true_r) in user_ratings)

        # Number of recommended items in top k
        n_rec_k = sum((est >= threshold) for (est, _) in user_ratings[:k])

        # Number of relevant and recommended items in top k
        n_rel_and_rec_k = sum(((true_r >= threshold) and (est >= threshold))
                              for (est, true_r) in user_ratings[:k])

        # Precision@K: Proportion of recommended items that are relevant
        precisions[uid] = n_rel_and_rec_k / n_rec_k if n_rec_k != 0 else 1

        # Recall@K: Proportion of relevant items that are recommended
        recalls[uid] = n_rel_and_rec_k / n_rel if n_rel != 0 else 1

    return precisions, recalls

#%%计算precision and recall
precisions, recalls = precision_recall_at_k(predictions, k=10, threshold=0.7)
# Precision and recall can then be averaged over all users
print(sum(prec for prec in precisions.values()) / len(precisions))
print(sum(rec for rec in recalls.values()) / len(recalls))

#%%推荐前topN物品
## code from scikit-surprise documentation FAQs
def get_top_n(predictions, n=10):
    '''Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    '''

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

#%%为第一位用户进行推荐
user = '8c075982f92d9e0d678680e4ffedf4c2'
itemlist = data.df[(data.df.User==user)&(data.df.rate==1)]['Item'] #取出已评分的物品
waitRec = pd.Series(data.df.Item.unique())
waitRec = waitRec.drop(waitRec.isin(itemlist))
predictionForUser1 = []
for item in waitRec.tolist():
    predictionForUser1.append(algo.predict(user,item))
    
a=get_top_n(predictionForUser1, 10)
#%%
remark = pd.read_pickle('2017年09-12月应聘数据之应聘记录_整理格式.pkl')
position = pd.read_pickle('2017年09-12月应聘数据之职位信息_整理格式.pkl')
remark.loc[remark.人才标识码==user].iloc[0].tolist()
position.loc[position.职位编号=='2028590'].iloc[0].tolist()
#%%持久化
from surprise import dump
#dump.dump(file_name='SVDmodel.pkl',algo = algo)
algo=dump.load('SVDmodel.pkl')

#%%调参
from surprise.model_selection import GridSearchCV
gridSearch = {'n_factors':[20,50,100,150],
              'lr_all':[0.010],
              'reg_all':[0.02]}

gs = GridSearchCV(SVDpp,param_grid=gridSearch,measures=['mae'],
                  n_jobs=-1,cv=3,refit=True,joblib_verbose=1)
gs.fit(data)
