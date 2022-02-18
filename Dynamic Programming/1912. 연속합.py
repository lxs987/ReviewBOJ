# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 11:57:56 2022

@author: lxs_9
"""
# 수열의 길이 N
n = int(input())

# 수열을 이루고 있는 정수를 입력받음
a = list(map(int, input().split()))

# 합을 저장할 list (비교를 위해 a[0]을 넣어줌)
sum = [a[0]]

# sum의 i번째 index와 a의 i+1번째 인덱스의 숫자를 합한 값과
# a의 i+1번째 숫자를 비교하여 더 큰 숫자를 sum 리스트에 넣어준다
for i in range(len(a) - 1):
    sum.append(max(sum[i] + a[i + 1], a[i + 1]))
    
# sum 리스트 중 가장 큰 수를 출력한다
print(max(sum))
