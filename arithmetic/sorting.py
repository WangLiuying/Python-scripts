# -*- coding: utf-8 -*-
"""
排序算法：
选择排序
冒泡排序
归并排序

Created on Fri Mar  9 22:07:57 2018

@author: Liuying Wang
"""
#%%排序算法
"""
进行N-1重循环，在第i轮，遴选i~N数中最小的，与第i位进行交换
即，第一轮将最小者排在第一位；
第二轮将次小者排在第二位；
……
"""
class SortSelection:
    mylist = []
    def __init__(self,alist):
        self.mylist = alist
    
    def sort(self):
        N = len(self.mylist)
        for i in range(N-1):
            m = i
            for j in range(i,N-1):
                if self.mylist[m]>self.mylist[j]:
                    m = j
            self.mylist[i],self.mylist[m] = self.mylist[m],self.mylist[i]
        print(self.mylist)
        
test = SortSelection([2,4,1,6,4,8,9])
print(test.mylist)
test.sort()
        
#%%冒泡排序
"""
在第i轮遍历1~N-i位元素，临近两位渐次比较，大者推后，则
每轮将最大者推至末尾
共需进行N-1轮
因此外重循环 range(N-1)
内重循环 range(1,N-i) 或range(N-i-1)
"""
class SortBubble:
    alist = []
    
    def __init__(self,a):
        self.alist = a
    
    def sort(self):
        N = len(self.alist)
        for i in range(N-1):
            flag = True
            for j in range(N-i-1):
                if self.alist[j]>self.alist[j+1]:
                    self.alist[j],self.alist[j+1] = self.alist[j+1],self.alist[j]
                    flag = False
            if flag:
                break
            
test = SortBubble([2,4,1,3,5,9,8])       
test.sort()
test.alist

#%%归并排序
"""
很奇妙，画了一会图稍微明白了一些些

“递归的基本思想是广义地把规模大的问题转化为规模小的相似的子问题或者相似的子问题集合来解决。”

规模为N的有序列表由两个规模N/2的有序子列合并
规模N/2的有序子列由两个规模N/4的有序子列合并
……
规模2的有序子列由两个规模1的（有序）子列合并（找到出口）
"""
#%%先要搭建 从 N/2>>>N 的桥梁
#import pdb
def merge(listL,listR):
    #pdb.set_trace()
    n1 = len(listL)
    n2 = len(listR)
    #merge[] 来存合并的列表
    merge = []
    while n1>0 and n2>0:
        if listL[0]<=listR[0]:
            merge.append(listL.pop(0))
            n1 -= 1
        else:
            merge.append(listR.pop(0))
            n2 -= 1
    merge.extend(listL)
    merge.extend(listR)   
    return(merge)
    
#test
a = [2,4]
b = [1,3]
merge(a,b)

#%% final box
def ssort(alist):
    if len(alist)==1:
        return alist
    mid = len(alist)//2
    lstL = alist[:mid]
    lstR = alist[mid:]
    sortedLstL = ssort(lstL)
    sortedLstR = ssort(lstR)
    merged = merge(sortedLstL,sortedLstR)
    return(merged)
    
#test
a = [1,3,2,4]
ssort(a)
