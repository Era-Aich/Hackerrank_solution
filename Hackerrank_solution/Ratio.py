# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:44:32 2025

@author: asus
"""

count1 = 0
count2 = 0
count3 = 0
n = int(input(""))

arr = list(map(int, input().strip().split()))

for num in arr:
    if num>0:
        count1+=1
    elif num<0:
        count2+=1
    else:
        count3+=1
        
ratio1 = count1/n
ratio2 = count2/n
ratio3 = count3/n

print(f"{ratio1:.6f}")

print(f"{ratio2:.6f}")

print(f"{ratio3:.6f}")