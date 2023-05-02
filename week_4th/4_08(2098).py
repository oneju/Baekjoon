# 외판원 순회
# https://www.acmicpc.net/problem/2098

# https://maivve.tistory.com/306

import sys
input = sys.stdin.readline
N = int(input())
lst = []

dp = [[0]*(1<<N) for _ in range(N)]
for i in range(N):
    lst.append(list(map(int,input().split())))

# 시작도시를 0번으로 설정하고 시작
def tsp(city, visited):
    # 모든 도시를 방문했다면 출발도시로 돌아오는 값 리턴
    if visited == (1<<N)-1:
        # 못가는 도시는 0으로 저장되어있으니까 예외
        if lst[city][0] != 0:return lst[city][0]
        else:return sys.maxsize
    # 이미 값이 존재하다면 있는 값 리턴
    if dp[city][visited]!=0:
        return dp[city][visited]
    
    dp[city][visited] = sys.maxsize
    for i in range(N):
        # 방문한 기록이 없으면서 갈 수 있는 도시
        if visited&(1<<i) == 0 and lst[city][i]!=0:
            # 방문했다고 체크하고 함수 재귀
            dp[city][visited] = min(dp[city][visited],tsp(i,visited|(1<<i))+lst[city][i])
    return dp[city][visited]

print(tsp(0,1))