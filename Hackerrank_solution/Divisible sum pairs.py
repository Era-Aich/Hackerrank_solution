# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:34:24 2025

@author: asus
"""

n= int(input())
arr = list(map(int,input().strip().split()))
k= int(input())

count = 0
for i in range(n):
    for j in range(i+1,n):
        if (arr[i]+arr[j])%5==0:
            count+=1
        
      
        
print(count)