# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 20:09:12 2017

@author: River

Objected-Oriented Programming
"""
#%%
class Bird(object):
    feather=True
    reproduction='egg'
    def chirp(self,sound):
        print(sound)
    def set_color(self,color):
        self.color=color

#%%
summer=Bird()
summer.reproduction
summer.chirp("gugugu")
summer.set_color('yellow')
summer.color

#%% 
#初始化方法：在每次创建对象时自动调用
class Bird(object):
    def __init__(self,sound):
        self.sound=sound
        print('my sound is:',sound)
    def chirp(self):
        print(self.sound)
        
summer=Bird('ji')
summer.chirp()

#%%
#继承
class Bird:
    feather=True
    reproduction="egg"
    def chirp(self,sound):
        print(sound)

class chicken(Bird):
    how_to_move='walk'
    edible=True

class swan(Bird):
    how_to_move='swim'
    edible=False
    
summer=chicken()
print(summer.feather)
summer.chirp('ji')
#%%
class Bird:
    feather=True
    reproduction="egg"
    def chirp(self):
        print('make sound')

class chicken(Bird):
    how_to_move='walk'
    edible=True
    def chirp(self):
        print('ji')
        
summer=Bird()
summer.chirp()

summer=chicken()
summer.chirp()

#%%
#调用父类中被覆盖掉的方法
class Bird(object):
    def chirp(self):
        print('make sound')
        
class Chicken(Bird):
    def chirp(self):
        print('jijiji')
        super().chirp() #内置类，产生一个指代父类的对象
        
bird=Bird()
bird.chirp()

summer=Chicken()
summer.chirp()

#%%
#一切皆对象
dir(list)#dir查看对象的所有属性
help(list)#help显示类的说明文档

#%%
#list method
a=[1,2,3,5,9.0,'good',-1,True,False,'Bye']
a.count(5)
a.index(3)
a.append(6)
a

#==============================================================================
# a.sort() 
# a.reverse()
# a.pop()
# a.remove(2)
# a.insert(0,'OK')
# a.clear()
#==============================================================================
#%%
#tuple method
a=(1,4,5)
a.count(5)
a.index(4)

#%%
#string
sstr='Hello World!'
ssub='World'

sstr.count(ssub)
sstr.find(ssub)
str.index(ssub)
sstr.rfind(ssub)#find from right
sstr.rindex(ssub)
sstr.isalnum()#alpha+number
sstr.isalpha()
sstr.isdigit()
sstr.istitle()
sstr.isspace()
sstr.islower()
sstr.isupper()
sstr.split(' ',2)
s=['a','b','c']
sstr.join(s)
sstr.strip(ssub)
sstr.replace(ssub,'Python')
sstr.capitalize()
sstr.upper()
sstr.lower()
sstr.swapcase()
sstr.title()
sstr.center(20)
sstr.ljust(20)
sstr.rjust(20)

#%%
#dict method
dd={'a':1,'b':2}
type(dd)
dd.keys()
dd.values()
dd.items()
dd.clear()
dd
#%%
#手动定义生成器
def gen():
    a=100
    yield a
    a=a*8
    yield a
    yield 1000

for i in gen():
    print(i)
    
def gen():
    i=0
    while i<100:
        i=i+1
        yield i
for i in gen():
    print(i)
    
#%%
#function
#函数是具有方法 __call__()的对象
class SampleMore:
    def __call__(self,a):
        return a+5
        
addfive=SampleMore()
addfive(3)

#%%
#模块对象

#==============================================================================
# import time
# 
# from time import sleep
# 
# from time import *
#==============================================================================

import time as t
t.sleep(10)
print('wake up')
print(t.__name__)

import this_dir.mysleeptime as ms
ms.my_time_sleep(10);print('wake up')

#%%
#异常对象
try:
    m=10/0
except ZeroDivisionError as e:
    print('Catch NameError in the sub-function')
    print('type(e)=');type(e)
    print('dir(e)=');dir(e)
    print('e.message=');print(e.message)
    
raise ZeroDivisionError()
