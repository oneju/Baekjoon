# 바이러스
# https://www.acmicpc.net/problem/2606
import sys
import collections
input = sys.stdin.readline
N = int(input())
M = int(input())
matrix = collections.defaultdict(list)
for _ in range(M):
    a,b = map(int,input().split())
    matrix[a].append(b)
    matrix[b].append(a)
    
visited = [0] * (N+1)
cnt=0
def dfs(x):
    global cnt
    if visited[x] == 1:return
    visited[x] = 1
    for i in matrix[x]:
        if visited[i] == 0:
            cnt+=1
            dfs(i)
dfs(1)
print(cnt)