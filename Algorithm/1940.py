# 주몽
# https://www.acmicpc.net/problem/1940
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
A = list(map(int,input().split()))
first = 0
rear = n-1
cnt = 0
A.sort()
while first<rear:
    num = A[first]+A[rear]
        
    if num == m:
        cnt+=1
        first+=1
        rear-=1
    elif num>m:
        rear-=1
    else:
        first+=1
print(cnt)