# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 23:31:09 2022

@author: lxs_9
"""
# 정수 n을 입력받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0 for _ in range (n+2)]

# 다이나믹 프로그래밍(Dynamic Programming) 진행 BOTTOM-UP
# d리스트의 범위를 n+1으로 지정했을 경우
# n의 입력이 1이면 indexError가 발생
d[1] = 1
d[2] = 2

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

# 계산된 결과 출력
print(d[n]%10007)
