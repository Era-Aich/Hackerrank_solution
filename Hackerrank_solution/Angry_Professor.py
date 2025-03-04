# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 08:38:36 2025

@author: asus
"""

def angryProfessor(n,k, a):
    count = 0
    for i in range(n):
        if a[i]<=0:
            count+=1
    if count >= k:
        return "Yes"
    else:
        return "NO"
    
t = int(input())
for j in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().strip().split()))
    
    re = angryProfessor(n, k, a)
    print(re)