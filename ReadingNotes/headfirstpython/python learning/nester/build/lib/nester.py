# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:44:04 2017

@author: River
"""


import sys    
def print_lol(the_list,level=0,indent=False,fn=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,fn)
        else:
            if(indent):
                print("\t"*level,end="",file=fn)
                #for tab_stop in range(level):
                 #   print("\t",end="")
            print(each_item,file=fn)

