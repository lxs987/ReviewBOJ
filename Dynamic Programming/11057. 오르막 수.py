# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 16:19:08 2022

@author: lxs_9
"""
# 자릿수 N 입력받기
n = int(input())

# 0~9의 길이를 갖는 리스트를 n+1개의 2차원 리스트로 만들기
# input이 0일 때 index error를 방지하기 위해 n+"2"로 범위 지정
dp = [[0 for _ in range(10)] for _ in range(n+2)]

# 일의자리 숫자는 모든 수가 각 하나의 오르막수이므로 1로 초기화
for j in range(0, 10):
    dp[1][j] = 1

# 마지막 자릿수가 올 수 있는 경우의 수를 구해 dp테이블에 삽입
for i in range(2, n+1):
    # 점화식 = [앞자릿수][10-index] 이므로 테이블의 index를 활용
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:])

print(sum(dp[n])%10007)
