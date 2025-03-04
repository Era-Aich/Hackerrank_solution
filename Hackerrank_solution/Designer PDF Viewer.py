# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:24:05 2025

@author: asus
"""

def pdf_viewer(h,word):
    
   
  
    h = max(h[ord(letter) - ord('a')] for letter in word)
    area = h *len( word)
    return area

h = list(map(int,input().strip().split()))
word = input()
result = pdf_viewer(h, word)
print(result)
        