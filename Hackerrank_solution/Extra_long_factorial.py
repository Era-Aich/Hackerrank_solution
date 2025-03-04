# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:47:08 2025

@author: asus
"""

def fact(n):
    if n == 0:
        return 1
    elif n>0:
        return n * fact(n-1)
    
    
    
n = int(input())
result = fact(n)
print(result)