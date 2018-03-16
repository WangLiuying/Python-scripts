# -*- coding: utf-8 -*-
"""
排序算法：
选择排序
冒泡排序
归并排序
插入排序
希尔排序
快速排序
堆排序

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

#%%插入排序
"""
从arr的第1位开始向后遍历：
 将第一位与第零位比较，排序
 将第二位与第一位比较排序，再与第零位比较
 ……
"""
def insertSort(a):
    for i in range(1,len(a)):
        while i>0 and a[i]<a[i-1]:
            a[i],a[i-1]=a[i-1],a[i]
            i -= 1
        print(a)
        
a = [4,2,1,6,3,4]
insertSort(a)

#%%快速排序
"""
从数组中随机选择一位数，将比它大的放右边，比它小的放左边
然后对左和右递归调用
"""
#import pdb

class QuickSort:
    a = []
    def __init__(self, alist):
        self.a = alist
        
    def quickSort(self,start = 0, end = None):
        #pdb.set_trace()
        if end==None:
            end = len(self.a)-1
        if len(self.a[start:end+1])<=1:
            return None
        partition = self.a[end]
        pointer = start
        for i in range(start,end+1):
            if self.a[i]<partition:
                self.a[i],self.a[pointer] = self.a[pointer],self.a[i]
                pointer += 1
        self.a[pointer],self.a[end] = self.a[end],self.a[pointer]
        print(self.a)
        self.quickSort(start = start, end = pointer-1)
        self.quickSort(start = pointer+1, end = end)
        return None
    
b = QuickSort([4,2,1,6,3,4])
b.quickSort()
#想了很久，不太懂python的函数传递机制，只能想到定义一个类，对类中的self.a进行修改的这种方式



#%%希尔排序
"""
希尔排序(Shell Sort)是插入排序的一种。
也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。
希尔排序是非稳定排序算法。
 希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
 随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，
 整个文件恰被分成一组，算法便终止。
"""
   
def shellSort(a,step):
    while step>0:
        for i in range(step,len(a)):
            while i-step>=0 and a[i]<a[i-step]:
                a[i],a[i-step] = a[i-step],a[i]
                i -= step
        step -= 1
        
b = [4,2,1,6,3,4]
shellSort(b,2)
b

#%%堆排序
"""
堆排序(Heapsort)是指利用堆积树（堆）这种数据结构所设计的一种排序算法
，它是选择排序的一种。
可以利用数组的特点快速定位指定索引的元素。
堆分为大根堆和小根堆，是完全二叉树。
大根堆的要求是每个节点的值都不大于其父节点的值，
即A[PARENT[i]] >= A[i]。在数组的非降序排序中，需要使用的就是大根堆，
因为根据大根堆的要求可知，最大的值一定在堆顶。
"""
def adjustHeap(a, nodeId, n):
     #n最大结点序号
    lchild = nodeId*2+1
    rchild = nodeId*2+2 #左右子结点的ID
    largest = nodeId #假设这个分支结点是最大的
    if lchild<=n and a[lchild]>a[nodeId]:
        largest = lchild
    if rchild<=n and a[rchild]>a[largest]:
        largest = rchild                  #找到三点中最大的
    if nodeId!=largest: #如果分支不是最大的
        a[nodeId],a[largest] = a[largest],a[nodeId]

def findMax(a,n):
    for node in range(int((n-1)/2),-1,-1):
        adjustHeap(a,node,n)

def heapSort(a):
    for i in range(len(a))[::-1]:
        findMax(a,i)
        a[0],a[i] = a[i],a[0]
    print(a)
        
a = [1,4,2,5,6,3,7]
heapSort(a)        


#%%draft
a = [1,4,2,5,6,3,7]
