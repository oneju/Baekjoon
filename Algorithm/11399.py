# ATM
# https://www.acmicpc.net/problem/11399
import sys
input = sys.stdin.readline
N = int(input())
P = list(map(int,input().split()))
P.sort()
ans = tmp = 0
for i in range(N):
    tmp += P[i]
    ans += tmp
print(ans)