# 동전 2
# https://www.acmicpc.net/problem/2294
import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

def bfs():
    visited = [0] * (k+1)
    queue = deque()
    queue.append([0,0])
    while queue:
        cost, count = queue.popleft()
        if cost == k:return count
        for i in range(n):
            if cost+coins[i] <= k and visited[cost+coins[i]] == 0:
                queue.append([cost+coins[i],count+1])
                visited[cost+coins[i]]=1
    return -1
print(bfs())