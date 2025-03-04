# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:12:36 2025

@author: asus
"""

def beautiful(i,j,k):
    count  = 0
    for day in range(i,j+1):
        reverse_day = int(str(day)[::-1])
        if abs(day-reverse_day)%k ==0:
            count+=1
            
    return count


i,j,k = map(int,input().split())
result = beautiful(i, j, k)
print(result)