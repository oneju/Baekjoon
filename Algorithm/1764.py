# 듣보잡
# https://www.acmicpc.net/problem/1764
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
A = [input().strip() for _ in range(n+m)]
A.sort()
ans = []
for i in range(m+n-1):
    if A[i] == A[i+1]:
        ans.append(A[i])    
print(len(ans))
[print(i)for i in ans]