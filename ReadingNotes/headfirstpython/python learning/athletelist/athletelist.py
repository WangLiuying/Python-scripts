# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 13:54:22 2017

@author: River

AthleteList mold
"""



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
"""def a function for reading file"""
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline().strip().split(",")
            data=AthleteList(data.pop(0),data.pop(0),data)
        return data
    except IOError as ioerr:
        print("file error:"+str(ioerr))
    return None
    

    

    