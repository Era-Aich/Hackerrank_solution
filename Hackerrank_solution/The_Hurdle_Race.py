# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 17:36:25 2025

@author: asus
"""

def hurdle(n,k,arr):
    
    
        arr = max(arr)
        if arr>k:
            return arr - k
        else:
            return 0
        

n,k = map(int,input().split())
arr = list(map(int,input().strip().split()))

re = hurdle(n, k, arr)
print(re)