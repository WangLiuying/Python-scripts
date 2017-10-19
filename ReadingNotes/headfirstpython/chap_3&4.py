# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:52:39 2017

@author: River

reference:headfirstPython chapter3

"""
import os
os.getcwd()
os.chdir("D:\DataAnalysis\python\headfirstpython\chap_3")
os.getcwd()

data=open("sketch.txt")
print(data.readline(),end="")
print(data.readline(),end="")

data.seek(0)
for each_line in data:
    print(data.readline(),end="")
data.close()


data=open("sketch.txt")
for each_line in data:
    try:
        (role,line_spoken)=each_line.split(":",1)
        print(role,end="")
        print("  said:  ",end="")
        print(line_spoken,end="")
    except:
        pass

data.close()

help(each_line.split)

try:
    data=open("sketch.txt")
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(":",1)
            print(role,end="")
            print("  said:  ",end="")
            print(line_spoken,end="")
        except ValueError:
            pass
    data.close()
except IOError:
    print("the file is missing!")
    
    
try:
    man=[]
    other=[]
    data=open("sketch.txt")
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(":",1)
            line_spoken=line_spoken.strip() #delete blank spaces
            if(role=="Man"):
                man.append(line_spoken)
            elif(role=="Other Man"):  #elif=else if
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
    try:
        man_file=open("man_data.txt","w")
        print(man,file=man_file)
        other_file=open("other_data.txt","w")
        print(other,file=other_file)
    except IOError:
        print("file error")
    finally:
        if man_file in locals():
            man_file.close()
        if other_file in locals():
            other_file.close()
except IOError:
    print("the file is missing!")
    


try:
    data=open("missing.txt")
    print(data.readline(),end="")
except IOError as err:
    print("file error:"+ str(err))
finally:
    if data in locals():
        data.close()
        
try:
    with open("its.txt","w") as data:
        print("It's ...", file=data)
except IOError as err:
    print("file error"+str(err))

try:
    with open("man_data.txt","w") as man_data, open("other_data.txt","w") as other_data:
        print(man,file=man_data)
        print(other,file=other_data)
except IOError as err:
    print("file error" + str(err))


import nester

try:
    with open("man_data.txt","w") as man_data, open("other_data.txt","w") as other_data:
        nester.print_lol(man,fn=man_data,level=1)
        nester.print_lol(other,fn=other_data,level=1)
except IOError as err:
    print("file error" + str(err))            
            
"""dump saving, load  loading"""

import pickle

with open("mydata.pickle","wb") as mysavedata:
    pickle.dump(man,mysavedata)
    
with open("mydata.pickle","rb") as mysavedata:
    alist=pickle.load(mysavedata)
print(alist)


import pickle
try:
    with open("man_data.txt","wb") as man_data, open("other_data.txt","wb") as other_data:
        pickle.dump(man,man_data)
        pickle.dump(other,other_data)
except pickle.pickleError as err:
    print("file error" + str(err))          
    
with open("man_data.txt","rb") as mysdata: 
    alist=pickle.load(mysdata)
            