# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 12:33:29 2022

@author: lxs_9
"""

# 포도주 잔의 개수 n
n = int(input())

# 각 포도주의 양을 저장할 리스트 lst (index error를 방지하기 위해 n+3까지 생성)
lst = [0 for _ in range(n+3)]

# 입력된 각 포도주의 양을 리스트에 저장
for i in range(1, n+1):
    lst[i] += int(input())

# 마실 수 있는 최대의 포도주 양을 저장할 리스트 dp 선언 (index error 방지)
dp = [0 for _ in range(n+3)]

# 잔이 1개, 2개일 경우 최댓값을 미리 저장 
# 잔이 2개 이하일 경우 조건을 고려하지 않아도 되므로
# 다 마시는 것이 최댓값이다.
dp[1] = lst[1]
dp[2] = lst[1] + lst[2]

# 잔이 3개 이상일 경우 
for i in range(3, n+1):
    # i번째 잔을 마신다고 가정할 때 OXO로 마실지, XOO로 마실 지
    dp[i] = max(dp[i-3] + lst[i-1] + lst[i], dp[i-2] + lst[i])
    # 연속으로 두 잔을 마시지 않을 경우도 고려한다.
    # 예시) 100, 400, 2, 1, 4, 200가 주어졌을 때, 위 식만 고려하면
    # 결과는 701이 나온다. 그러나 나올 수 있는 최댓값은 704이다
    # 따라서 2번 연속 먹지 않았을 때 최댓값일 수 있으므로 아래 식을 추가한다.
    dp[i] = max(dp[i-1], dp[i])
    
print(dp[n])
