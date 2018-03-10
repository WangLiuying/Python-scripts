# -*- coding: utf-8 -*-
"""
Spyder Editor

二分查找 按序添加
"""
import pdb
#%%例题：二分查找

alist=[1,3,5,7,9,11,13,15,17,19]

def binary_search(alist):
    #pdb.set_trace()
    x = int(input("please enter an number"))
    s = 0
    e = len(alist)-1
    noflag = True
    while s<=e:
        m = (s+e)//2
        if alist[m]==x:
            noflag = False
            print("Find number %d at index %d" %(x, m))
            break
        elif alist[m]<x:
            s = m+1
        else:
            e = m-1
    if noflag:
        print("There is no number %d!" % x)
    
#test  
binary_search(alist)         

#%%例题：在排序数组中插入一个数字
"""
输入x
1.从后往前找，方便挪动
2.比较x与list[i]，x大，往后放(放完break)；x小，放当前位置，list[i]后移
"""
class Solution_insert:
    alist=[1,3,5,7,9,12,14,-1,-1,-1]
    def insert(self, x):
        i = len(self.alist)-1
        while i>=0:
            if self.alist[i]==-1:
                pass
            elif self.alist[i]<=x:
                self.alist[i+1] = x
                break
            else:
                self.alist[i+1] = self.alist[i]
            i = i-1
        print(self.alist)

sorting_insert = Solution_insert()
sorting_insert.insert(9)

#%%例题：数据删除
class Solution_delete:
    alist = [1,3,5,7,9,2,4,6,8,10]
    def delete(self,x):
        n = len(self.alist)
        for i in range(n):
            if self.alist[i]==x:
                self.alist[i] = -1
        for i in range(n):
            if self.alist[i]!=-1:
                print(self.alist[i])

delete_obj = Solution_delete()               
delete_obj.delete(8)    
