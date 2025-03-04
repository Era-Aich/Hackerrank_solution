# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:54:43 2025

@author: asus
"""

def viral_adver(n):
    shared = 5
    cumulative = 0
    
    for _ in range(n):
        liked = shared //2
        cumulative+= liked
        shared = liked * 3
        
    return cumulative


n = int(input())
re =  viral_adver(n)
print(re)
        