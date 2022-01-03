# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 10:55:53 2022

@author: lxs_9
"""
# 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
n = [0]*100

n[1] = 1
n[2] = 2
max=99

for i in range(3, max+1):
    n[i] = n[i-1]+n[i-2]

print(n[max])