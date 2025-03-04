# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 07:49:41 2025

@author: asus
"""

def kangkaro(x1,v1,x2,v2):
    if v1 == v2:
        return "Yes" if x1==x2 else "NO"
    if (x2-x1)%(v1-v2)==0 and (x2-x1)/(v1-v2)>=0:
        return "Yes"
    
    return "NO"
    
    
    
x1,v1,x2,v2 = map(int,input().split())
result = kangkaro(x1, v1, x2, v2)
print(result)