# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 09:00:16 2017

@author: River
"""
#%%竞跑条件
import threading
x=5
def double():
    global x
    x=x*2
def plus10():
    global x
    x=x+10

thread1=threading.Thread(target=double)
thread2=threading.Thread(target=plus10)
thread1.start();thread2.start()
thread1.join();thread2.join()
print(x)

#%%并行运算
import multiprocessing
def proc1():
    return 999999*9999
def proc2():
    return 888888*8888

p1=multiprocessing.Process(target=proc1)
p2=multiprocessing.Process(target=proc2)

p1.start()
p2.start()

p1.join()
p2.join()

#%%
#函数闭包：环境变量+函数
#所谓环境变量即指与闭包内函数同属一个环境的变量
def line_conf():
    b=15
    def line(x):
        return 2*x+b
    b=5
    return line
    
if __name__=="__main__":
    my_line=line_conf()
    print(my_line(5))
    print(my_line.__closure__[0].cell_contents)
    
#%%
#闭包应用实例
def line_conf(a,b):
    def line(x):
        return a*x+b
    return line

line1=line_conf(1,1)
line2=line_conf(4,5)
lin33=line_conf(5,10)

  
#%%
def decorator_demo(old_function):
    def new_function(a,b):
        print("input:",a,b)
        return old_function(a,b)
    return new_function
    
@decorator_demo
def square_sum(a,b):
    return a**2+b**2
    
@decorator_demo
def square_diff(a,b):
    return a**2-b**2
    
if __name__=="__main__":
    print(square_sum(3,4))
    print(square_diff(3,4))
    
    
#%%
import time
def decorator_timer(old_function):
    def new_function(*arg,**dict_arg):
        t1=time.time()
        result=old_function(*arg,**dict_arg)
        t2=time.time()
        print("time:",t2-t1)
        return result
    return new_function
    
@decorator_timer
def square_diff(a,b):
    return a**2-b**2
    
if __name__=="__main__":
    print(square_diff(4232,2000))
    
#%%
#带参装饰器
def pre_str(pre=""):
    def decorator(old_function):
        def new_function(a,b):
            print(pre + "input",a,b)
            return old_function(a,b)
        return new_function
    return decorator
    
@pre_str("^_^")
def square_sum(a,b):
    return a**2+b**2

if __name__=="__main__":
    print(square_sum(242,343)
    
#%%装饰类
def decorator_class(SomeClass):
    class NewClass:
        def __init__(self,age):
            self.total_display=0
            self.wrapped=SomeClass(age)
        def display(self):
            self.total_display+=1
            print("total display:",self.total_display)
            self.wrapped.display()
    return NewClass
    
@decorator_class
class Bird:
    def __init__(self,age):
        self.age=age
    def display(self):
        print("My age is ",self.age)
        
if __name__=="__main__": 
    eagle_lord=Bird(5)
    for i in range(3):
        eagle_lord.display()
        
#%%
"""
高阶函数
e.g.map, filter, reduce
"""

#lambda函数
lambda_sum=lambda x,y:x+y
print(lambda_sum(3,4))

#%% map
data_list=[1,3,5,6]
result=map(lambda x:x+3,data_list)
print(result)

def square_sum(x,y):
    return x**2+y**2

data_list1=[1,3,5,7]
data_list2=[2,4,6,8]
result=map(square_sum,data_list1,data_list2)

#%% filter
def larger100(a):
    if a>100:
        return True
    else:
        return False
result=filter(larger100,[102,30,200,10])
print(result)

#%% reduce
data_list=[1,2,4,7,9]
import functools
result=functools.reduce(lambda x,y:x+y,data_list)
print(result)

#%%并行处理
import time
from multiprocessing import Pool
import requests

def decorator_timer(old_function):
    def new_function(*args,**dict_args):
        t1=time.time()
        result=old_function(*args,**dict_args)
        t2=time.time()
        print("time:",t2-t1)
        return result
    return new_function

def visit_once(i,address="http://www.cnblogs.com"):
    r=requests.get(address)
    return r.status_code
    
@decorator_timer
def single_thread(f,counts):
    result=map(f,range(counts))
    return list(result)
    
@decorator_timer
def multiple_thread(f,counts,process_number=10):
    p=Pool(process_number)
    return p.map(f,range(counts))
    
if __name__=="__main__":
    TOTAL=100
    print(single_thread(visit_once,TOTAL))
    print(multiple_thread(visit_once,TOTAL))

#%%
#生成器表达式
gen=(x for x in range(4))
l=[l**2 for l in range(10)]

x1=[1,3,4]
y1=[9,12,13]
l=[x**2 for(x,y) in zip(x1,y1) if y>10]
d={k:v for k,v in enumerate("Vamei") if val not in "Vi"}
   
#%%惰性求值与迭代器

from itertools import *
count(5,2) #5,7,9,11...
cycle("abc") #a,b,c,a,b,c,a....
repeat(1.2) #1.2,1.2,1.2,...
repeat(10,5) #10,10,10,10,10
chain([1,2,3],[4,5,6]) #连接两个迭代器变成1,2,3,4,5,6
product("abc",[1,2]) #笛卡尔积
for m,n in product("abc",[1,2]):
    print(m,n)
    
permutations("abc",2)
combinations("abc",2)
combinations_with_replacement("abc",2)

starmap(pow,[(1,1),(2,2),(3,3)]) #1**1,2**2,3**3

takewhile(lambda x:x<5,[1,3,6,7,1]) #1,3
dropwhile(lambda x:x<5,[1,4,6,7,1]) #6,7,1
help(takewhile)
#%%
from itertools import groupby

def height_class(h):
    if h>180:
        return "tall"
    elif h<160:
        return "short"
    else:
        return "middle"
        
friends=[191,158,182,162,184,170]
friends=sorted(friends,key=height_class)

for m,n in groupby(friends,key=height_class):
    print(m)
    print(list(n))
