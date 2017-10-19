# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:19:45 2017

@author: River
"""

3**2 #乘方
10%3 #求余

"""串接字符串"""
'Vamei say:'+'Hello World'
'Vamei'*2

"""逻辑值"""
True and True
False and True

True or True
True or False
False or False

not True

#序列 sequence
#包括元组Tuple和列表list
example_tuple=(2,1.3,'love',5.6,9,12,False)
example_list=[True,5,'smile']
#元组不能改变数据
example_tuple[2:0:-1]


#字典 dict
example_dict={'tom':11,'sam':57,'lily':100}
example_dict['tom']


for i in range(5):
    print(str(i))
#可以配合 continue和break使用


#help
help(max)

def square_sum(a,b):
    """return the square sum of two arguments"""
    return a**2+b**2
help(square_sum)

#%%
#包裹传参
def package_keyword(*all_arguments):
    print(type(all_arguments))
    print(all_arguments)
package_keyword(1,9) #元组

def package_keyword(**all_arguments):
    print(type(all_arguments))
    print(all_arguments)
package_keyword(a=1,b=9) #字典

#解包裹
def unpackage(a,b,c):
    print(a,b,c)
args=(1,3,4)
unpackage(*args)

args={'a':1,'b':3,'c':4}
unpackage(**args)

#%%
#递归用法：e.g.高斯求和
def gaussian(n):
    if n==1:
        return 1
    else:
        return n+gaussian(n-1)

gaussian(10)

#函数栈概念

#%%
"""异常处理机制的标准语法"""
#==============================================================================
# try:
#     ...
# except exception1:
#     ...
# except exception2:
#     ...
# else:
#     ...
# finally:
#     ...
#==============================================================================
    
#主动抛出异常信息
raise ZeroDivisionError()


#%%
#搜索路径设置
import sys
print(sys.path)
