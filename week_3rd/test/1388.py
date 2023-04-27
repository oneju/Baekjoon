# 바닥 장식
# https://www.acmicpc.net/problem/1388
import sys
input = sys.stdin.readline
# - 가로 | 세로 연결된 부분 탐색
n,m = map(int,input().split()) # 가로 n, 세로 m
room = [input() for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def dfs(x,y):
    visited[x][y] = 1
    stack = []
    stack.append([x,y])
    
    if room[x][y] == '-':
        while stack:
            cur_x,cur_y = stack.pop()
            for a in [1,-1]:
                yy = cur_y+a
                if yy in range(m) and room[cur_x][yy] == '-' and visited[cur_x][yy] == 0:
                    stack.append([cur_x,yy])
                    visited[cur_x][yy] = 1
    else:
        while stack:
            cur_x,cur_y = stack.pop()
            for a in [1,-1]:
                xx = cur_x+a
                if xx in range(n) and room[xx][cur_y] == '|' and visited[xx][cur_y] == 0:
                    stack.append([xx,cur_y])
                    visited[xx][cur_y] = 1

cnt = 0
for i in range(n):
    for j in range(m):
        if room[i][j] in ['-','|'] and visited[i][j] == 0:
            dfs(i,j)
            cnt+=1
print(cnt)