# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 08:47:56 2025

@author: asus
"""

def library_fine(d1,m1,y1,d2,m2,y2):
    if y1 < y2 or (y1 == y2 and m1 < m2) or (y1 == y2 and m1 == m2 and d1 <= d2):
        return 0
    if d1<=d2 and m1==m2 and y1==y2:
        fine = 0
        
        return fine
    elif d1>d2 and m1==m2 and y1==y2:
        fine = 15 * (d1-d2)
        return fine
    elif  d1==d2 and m1>m2 and y1==y2:
        fine = 500 * (m1-m2)
        return fine
    elif d1!=d2 and m1!=m2 and y1>y2:
        fine = 10000
        return fine
    

d1 ,m1 ,y1 = map(int,input().strip().split())
d2 ,m2 ,y2 = map(int,input().strip().split())

result = library_fine(d1, m1, y1, d2, m2, y2)
print(result)