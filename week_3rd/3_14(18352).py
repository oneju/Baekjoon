# 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352
import sys
from collections import deque

input = sys.stdin.readline
N, M, K, X = map(int, input().split())
road = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    road[a-1].append(b-1)

count = [sys.maxsize]*N
def bfs(start):
    queue = deque()
    count[start] = 0
    
    queue.append(start)
    visited = [0]*N
    visited[start] = 1
    
    while queue:
        city = queue.popleft()
            
        for i in road[city]:
            if visited[i] == 0:
                count[i] = count[city]+1
                queue.append(i)
                visited[i] = 1
    return

bfs(X-1)

flag = 0
for i in range(N):
    if count[i] == K:
        print(i+1)
        flag = 1
if flag == 0:print(-1)