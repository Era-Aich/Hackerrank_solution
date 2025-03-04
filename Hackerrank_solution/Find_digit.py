# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:57:02 2025

@author: asus
"""
def find_digit(n,listi):
    
    count = 0
    for num in listi:
        for digit in str(num):
            if digit != '0' and num% int(digit)==0:
                count+=1
            return count

n = int(input())  # Number of test cases
listi = list(map(int, input().strip().split()))  # Read input list

result = find_digit(n, listi)
print(result)