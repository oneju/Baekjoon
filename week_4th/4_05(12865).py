# 평범한 배낭
# https://www.acmicpc.net/problem/12865
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
objects = [list(map(int,input().split()))for _ in range(n)]

P = [[0]*(k+1) for _ in range(n)]

for i in range(n):
    weight = objects[i][0]
    value = objects[i][1]
    for w in range(1,k+1):
        if weight > w:
            P[i][w] = P[i-1][w]
        else:
            P[i][w] = max(value + P[i-1][w-weight],P[i-1][w])
            
print(P[n-1][k])