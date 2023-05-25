# 붙임성 좋은 총총이
# https://www.acmicpc.net/problem/26069
import sys
input = sys.stdin.readline
n = int(input())
chong = {"ChongChong":1}
ans = 0
for _ in range(n):
    a,b = input().split()
    if a in chong:
        chong[b]=1
    elif b in chong:
        chong[a]=1
for a in chong:ans+=1
print(ans)