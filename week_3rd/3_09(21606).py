# 아침 산책
# https://www.acmicpc.net/problem/21606
import sys
input = sys.stdin.readline
N = int(input())
in_out = input()
mat = [[]for _ in range(N)]
ret = 0

for _ in range(N-1):
    u,v = map(int, input().split())
    mat[u-1].append(v-1)
    mat[v-1].append(u-1)
    if in_out[u-1] == '1'and in_out[v-1] == '1': # 간선 양쪽이 실내일 경우
        ret += 2

visited = [0] * N
def dfs(v):
    cnt = 0    
    stack = [] 
    stack.extend(mat[v])
    while stack:
        node = stack.pop()
        if in_out[node] == '1': cnt+=1 # 실내에 도착하면 카운팅
        elif in_out[node]=='0' and visited[node] == 0:
            stack.extend(mat[node]) # 실외라면 인접한 노드들 스택에 추가
            visited[node] = 1
    return cnt

for i in range(N):
    if in_out[i] == '0' and visited[i] == 0: # 방문한 적 없는 실외일 경우
        visited[i] = 1
        cnt = dfs(i)
        ret += cnt*(cnt-1)  # 실내 에서 실내로 이동하는 모든 경우의 수 계산

print(ret)