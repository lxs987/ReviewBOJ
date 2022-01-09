# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 19:25:28 2022

@author: lxs_9
"""
# 풀이 참고: https://m.blog.naver.com/occidere/220788046159

# 자릿수 입력받기
n = int(input())

lst = [0 for _ in range(n+2)]
lst[1] = 1 # N=1 -> 1

# 예를 들어, N = 4일 때 10 다음에 나오는 2자리의 숫자는 00, 01, 10 이다.
# 이는 N-1일 때 뒤에서 N-2개의 숫자들과, N-2일 때 뒤에서 N-2개의 숫자들이다.
# 길이가 N인 이친수는 N-2번째 이친수의 개수 + N-1번째 이친수의 개수이다.
# 피보나치 수와 같다.
for i in range(2, n+1):
    lst[i] = lst[i-2]+lst[i-1]
    
print(lst[n])
