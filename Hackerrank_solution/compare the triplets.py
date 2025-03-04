# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 09:04:35 2025

@author: asus
"""

def compare(a,b):
   
    count1 = 0
    count2 = 0
  #  result1 = []
   # result2 = []
  
    for i in range(3):
        if a[i]>b[i]:
            count1+=1
            
           # result1.append(count1)
        elif a[i]<b[i]:
            count2+=1
        else:
            pass
            
   
    return count1, count2


a = list(map(int,input().strip().split()))
b = list(map(int,input().strip().split()))

c1, c2= compare(a, b)

print(c1,c2)