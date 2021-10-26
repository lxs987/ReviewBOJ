# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 11:28:41 2021

@author: lxs_9
"""
# 정수 X를 입력받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0 for _ in range(x+1)]

# 다이나믹 프로그래밍(Dynamic Programming) 진행(bottom-up)
for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1]+1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i%2==0:
        d[i] = min(d[i], d[i//2]+1)
    #현재의 수가 3으로 나누어 떨어지는 경우
    if i%3==0:
        d[i] = min(d[i], d[i//3]+1)
        
print(d[x])