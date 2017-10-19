# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 00:10:51 2017
python 编程入门 输入输出
@author: River
"""

#%%设置字符串格式

x=1/81
print(x)
print("value: %.2f" % x)
print("value: %.5f" % x)

a,b,c="cat",3.14,6
s="There\'s %d %ss older than %.2f years." %(c,a,b)
s

#或使用格式字符串
"My {pet} has {prob}.".format(pet="dog",prob="fleas")

"1/81={x}".format(x=1/81)
"1/81={x:f}".format(x=1/81)
"1/81={x:.3f}.".format(x=1/81)


"num={x:.{d}f}".format(x=1/81,d=3)


#%%#工作路径配置
#import os

#os.getcwd
#os.listdir
#os.chdir
#os.path.isfile
#os.path.isdir
#os.stat 返回信息，如大小和最后修改时间等


#%%处理文本文件

#逐行读取文件
def printfile1(fname):
    f=open(fname,"r")
    for line in f:
        print(line,end=" ")
    f.close()

#一次性读取

def printfile2(fname):
    f=open(fname)
    print(f.read())
    f.close()
    
#写入文本
import os

def make_story():
    if os.path.isfile("story.txt"):
        print("'story.txt' already exists.")
    else:
        f=open("story.txt","w")
        f.write("Mary had a little lamb,\n")
        f.write("and then she had some more.\n")
        f.close()

#附加文本至文件末尾

def add_to_story(line,fname="story.txt"):
    f=open(fname,"a")
    f.write(line)
    
#将字符串插入文件开头

def insert_title(title,fname="story.txt"):
    f=open(fname,"r+")
    temp=f.read()
    temp=title + "\n\n" + temp
    f.seek(0)
    f.write(temp)
    f.close()

#%%处理二进制文件

def is_gif(fname):
    f=open(fname,"br") #二进制模式打开
    first4=tuple(f.read(4))
    return (first==(0x47,0x49,0x46,0x38))
    
#%%pickle
import pickle
def make_pickled_file():
    grades={"alan":[4,8,10,10],
            "tom":[7,7,7,8],
            "dan":[5,None,7,7],
            "may":[10,8,10,10]}
    outfile=open("grades.dat","wb")
    pickle.dump(grades,outfile)
    
def get_pickled_data():
    infile=open("grades,dat","rb")
    grades=pickle.load(infile)
    return grades
    
#%%读取网页
import urllib.request
page=urllib.request. urlopen("http://python.org")
html=page.read()
html[:25]

import webbrowser
webbrowser.open("http://www.yahoo.com")
dir(webbrowser)


