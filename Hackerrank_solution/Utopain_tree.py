# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:42:09 2025

@author: asus
"""

def utopin(n):
    H = 1
    for cycle in range(1,n+1):
        if cycle%2 !=0:
            H *=2
        else:
            H+=1
    return H




t = int(input())
for _ in range(t):
    n = int(input())
    re= utopin(n)
    print(re)
    