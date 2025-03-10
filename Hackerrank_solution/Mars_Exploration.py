# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 09:25:01 2025

@author: asus
"""

def mars(s):
    expected = "SOS"*(len(s)//3)
    count = 0
    for i in range(len(s)):
        if s[i]!=expected[i]:
            count+=1
            
    return count
            
s=input().strip()
re= mars(s)
print(re)