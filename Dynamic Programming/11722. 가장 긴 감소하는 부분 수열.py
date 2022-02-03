# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 10:56:24 2022

@author: lxs_9
"""
import sys
# 수열의 크기 n
n = int(sys.stdin.readline())
# a 수열을 이루고 있는 수를 한 줄로 입력받는다. (각 수는 띄어쓰기로 구분된다.)
a = list(map(int, sys.stdin.readline().split()))
# 부분 감소 수열의 최대 길이를 저장할 dp 리스트 의 값을 1로 초기화
dp = [1 for _ in range(n)]


for i in range(n):
    for j in range(i):
        # 현재 위치(i)보다 이전에 있는 원소(j)가 큰지 확인한다.
        
        # 크다면, 현재 위치의 이전 숫자 중, dp의 최댓값을 구하고 그 길이에 1을 더해준다.
        if a[j]>a[i]:
            dp[i] = max(dp[i], dp[j]+1)
            
# DP배열의 원소 중 가장 큰 원소를 출력한다.
print(max(dp))
