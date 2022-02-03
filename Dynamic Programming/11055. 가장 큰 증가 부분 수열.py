# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 10:28:12 2022

@author: lxs_9
"""
# 참고: https://m.blog.naver.com/occidere/220793914361

import sys
# 수열의 크기 n
n = int(sys.stdin.readline())
# a 수열을 이루고 있는 수를 한 줄로 입력받는다. (각 수는 띄어쓰기로 구분된다.)
a = list(map(int, sys.stdin.readline().split()))
dp = []
max = 0

# 부분 증가 수열의 최대 합을 저장할 dp 리스트 의 값을 a[i]로 초기화
for i in range(n):
    # 비교 기준이 각 요소들의 합의 크기이므로
    # dp[i]의 초기값을 전부 a[i]로 초기화
    dp.append(a[i])
    
    # 만약 증가하는 수열임과 동시에
    # 현재 dp[i]의 값이 dp[j]+a[i]보다 작다면
    # dp[i]의 값을 dp[j]+a[i]로 초기화
    for j in range(i):
        if (a[j]<a[i]) and (dp[i] < dp[j]+a[i]):
            dp[i] = dp[j] + a[i]
            
    # max값이 dp[i]보다 작다면 dp[i]값으로 초기화
    if (max < dp[i]):
        max = dp[i]
        
# 합의 최댓값 출력
print(max)
