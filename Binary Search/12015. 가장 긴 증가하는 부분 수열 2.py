# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 19:19:07 2022

@author: lxs_9
"""
# 참고: https://seohyun0120.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC

# 가장 긴 증가하는 부분 수열(LIS)에 관한 문제이다.
# 해당 문제에 관한 풀이법은 DP, Binary Search가 있다.
# 해당 문제는 DP로 풀게 되면 시간 초과가 뜬다.
# 최댓값을 이미 알고 있다면 현재 이전의 모든 수를 반복할 필요가 없다.
# 따라서 Python의 bisect를 사용하여 시간 복잡도를 줄인다.
# DP를 사용했을 땐 O(N^2)이지만, 이진 탐색을 진행하면 O(NlogN)의 시간 복잡도를 갖는다.
# bisect.bisect_left(arr, x): arr가 정렬되어있다는 가정 하에 x값이 들어갈 위치 반환

import bisect
import sys

# 수열 A의 크기
x = int(sys.stdin.readline())
# 수열 A를 이루고 있는 A(i)를 담은 배열
arr = list(map(int, sys.stdin.readline().split()))

# 가장 긴 증가하는 부분 수열을 저장할 배열
# dp를 수열 A의 첫번째 수(arr[0])로 초기화한다.
dp = [arr[0]]

for i in range(x):
    # 현재 위치(i)가 이전 위치의 원소들보다 크면
    if arr[i] > dp[-1]:
        # dp에 추가한다.
        dp.append(arr[i])
    # 현재 위치(i)가 이전 위치의 원소보다 작거나 같으면
    else:
        # bisect.bisect_left로 이전 위치의 원소 중 가장 큰 원소의 index값을 구한다.
        idx = bisect.bisect_left(dp, arr[i])
        # 그리고 DP의 index의 원소를 arr[i]로 바꿔준다.
        dp[idx] = arr[i]
        
print(len(dp))
