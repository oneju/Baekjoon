# 구슬 찾기
# https://www.acmicpc.net/problem/2617
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
lst = [[float('INF')]*n for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    lst[a-1][b-1] = 1
# Fluyd
for i in range(n):
    for j in range(n):
        for k in range(n):
            if lst[j][i] == 1 and lst[i][k] == 1:
                lst[j][k] = 1
cnt = 0
for i in range(n):
    heavy = light = 0
    for j in range(n):
        if lst[i][j] == 1:
            light +=1
        if lst[j][i] == 1:
            heavy +=1
    if heavy > n//2 or light > n//2:
        cnt +=1
print(cnt)