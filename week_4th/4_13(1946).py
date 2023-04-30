# 신입 사원
# https://www.acmicpc.net/problem/1946
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    arr = []
    
    for _ in range(N):
        a,b = map(int,input().split())
        arr.append((a,b))
    arr.sort()
    cnt=1
    interview = arr[0][1]
    for i in range(1,N):
        if arr[i][1] < interview:
            cnt+=1
            interview = arr[i][1]
    print(cnt)