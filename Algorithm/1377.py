# 버블 소트
# https://www.acmicpc.net/problem/1377
import sys
input = sys.stdin.readline
N = int(input())
A = [(int(input()),i)for i in range(N)]
A.sort()
cnt = 0
for i in range(N):
    if cnt < A[i][1]-i:
        cnt=A[i][1]-i
print(cnt+1)