# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 21:00:45 2017

@author: River
"""

import os
os.chdir("D:\DataAnalysis\python\headfirstpython\hfpy_ch5_data")
os.getcwd()


with open("james.txt") as jaf:
    data=jaf.readline()
    james=data.strip().split(",")
with open("julie.txt") as juf:
    data=juf.readline()
    julie=data.strip().split(",")
with open("mikey.txt") as mif:
    data=mif.readline()
    mikey=data.strip().split(",")
with open("sarah.txt") as saf:
    data=saf.readline()
    sarah=data.strip().split(",")
    
sortdata=[2,4,5,1,3]
sortdata.sort() #原地排序
sortdata
sortdata=[2,4,5,1,3] 
sorted(sortdata) #复制排序

def sanitize(time_string):
    if "-" in time_string:
        splitter="-"
    elif ":" in time_string:
        splitter=":"
    else:
        return time_string
    (mins,secs)=time_string.split(splitter)
    return(mins + "." + secs)
    
james=[float(sanitize(each_time)) for each_time in james] #列表推导
julie=[float(sanitize(each_time)) for each_time in julie]
mikey=[float(sanitize(each_time)) for each_time in mikey]
sarah=[float(sanitize(each_time)) for each_time in sarah]

james[0:3] #访问第0至第3（不包括）个对象

"""method.1: edit the lists"""
unique_james=[]
for each_t in james:
    if each_t not in unique_james:
        unique_james.append(each_t)
unique_james.sort()
unique_james[0:3]

"""method.2: use set()"""
sorted(set(james))[0:3]
sorted(set(julie))[0:3]

"""def a function for reading file"""
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline().strip().split(",")
        return data
    except IOError as ioerr:
        print("file error:"+str(ioerr))
    return None
    
sarah=get_coach_data("sarah.txt")
