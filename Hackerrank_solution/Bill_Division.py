# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 06:42:33 2025

@author: asus
"""

n,k= map(int,input().split())

bill = list(map(int,input().strip().split()))

b = int(input())
actual_share = (sum(bill) - bill[k])//2

if b == actual_share:
    print("Bon Appetit")
else:
    print(b - actual_share)

    