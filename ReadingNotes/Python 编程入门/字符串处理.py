# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 15:37:41 2017
字符串处理
@author: River
"""
#%%字符串索引

s="apple"
for i in range(5):
    print(s[i])

for i in range(-1,-6,-1):
    print(s[i])
    
#%%查看字符对应的编码
ord("a")
ord("b")

#%%字符串切片

food="apple pie"
food[0:5]
#提取第0：n，则需写[0:n+1]

#提取拓展名
def get_ext(fname):
    """Return the extension of file"""
    dot=fname.rfind(".")
    if dot==-1:
        return ""
    else:
        return fname[dot+1:]
get_ext("hello.txt")


#%%标准字符串函数
dir("")#查看字符串类型的属性和方法

s="cheese"
s.index("ee")
s.rfind("ee")
s.rfind("s")


s.capitalize()
s#不会改变原始的字符串
s=s.capitalize()#只有第一个字母会被大写
s
s.swapcase()#大小写逆反
s.title()#每个单词的首字母大写

s.center(10,"*")
s.ljust(10,"*")
s.rjust(10,"*")


"{whose} {pet} hat fleas".format(pet="dog",whose="my")

s
s.strip("e")#从开头和末尾删除“e”字符
s.lstrip("e")
s.rstrip("e")

name="  Gill Bates "
name.lstrip()
name.rstrip()
name.strip()
title="--Happy Days!--"

url="www.google.com"
url.partition(".")#找到第一个‘.’，分割
url.rpartition(".")#找到最后一个'.'，分割

url.split(".")#所有的‘.’,分割
story="A long time ago, a princess ate an apple."
story.split()

s="up up and away"
s.replace("up","down")

#%%others
leet_table="".maketrans("EIOBT","31087")
"BE COOL. SPEAK LEET!".translate(leet_table)
"Be COoL. SPeaK LeET!".translate(leet_table)

"23".zfill(5)
"-83".zfill(5)

" ".join(["once","upon","a","time"])
"-".join(["once","upon","a","time"])
"".join(["once","upon","a","time"])
#s.count
#s.encode
#s.join
#s.maketrans
#s.translate
#s.zfill

#%%
def is_done1(s):
    return s=="done" or s=="quit"
import re
def is_done2(s):
    return re.match("done|quit",s)!=None

dir(re)
