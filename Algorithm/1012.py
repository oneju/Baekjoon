# 유기농 배추
# https://www.acmicpc.net/problem/1012
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
dir_x = [1,-1,0,0]
dir_y = [0,0,-1,1]
def dfs(x,y):
    stack = []
    stack.append([x,y])
    while stack:
        a,b = stack.pop()
        lst[a][b] = 0
        for i in range(4):
            ax = a+dir_x[i]
            by = b+dir_y[i]
            if ax in range(n) and by in range(m):
                if lst[ax][by] == 1:
                    stack.append([ax,by])

for _ in range(T):
    n,m,k = map(int,input().split())
    lst = [[0]*m for _ in range(n)]
    vis = [[0]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        lst[x][y] = 1
    worm = 0
    for i in range(n):
        for j in range(m):
            if vis[i][j] == 0 and lst[i][j] == 1:
                dfs(i,j)
                worm+=1
    print(worm)

