# 연결 요소의 개수
# https://www.acmicpc.net/problem/11724
import sys
import collections
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M = map(int,input().split())
matrix = collections.defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
visited = [0] * (N+1)

def dfs(x):
    if visited[x] == 1:return
    
    visited[x] = 1
    for i in matrix[x]:
        if visited[i] == 0:
            dfs(i)

cnt = 0
for i in range(1,N+1):
    if visited[i] ==0:
        dfs(i)
        cnt+=1
print(cnt)