# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 19:47:04 2017
python编程入门 数据结构
元组、列表、字典
@author: River
"""

#%%
type(5.0)
type(print)

#%%序列
#可用正索引和负索引
#使用+或*进行拼接

#%%元组
items=(-6,"cat",(1,2))
len(items)
items[-1]
items[-1][0]

#%%元组函数
#in,len,tup.count,tup.index

pets=("dog","cat","bird","dog")
"bird" in pets

len(pets)

pets.count("dog")
pets.index("dog")#只能找到第一个

tup1=(1,2,3)
tup2=(3,4,5)
tup1+tup2
tup1*2

#%%列表
numbers=[7,-7,2,3,2]
numbers+numbers#注意与R区分开。。。。。。

numbers*2

#列表的自引用
snake=[1,2,3]
snake[1]=snake
snake

#%%列表函数
#s.append;s.count;s.extend;s.index;s.insert;s.pop;s.remove;s.reverse;s.sort

lst=[]

lst.extend("cat")
lst

lst.extend([1,4,3])
lst

lst=["a","b","c","d"]
lst.pop(2)
lst
lst.pop()
lst

lst=["a","b","c","a"]
lst.remove("a")
lst

lst
lst.reverse()#反转是就地完成的
lst


lst=[6,4,5,3,2,3,5]
lst.sort()
lst

pts=[(1,2),(2,2),(1,1),(2,1)]
pts.sort()
pts

#%%列表解析
[n*n for n in range(1,11)]
[c for c in "pizza"]
[c.upper() for c in "pizza"]

 
 #使用列表解析进行筛选
nums=[-1,0,6,4,-2,3]
[n for n in nums if n>0]

#示例，去掉字符串中的元音字母
def eat_vowels(string):
    """Remove the vowels from s"""
    return "".join([s for s in string if s.lower() not in "aeiou"])
                   
eat_vowels("Apple Sauce")

#生成器版
def eat_vowels(string):
    """Remove the vowels from s"""
    return "".join(s for s in string if s.lower() not in "aeiou")
                   
eat_vowels("Apple Sauce")

#%%字典
color={"red":1,"green":3,"blue":5}

#键唯一且不可改变

#相关函数
#d.items;d.keys;d.values;d.get;d.pop;d.ppitem;d.clear;d.copy;
#d.fromkeys;d.setdefault;d.update

color.items()
color.keys()
color.values()

color.pop("red")
color
color.popitem("blue",5)
