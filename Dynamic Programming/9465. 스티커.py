# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 22:44:57 2022

@author: lxs_9
"""
# testcase t 입력받기
t = int(input())

for i in range(t):
    # 스티커의 점수를 저장할 list
    s = []
    # 2×n 개의 스티커이므로 n 입력받기
    n = int(input())
    for k in range(2):
        # 스티커의 점수를 한 줄씩 띄어쓰기로 구분하여 입력받기(총2줄)
        s.append(list(map(int, input().split())))
        
    for j in range(1, n):
        # 첫번째의 경우, 대각선에 있는 스티커의 점수를 더한다.
        if j==1:
            s[0][j] += s[1][j-1]
            s[1][j] += s[0][j-1]
        # 두번째부터는 대각선 or 그 옆에 있는 스티커의 점수를 비교하여 큰 값을 더한다
        else:
            s[0][j] += max(s[1][j-1], s[1][j-2])
            s[1][j] += max(s[0][j-1], s[0][j-2])
            
    # 각 테스트 케이스 마다 스티커 점수의 최댓값을 출력한다.
    print(max(s[0][n-1], s[1][n-1]))
