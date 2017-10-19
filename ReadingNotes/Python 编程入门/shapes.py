# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 15:24:49 2017

@author: River

python编程入门 模块
"""
##模块是一个由函数组成的工具箱，用于编写其它程序。因此，模块通常没有main函数

"""
A collection of functions for printing basic shapes.
"""
CHAR="*"

def rectangle(height,weight):
    """prints a rectangle."""
    for row in range(height):
        for col in  range(weight):
            print(CHAR,end="")
        print()

        
def triangle(height):
    """prints a triangle"""
    for row in range(height):
        for col in range(1,row+2):
            print(CHAR,end="")
        print("")

