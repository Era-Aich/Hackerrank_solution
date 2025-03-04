# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 20:01:36 2025

@author: asus
"""

def minimum(n,arr):
    listi=[]
    
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                x=abs(j-i)
                listi.append(x)
            
                
    y=min(listi)
    return y
    return -1
    


n= int(input())
arr=list(map(int,input().strip().split()))
re= minimum(n, arr)
print(re)