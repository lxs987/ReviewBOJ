# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 11:05:05 2022

@author: lxs_9
"""
# 정수 X를 입력받기
x = int(input()) 


# 앞서 계산된 결과를 지정하기 위한 DP 테이블 초기화
# d = [0]*10000001 이 식보단 아래 식으로 DP 테이블 초기화
d = [0 for _ in range(x+1)]

# 다이나믹 프로그래밍 진행(BOTTOM-UP)
for i in range(2, x+1):
    
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1]+1
    
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i%2==0:
        d[i] = min(d[i], d[i//2]+1)
        
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i%3==0:
        d[i] = min(d[i], d[i//3]+1)
    
print(d[x])
