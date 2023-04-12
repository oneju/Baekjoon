#외판원 순회 2
'''
TSP
숫자 N과 int[N][N]의 2차원 배열을 받아서
[i][j] 를 N번 더해서 가장 작은 수

DFS 깊이 우선 탐색

4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0

35

'''
import sys
N = int(sys.stdin.readline())
lst = [list(map(int,sys.stdin.readline().split(" "))) for _ in range(N)]

visited = [False] * N #방문한 나라 True
cost = sys.maxsize

# 나라 -> 나라 비용계산
def DFS(start, cur, cnt, val):
    
    global cost
    #start -> cur, cnt
    if cnt==N and lst[cur][start]:               # 방문 수가 
        cost = min(cost,val+lst[cur][start])       # 최소비용 저장
        return
    if val > cost:                                 # 계산 비용이 최소 비용보다 커지면 탈출
        return
    for i in range(N): #lst[][] 순회
        if lst[cur][i] and visited[i] == False:
            visited[i] = True
            DFS(start, i, cnt+1, val+lst[cur][i])
            visited[i] = False
'''
if not visited[i] and lst[start][i] != 0:
    visited[i] = True
    DFS(i,cnt+1,val+lst[start][i])
    visited[i] = False
'''
for i in range(N): #lst[] 순회
    visited[i] = True
    DFS(i,i,1,0)
    visited[i] = False
    
print(cost)