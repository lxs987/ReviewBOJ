# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 23:46:36 2022

@author: lxs_9
"""
# 정수 n을 입력받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0 for _ in range(n+2)]

# 다이나믹 프로그래밍(Dynamic Programming) 진행 BOTTOM-UP
d[1] = 1

# 2×2 를 채우는 방법은 2×1, 1×2, 2×2 총 3가지
d[2] = 3

for i in range(3, n+1):
    d[i] = d[i-2]*2 + d[i-1]
    
# 계산된 결과 출력
print(d[n]%10007)
