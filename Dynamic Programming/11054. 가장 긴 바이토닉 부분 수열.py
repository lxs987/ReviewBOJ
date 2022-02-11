# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 10:41:24 2022

@author: lxs_9
"""
n = int(input())
a = list(map(int, input().split()))
dpp = [0 for i in range(n)]
dpm = [0 for i in range(n)]
dpb = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dpp[i] < dpp[j]:
            dpp[i] = dpp[j]
    dpp[i] += 1
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if a[i] > a[j] and dpm[i] < dpm[j]:
            dpm[i] = dpm[j]
    dpm[i] += 1
for i in range(n):
    dpb[i] = dpp[i] + dpm[i] - 1
print(max(dpb))
