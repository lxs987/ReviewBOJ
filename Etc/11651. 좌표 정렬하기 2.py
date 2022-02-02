# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 14:59:12 2022

@author: lxs_9
"""
import sys
# 좌표의 갯수 입력받기
n = int(sys.stdin.readline())
# 좌표를 저장할 리스트 선언
lst = []
# 띄어쓰기로 구분하여 x좌표, y좌표를 각각 입력받아 리스트로 저장
# 예시) [[x, y], [x, y], ...]
for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))
# lambda를 사용하여 정렬(x[1](y좌표)와 x[0](x좌표) 차례로)
lst.sort(key=lambda x: (x[1], x[0]))
# 정렬된 순으로 출
for i in lst:
    print(i[0], i[1])
