# 안전 영역
# https://www.acmicpc.net/problem/2468
import sys

input = sys.stdin.readline
N = int(input())
lst_h = [list(map(int,input().split()))for _ in range(N)]

visit = [[0]*N for _ in range(N)]
xi = [0,0,1,-1]
yi = [1,-1,0,0]

'''
from collections import deque

def bfs(x,y,a):
    queue = deque([(x,y)])
    visit[x][y] = 1
    while queue:
        ax,ay = queue.popleft()
        for i in range(4):
            nx,ny = ax+xi[i], ay+yi[i]
            if 0<=nx<N and 0<=ny<N:
                if lst_h[nx][ny] > a and visit[nx][ny] == 0:
                    queue.append([nx,ny])
                    visit[nx][ny] = 1
'''
def dfs(x,y,a):
    for i in range(4):
        nx = x+xi[i]
        ny = y+yi[i]
        if 0<=nx<N and 0<=ny<N:
            if lst_h[nx][ny] > a and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                dfs(nx,ny,a)

def rain(a):
    cnt = 0

    for i in range(N):
        for j in range(N):
            if lst_h[i][j] > a and visit[i][j] == 0:
                # bfs(i,j,a)
                dfs(i,j,a)
                cnt+=1
    return cnt

ans = 0 # 안전영역 수
for a in range(101):
    visit = [[0]*N for _ in range(N)]
    temp = rain(a)
    ans = max(ans,temp)

    if temp == 0: break
'''
↓ 아직도 이게 왜 안되는지 모르겠어요
a = 1
ans = 0
while True:
    visit = [[0]*N for _ in range(N)]
    temp = rain(a)
    if ans > temp: break
    ans = temp
    a+=1
'''
print(ans)