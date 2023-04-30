# 동전
# https://www.acmicpc.net/problem/9084
import sys
input = sys.stdin.readline
T = int(input())

def coins(n,m):
    for i in range(n):
        for k in range(m+1):
            if coin[i] < k:
                P[k][i] = sum(P[k-coin[i]])
            elif coin[i] == k: 
                # 금액과 동전 크기가 같다면 방법이 한가지 밖에 없겠죠?
                P[k][i] = 1

for _ in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    
    P = [[0] * N for _ in range(M+1)] # 금액을 인덱스로 배열 생성 계산을 위해 0으로 초기화
    coins(N,M)
    print(sum(P[-1]))