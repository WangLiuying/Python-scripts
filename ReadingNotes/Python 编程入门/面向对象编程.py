# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:54:50 2017
python编程入门 面向对象编程
@author: River
"""

#%%编写类
class Person:
    """class to represent a person"""
    def __init__(self,name='',age=0):
        self.name=name
        self.age=age
    def display(self):
        print('Person("%s","%d")' %(self.name,self.age))
    def __str__(self):
        return 'Person("%s , %d")' %(self.name,self.age)
    def __repr__(self):
        return str(self)
per=Person()
per
per.age
per.name='Moe'
per.name
per.display()

str(per)
per

#%%特性装饰器 没看懂，参考以前的笔记

#%%私有变量命名为 p._age

#调用时需要用 p._Person__age

#%%继承
class Player:
    def __init__(self,name):
        self._name=name
        self._score=0
    def reset_score(self):
        self._score=0
    def incr_score(self):
        self._score=self._score + 1
    def get_name(self):
       return self._name
    def __str__(self):
        return "name='%s',score='%d'." %(self._name,self._score)
    def __repr__(self):
        return "Player('%s')" % str(self)

#test
p=Player("Mona")
p
p.incr_score()
p
p.reset_score()
p

#%%
class Human(Player):#继承
    def __repr__(self):
        return "Human('%s')" %str(self)
    def get_move(self):
        while True:
            try:
                n=int(input("%s move (1-10)" %self.get_name()))
                if 1 <= n <= 10:
                    return n
                else:
                    print("Oops!")
            except:
                print("Oops!")
import random                
class Computer(Player):
    def __repr__(self):
        return "Computer('%s')" %str(self)
    def get_move(self):
        return random.randint(1,10)    
        
#%%多态

def play_undercut(p1,p2):
    p1.reset_score()
    p2.reset_score()
    m1=p1.get_move()
    m2=p2.get_move()
    if m1 == m2 - 1:
        return p1,p2,"%s wins!" %p1
    elif m2 == m1 - 1:
        return p1,p2,"%s wins!" %p2
    else:
        return p1,p2,"draw: no winner"
 
#test
c=Computer("Hal Bot")
h=Human("Lia")
play_undercut(c,h)

        