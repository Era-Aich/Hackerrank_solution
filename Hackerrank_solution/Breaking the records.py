# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:20:08 2025

@author: asus
"""

def breaking_records(score):
    max_score=min_score=score[0]
    max_count=min_count = 0
    
    for scores in score[1:]:
        if scores>max_score:
            max_score = scores
            max_count+=1
        elif scores<min_score:
            min_score = scores
            min_count+=1
            
    return max_count,min_count




n = int(input())
score = list(map(int,input().strip().split()))

c1,c2 = breaking_records(score)

print(c1,c2)