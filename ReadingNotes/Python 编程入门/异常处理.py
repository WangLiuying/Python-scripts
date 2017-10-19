# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:12:54 2017

@author: River
"""

#%%异常

open("unicorn.dat")

#%%引发异常
raise IOError('This is a test!')

#%%忽略异常（调试代码时）
#捕获异常（使程序更加友好）

def get_age():
    while True:
        try:
            n=int(input('How old are you?'))
            return n
        except ValueError:
            print('Please enter an integer value.')
            
#清理操作finally

#with语句

num=1
with open(fname,'r') as f:
    for line in f:
        print('%04d %s' %(num,line),end=" ")
        num=num+1
        