# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 08:04:15 2025

@author: asus
"""

def subarray(arr,d,m):
    count = 0
   
    for i in range(0,m):
        if sum(arr[i:i+m])==d:
            count+=1
    return count


n= int(input())
arr = list(map(int,input().strip().split()))
d,m = map(int,input().split())

result = subarray(arr, d, m)
print(result)