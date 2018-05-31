# -*- coding: utf-8 -*-
"""
Created on Sun May 27 01:01:03 2018
基于FP-Growth算法的推荐
@author: Liuying Wang
"""
import pyfpgrowth as fp
import pandas as pd
import numpy as np
from scipy import 
#%%获取transactions集子
records = pd.read_pickle('recordsForSurprise.pkl')
del records['rate']
group = records.groupby('User')
trans = list(group.groups.values())
trans = [item.tolist() for item in trans]

#%%过于稀疏，无法找到
patterns = pyfpgrowth.find_frequent_patterns(trans, 2)
rules = pyfpgrowth.generate_association_rules(patterns, 0.1)

