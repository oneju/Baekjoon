# 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725
import sys

input = sys.stdin.readline
N = int(input())
matrix = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    matrix[a].append(b)
    matrix[b].append(a)
visited = [0]*(N+1)
stack = []
def dfs(v):
    stack.append(v)
    visited[v] = 1
    while stack:
        cur = stack[-1]
        flag = False
        for a in matrix[cur]:
            if visited[a] == 0:
                stack.append(a)
                visited[a] = cur
                flag = True
                break
        if not flag:
            stack.pop()
            
dfs(1)
[print(visited[i]) for i in range(2,N+1)]