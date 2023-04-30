# 미로 탐색
# https://www.acmicpc.net/problem/2178
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
maze = [list(input()) for _ in range(n)]
# 이동할 방향 (↓ → ↑ ←)
dist_x = [0, -1, 0, 1]
dist_y = [1, 0, -1, 0]
# 방문 확인
visited = [[0 for _ in range(m)] for _ in range(n)]
def bfs(n,m):
    queue = deque()
    visited[0][0] = 1
    queue.append((0,0))
    
    while queue:
        x, y = queue.popleft()
        if x == n-1 and y == m-1:break # 목적지에 도착하면 탈출

        for i in range(4):
            adj_x = x + dist_x[i]
            adj_y = y + dist_y[i]

            if adj_x in range(0,n) and adj_y in range(0,m):
                if visited[adj_x][adj_y] == 0 and maze[adj_x][adj_y] == '1':
                    
                    visited[adj_x][adj_y] = visited[x][y] + 1
                    queue.append((adj_x, adj_y))
                    
    return print(visited[n-1][m-1])

bfs(n,m)