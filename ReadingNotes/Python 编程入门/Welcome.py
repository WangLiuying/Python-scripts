# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 00:38:36 2017

@author: River
"""
print("Welcome to Python")

#%%
name=input("What is your name?").strip()#strip去掉空格
print("Hello "+name.capitalize()+"!")#capitalize首字大写

#%%print
print("jack","ate","no","fat")
print("jack","ate","no","fat",sep=".")
print("jack","ate",end=" ")
print("no","fat")

#%%if简写

food=input("What is your favorite food?")
reply="yuck" if food=="lamb" else "yam"


#%%函数的说明文档

import math

def area(radius):
    """Return the area of a circle with the given radius."""
    return math.pi * radius ** 2
    
print(area.__doc__)

#%%调用全局变量的一个方法

name="jack"

def say_hello():
    print("hello " + name + "!")
    
def change_name(newname):
    global name #指明为全局变量
    name=newname
    
#test
say_hello()
change_name("WangLiuying")
say_hello()



#%%一些常识
#使用main函数：程序的起点；
#函数参数传递：引用传递
