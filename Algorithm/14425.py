# 문자열 집합
# https://www.acmicpc.net/problem/14425
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
S = []
for _ in range(n):
    S.append(input().strip())
ans = 0
for _ in range(m):
    word = input().strip()
    if word in S:ans+=1
print(ans)