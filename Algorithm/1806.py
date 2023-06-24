# 부분합
# https://www.acmicpc.net/problem/1806
import sys
input = sys.stdin.readline
N,S = map(int,input().split())
A = list(map(int,input().split()))
f = r = 0
hap = A[f]
diff = N+1
while f <= r:
    if hap >= S:
        if r==f:
            diff = 1
            break        
        diff = min(diff, r-f+1)
        hap-=A[f]
        f+=1
    else:
        if r < N-1:
            r+=1
            hap+=A[r]
        else:
            break
if diff == N+1:
    print(0)
else: 
    print(diff)