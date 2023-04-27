# 이분 그래프
# https://www.acmicpc.net/problem/1707
import sys
input = sys.stdin.readline
k = int(input())

def dfs(n):
    # 탐색 시작
    node = n
    stack = []
    
    stack.extend(graph[node])
    
    while stack:
        x, y = stack.pop()
        if visited[x] != visited[y] and visited[y] == 0:
            visited[y] = -visited[x]
            stack.extend(graph[y])
        elif visited[x] == visited[y]:
            return False
    return True

for _ in range(k): # 테스트 케이스 실행
    v,e = map(int,input().split())
    graph = [[] for _ in range(v)] # 무방향 그래프 행렬화
    visited = [0] * v
    
    for _ in range(e):
        a,b = list(map(int,input().split()))
        graph[a-1].append([a-1,b-1])
        graph[b-1].append([b-1,a-1])
        
    for i in range(v):
        if visited[i] == 0:
            visited[i] = 1
            flag = dfs(i)
            if flag == False:break
    if flag == False:print('NO')
    else:print('YES')
    