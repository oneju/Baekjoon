# 붙임성 좋은 총총이
# https://www.acmicpc.net/problem/26069
import sys
input = sys.stdin.readline
n = int(input())
chong = {}
ans = 0
for _ in range(n):
    a,b = input().split()
    if "ChongChong" in [a,b]:
        chong[a] = 1
        chong[b] = 1
    elif a in chong and chong[a]==1:
        chong[b]=1
    elif b in chong and chong[b]==1:
        chong[a]=1
    else:
        chong[a]=0
        chong[b]=0
for a in chong:
    if chong[a] == 1:ans+=1
print(ans)