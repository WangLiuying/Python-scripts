# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 23:00:28 2017

@author: River
"""
#%%
import os
os.chdir("D:\DataAnalysis\python\headfirstpython\hfpy_ch6_data")
os.getcwd()

#%%
"""def a function for reading file"""
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline().strip().split(",")
        return data
    except IOError as ioerr:
        print("file error:"+str(ioerr))
    return None
    
def sanitize(time_string):
    if "-" in time_string:
        splitter="-"
    elif ":" in time_string:
        splitter=":"
    else:
        return time_string
    (mins,secs)=time_string.split(splitter)
    return(mins + "." + secs)
    
#%%    
james=get_coach_data("james2.txt")
(james_name,james_bod)=james.pop(0),james.pop(0)
print(james_name+"' fastest times are: "+str(sorted(set([sanitize(t) for t in james]))[0:3]))

"""创建字典"""
cleese={}
type(cleese)
palin=dict()
type(palin)


cleese["name"]="John Cleese"
cleese["Occupations"]=['actor','comedian','writer','film producer']
palin={"name":'Michael Palin','Occupations':['comedian','actor','writer','tv']}
palin['name']
palin['Occupations'][-1]


"""使用字典数据结构处理健身数据"""
sarah=get_coach_data("sarah2.txt")
sarah_data={'name':sarah.pop(0),'dob':sarah.pop(0),'times':[float(sanitize(t)) for t in sarah]}

#%%           
"""定义一个类"""
class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name=a_name
        self.dob=a_dob
        self.times=a_times
    
    def top3(self):
        return(sorted(set(self.times))[0:3])
    
    def add_times(self,time_value):
        self.times.extend(time_value)
        return None

        
        
 #%%

sarah=get_coach_data('sarah2.txt')
sarah=Athlete(sarah.pop(0),sarah.pop(0),[float(sanitize(t)) for t in sarah])
james=Athlete('James Jones')
type(sarah)
sarah;james
sarah.name
sarah.times
james.times
sarah.top3()

#%%

vera=Athlete('Vera Vi')
vera.add_times([1.41])
print(vera.top3())
vera.add_times([1.43,2.13,2.22])
print(vera.top3())


#%%
"""如何继承list类"""
class NamedList(list):
    def __init__(self,a_name):
        list.__init__([])
        self.name=a_name
johnny=NamedList('John Paul Jones')
type(johnny)
dir(johnny)

#%%
johnny.append('Bass Player')
johnny.extend(['Compposer','Arranger','Musician'])
johnny
johnny.name

#%%           
"""定义一个类"""
class AthleteList(list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name=a_name
        self.dob=a_dob
        list.__init__([])
        self.extend(a_times)
    
    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])

vera=AthleteList('Vera Vi')
vera.append('1.31')
vera.extend(['1.32','2:33','0:14'])
vera
vera.top3()

