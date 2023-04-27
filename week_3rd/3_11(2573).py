# 빙산
# https://www.acmicpc.net/problem/2573
import sys
input = sys.stdin.readline
N,M = map(int, input().split())
ice = [list(map(int,input().split())) for _ in range(N)]

x_info = [1,-1,0,0]
y_info = [0,0,-1,1]

def melting(a,b):
    change = []
    visited[a][b] = 1
    stack = [(a,b)]
    while stack:
        x,y = stack.pop()
        cnt = 0 
        for k in range(4):
            xx = x+x_info[k]
            yy = y+y_info[k]
            if xx in range(N) and yy in range(M) and visited[xx][yy] == 0:
                if ice[xx][yy]==0:
                    cnt +=1
                else:
                    stack.append((xx,yy))
                    visited[xx][yy] = 1

        if ice[x][y] - cnt < 0:change.append([x,y])
        else:ice[x][y] -= cnt
    for x,y in change:ice[x][y] = 0
    
day = 0
while True:
    count = 0
    visited = [[0]*M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0 and visited[i][j] == 0:
                melting(i,j)
                count +=1
                
    if count >= 2:break
    
    if count ==0:
        day = 0
        break
    day +=1
print(day)