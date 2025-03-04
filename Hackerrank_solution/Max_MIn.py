# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:51:48 2025

@author: asus
"""

arr = list(map(int,input().strip().split()))
total = sum(arr)
min_sum = total - max(arr)
max_sum  = total - min(arr)

print(min_sum, max_sum)
