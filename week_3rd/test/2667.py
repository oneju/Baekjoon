# 단지번호붙이기
# https://www.acmicpc.net/problem/2667
import sys
input = sys.stdin.readline
n = int(input())
house = [list(input()) for _ in range(n)]

def dfs(x,y):
    cnt = 1
    stack = []
    stack.append([x,y])
    while stack:
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
    
        cur = stack.pop()
        for i in range(4):
            xx = cur[0] + dx[i]
            yy = cur[1] + dy[i]
            if xx in range(n) and yy in range(n):
                if house[xx][yy] == '1' and visited[xx][yy] == 0:
                    cnt+=1
                    stack.append([xx,yy])
                    visited[xx][yy] = 1
    return cnt

counting = []
visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and house[i][j] == '1':
            visited[i][j] = 1
            counting.append(dfs(i,j))
counting.sort()

print(len(counting))
[print(c) for c in counting]