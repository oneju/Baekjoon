# 경쟁적 전염
# https://www.acmicpc.net/problem/18405
import sys
from collections import deque

input = sys.stdin.readline
n,k = map(int,input().split())
virus = [list(map(int,input().strip().split())) for _ in range(n)]
s,x,y = map(int,input().split())

arr = []
for i in range(n):
    for j in range(n):
        if virus[i][j] != 0:
            arr.append([virus[i][j],i,j])
arr.sort()

sec = t = 0
queue = deque(arr)
warning = 0

while queue:
    cur = queue.popleft()
    dir = [[0,1],[0,-1],[1,0],[-1,0]]
    
    if t > cur[0] : sec += 1
    if sec == s:break
    
    t = cur[0]
    for i in range(4):
        xx = cur[1] + dir[i][0]
        yy = cur[2] + dir[i][1]
        if xx in range(n) and yy in range(n):
            if virus[xx][yy] == 0:
                queue.append([cur[0],xx,yy])
                virus[xx][yy] = cur[0]
            if xx == x-1 and yy == y-1:
                warning = 1
                break
    if warning==1:break
print(virus[x-1][y-1])