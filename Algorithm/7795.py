# 먹을 것인가 먹힐 것인가
# https://www.acmicpc.net/problem/7795
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    cnt = 0
    a = n-1
    b = m-1
    while a>=0 and b>=0:
        if A[a] > B[b]:
            cnt+=(b+1)
            a-=1
        else:
            b-=1
    print(cnt)