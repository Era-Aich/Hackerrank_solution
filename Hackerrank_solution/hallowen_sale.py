# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 09:58:10 2025

@author: asus
"""

def hallowen_sale(p,d,m,s):
    count = 0
    
    while(s>=p):
        s-=p
        count+=1
        p=max(p-d,m)
    return count


p,d,m,s = map(int,input().strip().split())
re = hallowen_sale(p, d, m, s)
print(re)   