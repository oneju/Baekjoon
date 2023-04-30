# 동전 0
# https://www.acmicpc.net/problem/11047
N,K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
ans = 0
for i in range(N-1,-1,-1):
    if coins[i] <= K:
        ans+=(K//coins[i])
        K%=coins[i]
    if K ==0:break
print(ans)