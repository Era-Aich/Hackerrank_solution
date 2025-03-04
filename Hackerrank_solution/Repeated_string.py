# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 11:10:59 2025

@author: asus
"""

def repeated_string(s,n):
    actual_string = s.count('a')
    string = n//len(s)
    remainder= n%len(s)
    
    total=(actual_string*string)+remainder
    return total
    
    
s= input().strip()
n= int(input())
result = repeated_string(s, n)
print(result)