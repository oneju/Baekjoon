# 두 수의 합
# https://www.acmicpc.net/problem/3273
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))
x = int(input())
A.sort()
a = 0
b = n-1
cnt = 0
while a<b:
    if A[a]+A[b] == x:
        cnt+=1
        a+=1
        b-=1
    elif A[a]+A[b] > x:
        b-=1
    else:
        a+=1
print(cnt)