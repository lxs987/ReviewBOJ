# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 11:48:04 2021

@author: lxs_9
"""

# Dynamic Programming
# 11726. 2×n 타일링
# Recurrence Relation: dp[N] = dp[N-1] + dp[N-2]

# Initial List. index = n, lst[index] = the number of cases
lst = [0,1,2]

# Make list(the number of cases) with recurrence relation
for i in range(3, 1001):
    lst.append(lst[i-2]+lst[i-1])

# Type input
n = int(input())

# Print result
print(lst[n]%10007)