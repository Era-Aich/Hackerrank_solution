# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:40:11 2025

@author: asus
"""

q = int(input())

for q_itr in range(q):
    xyz = list(map(int,input().strip().split()))
    x= xyz[0]
    y=xyz[1]
    z=xyz[2]
    
    catA_pro = abs(z-x)
    
    catB_pro = abs(z-y)
    
    if catA_pro< catB_pro:
        print("Cat A")
    elif catB_pro<catA_pro:
        print("Cat B")
    else:
        print("Mouse C")