# 탈출
# https://www.acmicpc.net/problem/3055
import sys
from collections import deque

input = sys.stdin.readline
r,c = map(int, input().split())
forest_map = [list(input().strip()) for _ in range(r)]
queue = deque()

x_info = [1, 0, -1, 0]
y_info = [0, -1, 0, 1]
dir = [[0]*c for _ in range(r)]

def bfs(dx,dy):
    while queue:
        x,y = queue.popleft()
        if forest_map[dx][dy] == 'S':
            return dir[dx][dy]
        
        for i in range(4):
            xx = x+x_info[i]
            yy = y+y_info[i]
            if xx in range(r) and yy in range(c):
                if forest_map[x][y] == 'S' and (forest_map[xx][yy] == '.' or forest_map[xx][yy] == 'D'):
                    forest_map[xx][yy] = 'S'
                    dir[xx][yy] = dir[x][y] +1
                    queue.append((xx,yy))
                elif forest_map[x][y] == '*' and (forest_map[xx][yy] == '.' or forest_map[xx][yy] == 'S'):
                    forest_map[xx][yy] = '*'
                    queue.append((xx,yy)) 
    return 'KAKTUS'

for i in range(r):
    for j in range(c):
        if forest_map[i][j] == 'S':
            queue.append((i,j))
        elif forest_map[i][j] == 'D':
            dx,dy = i, j
            
for i in range(r):
    for j in range(c):
        if forest_map[i][j] == '*':
            queue.append((i,j))
print(bfs(dx,dy))
