# N과 M (6)
# https://www.acmicpc.net/problem/15655
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
def dfs(i,a):
    if a == m:
        print(*ans)
        return
    for j in range(i+1,n):
        ans.append(lst[j])
        dfs(j,a+1)
        ans.pop()
for i in range(n):
    ans = []
    ans.append(lst[i])
    dfs(i,1)
