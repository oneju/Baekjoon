# 멀티탭 스케줄링
# https://www.acmicpc.net/problem/1700
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
lst = list(map(int,input().split()))
S = [0]*n
cnt = 0
for i in range(m):
    if lst[i] in S:continue
    if 0 in S:
        S[S.index(0)] = lst[i]
        continue    
    
    b = [0,0]
    for j in range(n):
        if S[j] not in lst[i:]:
            b=[j,lst[i]]
            break
        if lst[i:].index(S[j]) > b[1]:
            b = [j,lst[i:].index(S[j])]
    S[b[0]] = lst[i]
    cnt+=1
    
print(cnt)