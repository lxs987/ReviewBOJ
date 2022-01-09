# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 00:43:02 2022

@author: lxs_9
"""

# 합을 나타낼 때는 수를 1개 이상 사용해야 한다 라는 조건이 있으므로
# 만약 n이 2라면 1+1, 2 이렇게 2가지로 표현할 수 있음
# n이 3이라면 1+1+1, 1+2, 2+1, 3 총 4가지
lst = [0 for _ in range(12)]
lst[1] = 1
lst[2] = 2
lst[3] = 4
for i in range(4, 11):
   lst[i] = lst[i-3]+lst[i-2]+lst[i-1]
   
# 테스트케이스 t
t = int(input())
for i in range(t):
    n = int(input())
    print(lst[n])
