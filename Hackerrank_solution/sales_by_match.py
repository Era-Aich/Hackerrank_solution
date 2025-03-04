# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 11:34:00 2025

@author: asus
"""

def sales_by_match(n,arr):
    socks = set()
    pairs = 0
    for sock in arr:
        if sock in socks:
            pairs+=1
            socks.remove(sock)
        else:
            socks.add(sock)
    return pairs


n = int(input())
arr = list(map(int, input().split()))

result = sales_by_match(n, arr)
print(result)
        