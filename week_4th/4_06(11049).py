# 행렬 곱셉 순서
# https://www.acmicpc.net/problem/11049
import sys
input = sys.stdin.readline
N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

for i in range(1,N):
    for j in range(N-i):
        dp[j][i+j] = sys.maxsize
        for k in range(j,i+j):
            size = dp[j][k] + dp[k+1][i+j] + lst[j][0] * lst[k][1] * lst[i+j][1]
            if size < dp[j][i+j]:dp[j][i+j] = size

print(dp[0][N-1])