# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 15:11:18 2017
Numpy learning
@author: River
"""

import numpy as np
a=np.array([1,2,3])
type(a)
a
a.dtype
a.ndim
a.size
a.shape

b=np.array([[1.3,2.4],[3.4,2.4]])
b.dtype
b.ndim
b.size
b.shape
b.itemsize
b.data

#%%创建数组
c=np.array([[1,2,3],[5,6,7]])
c
c.shape
g=np.array([['a','b'],['c','d']])
g
g.dtype.name

#%%定义dtype
f=np.array([[1,2,3],[2,3,4],[4,5,6]],dtype=complex)
f
#%%
np.zeros((3,3))
np.ones((3,3))
np.arange(4,10)
np.arange(0,12,3)
np.arange(0,6,.6)

np.arange(0,10).reshape(2,5)
np.linspace(0,10,4).reshape(2,2)
np.random.random(3)
np.random.random((3,3))




#%%基本操作
a=np.arange(4)
a
a+4
a*2
b=np.arange(4,8)
b
a+b
a*b
np.sin(b)
np.sqrt(b)

A=np.arange(0,9).reshape(3,3)
B=np.ones((3,3))
A+B
A*B#对应位相乘
np.dot(A,B)#矩阵乘法
A.dot(B) #is not equal to np.dot(B,A)

#%%自加和自减
a=np.arange(1,5)
a += 2
a

#%%通用函数：逐一对数组中的元素进行操作
a=np.arange(1,5)
a
np.sqrt(a)
np.log(a)
np.sin(a)

#%%聚合函数:对一组值进行操作，返回一个单一值
a=np.array([3.3,2.4,5.5,1.2,5.2])
a.sum()
a.min()
a.max()
a.std()

#%%索引
a=np.arange(10,16)
a
a[4]
a[-1]
a[-6]
a[[1,3,4]]

A=np.arange(10,19).reshape((3,3))
A
A[1,2]#第二行第三列

#%%切片
a[1:5]
a[1:5:2]#每间隔2抽取一个
a
a[::2]
a[1::2]
a[:5:]

A=np.arange(10,26).reshape((4,4))
A
A[0,1::2]
A[:,0]
A[0:2,0:2]
A[[0,2],0:2]


#%%数组迭代
a=np.arange(10,16)
for item in a:
    print(item)
    
A=np.arange(10,19).reshape(3,3)
A    
#for row in A：
 #   print(row)????why

for item in A.flat:
    print(item)    

#%%apply_along_axis
np.apply_along_axis(np.mean,axis=0,arr=A)#按行
np.apply_along_axis(np.mean,axis=1,arr=A)#按列

def foo(x):
    return x.sum()/2
    
np.apply_along_axis(foo,axis=0,arr=A)

#%%条件和布尔数组

A=np.random.random((4,4))
A
A<0.5
A[A<0.5]

#%%形状变换
a=np.random.random(12)
a
a.reshape(3,4)#并没有改变a
a
a.shape=(3,4)#直接改变了a
a
a.shape=(12)#我再变回来
a
A
A.transpose()#转置

#%%数组操作

#%%连接数组
A=np.ones((3,3))
B=np.zeros((3,3))
np.vstack((A,B))#竖直入栈
np.hstack((A,B))#横向入栈

#%%
a=np.array([0,1,2])
b=np.array([3,4,5])
c=np.array([6,7,8])
np.column_stack((a,b,c))
np.row_stack((a,b,c))

#%%数组切分
A=np.arange(16).reshape(4,4)
A
[B,C]=np.hsplit(A,2)
[B,C]=np.vsplit(A,2)#等长、宽 切分

[A1,A2,A3]=np.split(A,[1,3],axis=1)#第二个参数：从哪里开始切分；
A1
A2
A3

#%%常用概念

#%%对象的副本或视图
#Numpy中，进行数组运算或数组操作时，返回结果不是数组的副本就是视图
#Numpy中，所有赋值运算不会为数组和数组中的任何元素创建副本
a=np.array([1,2,3,4])
b=a
a[2]=0
b#注意b[2]改为了0 #指针的概念

c=a[:2]
c
a[0]=0
c

#正确得到副本的方法
a=np.array([1,2,3,4])
c=a.copy()
a[1]=0
c

#%%向量化
a*c
A.dot(B.transpose())
#内部实现依靠循环，语法糖

#%%广播机制
#规则一：为却是的维度补上个1
#规则二：嘉定却是元素都用已有值进行填充

A=np.arange(16).reshape((4,4))
b=np.arange(4)
b
A+b

#%%结构化数组
#bytes b1; int i1,i2,i4,i8; unsigned ints u1,u2,u4,u8;
#floats f2,f4,f8; complex c8,c16; fixed length strings a<n>

structured=np.array([(1,'First',.5,1+2j),(2,'Second',1.3,2-2j)],dtype=('i2,a6,f4,c8'))
structured
structured[1]
structured['f1']


structured=np.array([(1,'First',.5,1+2j),(2,'Second',1.29999,2-2j)],
                    dtype=[('id','i2'),('position','a6'),('value','f4'),('complex','c8')])
structured.dtype.names
structured.dtype.names=('id','order','value','complex')
structured
structured['order']

#%%数组数据文件的读写
data=np.random.random(16).reshape((4,4))
np.save("saved_data",data)
loaded_data=np.load("saved_data.npy")
print(np.__doc__)
data=np.genfromtxt("data.csv",delimiter=',',names=True)
data
