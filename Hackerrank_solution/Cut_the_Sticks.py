# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:45:32 2025

@author: asus
"""

def Cutthe_sticks(arr):
    arr.sort()
    result = []
    
    while arr:
        result.append(len(arr))
        smallest = arr[0]
        new_arr = []
        
        for stick in arr:
            if stick - smallest > 0:
                new_arr.append(stick - smallest)
                
            arr = new_arr
    return result


n = int(input().strip())
arr = list(map(int,input().strip().split()))
for count in Cutthe_sticks(arr):
    print(count)
                
            
        
        