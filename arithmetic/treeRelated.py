# -*- coding: utf-8 -*-
"""
二叉树
定义了二叉树类和二叉排序树类
实现 树搜寻，树遍历，排序树的增删
Created on Sat Mar 10 22:39:36 2018

@author: Liuying Wang
"""
#%%实现二叉树类型
class BinaryTree:
    tree = []

    #初始化，给出根节点
    def __init__(self, rootVar):
        self.tree = [rootVar,[],[]]
        
    #给出父节点，在节点的左侧加入子节点
    def insertLeft(self, parent, value):
        childnode = parent.pop(1)
        if len(childnode)>0:
            parent.insert(1,[value,childnode,[]])
        else:
            parent.insert(1,[value,[],[]])

    
    #给出父节点，在节点的右侧加入子节点
    def insertRight(self, parent, value):
        childnode = parent.pop(2)
        if len(childnode)>0:
            parent.insert(2,[value,[],childnode])
        else:
            parent.insert(2,[value,[],[]])
    
    #给定父节点，找到左子结点        
    def getLeftChild(self, parent):
        return parent[1]
    
    def getRightChild(self, parent):
        return parent[2]
    
    #更改某个节点的值    
    def changeNodeValue(self, node, newValue):
        if len(node)>0:
            node[0]=newValue
        else:
            node = [newValue,[],[]]
            
    #取出某个节点的值
    def getNodeValue(self, node):
        return node[0]
        
    #先序遍历:根-左-右
    def preOrder(self, node = None):
        if node==None:
            node = self.tree
        if len(node)!=0:
            print(node[0], end = ' ')
            self.preOrder(node[1])
            self.preOrder(node[2])
     
    #中序遍历：左根右
    def inOrder(self, node = None):
        if node==None:
            node = self.tree
        if len(node)!=0:
            self.inOrder(node[1])
            print(node[0], end = ' ')
            self.inOrder(node[2])
    
    #后序遍历：左右根
    def postOrder(self, node = None):
        if node==None:
            node = self.tree
        if len(node)!=0:
            self.postOrder(node[1])
            self.postOrder(node[2])
            print(node[0], end = ' ')
            
    #计算节点总数
    def countNodes(self, node=tree):
        if len(node)==0:
            return 0
        else:
            nL = self.countNodes(node[1])
            nR = self.countNodes(node[2])
            return 1+nL+nR

#%%test
test = BinaryTree(3)
print(test.tree)
test.insertLeft(test.tree,5)
test.insertRight(test.tree,1)
test.insertLeft(test.getLeftChild(test.tree),2)
print(test.tree)
test.changeNodeValue(test.getRightChild(test.tree),5)
print(test.tree)
test.getNodeValue(test.tree)
test.preOrder()
print('')
test.inOrder()
print('')
test.postOrder()

#%% 排序树
class SortTree(BinaryTree):

    #树的查找：
    def search(self, num, node = None, record = 'root'):
        if record=='root':
            record = ['Root']
            node = self.tree
        if len(node)==0:
            print("The number %2f is not in tree!" %num)
            return None
        if num==node[0]:
            record.append('Here')
            print(record)
            return None
        elif num<node[0]:
            record.append('Left')
            self.search(num, node[1], record)
        else:
            record.append('Right')
            self.search(num, node[2], record)
    
    #插入一个数
    def insert(self, num, node = None):
        if node==None:
            node = self.tree
        if len(node)==0:
            node = [num,[],[]]
            return node
        if num<=node[0]:
            node[1] = self.insert(num, node[1])
            return node
        else:
            node[2] = self.insert(num, node[2])
            return node
        
    #析构函数,重定义一个初始化方法
    def __init__(self, alist):
        if len(alist)==0:
            raise ValueError('invalid input')
        else:
            self.tree = [alist.pop(),[],[]]
        while len(alist)>0:
            self.insert(alist.pop())
        return None
        
    #取得最大值
    def __getmax(self, node=None):
        if node==None:
            node = self.tree
        if node[2]==[]:
            m = node[0]
            if node[1]==[]:
                node.clear()
            else:
                node[:] = node[1]
            return m
        else:
            return self.__getmax(node[2])

    #从排序树移除一个数字
    def delete(self, num, node=None):
        if node==None:
            node = self.tree
        if len(node)==0:
            print("The number %2f is not in tree!" %num)
            return None
        if num==node[0]:
            if node[1]==[] and node[2]==[]:
                node[:] = []
            elif node[1]!=[] and node[2]==[]:
                node[:] = node[1]
            elif node[2]!=[] and node[1]==[]:
                node[:] = node[2]
            else:
                m = self.__getmax(node[1])
                node[0] = m
            return None        
        elif num<node[0]:
            self.delete(num, node[1])
        else:
            self.delete(num, node[2])         
          

    
#%%test 
tree = SortTree([50,15,12,23,52,74,30])
tree.search(25)
tree.insert(25)
tree.inOrder()

tree.tree
tree.delete(15)
