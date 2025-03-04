# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 18:48:10 2025

@author: asus
"""

def append_delete(s,t,k):
    complete_length =0
    for i in range(min(len(s),len(t))):
        if s[i] == t[i]:
            complete_length+=1
        else:
            break
        
    deletion = len(s) - complete_length
    insertion = len(t) - complete_length 
    total = deletion + insertion
    
    if total==k:
        return "Yes"
    elif total<=k and (k-total)%2==0:
        return "Yes"
    elif len(s)+len(t)<=k:
        return "Yes"
    else:
        return "No"
    

s= input().strip()
t= input().strip()
k= int(input())

re = append_delete(s, t, k)
print(re)