# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 20:24:27 2017

@author: River
"""

#%%
#文件存储

#==============================================================================
# f=open(filename,way)
# 'r'-read
# 'w'-write
# 'a'-append
#==============================================================================

#'r'
#==============================================================================
# f.read(10) 读取10个字节
# f.readline() 读一行
# f.readlines() 读取所有行并存储为列表
#==============================================================================

#'w'
f=open('test.txt','w')
f.write('I like apple\r\n')
f.close()

#%%
#上下文管理器
f=open('new.txt','w')
f.closed
f.write('hello world')
f.close()
f.closed

with open('new.txt','w') as f:
    f.write('hello world')

print(f.closed)

#%%
class Vow:
    text=""
    def __init__(self,text):
        self.text=text
    def __enter__(self):
        self.text='I say:'+self.text
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        self.text=self.text+'!'
        
with Vow("I'm fine") as v:
    print(v.text)    
print(v.text)
"""pickle"""
#%%
#pickle 存储数据
import pickle
class Bird:
    have_feather=True
    reproduction_method='egg'
    
summer=Bird()
pickle_string=pickle.dumps(summer)

with open('summer.pickle','wb') as f:
    f.write(pickle_string)
    
#%%
with open('summer.pickle','wb') as f:
     pickle.dump(summer,f)
#%%
with open('summer.pickle','rb') as f:
    summer=pickle.load(f)

#%%
"""time"""
import time
time.time()
help(time.time)
time.clock()
help(time.clock)

#%%计时
start=time.clock()
for i in range(1000):
    print(i**2)
end=time.clock()
end-start

#%%程序休眠
print('start')
time.sleep(10)
print('wake up')

#%%结构时间
st=time.gmtime()
st=time.localtime()
time.mktime(st)

#%%
"""datetime"""
import datetime
t=datetime.datetime(2012,9,3,21,30)
t_delta=datetime.timedelta(seconds=600)
t_next=t+t_delta
print(t_next)
print(t>t_next)

#%%
import datetime
str='output-1993-12-03-010000.txt'
format='output-%Y-%m-%d-%H%M%S.txt'
t=datetime.datetime.strptime(str,format)
print(t)
#%A星期几,%a星期几简写,%I12小时制时间,%p上午下午,%毫秒

#%%
"""正则表达式"""
import re
m=re.search("[0-9]","abcd4ef")
print(m.group(0))
#re.search(pattern,string)
#re.match(pattern,string)
#str=re.sub(pattern,replacement,string)
re.split()
re.findall()

#%%
content="abcd_output_1994_abcd_1912_abcd"
m=re.search("output_\d{4}",content)
m.group(0)
m.group(1) #error
m=re.search("output_(\d{4})",content)
m.group(0)
m.group(1)
m=re.search("output_(?P<year>\d{4})",content)
m.group(0)
m.group(1)
m.group('year')

#%%
"""http.client"""
import http.client
conn=http.client.HTTPConnection("www.example.com")
conn.request("GET","/")
response=conn.getresponse()
print(response.status,response.reason)
content=response.read()
print(content)


#%%
import http.client
conn=http.client.HTTPConnection("www.cnblogs.com")
conn.request("GET","/Vamei")
response=conn.getresponse()
content=response.read()
content=content.split("\r\n")

import re
pattern="posted(?P<time>\d{4}-\d{2}-\d{2} \d{2}:\d{2}) Vamei 阅读\((?P<read>\d+)\) 评论\((?P<comment>\d+)\)" 
for line in content:
    m=re.search(pattern,line)
    if m != None:
        print(m.group(1),m.group(2),m.group(3))
        
dir(m)


#%%
"""定义运算符函数"""
class SuperList(list):
    def __sub__(self,b):
        a=self[:]
        b=b[:]
        for b_element in b:
            if b_element in a:
                a.remove(b_element)
        return a

print(SuperList([1,2,3])-SuperList([3,4]))
#%%
"""元素引用"""
li=[1,2,3,4,5,6]
print(li[3])
print(li.__getitem__(3))

li[3]=1
li
li.__setitem__(3,2)
li

li.__delitem__(3)
li

#%%属性管理
class Bird(object):
    feather=True
    
    def chirp(self):
        print("some sound")
    
class Chicken(Bird):
    fly=False
    
    def __init__(self,age):
        self.age=age
        
    def chirp(self):
        print("ji")
        
summer=Chicken(2)
print("===>summer")
print(summer.__dict__)

print("===>Chicken")
print(Chicken.__dict__)

print("===>object")
print(object.__dict__)

autumn=Chicken(3)
autumn.feather=False
summer.feather
Bird.feather=False
summer.feather#父类属性变动会动态地影响子类

#%%特性
class Bird:
    feather=True
    
class Chicken(Bird):
    fly=False
    def __init__(self,age):
        self.age=age
    
    def get_adult(self):
        if self.age>1.0:
            return True
        else:
            return False
    adult=property(get_adult)
    
summer=Chicken(2)
print(summer.adult)

class num(object):
    def __init__(self,value):
        self.value=value
    
    def get_neg(self):
        return -self.value
        
    def set_neg(self,value):
        self.value=-value
        
    def del_neg(self):
        print("value also delete")
        del self.value
        
    neg=property(get_neg,set_neg,del_neg,"I'm negative.")

x=num(1.1)
print(x.neg)
x.neg=-22
print(x.value)
print(num.neg.__doc__)
del x.neg

#%%getattr()
class chicken(Bird):
    fly=False
    
    def __init__(self,age):
        self.age=age
        
    def __getattr__(self,name):
        if name=="adult":
            if self.age>1:
                return True
            else:
                return False
        else:
            raise AttributeError(name)

summer=Chicken(2)
print(summer.adult)

#%%
"""动态类型"""
a=1
print(id(1))
print(id(a))

a=3
print(id(a))
a="at"
print(id(a))

a=3
b=3
a is b

#%%
"""可变与不可变对象"""
a=5
print(id(a))
b=a
print(id(a))
print(id(b))
a=a+2
print(id(a))
print(id(7))
print(id(b))


#%%
list2=[1,2,3]
list1=list2
list1[0]=10
list2

#%%引用管理
def print(id(x)):
    x=100
