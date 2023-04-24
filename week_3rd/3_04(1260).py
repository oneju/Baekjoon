# DFS 와 BFS
# https://www.acmicpc.net/problem/1260
from collections import deque
n, m, v = map(int, input().split()) #n 정점의 수, m 간선의 수, v 시작 정점
lst = []
for _ in range(m):
    arr = list(map(int, input().split(" ")))
    lst.append(arr)
    lst.append(arr[::-1])   # 양방향 간선, 받은 내용 반대로 한번 더 저장
lst.sort()

dfs_lst = []
def dfs(v):
    if len(dfs_lst) == n:
        return
    dfs_lst.append(v)
    for edge in lst:
        if v == edge[0] and edge[1] not in dfs_lst:
            dfs(edge[1])

def bfs(v):
    visited = [0] * (n+1)

    queue = deque()
    visited[v] = 1
    queue.append(v)
    
    while queue:
        node = queue.popleft()
        print(node,end= " ")
        visited[node] = 1
        for edge in lst:
            if edge[0] == node and visited[edge[1]] == 0:
                visited[edge[1]] = 1
                queue.append(edge[1])

dfs(v)
[print(i, end=" ") for i in dfs_lst]
print()

bfs(v)