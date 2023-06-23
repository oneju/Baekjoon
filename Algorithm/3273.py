# 두 수의 합
# https://www.acmicpc.net/problem/3273
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
x = int(input())
a.sort()
i = 0
j = n-1
cnt = 0
while i<j:
    add = a[i]+a[j]
    if add == x:
        cnt+=1
        i+=1
        j-=1
    elif add > x:
        j-=1
    else:
        i+=1
print(cnt)