# 집합의 표현
# https://www.acmicpc.net/problem/1717
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
lst = [i for i in range(n+1)]

# x의 루트 찾기
def find(x):
    y = x
    while y!=lst[y]:
        y = lst[y]
    lst[x] = y
    return y

# x, y 합치기
def union(x, y):
    a = find(x)
    b = find(y)
    if a!=b:
        if a>b:
            lst[a] = b
        else:
            lst[b] = a

for _ in range(m):
    x,a,b = map(int,input().split())
    if x==0:
        union(a,b)
    else:
        if find(a)==find(b):
            print("yes")
        else:
            print("no")