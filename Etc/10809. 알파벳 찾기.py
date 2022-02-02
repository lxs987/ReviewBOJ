# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 14:24:42 2022

@author: lxs_9
"""
# 단어를 입력받는다
s = input()

# 알파벳 총 갯수(26)만큼의 길이를 갖는 -1로 이루어진 리스트를 생성한다.
arr = [-1 for _ in range(26)]

# 단어의 길이만큼 해당 반복문을 실행한다
# 단어의 첫 번째 글자가 해당하는 위치에 -1대신 index를 삽입한다.
# 중복으로 나타나는 경우 처음의 위치를 기록하기 위해, -1일 때에만 결과를 삽입한다.
for i in range(len(s)):
    if(arr[ord(s[i])-97]==-1):
        arr[ord(s[i])-97] = i

# 결과 리스트를 대괄호, 콤마 없이 출력한다.
print(*arr, sep = ' ')
