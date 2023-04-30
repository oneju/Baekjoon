# 줄 세우기
# https://www.acmicpc.net/problem/2252
import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int,input().split())

graph = [[] for _ in range(n)]
indegree = [0 for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    indegree[b-1]+=1
    
T = []
visited = [0] * n

def topological(i):
    queue = deque()
    queue.append(i)
    visited[i] = 1
            
    while queue:
        cur = queue.popleft()
        T.append(cur)
        for next in graph[cur]:
            if visited[next] == 0:
                indegree[next]-=1
                if indegree[next] <= 0:
                    queue.append(next)
                    visited[next] = 1
                
for i in range(n):
    if indegree[i] == 0 and visited[i] == 0:
        topological(i)

[print(i+1, end=" ") for i in T]