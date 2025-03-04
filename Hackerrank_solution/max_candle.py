# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 08:58:03 2025

@author: asus
"""
n = int(input())
count = 1

arr = list(map(int,input().strip().split()))

max_can = arr[0]

for i in range(1, n):
    if arr[i]>max_can:
        max_can = arr[i]
        count = 1
    elif arr[i] == max_can:
        count += 1 
   
        
print(count)
        